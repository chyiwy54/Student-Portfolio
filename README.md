# 學習歷程產生器 (Learning Portfolio Generator)

## 專案簡介 (Project Introduction)
本專案是一個基於 **Flask** 的網頁應用程式，協助學生快速生成符合「學習歷程檔案」需求的文件。  
使用者只需在表單填寫主題說明、心得反思、成果展示等內容，並可上傳多張活動照片，  
系統會呼叫 **Google Gemini API** 進行內容整理，最後輸出成 **DOCX** 或 **PDF** 檔。  

This project is a **Flask-based web application** that helps students quickly generate documents that meet the requirements of a *Learning Portfolio*.  
Users only need to fill in form fields such as **Topic Description**, **Reflection**, and **Project Results**, and can also upload multiple activity photos.  
The system calls the **Google Gemini API** to organize the content, and finally exports the result as a **DOCX** or **PDF** file.  

---

##  功能特色 (Features)
- 表單輸入介面簡潔，支援桌機與手機  
  Simple form-based interface, mobile and desktop friendly  
- 可先進行 **HTML 預覽**  
  Preview generated content in HTML before exporting  
- 支援多張圖片上傳，並統一放在文件最後  
  Supports multiple photo uploads, appended at the end of the document  
- 輸出格式：**DOCX / PDF**  
  Export formats: **DOCX / PDF**  
- 自動產生「主題說明、心得反思、成果展示、未來展望」等段落  
  Automatically generates structured sections (Topic, Reflection, Results, Future Outlook)  

---

## 🛠 使用技術 (Tech Stack)
- **後端 / Backend**: Flask  
- **AI 生成 / AI Generation**: Google Gemini 1.5 Flash API  
- **文件產生 / Document Generation**: python-docx  
- **前端 / Frontend**: Tailwind CSS  

---

## 專案結構 (Project Structure)
```
.
├─ app.py              # Flask 主程式 / main application
├─ templates/
│  ├─ index.html       # 表單頁 / form page
│  └─ preview.html     # 預覽頁 / preview page
├─ template.docx       # Word 範本檔 / Word template
├─ requirements.txt    # Python 套件需求 / dependencies
└─ README.md
```

---

## 🚀 安裝與執行 (Installation & Usage)

### 本地執行 (Local Execution)
```bash
git clone https://github.com/yourusername/learning-portfolio-generator.git
cd learning-portfolio-generator
pip install -r requirements.txt

# 設定 API Key / Set environment variable
export GEMINI_API_KEY=your_api_key_here

# 啟動伺服器 / Start server
python app.py
```
打開 [http://127.0.0.1:5000](http://127.0.0.1:5000)  

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.  

---

## 📑 後續規劃 (Future Plans)
- [ ] 新增 PDF 輸出（LibreOffice / WeasyPrint）  
  Add PDF export (LibreOffice / WeasyPrint)  
- [ ] 改善圖片處理（支援 PNG/WebP、自動壓縮）  
  Improve image handling (support PNG/WebP, auto compression)  
- [ ] 優化預覽功能（Markdown → HTML 美化）  
  Enhance preview (render Markdown to HTML)   

---
