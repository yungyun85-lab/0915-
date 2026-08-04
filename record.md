# 📝 個人學習與專案開發紀錄 (Development & Learning Record)

> **建立日期**：2026-07-21  
> **專案名稱**：個人求職靜態作品集網站 (Personal Portfolio Website)  
> **專案路徑**：`/Users/annamei/notes`

---

## 📑 目錄
1. [CLI 基礎指令學習筆記](#1-cli-基礎指令學習筆記)
2. [個人求職作品集開發紀錄](#2-個人求職作品集開發紀錄)
3. [專案目錄結構](#3-專案目錄結構)
4. [未來優化與部署計畫](#4-未來優化與部署計畫)

---

## 1. CLI 基礎指令學習筆記

| 指令 | 說明 | 範例與實際操作結果 |
| :--- | :--- | :--- |
| `mkdir` | 建立新資料夾 | `mkdir notes` (建立了 `notes` 專案目錄) |
| `touch` | 建立空白檔案 | `touch week1.md` |
| `echo` | 寫入文字內容至檔案 | `echo "今天學 CLI" > week1.md` |
| `cp` | 複製檔案 | `cp a.md b.md` (保留原檔並複製出 `b.md`) |
| `mv` | 移動或重命名檔案 | `mv a.md c.md` (將 `a.md` 重命名為 `c.md`) |
| `code` | 使用 VS Code 開啟目錄 | `code .` (需在 PATH 中配置 VS Code 命令) |

---

## 2. 個人求職作品集開發紀錄

為尋求軟體開發/前端工程新職缺，於 `notes` 目錄中構建了完整且具備現代視覺感的 **完全靜態個人作品集網頁**。

### 🎨 視覺與設計亮點
* **設計風格**：採用現代深色質感主題 (Modern Dark Mode)、玻璃擬態 (Glassmorphism)、漸層霓虹色彩與微互動動畫。
* **主題切換**：支援一鍵切換深色/淺色模式 (Dark/Light Mode)，並自動儲存至 LocalStorage。
* **無 Placeholder 圖片**：使用 AI 算圖生成 3D 高畫質個人頭像與 2 個精選專案展示圖。

### 🛠️ 網站功能模組
* **Hero 區塊**：亮眼標題、個人簡介、重點數據統計 (4+年經驗、15+專案、99.8%穩定度) 與雙 CTA 按鈕。
* **核心優勢 (About Me)**：展示技術底蘊、UI/UX 敏銳度與敏捷解決問題能力。
* **技能地圖 (Skills & Tools)**：具備前端、後端與工具分類標籤篩選，滾動時觸發動態進度條動畫。
* **精選作品 (Projects)**：包含 Quantum Analytics 數據儀表板與 Synapse AI 平台，支援彈出式詳細資訊 Modal 視窗。
* **經歷時間軸 (Milestones)**：清晰列出過往工作經歷與量化貢獻。
* **聯絡資訊 (Contact)**：一鍵複製 Email 地址、社群連結與發送互動表單 (含 Toast 提示)。

---

## 3. 專案目錄結構

```text
/Users/annamei/notes/
├── index.html        # 語意化 HTML5 靜態頁面主結構
├── style.css         # CSS3 設計系統 (包含 CSS 變數與動畫)
├── script.js         # JavaScript 互動邏輯 (主題切換、篩選、Modal、Toast)
├── record.md         # 本開發紀錄檔案
├── week1.md          # CLI 練習檔案 ("今天學 CLI")
├── b.md / c.md       # CLI 複製與移動練習檔
└── assets/           # 靜態影像資源
    ├── avatar.jpg    # 3D 個人頭像
    ├── project1.jpg  # Quantum Analytics 專案預覽圖
    └── project2.jpg  # Synapse AI 專案預覽圖
```

---

## 4. 未來優化與部署計畫

- [ ] **內容客製化**：填入真實姓名、個人聯絡 Email、LinkedIn/GitHub 網址。
- [ ] **安裝 Git**：在 Mac 完成 Xcode Command Line Tools 安裝後，進行 Git 初始化與版本控制。
  ```bash
  git init
  git add .
  git commit -m "feat: 新增個人求職靜態作品集網站"
  ```
- [ ] **免費線上部署**：將專案部署至 **GitHub Pages** 或 **Vercel**，取得公開瀏覽網址以供履歷附檔使用。

---

*紀錄生成於 Google Antigravity AI Pair Programming Session*
