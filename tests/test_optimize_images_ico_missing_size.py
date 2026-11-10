"""A missing favicon size is resized from the file's default frame, not from the
last frame the loop selected (the 32 px frame here)."""

import importlib.util
import io
from pathlib import Path

from PIL import Image

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "optimize_images.py"
spec = importlib.util.spec_from_file_location("optimize_images", SCRIPT)
optimize_images = importlib.util.module_from_spec(spec)
spec.loader.exec_module(optimize_images)


def test_missing_48px_frame_is_resized_from_default_frame(tmp_path: Path):
    # Master ICO: default (largest) frame is blue 256 px, plus a red 32 px frame.
    # 16 and 48 are missing; 32 is present and gets selected before 48 is needed.
    red_32 = Image.new("RGBA", (32, 32), (255, 0, 0, 255))
    blue_256 = Image.new("RGBA", (256, 256), (0, 0, 255, 255))
    master = tmp_path / "master.ico"
    blue_256.save(master, "ICO", sizes=[(32, 32), (256, 256)], append_images=[red_32])

    out = optimize_images.ico_bytes(master)

    with Image.open(io.BytesIO(out)) as result:
        result.size = (48, 48)
        pixel = result.convert("RGBA").getpixel((24, 24))
    # Resized from the blue default frame; the old code produced red here.
    assert pixel[2] > 200 and pixel[0] < 50, pixel
