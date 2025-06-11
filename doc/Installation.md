# Installation Instructions

## Prerequisites

- Raspberry Pi Zero 2 W
- Python 3（預設已安裝於 Raspberry Pi OS）


## Download from .zip
[offline-timetable.zip](https://github.com/user-attachments/files/20649531/offline-timetable.zip)

### 在Pi 中 解壓縮 (假設在/root中)
```bash
cd /root
unzip offline-timetable.zip
```

### 在pi 中輸入以下 code :
```bash
cd offline-timetable
python3 generate_schedule.py
python3 -m http.server 8000
```

*可透過 ls 檢查檔案是否解壓縮成功
*Default server is operation on 8000,So needs to open website with pi.ip:8000
## File Setup

1. 透過 USB、SCP、WinSCP 等方式，將以下檔案複製到 Raspberry Pi 的某個資料夾中，例如 `/root/schedule_project`：

   - `course.csv`（課表資料）
   - `generate_schedule.py`（產生網頁）
   - `index.html`（執行後自動產生）
   - `edit_schedule.sh`（一鍵修改用）
   - （可選）`upload_form.html`, `upload_server.py`（不需使用）

2. 進入資料夾：

```bash
cd /root/schedule_project
```
3.產生網頁檔：
```bash
python3 generate_schedule.py
```
### To View the Schedule
若要在區網內用瀏覽器開啟：
python3 -m http.server 8000
然後在瀏覽器中輸入：
http://<你的 Pi IP>:8000
(你可以使用以下指令查詢 IP：hostname -I)

### 更新課表

你可以用以下指令編輯並自動更新課表：
./edit_schedule.sh
或手動更新：
nano course.csv
python3 generate_schedule.py

> 本系統不使用任何伺服器端或前端框架，所有內容皆可離線運作。
