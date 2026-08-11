# 📱 FocusLingua | 英語學習 App 介面設計規格藍圖 v2.1
### (新增：受眾分流、句子輔助與特教教師後台模組)

本版規格書新增三項核心變革：**首頁受眾雙分流（閱讀障礙/ADHD）**、**單字卡輔助句子折疊器**、**設定頁特教教師端（學生進度追蹤與教材上傳機制）**。

---

## 🔑 v2.1 新增功能架構與效果分析

### 1. 受眾分流與句子折疊（對學習障礙學生的效果評估）
* **首頁選擇「閱讀障礙」與「ADHD」雙分流**：
  * **效果**：**極佳。** 這兩種障礙的認知瓶頸不同：ADHD 需要**防止注意力漂移與任務啟動障礙**（以計時器與隨機獎勵為主）；而閱讀障礙需要**防止字元識別疲勞與跳行**（以 OpenDyslexic、高對比、TTS 發音為主）。分流能防止對 ADHD 而言多餘的視覺輔助反而成為分心源，也防止閱讀障礙者被過度晃動的動態干擾。
* **單字卡「輔助句子折疊按鈕」**：
  * **效果**：**極佳。** ADHD 大腦在看到密密麻麻的一長串段落時會直接觸發**「任務癱瘓 (Task Paralysis)」**而放棄。採用折疊機制，預設「僅展示單字」，使用者可以自己決定是否展開例句，這將資訊負載主導權還給學生，能顯著降低焦慮。

### 2. 設定頁「教師/學生切換與教材管理」
* **學生端**：維持專注學習功能。
* **教師端**：
  * **學生學習成果看板**：檢視所有綁定學生的完成率、平均反應時間（Latency）、連續專注天數與錯題簿。
  * **自訂教材上傳**：支援上傳 CSV 或輸入單字與例句，並設定為 `公開 (Public)`（開放給全社群）或 `私人 (Private)`（僅自己班級學生可見）。

---

## 1. 首頁 (Home Screen) — v2.1 分流改版

### ① 需求 (Requirements)
* **目的**：第一次開啟 App 時，引導使用者進行分流選擇，並將選擇記錄於 User Profile。
* **畫面元素**：
  * **分流引導卡片**：
    * **左按鈕 (ADHD/專注挑戰模式)**：強調 90s 沙漏、白噪音、遊戲化多巴胺回饋。
    * **右按鈕 (閱讀障礙/視覺優化模式)**：預設啟用 OpenDyslexic 字型、寬行高、無突兀動態。
  * **今日進度、微入口與連續天數**：根據所選模式微調 UI 複雜度。

### ② 線稿 WIREFRAME
```text
+---------------------------------------+
|  [Logo] FocusLingua           (User)  |
+---------------------------------------+
|                                       |
|  🌟 請選擇最適合您的學習模式：         |
|                                       |
|  +---------------------------------+  |
|  |  🔘 ADHD 專注挑戰模式           |  |
|  |  (90s 計時器、背景白噪音、驚喜獎勵) |  |
|  +---------------------------------+  |
|  |  🔘 閱讀障礙視覺模式            |  |
|  |  (OpenDyslexic 字型、高對比字距) |  |
|  +---------------------------------+  |
|                                       |
|  [ 確定進入學習 ]                     |
|                                       |
+---------------------------------------+
```

### ③ PROMPT
> A mobile app onboarding screen UI for FocusLingua. Features a clean, soothing background. In the center, two large, friendly card-style selectors are presented side-by-side or stacked: "ADHD Focus Mode" (with an hourglass and music icon) and "Dyslexia Visual Mode" (with a large font letter A and reading ruler icon). Below them is a large primary button "Enter Learning Cabin". Distraction-free, friendly and welcoming illustration.

---

## 2. 單字卡頁 (Flashcard Screen) — v2.1 輔助句子折疊

### ① 需求 (Requirements)
* **目的**：提供單字卡片，並將句子作為「輔助工具」做成可折疊開關。
* **畫面元素**：
  * **單字正面卡**：單字 + 音標。
  * **展開句子開關 (Toggle Sentence)**：一個小眼睛或展開圖示。點擊後才由下方滑出英文例句，例句中的單字會自動高亮。

### ② 線稿 WIREFRAME
```text
+---------------------------------------+
|  < 返回                               |
+---------------------------------------+
|                                       |
|       +-----------------------+       |
|       |         FOCUS         |       |
|       |        /ˈfoʊ.kəs/       |       |
|       +-----------------------+       |
|                                       |
|  [👁️ 顯示輔助例句 (Show Sentence) ]  |
|                                       |
|  +---------------------------------+  |
|  | 例句：You need to FOCUS on your   |  |
|  | study. (點擊發音)               |  |
|  +---------------------------------+  |
|                                       |
|  [ 標記熟悉 ✔️ ]   [ 繼續學習 ❌ ]  |
+---------------------------------------+
```

### ③ PROMPT
> A mobile flashcard UI with an expandable text block. The main card shows "FOCUS" in big bold font. Below the card is an elegant outline button with an eye-icon labeled "Show Example Sentence". When clicked, a secondary soft tinted card slides out below containing: "Example: You need to FOCUS on your study." with a small audio icon next to it. Low-clutter, clean Morandi green accents.

---

## 3. 設定頁 (Settings Screen) — v2.1 教師/學生切換與教材上傳

### ① 需求 (Requirements)
* **目的**：允許特教老師切換為「教師模式」，進行班級進度追蹤與教材發佈管理。
* **畫面元素**：
  * **模式切換開關**：學生 (Student) / 教師 (Teacher) 切換 Slider。
  * **教師專屬管理面板 (切換為教師後顯示)**：
    * **學生學情追蹤 (Student Roster)**：點擊展開各學生名單，顯示完成率、平均反應時間及連續專注天數。
    * **自訂教材上傳區 (Lesson Uploader)**：
      * 文字輸入欄（單字與輔助句子）。
      * 權限單選鈕：`● 公開使用 (Public)`（所有使用者皆可下載）、`○ 私人使用 (Private)`（僅綁定該教師的學號可看）。

### ② 線稿 WIREFRAME
```text
+---------------------------------------+
|  設定與管理 (Settings & Dashboard)     |
+---------------------------------------+
|                                       |
|  身份角色設定                          |
|  模式切換： [ 學生 (Student) | 教師 (Teacher) ]|
|                                       |
|  [ 以下為教師專屬管理區 ]               |
|  👥 學生學習追蹤 (Student Dashboard)    |
|  - 王小明：進度 85% | 平均延遲 240ms   |
|  - 李小華：進度 40% | 平均延遲 410ms   |
|                                       |
|  📤 自訂教材上傳 (Upload Materials)    |
|  課程名稱: [ 基礎感官單字組-A        ] |
|  上傳 CSV: [ 選擇檔案...             ] |
|  權限設定: (● 公開共享  ○ 私人專屬)     |
|  [ 確定發布教材 ]                     |
+---------------------------------------+
```

### ③ PROMPT
> A premium mobile app settings screen for teachers in FocusLingua app. In the upper part, a segmented switch allows toggling between "Student" and "Teacher" mode. The Teacher section expands below, featuring: 1. A clean student monitoring list showing completion percentages and click latency metrics. 2. A drag-and-drop file upload section for CSV lesson plans with a permission toggle: "Public (Share with community)" / "Private (Classroom only)". Calm slate, teal, and white theme.
