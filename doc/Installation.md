# Installation Instructions


## Zipfile for Installation
[📦 點此下載 offline-timetable.zip](https://github.com/TWsimplecat/113poss-IDK/raw/main/doc/offline-timetable.zip)
## Prerequisites

Raspberry Pi Zero 2 W
Raspberry Pi OS (建議使用含桌面版)
網路連線能力
安裝好 Docker 與 Docker Compose

### Step 1: 安裝 Docker & Docker Compose
可透過以下指令在 Pi 上安裝：

```bash
sudo apt update
sudo apt install -y docker.io docker-compose
```

### Step 2: 複製專案
你可以透過 USB、SCP 或 WinSCP 將 offline-timetable 專案整包資料夾複製進 Raspberry Pi，例如：

```bash
/home/pi/offline-timetable
```
### Step 3: 啟動服務
打開終端機，進入資料夾並執行：

```bash
cd ~/offline-timetable
docker-compose build
docker-compose up -d
```
這會啟動：
MariaDB 資料庫
PHP + Apache 網頁伺服器

### Step 4: 初始化資料庫（第一次安裝）
用以下指令啟動 MariaDB 客戶端（進入資料庫）：

```bash
docker run -it --rm --network offline-timetable_default mysql:8 mysql -h test-mysql -u root -p
```
輸入密碼：root，接著建立資料表：

```sql
USE schedule_db;
CREATE TABLE schedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    day_of_week VARCHAR(10) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);
```
插入一筆課程資料：
```sql
INSERT INTO schedule (course_name, day_of_week, start_time, end_time)
VALUES ('Math', 'Monday', '09:00:00', '10:00:00');
```
### Step 5: 開啟網頁
瀏覽器中輸入：

```cpp
http://<你的Pi的IP>:8080
```
你可以看到主畫面，並使用按鈕進入：
查看課表
編輯課表（新增或刪除課程）

備註
本系統不使用任何伺服器端或前端框架，所有功能均基於 PHP + MariaDB + Docker。
所有程式皆可離線運作，只需確保區網內可訪問 Raspberry Pi。
