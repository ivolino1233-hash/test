"""A stand-in for the vLLM OpenAI-compatible server, for tests and the end-to-end demo.

Usable two ways: `handler` for httpx.MockTransport, or `app` served by uvicorn."""
from __future__ import annotations

import json

import httpx
from fastapi import FastAPI, Request

MODEL = "Qwen/Qwen3.8-Flash-Next"
CALLS: list[dict] = []


def reply(body: dict) -> dict:
    CALLS.append(body)
    msgs = body.get("messages", [])
    user = msgs[-1]["content"]
    has_image = isinstance(user, list) and any(p.get("type") == "image_url" for p in user)
    if has_image:
        content = json.dumps({"garment_type": "sweater", "type_matches": True, "lying_flat": True,
                              "sleeves_or_legs_folded": False, "wrinkles_or_stretching": False,
                              "sheet_visible_and_flat": True, "issues": [],
                              "notes": "Garment is flat with sleeves spread; photo looks good."})
        if "response_format" not in body:
            content = "<think>checking</think>```json\n" + content + "\n```"
    else:
        content = ("Chest is within tolerance. Sleeve length on the left is 1.5 cm long, most likely the sleeve "
                   "was stretched when laid out; re-lay it straight and measure again.")
    return {"id": "x", "object": "chat.completion", "model": body.get("model"),
            "choices": [{"index": 0, "message": {"role": "assistant", "content": content}, "finish_reason": "stop"}]}


def handler(request: httpx.Request) -> httpx.Response:
    if request.url.path.endswith("/models"):
        return httpx.Response(200, json={"object": "list", "data": [{"id": MODEL, "object": "model"}]})
    if request.url.path.endswith("/chat/completions"):
        return httpx.Response(200, json=reply(json.loads(request.content)))
    return httpx.Response(404)


def make_app():
    app = FastAPI()

    @app.get("/v1/models")
    def models():
        return {"object": "list", "data": [{"id": MODEL, "object": "model"}]}

    @app.post("/v1/chat/completions")
    async def chat(request: Request):
        return reply(await request.json())

    return app


app = make_app()
