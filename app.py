import os
import base64
import requests
from flask import Flask, render_template, request, send_file
from io import BytesIO
from docx import Document
from docx.shared import Inches

app = Flask(__name__)
GEMINI_API_KEY = "AIzaSyDEjjmrDEQFLxdUA0OsiCGVwUVvgVr7r8w" #自己創的API
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def call_gemini_api(image_bytes, user_input):
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    prompt = f"""請使用繁體中文，根據以下活動資訊，撰寫以下七個段落，請加上標題：

一、 主題說明  
二、 心得反思  
三、學習歷程檔案內容簡介（100 字內）  
四、檢討或反思  
五、學習或執行過程（步驟、結果）  
六、對未來的影響  
七、學習成果佐證說明  

活動資訊如下：
{user_input}
"""

    payload = {
        "contents": [{
            "parts": [
                {
                    "inlineData": {
                        "mimeType": "image/jpeg",
                        "data": image_base64
                    }
                },
                {
                    "text": prompt
                }
            ]
        }]
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(GEMINI_ENDPOINT, json=payload, headers=headers)
    result = response.json()

    if "candidates" in result:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "[錯誤] Gemini 回傳內容如下：\n" + str(result)

def split_sections(text):
    sections = {}
    current_title = None
    known_titles = [
        "主題說明", "心得反思", "學習歷程檔案內容簡介",
        "檢討或反思", "學習或執行過程", "對未來的影響", "學習成果佐證說明"
    ]

    for line in text.splitlines():
        line = line.strip()
        for title in known_titles:
            if line.startswith(title):
                current_title = title
                sections[current_title] = ""
                break
        else:
            if current_title:
                sections[current_title] += line + "\n"
    return sections

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image_files = request.files.getlist("images")
        user_input = request.form["user_input"]

       
        result = call_gemini_api(image_files[0].read(), user_input)

        
        doc = Document()
        doc.add_heading("學習歷程紀錄", 0)

        for section in result.split("**"):
            if section.strip():
                doc.add_paragraph(section.strip())

        doc.add_page_break()
        doc.add_heading("活動照片", level=1)

        # 加入所有圖片
        for img in image_files:
            img.seek(0)
            doc.add_picture(img, width=Inches(4))
            doc.add_paragraph("") 

        # 輸出 Word 到記憶體
        doc_stream = BytesIO()
        doc.save(doc_stream)
        doc_stream.seek(0)

        return send_file(doc_stream, as_attachment=True, download_name="learning.docx", mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    return render_template("index.html", generated_text=None)

if __name__ == "__main__":
    app.run(debug=True)
