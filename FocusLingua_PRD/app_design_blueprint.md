# 📱 FocusLingua | 英語學習 App 介面設計規格藍圖 (App Design Blueprint)

本規格藍圖針對 **FocusLingua**（注意力障礙與閱讀障礙友善英語學習 App）的六大核心畫面，分別定義其「需求規格」、「AI 生成 Prompt」、「ASCII 線框圖」以及「高保真 UI 說明」，以利進行下一階段的程式碼實作。

---

## 1. 首頁 (Home Screen)

### ① 需求 (Requirements)
* **目的**：讓注意力不易集中的使用者在開啟 App 時能一眼看清當前狀態，並提供低阻力的學習入口，降低啟動成本。
* **畫面元素**：
  * **今日進度看板**：顯示今日已學單字數與目標進度條（例：今日已學 3/5 個單字）。
  * **主動按鈕（開始今天的單字）**：大面積、高對比的視覺按鈕。
  * **次要按鈕（繼續上次）**：供中斷後快速重回上次進度。
  * **每日一句減壓卡片**：一句溫慢的英語激勵短句。

### ② PROMPT (for Stitch / UI Generator)
> A high-fidelity mobile app home screen UI for FocusLingua, an ADHD-friendly English learning app. Calming teal and white palette. Features a clean card at the top showing "Today's Progress: 3/5 words" with a soft blue progress bar. In the center, a prominent rounded button says "Start Today's Words" in vibrant teal gradient. Below it, a smaller ghost button says "Continue Last Session". At the bottom, a minimalist text card says "Take it one word at a time". Distraction-free, modern, premium UI.

### ③ 線稿 WIREFRAME (ASCII Layout)
```text
+---------------------------------------+
|  [Logo] FocusLingua           (User)  |
+---------------------------------------+
|                                       |
|  +---------------------------------+  |
|  |  🌟 今日進度 (Today's Progress)  |  |
|  |  [====== 60% Progress Bar =====] |  |
|  |  今日已學: 3 / 5 個單字          |  |
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  |       [ 開始今天的單字 (P0) ]      |  |
|  |        (大面積主導按鈕，漸層色)     |  |
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  |           [ 繼續上次 ]          |  |
|  +---------------------------------+  |
|                                       |
|  "Take it one word at a time."        |
|                                       |
+---------------------------------------+
|  [首頁]  [字卡]  [測驗]  [複習]  [設定]  |
+---------------------------------------+
```

### ④ STITCH MOCK UP
* **視覺特徵**：背景採用清爽的 `#f8fafc` 減壓灰底，字體採用加粗的黑體，提高視覺抓取度。進度條有發光呼吸燈特效，點擊「開始」時按鈕會有縮放彈彈回饋。

---

## 2. 單字卡頁 (Flashcard Screen)

### ① 需求 (Requirements)
* **目的**：提供無干擾的單字記憶卡，透過「翻卡」與「標記熟悉」協助閱讀障礙者高效吸收。
* **畫面元素**：
  * **大字體單字卡**：中央展示大單字，可點擊朗讀。
  * **正面/反面翻頁機制**：點擊卡片觸發旋轉翻卡（正面：英文單字與音標；反面：中文解釋與英文例句）。
  * **底欄按鈕**：
    * 左下按鈕：`標記熟悉`（標記後移出今日新單字庫）。
    * 右下按鈕：`不熟悉/下一個`。

### ② PROMPT (for Stitch / UI Generator)
> A minimalist mobile app flashcard screen UI for FocusLingua. The font is styled like OpenDyslexic (heavy bottom, wide letter spacing). The card is clean white with rounded corners on a soft mint green background. On the card, the word "CALM /kɑːm/" is displayed in dark teal. Below are two intuitive control buttons: "Mastered" in soft green with a check icon, and "Still Learning" in outline style. Distraction-free, focusing on one single word.

### ③ 線稿 WIREFRAME (ASCII Layout)
```text
+---------------------------------------+
|  < 返回                               |
+---------------------------------------+
|                                       |
|       +-----------------------+       |
|       |                       |       |
|       |         CALM          |       |
|       |        /kɑːm/         |       |
|       |                       |       |
|       |       ( 點選翻卡 )     |       |
|       +-----------------------+       |
|                                       |
|       [🔊 朗讀發音] [🎧 專注噪音]       |
|                                       |
|  +---------------------------------+  |
|  |  [ 標記熟悉 ✔️ ]   [ 繼續學習 ❌ ]  |
|  +---------------------------------+  |
|                                       |
+---------------------------------------+
```

### ④ STITCH MOCK UP
* **視覺特徵**：點選卡片時會有 3D 翻轉動畫（卡片背面倒角加重，排版清晰）。字體可由使用者隨時在設定中一鍵轉為閱讀障礙字型，提升字母區辨度。

---

## 3. 測驗頁 (Quiz Screen)

### ① 需求 (Requirements)
* **目的**：即時驗證學習成果，強調無延遲的視覺觸覺多巴胺反饋。
* **畫面元素**：
  * **題目卡**：展示待測試的英文單字。
  * **四選一選項區**：提供四個釋義選項。
  * **回饋動態**：答對時噴發大量彩帶粒子並發出啵啵聲；答錯時卡片震動並維持紅色提示。

### ② PROMPT (for Stitch / UI Generator)
> A high-fidelity mobile app quiz screen UI for FocusLingua. At the top, a stylized teal hourglass timer shows "5:42". In the center, a large white card displays the word "FOCUS" in a bold, bottom-heavy, dyslexia-friendly font. Below the card are three minimalist multiple choice buttons. The design is modern, premium, and distraction-free.

### ③ 線稿 WIREFRAME (ASCII Layout)
```text
+---------------------------------------+
|  [X] 結束專注                  [⏳ 56s] |
+---------------------------------------+
|                                       |
|       +-----------------------+       |
|       |                       |       |
|       |         FOCUS         |       |
|       |                       |       |
|       +-----------------------+       |
|                                       |
|  +---------------------------------+  |
|  |  A. 模糊或不清晰                |  |
|  +---------------------------------+  |
|  |  B. 專注、集中注意力 (Correct)  |  |
|  +---------------------------------+  |
|  |  C. 忽視與遺忘                  |  |
|  +---------------------------------+  |
|                                       |
+---------------------------------------+
```

### ④ STITCH MOCK UP
* **實體畫面輔助**：
  * [關卡測驗畫面](../assets/focuslingua_learning_ui.jpg)
  * [答對慶賀畫面](../assets/focuslingua_victory_ui.jpg)

---

## 4. 複習頁 (Review Screen)

### ① 需求 (Requirements)
* **目的**：彙整使用者在測驗中答錯的字，給予集中二次曝光機會，加深記憶。
* **畫面元素**：
  * **錯題單字卡清單**：列出所有錯誤單字與答錯次數（例：`FOCUS - 錯題 2 次`）。
  * **重新測驗按鈕**：一鍵開啟「錯題加強包」進行微型測驗。
  * **標記已熟悉**：在此手動將錯題從複習清單中移除。

### ② PROMPT (for Stitch / UI Generator)
> A mobile app review and correction book UI for FocusLingua. Uses a gentle slate and light blue theme. A list displays incorrect words, such as "FOCUS" with a tiny red indicator showing "Failed 2x". Next to each word is a small checkmark button to "Mark as Mastered". At the bottom, a prominent blue button says "Re-Test Errors". Modern, highly organized interface.

### ③ 線稿 WIREFRAME (ASCII Layout)
```text
+---------------------------------------+
|  錯題複習簿 (Review Book)               |
+---------------------------------------+
|                                       |
|  +---------------------------------+  |
|  | ❌ FOCUS          (答錯 2 次) [✔️] |
|  +---------------------------------+  |
|  | ❌ CALM           (答錯 1 次) [✔️] |
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  |       [ 重新測驗錯題 (P0) ]        |  |
|  +---------------------------------+  |
|                                       |
+---------------------------------------+
|  [首頁]  [字卡]  [測驗]  [複習]  [設定]  |
+---------------------------------------+
```

### ④ STITCH MOCK UP
* **視覺特徵**：採用溫和的卡片式條列排版，將錯題按時間序或錯誤頻率高低排列。點選「標記已熟悉」時，卡片會以向右滑出的特效消失。

---

## 5. 進度頁 (Progress Screen)

### ① 需求 (Requirements)
* **目的**：以圖像化數據（非密集數字）展示學習成果，給予過動症學習者視覺化的成就激勵。
* **畫面元素**：
  * **圓環進度圖**：顯示當前學習總進度（如 75% 已完成）。
  * **量化指標三色區**：
    * **已學 (Learned)**：累計學習的單字總量（搭配藍色進度條）。
    * **待複習 (To Review)**：錯題與待加強單字數（搭配黃色進度條）。
    * **已熟悉 (Mastered)**：已內化熟記的單字數（搭配綠色進度條）。

### ② PROMPT (for Stitch / UI Generator)
> A high-fidelity mobile app progress dashboard UI for FocusLingua. Features a clean circle chart showing "75% Complete". Below it, three cards show progress metrics: "Learned: 120 words" with a blue progress bar, "To Review: 15 words" with a yellow bar, and "Mastered: 90 words" with a green bar. Modern, friendly, encouraging UI.

### ③ 線稿 WIREFRAME (ASCII Layout)
```text
+---------------------------------------+
|  我的學習進度 (My Progress)             |
+---------------------------------------+
|                                       |
|                /=====\                |
|               /   75% \               |
|               |  已完成|               |
|               \       /               |
|                \=====/                |
|                                       |
|  +---------------------------------+  |
|  | ⭐ 已學 (Learned)         120 字  |
|  | [===========藍色進度條==========] |
|  +---------------------------------+  |
|  | 🔄 待複習 (To Review)     15 字   |
|  | [==黃色進度條==]                  |
|  +---------------------------------+  |
|  | 檢 已熟悉 (Mastered)      90 字   |
|  | [=========綠色進度條========]     |
|  +---------------------------------+  |
|                                       |
+---------------------------------------+
|  [首頁]  [字卡]  [測驗]  [複習]  [設定]  |
+---------------------------------------+
```

### ④ STITCH MOCK UP
* **實體畫面輔助**：
  * [學習進度統計畫面](../assets/focuslingua_progress_ui.jpg)

---

## 6. 設定頁 (Settings Screen)

### ① 需求 (Requirements)
* **目的**：提供學習節奏與介面偏好的深度自訂，滿足學習障礙者多元的感官補償偏好。
* **畫面元素**：
  * **每日學習目標**：自訂每日學習單字量（如 5 字 / 10 字 / 20 字）。
  * **提醒時間 (Push Notification)**：設定每日專注提醒鬧鐘。
  * **中英解釋切換模式**：可開關「全英文釋義」或「中英雙語釋義」，以降低視覺繁雜度。
  * **感官功能開關**：震動強度開關、專注背景音樂主題選擇（雙耳節拍/粉紅噪音/靜音）。

### ② PROMPT (for Stitch / UI Generator)
> A clean mobile settings screen UI for FocusLingua app. Contains option lists with toggle switches: "Daily Word Count" (shows input selector), "Daily Reminder Time", and a segment selector for "Explanations" (English-Chinese / English Only). Below are sensory toggles: "Haptic Vibration Strength" and "Focus Background Noise". Standard slate and white premium clean theme.

### ③ 線稿 WIREFRAME (ASCII Layout)
```text
+---------------------------------------+
|  設定與偏好 (Settings)                 |
+---------------------------------------+
|                                       |
|  📊 學習目標                           |
|  每日單字量      [ 5 字 | 10 字 | 20 字] |
|                                       |
|  ⏰ 通知設定                           |
|  每日提醒時間            [ 下午 20:00 > ] |
|                                       |
|  🌐 顯示偏好                           |
|  翻譯解釋      (● 中英對照  ○ 僅英文)    |
|                                       |
|  🎧 感官整合                           |
|  閱讀障礙字型            [ 開啟  (🔘) ] |
|  答對震動反饋            [ 輕微  (🔘) ] |
|  專注背景噪音            [ 40Hz雙耳節拍 ]|
|                                       |
+---------------------------------------+
|  [首頁]  [字卡]  [測驗]  [複習]  [設定]  |
+---------------------------------------+
```

### ④ STITCH MOCK UP
* **視覺特徵**：開關鈕（Toggle）與分段選擇器（Segmented Control）設計圓潤好按，符合特教介面防誤觸規格。所有文字字距、行高皆預設放大 1.25x 以優化視覺追蹤。
