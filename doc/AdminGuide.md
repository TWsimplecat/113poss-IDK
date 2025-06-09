2.1 資料庫備份與還原
為了避免資料丟失，應定期備份 course.db 資料庫。你可以使用以下指令將資料庫檔案複製到備份位置：

bash
複製
cp course.db /path/to/backup/course_backup.db
若要還原資料庫，可以將備份檔案複製回原位置：

bash
複製
cp /path/to/backup/course_backup.db course.db
2.2 定期檢查 CSV 匯入格式
如果使用者經常匯入 CSV，請定期檢查 CSV 格式是否正確，以確保資料匯入不會出現錯誤。

day 欄位必須是 一 到 五，對應星期

time 欄位必須是 HH:MM-HH:MM 格式

2.3 清理不必要的檔案
定期清理 uploads/ 資料夾，刪除不再需要的 CSV 上傳檔案。

避免在 GitHub 上上傳 course.db 等資料庫檔案，這樣能保護資料並減少不必要的文件被公開。

2.4 更新 Python 套件
定期更新 Python 套件，保持應用在最新狀態：

bash
複製
pip freeze > requirements.txt
pip install --upgrade -r requirements.txt
3. Troubleshooting
這部分列出一些常見問題及解決方法。

3.1 應用無法啟動
如果你遇到應用無法啟動的情況，檢查以下幾點：

確認 app.py 中的 Flask 配置是否正確

確認資料庫 course.db 是否存在，並且有正確的權限

如果是部署模式，檢查 Gunicorn 或其他伺服器的設定

3.2 資料匯入問題
如果匯入 CSV 時發生錯誤，檢查以下問題：

確認 CSV 格式正確

確認 course.db 是否有足夠的空間來儲存新資料

檢查資料庫欄位名稱是否正確（如 day, time, subject 等）

3.3 網頁無法正確顯示
確認 HTML 檔案是否有錯誤或格式問題

檢查 static/ 資料夾中的資源（如 CSS、JS 是否正確加載）

如果使用其他伺服器（如 Gunicorn），檢查伺服器設定是否正確

4. 結語
這份指南將幫助管理員順利配置與維護課表系統。建議定期檢查系統、更新套件，並做好資料庫備份，保持應用穩定運行。

