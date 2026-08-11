# 📱 FocusLingua | 英語學習 App 介面設計規格藍圖 v2.0
### (新增：ADHD/ADD 留存機制版)

本版在原有六大畫面基礎上，加入五項核心留存機制：**連續天數(Streak)**、**隨機化獎勵**、**微入口(Micro-entry)**、**溫柔召回**、**動態主題色**。目標是把「靜態展示進度」升級為「製造想打開 App 的衝動」。

---

## 🔑 新增機制總覽

| 機制 | 解決的問題 | 套用畫面 |
|---|---|---|
| 🔥 連續天數 Streak | 進度條只會累積、不會製造損失感 | 首頁、進度頁 |
| 🎲 隨機化獎勵 | 固定獎勵會習慣化、失去多巴胺效果 | 測驗頁 |
| 👆 微入口 | 「開始今天的單字」暗示要完成一整組任務，啟動門檻太高 | 首頁 |
| 💌 溫柔召回 | 中斷後只有「繼續上次」，沒有喚回機制 | 全新畫面：召回卡片 |
| 🎨 動態主題色 | 六畫面色調統一，長期使用容易乏味 | 全域 |

---

## 1. 首頁 (Home Screen) — 改版

### ① 新增需求
- **連續天數計數器**：畫面最上方，比進度條更顯眼，使用火焰圖示 + 天數。若使用者今天還沒學習，計數器旁顯示「保護你的紀錄」的柔性提醒（非威脅語氣）。
- **微入口按鈕**：主按鈕文字從「開始今天的單字」改為「先學 1 個字就好」，降低啟動門檻；使用者完成第 1 個字後，App 自然銜接下一個字，不需要重新點擊。
- **今日主題色**：背景色從固定薄荷綠，改為依據星期幾或連續天數里程碑輪替 5-6 組莫蘭迪色系，保留同一套排版但降低視覺疲乏。

### ② 線稿 WIREFRAME
```
+---------------------------------------+
|  [Logo] FocusLingua           (User)  |
+---------------------------------------+
|                                       |
|   🔥 連續學習 7 天  (今天還沒打卡！)      |
|                                       |
|  +---------------------------------+  |
|  |  🌟 今日進度 (Today's Progress)  |  |
|  |  [====== 60% Progress Bar =====] |  |
|  |  今日已學: 3 / 5 個單字          |  |
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  |     [ 先學 1 個字就好 (P0) ]      |  |
|  |    (大面積主導按鈕，今日主題色)      |  |
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  |           [ 繼續上次 ]          |  |
|  +---------------------------------+  |
|                                       |
|  "Take it one word at a time."        |
|                                       |
+---------------------------------------+
|  [今日任務]  [字卡]  [測驗]  [進度]      |
+---------------------------------------+
```
> 底部導覽從 5 個分頁減為 4 個，把「設定」移進右上角 icon，降低選擇項目、減少決策負擔。

### ③ PROMPT
> A high-fidelity mobile app home screen UI for FocusLingua, ADHD-friendly English learning app. At the top, a warm flame-icon streak counter shows "7 day streak" in amber. Below it, a soft progress card shows "3/5 words today". A large rounded primary button in today's rotating accent color (currently dusty rose) says "Just Learn 1 Word". A ghost button below says "Continue Last Session". Calming, low-clutter, premium mobile UI, warm and encouraging tone rather than clinical.

---

## 2. 測驗頁 (Quiz Screen) — 改版

### ① 新增需求
- **選項數固定為 3 個**（原線稿與需求文字不一致，統一收斂為 3，降低選擇負荷）。
- **隨機化獎勵系統**：答對後，系統從獎勵池中隨機抽取一種回饋，而非每次都相同：
  1. 標準版：輕微震動 + 綠色勾勾
  2. 驚喜版（約 20% 機率）：全螢幕彩帶 + 音效
  3. 幽默版（約 10% 機率）：彈出一句俏皮小評語（如「你的大腦剛剛偷偷開心了一下」）
  4. 累積版（約 10% 機率）：額外贈送 1 個「連續天數保護盾」，可在漏學一天時自動補上 streak

### ② 線稿 WIREFRAME
```
+---------------------------------------+
|  [X] 結束專注                  [⏳ 56s] |
+---------------------------------------+
|                                       |
|       +-----------------------+       |
|       |         FOCUS         |       |
|       +-----------------------+       |
|                                       |
|  +---------------------------------+  |
|  |  A. 模糊或不清晰                |  |
|  +---------------------------------+  |
|  |  B. 專注、集中注意力            |  |
|  +---------------------------------+  |
|  |  C. 忽視與遺忘                  |  |
|  +---------------------------------+  |
|                                       |
|  [答對後隨機觸發 4 種獎勵之一，見上方說明]  |
+---------------------------------------+
```

### ③ PROMPT
> A mobile quiz screen UI for FocusLingua. Three multiple-choice options (not four) for lower cognitive load. On correct answer, randomly show ONE of: a subtle checkmark micro-animation, a full-screen confetti burst, a playful text toast ("Your brain just had a tiny party"), or a shield icon indicating a streak-protection reward earned. The variability should feel like a slot-machine style surprise, not a fixed pattern.

---

## 3. 溫柔召回卡片 (Re-engagement Screen) — 全新畫面

### ① 需求
- **觸發時機**：使用者超過 48 小時未開啟 App。
- **目的**：用同理而非指責的語氣召回，避免罪惡感式推播（那類語氣通常會讓 ADHD 使用者選擇乾脆刪除 App，而不是回來）。
- **畫面元素**：
  * 溫暖插畫（不使用哭臉或警告色）
  * 文案：「你的字卡在等你，休息幾天也沒關係」
  * 顯示「你上次的連續紀錄是 7 天，現在重新開始也完全可以」，降低重啟的心理門檻
  * 單一按鈕：「先學 1 個字就好」，與首頁微入口邏輯一致

### ② 線稿 WIREFRAME
```
+---------------------------------------+
|                                       |
|          [溫暖插畫：字卡在打盹]           |
|                                       |
|      你的字卡在等你，                    |
|      休息幾天也沒關係。                   |
|                                       |
|      上次連續紀錄：7 天                  |
|      現在重新開始，也完全可以。             |
|                                       |
|  +---------------------------------+  |
|  |     [ 先學 1 個字就好 ]           |  |
|  +---------------------------------+  |
|                                       |
+---------------------------------------+
```

### ③ PROMPT
> A gentle re-engagement screen for FocusLingua, shown after a user has been away for 2+ days. Soft illustration of flashcards "napping" (no sad faces, no red warning colors). Warm copy: "Your flashcards missed you. It's okay to take breaks." Shows previous streak count with encouraging reframe. Single low-pressure CTA button "Just Learn 1 Word". Tone: compassionate, zero guilt, cozy pastel palette.

---

## 4. 進度頁 (Progress Screen) — 局部改版

### 新增元素
- 圓環進度圖旁新增「🔥 最長連續紀錄」與「目前連續天數」並列顯示，讓使用者同時看到「歷史最佳」與「現在狀態」，製造想超越自己紀錄的動機。
- 三色量化區維持原設計不變（已學/待複習/已熟悉），僅在配色上跟隨當日主題色微調。

---

## 5. 單字卡頁、複習頁、設定頁

維持原藍圖設計，僅需配合「動態主題色」全域套用當日配色，其餘互動邏輯不變。

---

## 📋 實作優先順序建議

1. **連續天數 Streak（首頁 + 進度頁）** — 影響留存率最大，且開發成本相對低
2. **隨機化獎勵（測驗頁）** — 次要優先，需要設計獎勵池與觸發機率
3. **溫柔召回畫面** — 需搭配推播通知邏輯，中期實作
4. **微入口按鈕文案** — 純文案調整，可立即上線測試
5. **動態主題色** — 視覺優化，優先順序最低，可留到 polish 階段
