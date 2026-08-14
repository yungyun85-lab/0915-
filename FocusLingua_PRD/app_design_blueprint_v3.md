# 📱 FocusLingua | 英語學習 App 介面設計規格藍圖 v3.0

依「首頁 / 學習模式(練習・測驗・程度測試) / 教師模式 / 複習 / 進度 / 設定」重新整理，每個畫面統一用①需求 ②PROMPT ③線稿 三段呈現。

---

## 0. 首次使用引導 (Onboarding)

### ① 需求
- **目的**：取代「選擇 ADHD 或 Dyslexia」這種自我診斷式選項，改用行為式問卷讓系統自行判斷呈現模式，降低使用者的標籤壓力與啟動門檻。
- **畫面元素**：
  * 帳號建立/登入（Email 或第三方登入）
  * 3-5 題感受式問句（非診斷用語），例如：「文字太多的時候，你會想直接跳過嗎？」「你比較容易因為畫面雜亂而分心，還是因為字看不清楚？」
  * 系統依回答自動設定初始字體、間距、任務長度、提醒頻率（使用者無感知）
  * 選填的極短程度測試（可跳過，跳過則從基礎難度開始，之後動態調整）

### ② PROMPT
> A warm, low-pressure onboarding flow for FocusLingua, an English learning app. Screen shows a friendly question "Do you tend to skip text when there's too much of it?" with two large tappable answer cards (not radio buttons). No diagnostic labels like ADHD or Dyslexia visible anywhere. Progress dots at top show step 2 of 4. Soft pastel background, generous whitespace, encouraging tone, no clinical or clinical-sounding language.

### ③ 線稿 WIREFRAME
```
+---------------------------------------+
|  ● ● ○ ○                    [跳過 >]  |
+---------------------------------------+
|                                       |
|   文字太多的時候，                       |
|   你會想直接跳過嗎？                     |
|                                       |
|  +---------------------------------+  |
|  |         會，容易分心              |  |
|  +---------------------------------+  |
|  +---------------------------------+  |
|  |       不會，但看太久會很累          |  |
|  +---------------------------------+  |
|                                       |
+---------------------------------------+
```

---

## 1. 首頁 (Home Screen)

### ① 需求
- **目的**：開啟 App 立刻看到今天要做什麼，零決策直接進入學習，並用連續紀錄製造想回來的動機。
- **畫面元素**：
  * 連續學習天數（火焰圖示 + 天數，今日未打卡時有柔性提醒）
  * 今日任務包摘要（系統自動組合聽說讀寫，不需使用者自選）
  * 微入口主按鈕：「先學 1 個字就好」
  * 次要按鈕：「繼續上次」
  * 底部導覽：首頁／學習模式／進度／設定（教師模式使用者看到的底部導覽不同，見第 5 節）

### ② PROMPT
> A mobile app home screen for FocusLingua. Top shows an amber flame-icon streak counter "7 day streak". Below, a card summarizes "today's task: 3 items — 1 listening, 1 flashcard set, 1 speaking". A large rounded primary button says "Just learn 1 word". A secondary ghost button says "Continue last session". Bottom nav has 4 items: Home, Learn, Progress, Settings. Calm, low-clutter, encouraging tone.

### ③ 線稿 WIREFRAME
```
+---------------------------------------+
|  FocusLingua                  (User)  |
+---------------------------------------+
|  🔥 連續學習 7 天 (今天還沒打卡)          |
+---------------------------------------+
|  +---------------------------------+  |
|  |  今日任務：3 件                  |  |
|  |  🎧 聽力 x1  🗂 字卡 x1  🗣 口說 x1 |  |
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  |     [ 先學 1 個字就好 (P0) ]      |  |
|  +---------------------------------+  |
|  +---------------------------------+  |
|  |           [ 繼續上次 ]          |  |
|  +---------------------------------+  |
+---------------------------------------+
|  [首頁]  [學習模式]  [進度]  [設定]      |
+---------------------------------------+
```

---

## 2. 學習模式 — 練習 (Practice)

### ① 需求
- **目的**：無干擾單字/技能練習，一次只呈現一項內容，答案不需要判對錯，降低壓力。
- **畫面元素**：
  * 內容卡（單字卡／聽力片段／跟讀句子，依今日任務類型切換呈現方式，但版面結構一致）
  * 朗讀按鈕（TTS，全內容皆可點擊播放）
  * **例句輔助（預設隱藏）**：卡片下方一個小的「顯示例句」按鈕，點擊後才展開例句與中文翻譯，不點就不佔畫面空間。展開後按鈕變成「隱藏例句」可再收起。目的是讓需要語境輔助的使用者能取用，但不強迫每個人都要多看一段文字——保持卡片預設的乾淨程度。
  * 底欄兩個按鈕：「熟悉／完成」「還需要多練習」

### ② PROMPT
> A minimalist practice screen for FocusLingua. One large card centered showing a single word "CALM /kɑːm/" with a speaker icon for audio playback. Below the word, a small text-link style button says "Show example sentence" — collapsed by default. When tapped, it expands inline to reveal an example sentence with Chinese translation, and the button label changes to "Hide example sentence". The expansion should push content down smoothly, not overlay. Same layout is reused for listening clips (waveform icon) and speaking prompts (mic icon) — structure stays identical, only the icon and content type change. Two buttons at bottom: "Got it" and "Need more practice". No red/wrong indicators — neutral, non-judgmental tone.

### ③ 線稿 WIREFRAME
```
收合狀態（預設）：
+---------------------------------------+
|  < 返回                    今日 2/3    |
+---------------------------------------+
|       +-----------------------+       |
|       |         CALM          |       |
|       |        /kɑːm/         |       |
|       |      [🔊 朗讀]        |       |
|       +-----------------------+       |
|                                       |
|          [ ▾ 顯示例句 ]                |
|                                       |
|  +---------------------------------+  |
|  |  [ 熟悉了 ✔️ ]   [ 還要練習 🔁 ]   |  |
|  +---------------------------------+  |
+---------------------------------------+

展開狀態（點擊後）：
+---------------------------------------+
|  < 返回                    今日 2/3    |
+---------------------------------------+
|       +-----------------------+       |
|       |         CALM          |       |
|       |        /kɑːm/         |       |
|       |      [🔊 朗讀]        |       |
|       +-----------------------+       |
|                                       |
|          [ ▴ 隱藏例句 ]                |
|  +---------------------------------+  |
|  |  Stay calm and take a breath.    |  |
|  |  保持冷靜，深呼吸一下。              |  |
|  |  [🔊 朗讀例句]                   |  |
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  |  [ 熟悉了 ✔️ ]   [ 還要練習 🔁 ]   |  |
|  +---------------------------------+  |
+---------------------------------------+
```

---

## 3. 學習模式 — 測驗 (Quiz)

### ① 需求
- **目的**：驗證學習成果，用隨機化獎勵維持新鮮感，避免固定反饋讓人習慣化。
- **畫面元素**：
  * 題目卡（單一題目，避免任務堆疊）
  * 三選一選項（非四選一，降低選擇負荷）
  * 隨機獎勵系統：答對後隨機觸發「輕微震動」「彩帶」「幽默評語」「連續天數保護盾」四種回饋之一

### ② PROMPT
> A quiz screen for FocusLingua. Large card shows the word "FOCUS" in bold dyslexia-friendly font. Below are three multiple-choice buttons (not four). On correct answer, randomly trigger one of four reward states: subtle vibration checkmark, full-screen confetti, a playful toast message, or a shield icon for streak protection — varying each time to feel unpredictable, not repetitive.

### ③ 線稿 WIREFRAME
```
+---------------------------------------+
|  [X] 結束                     ⏳ 56s   |
+---------------------------------------+
|       +-----------------------+       |
|       |         FOCUS         |       |
|       +-----------------------+       |
|  +---------------------------------+  |
|  |  A. 模糊或不清晰                |  |
|  +---------------------------------+  |
|  |  B. 專注、集中注意力            |  |
|  +---------------------------------+  |
|  |  C. 忽視與遺忘                  |  |
|  +---------------------------------+  |
+---------------------------------------+
```

---

## 4. 學習模式 — 程度測試 (Level Test)

### ① 需求
- **目的**：判定或動態調整使用者難度分級，過程不對使用者呈現「初級/中級/高級」標籤，只顯示為「幫你找到最適合的內容」。
- **畫面元素**：
  * 簡短適應性題組（依作答表現即時調整下一題難度）
  * 進度指示（用「還剩幾題」而非「你現在是什麼等級」）
  * 結束後直接導回首頁，不顯示分數，只顯示「已幫你調整好內容囉」

### ② PROMPT
> A short adaptive level-check flow for FocusLingua. Progress indicator shows "3 of 6 questions left", not a score or level label. After completion, a single confirmation screen says "We've tuned your content to fit you" with a simple checkmark illustration — no grade, percentile, or difficulty label shown to the user.

### ③ 線稿 WIREFRAME
```
+---------------------------------------+
|  找到適合你的內容            剩 3 題    |
+---------------------------------------+
|       +-----------------------+       |
|       |      題目內容區          |       |
|       +-----------------------+       |
|  +---------------------------------+  |
|  |  選項 A                        |  |
|  +---------------------------------+  |
|  |  選項 B                        |  |
|  +---------------------------------+  |
+---------------------------------------+
|         [完成後] ✔️ 已幫你調整好內容囉    |
+---------------------------------------+
```

---

## 5. 教師模式 — 教材上傳與 AI 出題

### ① 需求
- **目的**：讓教師上傳教材，AI 自動生成適合的題型草稿，但必須經教師確認才會推送給學生，避免未經把關的內容破壞既有的無障礙設計原則。
- **畫面元素**：
  * 檔案上傳區（支援 PDF/Word/圖片）
  * AI 生成中狀態提示
  * 草稿題目預覽清單，每題可編輯/刪除/調整難度
  * 「確認並發布給班級」按鈕（此步驟前題目不會出現在學生任務池）

### ② PROMPT
> A teacher-mode content screen for FocusLingua. Top has a drag-and-drop file upload zone labeled "Upload teaching material (PDF, Word, image)". Below, a list of AI-generated draft questions, each with edit and delete icons, and a difficulty tag the teacher can adjust. A prominent button at the bottom says "Confirm and publish to class" — visually distinct from the student-facing UI, denser information, more controls, efficiency-oriented layout.

### ③ 線稿 WIREFRAME
```
+---------------------------------------+
|  教材上傳                     [班級 A] |
+---------------------------------------+
|  +---------------------------------+  |
|  |     📄 拖曳檔案到此處或點擊上傳      |  |
|  +---------------------------------+  |
|                                       |
|  AI 生成題目草稿 (5 題)                 |
|  +---------------------------------+  |
|  | 1. FOCUS 的中文意思是？ [編輯][刪除] |  |
|  |    難度：[中 ▾]                  |  |
|  +---------------------------------+  |
|  | 2. ...                          |  |
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  |     [ 確認並發布給班級 ]          |  |
|  +---------------------------------+  |
+---------------------------------------+
```

---

## 6. 教師模式 — 班級/學生進度總覽

### ① 需求
- **目的**：讓教師快速掌握班級整體與個別學生的學習狀況，介面以效率與資訊密度優先，與學生端的低干擾原則相反。
- **畫面元素**：
  * 班級整體完成率摘要
  * 學生清單，顯示個別連續天數、完成率、待複習字數
  * 點擊個別學生可進入詳細報表

### ② PROMPT
> A teacher dashboard for FocusLingua showing class overview. Top summary card shows "Class average completion: 68%". Below, a table-like list of students, each row showing name, streak days, completion percentage, and words pending review. Dense, data-forward layout suited for quick scanning, unlike the sparse student-facing screens.

### ③ 線稿 WIREFRAME
```
+---------------------------------------+
|  班級總覽                     [班級 A] |
+---------------------------------------+
|  班級平均完成率：68%                    |
+---------------------------------------+
|  學生        連續天數   完成率   待複習   |
|  王小明        5天      80%      3字    |
|  李小華        0天      20%      12字   |
|  陳小美        12天     95%      1字    |
+---------------------------------------+
```

---

## 7. 複習頁 (Review Screen)

### ① 需求
- **目的**：系統自動排程間隔複習，把錯題/待複習內容排入未來的任務包，而非要求使用者自己記得回來複習。
- **畫面元素**：
  * 待複習清單（依系統排程自動浮出，非使用者手動整理）
  * 每項顯示錯誤次數（用中性色調，非紅色警示）
  * 「重新測驗」按鈕一鍵開啟微型測驗

### ② PROMPT
> A review screen for FocusLingua. List of words due for spaced review, each showing a neutral gray "missed 2x" tag instead of a red warning. A prominent button at the bottom says "Re-test these words". Gentle, organized, non-judgmental tone — the review queue is framed as scheduled practice, not as a list of failures.

### ③ 線稿 WIREFRAME
```
+---------------------------------------+
|  今日待複習 (系統已排程)                 |
+---------------------------------------+
|  +---------------------------------+  |
|  |  FOCUS          (複習 2 次) [✔️] |  |
|  +---------------------------------+  |
|  |  CALM           (複習 1 次) [✔️] |  |
|  +---------------------------------+  |
|                                       |
|  +---------------------------------+  |
|  |       [ 重新測驗這些字 ]          |  |
|  +---------------------------------+  |
+---------------------------------------+
```

---

## 8. 進度頁 (Progress Screen)

### ① 需求
- **目的**：以圖像化資料呈現成果，並同時顯示「最長連續紀錄」與「目前連續天數」，製造想超越自己的動機。
- **畫面元素**：
  * 圓環進度圖（整體完成度）
  * 連續天數對照（🔥目前 / 🏆歷史最長）
  * 三色量化區：已學／待複習／已熟悉

### ② PROMPT
> A progress dashboard for FocusLingua. Circle chart shows "75% complete". Below it, two side-by-side stat cards show "current streak: 7 days" and "longest streak: 14 days". Three metric bars below show Learned, To Review, Mastered word counts in blue, amber, and green. Encouraging, achievement-oriented tone.

### ③ 線稿 WIREFRAME
```
+---------------------------------------+
|  我的學習進度                          |
+---------------------------------------+
|              /=====\                  |
|             /  75%  \                 |
|             \=====/                   |
|                                       |
|  🔥 目前連續 7 天    🏆 歷史最長 14 天    |
|                                       |
|  已學 120 字      [藍色進度條]           |
|  待複習 15 字      [黃色進度條]          |
|  已熟悉 90 字      [綠色進度條]          |
+---------------------------------------+
```

---

## 9. 設定頁 (Settings Screen)

### ① 需求
- **目的**：集中管理語言、身份模式與個人化顯示偏好，進階自訂功能收在此頁，不干擾首頁的零決策體驗。
- **畫面元素**：
  * 語言切換（Eng / 中文）
  * 身份模式切換（學生模式 / 教師模式）
  * 個人化顯示：字體大小、行距、對比模式、TTS 開關
  * 提醒時間/頻率設定
  * 進階選項：手動選擇想加強的技能（聽/說/讀/寫），僅供想自主調整的使用者

### ② PROMPT
> A settings screen for FocusLingua. Top has a language toggle (Eng/中文) and a mode switch between "Student mode" and "Teacher mode". Below, personalization options: font size, line spacing, contrast mode, text-to-speech toggle. A reminders section for notification time. At the bottom, a collapsed "Advanced: choose skills to focus on" section for users who want manual control, clearly secondary to the rest.

### ③ 線稿 WIREFRAME
```
+---------------------------------------+
|  設定                                  |
+---------------------------------------+
|  🌐 語言        [ Eng | 中文 ]          |
|  👤 模式        [ 學生模式 | 教師模式 ]   |
+---------------------------------------+
|  🔠 字體大小     [ 小 | 中 | 大 ]         |
|  ↕️ 行距         [ 標準 | 寬鬆 ]          |
|  🎨 對比模式     [ 開啟 (🔘) ]           |
|  🔊 語音朗讀     [ 開啟 (🔘) ]           |
+---------------------------------------+
|  ⏰ 提醒時間            [ 下午 20:00 > ] |
+---------------------------------------+
|  ▾ 進階：手動選擇加強技能                 |
+---------------------------------------+
```
