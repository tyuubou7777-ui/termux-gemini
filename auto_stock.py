import google.generativeai as genai
import os

# Geminiにトレンドを聞く
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("""
Adobe Stockで今日需要が高く、AI生成画像でも採用されやすいジャンルを3つ教えてください。
各ジャンルについて以下を日本語で答えてください：
1. ジャンル名
2. Fireflyで使える英語プロンプト
3. 推奨キーワード（英語）
""")

print(response.text)

# 結果をファイルに保存
with open(os.path.expanduser("~/today_prompts.txt"), "w") as f:
    f.write(response.text)
    
print("\n~/today_prompts.txt に保存しました！")
