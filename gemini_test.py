import google.generativeai as genai
import os
import csv
from datetime import datetime

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

prompt = """
Adobe Stockで海外向けに売れるAI生成画像のアイデアを5つ提案してください。
各アイデアについて以下を出力してください：

1. TITLE: Adobe Stock用の英語タイトル（10語以内）
2. PROMPT: Adobe Firefly 3.0向けの英語プロンプト（スタイル・ライティング・雰囲気を含む）
3. KEYWORDS: Adobe Stock用の英語キーワード25個（カンマ区切り）

トレンドを反映し、ビジネス・自然・テクノロジー・ライフスタイル系を含めてください。

出力形式（必ずこの形式で）:
===ITEM1===
TITLE: ここにタイトル
PROMPT: ここにプロンプト
KEYWORDS: keyword1, keyword2, keyword3...
===ITEM2===
...
"""

try:
    print("Gemini APIに接続中...")
    response = model.generate_content(prompt)
    text = response.text

    with open("stock_ideas.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("[成功] stock_ideas.txt に保存しました")

    items = text.split("===ITEM")
    rows = []
    for item in items:
        if "TITLE:" not in item:
            continue
        try:
            title = item.split("TITLE:")[1].split("\n")[0].strip()
            prompt_text = item.split("PROMPT:")[1].split("\n")[0].strip()
            keywords = item.split("KEYWORDS:")[1].split("\n")[0].strip()
            rows.append([title, prompt_text, keywords])
        except:
            continue

    if rows:
        filename = f"adobe_stock_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Filename", "Title", "Keywords"])
            for i, row in enumerate(rows):
                writer.writerow([f"image_{i+1:03}.jpg", row[0], row[2]])
        print(f"[成功] {filename} に保存しました")
        print(f"[情報] {len(rows)}件のアイデアを生成しました")

except Exception as e:
    print(f"[エラー] {e}")
