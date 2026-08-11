# 📘 FocusLingua | 項目四：架構與資料模型 (Architecture & Data Model)

> 三層怎麼分工，資料結構長什麼樣。

---

### 4.1 三層分工架構 (3-Tier Architecture)

* **展示層 (Client - Presentation)**：
  * 技術：HTML5 / CSS / React Native。
  * 職責：無延遲的視覺渲染、BGM 白噪音音效播放、接收並渲染 Web Audio API/Canvas 動畫。確保離線優先，零卡頓。
* **邏輯服務層 (Server - Application)**：
  * 技術：Node.js API Gateway / Go Microservices。
  * 職責：處理使用者認證、關卡內容分發、專注自適應演算法邏輯。
* **資料儲存層 (Database - Data Storage)**：
  * 技術：PostgreSQL + ClickHouse。
  * 職責：PostgreSQL 儲存使用者靜態資訊與進度；ClickHouse 串流寫入點擊 Latency 與專注時長以利大數據分析。

---

### 4.2 核心資料模型 (Data Schema)

#### USER (使用者偏好設定)
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    nickname VARCHAR(100),
    use_dyslexic_font BOOLEAN DEFAULT FALSE,
    bgm_type VARCHAR(50) DEFAULT 'none',
    haptic_enabled BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### PROGRESS (關卡學習進度)
```sql
CREATE TABLE progress (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    lesson_id UUID,
    accuracy_rate FLOAT,
    consecutive_days INT DEFAULT 0,
    last_played TIMESTAMP
);
```

#### FOCUS_SESSION (專注力紀錄)
```sql
CREATE TABLE focus_sessions (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    start_time TIMESTAMP,
    duration_seconds INT,
    avg_reaction_ms FLOAT,
    distraction_spikes INT -- 點擊反應延遲峰值次數
);
```
