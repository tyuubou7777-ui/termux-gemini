import os
import glob
import subprocess
from datetime import datetime

print("=== Adobe Stock 自動化スクリプト ===\n")

# 1. リネーム
from PIL import Image
download_dir = os.path.expanduser("~/storage/downloads")
files = glob.glob(f"{download_dir}/Firefly_*.png") + glob.glob(f"{download_dir}/Firefly_*.jpg")

if files:
    print(f"【リネーム】{len(files)}件処理中...")
    for i, f in enumerate(sorted(files), 1):
        date = datetime.now().strftime("%Y%m%d")
        ext = os.path.splitext(f)[1]
        new_name = f"{download_dir}/stock_{date}_{i:03d}{ext}"
        os.rename(f, new_name)
        print(f"  {os.path.basename(f)} → {os.path.basename(new_name)}")
else:
    print("【リネーム】対象ファイルなし")

# 2. アップスケール
files2 = glob.glob(f"{download_dir}/stock_*.png") + glob.glob(f"{download_dir}/stock_*.jpg")
files2 = [f for f in files2 if "upscaled" not in f]

if files2:
    print(f"\n【アップスケール】{len(files2)}件処理中...")
    for f in files2:
        filename = os.path.splitext(os.path.basename(f))[0]
        output = f"{download_dir}/upscaled_{filename}.jpg"
        img = Image.open(f)
        new_size = (img.width * 4, img.height * 4)
        img.resize(new_size, Image.LANCZOS).save(output, "JPEG", quality=95)
        print(f"  完了: {os.path.basename(output)} {img.size}→{new_size}")
else:
    print("\n【アップスケール】対象ファイルなし")

# 3. Stockアップロード画面を開く
print("\n【Stock】ブラウザを開きます...")
os.system("am start -a android.intent.action.VIEW -d 'https://contributor.stock.adobe.com' > /dev/null 2>&1")

print("\n=== 完了！アップロード画面を確認してください ===")
