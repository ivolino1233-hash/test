"""Write an MJPEG file Chromium can use as a fake camera (--use-file-for-fake-video-capture)."""
import sys
from pathlib import Path

import cv2

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tests.synth.cases import photo  # noqa: E402


def main(case: str, out: str, width: int = 1920, frames: int = 60) -> None:
    img, _ = photo(case)
    h = int(round(img.shape[0] * width / img.shape[1]))
    frame = cv2.resize(img, (width, h), interpolation=cv2.INTER_AREA)
    jpg = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 92])[1].tobytes()
    Path(out).write_bytes(jpg * frames)
    print(f"{out}: {frames} frames {width}x{h}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
