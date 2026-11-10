"""copy-budget leaves no copy from a hidden div behind when that div holds a nested div.
Its old regex stopped at the first </div>, so the paragraph after the nested div was counted."""

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "copy-budget.mjs"


def test_hidden_div_with_nested_div_drops_all_of_its_copy(tmp_path: Path):
    # The script reads ROOT/index.html, so run a copy of it inside a temp tree.
    (tmp_path / "scripts").mkdir()
    shutil.copy(SCRIPT, tmp_path / "scripts" / "copy-budget.mjs")
    (tmp_path / "index.html").write_text(
        "<!doctype html><html><body><p>Plain copy.</p>"
        "<div hidden><div>x</div><p>leaked one two three</p></div></body></html>",
        encoding="utf-8",
    )

    result = subprocess.run(
        ["node", str(tmp_path / "scripts" / "copy-budget.mjs")],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    # Only "Plain copy." is visible; the hidden block's paragraph must not be counted.
    assert "copy-budget: 2 visible words" in result.stdout, result.stdout
