from PIL import Image
import os
import glob

download_dir = os.path.expanduser("~/storage/downloads")
files = glob.glob(f"{download_dir}/*.png") + glob.glob(f"{download_dir}/*.jpg")
files = [f for f in files if "upscaled" not in f]
latest = max(files, key=os.path.getmtime)

filename = os.path.splitext(os.path.basename(latest))[0]
output_path = f"{download_dir}/upscaled_{filename}.jpg"

img = Image.open(latest)
new_size = (img.width * 4, img.height * 4)
img_upscaled = img.resize(new_size, Image.LANCZOS)
img_upscaled.save(output_path, "JPEG", quality=95)
print(f"入力: {os.path.basename(latest)}")
print(f"完了！サイズ: {img.size} → {img_upscaled.size}")
