# 本機測試專案入口，可以執行 Flask 應用
from app import create_app
import os

app = create_app()

# 確保這段程式只在直接執行該檔案時才會執行，不會在被其他模組匯入時執行 app.run()。
if __name__ == '__main__':
    # 如果本機開發，使用預設 5000；Render 部屬會從環境變數 PORT 拿值
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)
