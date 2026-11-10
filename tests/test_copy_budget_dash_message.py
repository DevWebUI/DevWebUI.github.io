"""The em-dash failure message says what is counted: the whole page source outside
<style>/<script>, not only visitor-visible copy. A hidden block's dash still fails."""

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "copy-budget.mjs"


def test_em_dash_failure_message_says_page_source(tmp_path: Path):
    # The script reads ROOT/index.html and ROOT/scripts/copy-budget.mjs, so run a copy
    # of it inside a temp tree that holds only a fixture page.
    (tmp_path / "scripts").mkdir()
    shutil.copy(SCRIPT, tmp_path / "scripts" / "copy-budget.mjs")
    (tmp_path / "index.html").write_text(
        "<!doctype html><html><body><p>Plain copy.</p>"
        "<div hidden>An em-dash — inside a hidden block.</div></body></html>",
        encoding="utf-8",
    )

    result = subprocess.run(
        ["node", str(tmp_path / "scripts" / "copy-budget.mjs")],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1, result.stdout + result.stderr
    assert "1 em-dash(es) in page source" in result.stderr, result.stderr
    assert "visitor-facing" not in result.stderr, result.stderr
