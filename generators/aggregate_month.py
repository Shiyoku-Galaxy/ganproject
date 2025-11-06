from pathlib import Path
from datetime import datetime
import re

ROOT = Path(__file__).resolve().parents[1]
daily_dir = ROOT / "docs" / "daily"
monthly_dir = ROOT / "docs" / "monthly"
monthly_dir.mkdir(parents=True, exist_ok=True)

# 今月を対象（必要なら INPUT_YYYY_MM=YYYY-MM を環境変数で指定）
target = Path(f"{Path.cwd()}")  # dummy to keep similar structure
ym = (datetime.now().strftime("%Y-%m"))
import os
ym = os.environ.get("INPUT_YYYY_MM", ym)

src_dir = daily_dir / ym
files = sorted(src_dir.glob("*.md"), key=lambda p: p.name)

# YYYY-MM の月次統合ファイル名
out = monthly_dir / f"{ym}_Shibi_Daily_Log_All.md"

lines = []
lines.append(f"# Shibi Daily Logs — {ym}\n")
for f in files:
    date_m = re.search(r"(\d{4}-\d{2}-\d{2})", f.name)
    date_s = date_m.group(1) if date_m else f.name
    lines.append(f"\n---\n\n## {date_s}\n")
    lines.append(f.read_text(encoding="utf-8"))

out.write_text("\n".join(lines), encoding="utf-8")
print(f"[OK] monthly aggregate created: {out}")
