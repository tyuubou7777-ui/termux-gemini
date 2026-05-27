import os
import glob
from datetime import datetime

download_dir = os.path.expanduser("~/storage/downloads")
files = glob.glob(f"{download_dir}/Firefly_*.png") + glob.glob(f"{download_dir}/Firefly_*.jpg")

for i, f in enumerate(sorted(files), 1):
    date = datetime.now().strftime("%Y%m%d")
    ext = os.path.splitext(f)[1]
    new_name = f"{download_dir}/stock_{date}_{i:03d}{ext}"
    basename = os.path.basename(f)
    os.rename(f, new_name)
    print(f"{basename} → {os.path.basename(new_name)}")

print("リネーム完了！")
