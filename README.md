📋 To-do List 會員任務管理系統

✨ 一個基於 Flask 開發的待辦事項管理網站，具備會員註冊、登入、登出功能，並可進行待辦清單的新增、修改、刪除及任務狀態的切換(完成/未完成)。

🚀 專案簡介

本專案主要目的是練習使用 Flask 架構開發小型完整應用，學習後端與資料庫整合、會員驗證保護、網站前後端基本互動，以及環境變數的安全管理。

🛠️ 核心功能

◆  會員系統

  ●  使用者註冊 / 登入 / 登出

  ●  密碼加密（bcrypt）

  ●  Session 維持登入狀態
  

◆  任務管理

  ●  新增待辦事項

  ●  編輯待辦事項

  ●  切換完成 / 未完成狀態

  ●  刪除待辦事項
  

◆  系統設計

  ●  Blueprint 模組化架構

  ●  dotenv 管理環境變數

  ●  MySQL 資料庫連接與操作

  ●  自訂裝飾器保護路由（登入驗證）
  

🗂️ 專案結構

To-do_list_online-server/

wsgi.py                  # 啟動 Flask 應用(正式網路窗口)

run.py                  # 啟動 Flask 應用 (本機測試用)

init_db.py               # 初始化資料庫

config.py                # Flask設定及DB設定

.env                     # 環境變數（敏感資料）

requirements.txt         # 套件需求

LICENSE                  # 授權說明

README.md                # 專案介紹文件

Procfile                 # 應用程式啟動命令

app/

__init__.py          # 建立 Flask App，註冊 Blueprint

..routes/

__init__.py

auth.py          # 會員註冊與登入功能

todo.py          # 待辦清單功能

main.py          # 首頁邏輯

..utils/

__init__.py      

 decorators.py    # 登入驗證裝飾器
 
..static/

style.css        # 網頁樣式

..templates/

base.html        # 共用基礎模板

register.html    # 註冊頁面

login.html       # 登入頁面

dashboard.html   # 待辦事項頁面

edit.html        # 編輯待辦事項頁


⚙️ 安裝與執行

1. 複製專案
   
   git clone https://github.com/PoJungHsiao/To-do_list_online-server.git
   
   cd To-do_list_online-server

2. 建立虛擬環境並安裝套件
   
    python -m venv venv
  
    venv\Scripts\activate   # Windows
  
    source venv/bin/activate # macOS / Linux

    pip install -r requirements.txt

3. 建立 .env 檔案(參數由railway建立資料庫時產生)
   
    SECRET_KEY=你的隨機字串
  
    DB_HOST=你的 DB Host
  
    DB_PORT=你的DB Port 號
  
    DB_USER=你的DB使用者
  
    DB_PASSWORD=你的DB密碼
  
    DB_NAME=你的DB名字

4. 初始化資料庫
   
     python init_db.py

5. 啟動應用
   
     python run.py (測試用)

🧠 學到的技術

●  Flask 框架基本使用

●  Blueprint 模組化開發

●  MySQL 資料庫設計與操作

●  Session 管理

●  密碼加密與認證流程

●  使用 dotenv 保護敏感資料

●  網頁版面基礎設計（HTML + CSS）

●  使用 Railway 建立雲端資料庫

●  使用 Render 做網頁部署

📜 授權

本專案遵循 MIT License。

📎 專案連結
https://to-do-list-ucnc.onrender.com

🧑‍💻 作者

GitHub: PoJungHsiao(https://github.com/PoJungHsiao)

Email: happy10246308@gmail.com


