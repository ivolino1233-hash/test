"""SQLite storage: styles with per-size specs, scans, and a few app settings."""
from __future__ import annotations

import json
import sqlite3
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCHEMA = [
    # v1
    """
    CREATE TABLE styles (
        id INTEGER PRIMARY KEY,
        code TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL DEFAULT '',
        customer TEXT NOT NULL DEFAULT '',
        garment_type TEXT NOT NULL,
        sizes TEXT NOT NULL DEFAULT '[]',
        params TEXT NOT NULL DEFAULT '{}',
        notes TEXT NOT NULL DEFAULT '',
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    );
    CREATE TABLE spec_points (
        style_id INTEGER NOT NULL REFERENCES styles(id) ON DELETE CASCADE,
        size TEXT NOT NULL,
        key TEXT NOT NULL,
        target_mm REAL NOT NULL,
        tol_minus_mm REAL NOT NULL,
        tol_plus_mm REAL NOT NULL,
        PRIMARY KEY (style_id, size, key)
    );
    CREATE TABLE scans (
        id TEXT PRIMARY KEY,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL,
        status TEXT NOT NULL,
        style_id INTEGER REFERENCES styles(id) ON DELETE SET NULL,
        size TEXT NOT NULL DEFAULT '',
        garment_type TEXT NOT NULL,
        label TEXT NOT NULL DEFAULT '',
        notes TEXT NOT NULL DEFAULT '',
        px_per_mm REAL NOT NULL,
        landmarks TEXT NOT NULL,
        confidence TEXT NOT NULL,
        measurements TEXT NOT NULL,
        results TEXT NOT NULL,
        warnings TEXT NOT NULL,
        debug TEXT NOT NULL,
        params TEXT NOT NULL,
        ai_status TEXT NOT NULL DEFAULT 'off',
        ai TEXT NOT NULL DEFAULT '{}',
        pass_count INTEGER NOT NULL DEFAULT 0,
        fail_count INTEGER NOT NULL DEFAULT 0
    );
    CREATE INDEX scans_style ON scans(style_id, created_at);
    CREATE TABLE settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
    """,
]

JSON_COLS = {"sizes", "params", "landmarks", "confidence", "measurements", "results", "warnings", "debug", "ai"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class DB:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(path), check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.lock = threading.RLock()
        with self.lock:
            self.conn.execute("PRAGMA journal_mode=WAL")
            self.conn.execute("PRAGMA foreign_keys=ON")
            v = self.conn.execute("PRAGMA user_version").fetchone()[0]
            for i, sql in enumerate(SCHEMA[v:], start=v + 1):
                self.conn.executescript(sql)
                self.conn.execute(f"PRAGMA user_version={i}")
            self.conn.commit()

    def _row(self, r) -> dict | None:
        if r is None:
            return None
        d = dict(r)
        for k in JSON_COLS & d.keys():
            d[k] = json.loads(d[k]) if d[k] else None
        return d

    def q(self, sql, args=()) -> list[dict]:
        with self.lock:
            return [self._row(r) for r in self.conn.execute(sql, args).fetchall()]

    def one(self, sql, args=()) -> dict | None:
        with self.lock:
            return self._row(self.conn.execute(sql, args).fetchone())

    def x(self, sql, args=()) -> int:
        with self.lock:
            cur = self.conn.execute(sql, args)
            self.conn.commit()
            return cur.lastrowid

    # --- styles -------------------------------------------------------------------------------
    def styles(self) -> list[dict]:
        return self.q("SELECT * FROM styles ORDER BY code COLLATE NOCASE")

    def style(self, style_id: int) -> dict | None:
        s = self.one("SELECT * FROM styles WHERE id=?", (style_id,))
        if s:
            s["spec"] = self.spec(style_id)
        return s

    def style_by_code(self, code: str) -> dict | None:
        return self.one("SELECT * FROM styles WHERE code=? COLLATE NOCASE", (code,))

    def spec(self, style_id: int, size: str | None = None) -> list[dict]:
        if size is None:
            return self.q("SELECT * FROM spec_points WHERE style_id=? ORDER BY size, key", (style_id,))
        return self.q("SELECT * FROM spec_points WHERE style_id=? AND size=? ORDER BY key", (style_id, size))

    def save_style(self, data: dict, style_id: int | None = None) -> int:
        t = now()
        fields = (data["code"].strip(), data.get("name", ""), data.get("customer", ""), data["garment_type"],
                  json.dumps(data.get("sizes", [])), json.dumps(data.get("params", {})), data.get("notes", ""))
        with self.lock:
            if style_id is None:
                cur = self.conn.execute(
                    "INSERT INTO styles(code,name,customer,garment_type,sizes,params,notes,created_at,updated_at)"
                    " VALUES(?,?,?,?,?,?,?,?,?)", fields + (t, t))
                style_id = cur.lastrowid
            else:
                self.conn.execute(
                    "UPDATE styles SET code=?,name=?,customer=?,garment_type=?,sizes=?,params=?,notes=?,updated_at=?"
                    " WHERE id=?", fields + (t, style_id))
            if "spec" in data:
                self.conn.execute("DELETE FROM spec_points WHERE style_id=?", (style_id,))
                self.conn.executemany(
                    "INSERT INTO spec_points(style_id,size,key,target_mm,tol_minus_mm,tol_plus_mm) VALUES(?,?,?,?,?,?)",
                    [(style_id, p["size"], p["key"], float(p["target_mm"]), float(p["tol_minus_mm"]),
                      float(p["tol_plus_mm"])) for p in data["spec"]])
            self.conn.commit()
        return style_id

    def delete_style(self, style_id: int) -> None:
        self.x("DELETE FROM styles WHERE id=?", (style_id,))

    # --- scans --------------------------------------------------------------------------------
    def insert_scan(self, s: dict) -> None:
        cols = list(s.keys())
        vals = [json.dumps(s[c]) if c in JSON_COLS else s[c] for c in cols]
        self.x(f"INSERT INTO scans({','.join(cols)}) VALUES({','.join('?' * len(cols))})", vals)

    def update_scan(self, scan_id: str, **fields) -> None:
        fields["updated_at"] = now()
        cols = list(fields.keys())
        vals = [json.dumps(fields[c]) if c in JSON_COLS else fields[c] for c in cols]
        self.x(f"UPDATE scans SET {','.join(c + '=?' for c in cols)} WHERE id=?", vals + [scan_id])

    def scan(self, scan_id: str) -> dict | None:
        return self.one("SELECT * FROM scans WHERE id=?", (scan_id,))

    def scans(self, style_id: int | None = None, status: str = "saved", limit: int = 200, offset: int = 0):
        sql = "SELECT * FROM scans WHERE status=?"
        args: list = [status]
        if style_id is not None:
            sql += " AND style_id=?"
            args.append(style_id)
        sql += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
        return self.q(sql, args + [limit, offset])

    def delete_scan(self, scan_id: str) -> None:
        self.x("DELETE FROM scans WHERE id=?", (scan_id,))

    def old_drafts(self, days: int) -> list[str]:
        cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat(timespec="seconds")
        return [r["id"] for r in self.q("SELECT id FROM scans WHERE status='draft' AND created_at<?", (cutoff,))]

    # --- settings -----------------------------------------------------------------------------
    def get_settings(self) -> dict:
        return {r["key"]: json.loads(r["value"]) for r in self.q("SELECT key, value FROM settings")}

    def set_settings(self, values: dict) -> None:
        with self.lock:
            self.conn.executemany("INSERT INTO settings(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET "
                                  "value=excluded.value", [(k, json.dumps(v)) for k, v in values.items()])
            self.conn.commit()
