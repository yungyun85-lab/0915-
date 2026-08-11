# 🎨 FocusLingua | Stitch UI 生成 Prompt 彙整指南

本文件專門彙整 **FocusLingua v2.0** 所有核心介面的 Stitch / AI UI 生成器專用 Prompt。您可以直接複製以下 Prompt 貼入 Stitch, v0.dev, Claude Artifacts 或其他 AI 前端生成工具中，快速產出符合 ADHD/Dyslexia 友善設計的高保真 UI。

---

## 1. 首頁 (Home Screen)
* **設計要點**：突出「微入口」按鈕，顯示火焰 Streak，使用溫和的主題色（如莫蘭迪玫瑰色/灰綠色）。

```text
A high-fidelity mobile app home screen UI for FocusLingua, an ADHD-friendly English learning app. Calming sand and white background. At the very top, a warm flame-icon streak counter shows "7 day streak" in amber orange. Below the streak, a clean container card shows today's learning progress: "3/5 words today" with a soft, glowing progress bar. In the center, a large prominent rounded primary button in a warm dusty rose color says "Just Learn 1 Word" in bold text. A smaller ghost button below says "Continue Last Session". At the bottom, a minimalist text card displaying a quote "Take it one word at a time" in low-contrast font. Distraction-free, premium mobile UI.
```

---

## 2. 單字卡頁 (Flashcard Screen)
* **設計要點**：中央單字卡使用大字距、底加重字體（模擬 OpenDyslexic），無其他雜亂按鈕，支援翻卡手勢。

```text
A minimalist mobile app flashcard screen UI for FocusLingua. The font is styled like OpenDyslexic (heavy bottom, wide letter spacing). The main word card is clean white with rounded corners, casting a soft shadow on a quiet mint green background. On the card, the English word "CALM" and its pronunciation "/kɑːm/" are displayed in dark slate color. Below the card, two intuitive tactile buttons are placed side-by-side: "Mastered" in a soft green button with a check icon, and "Still Learning" in a light outline style button. Low cognitive load, zero clutter.
```

---

## 3. 測驗與回饋頁 (Quiz & Reward Screen)
* **設計要點**：頂部放置 90s 沙漏進度，題目卡片乾淨，下方僅有 3 個選項以降低決策負荷。

```text
A high-fidelity mobile app quiz screen UI for FocusLingua. At the top, a stylized teal hourglass timer shows "5:42" remaining in a 90-second session. In the center, a large white card displays the word "FOCUS" in a bold, bottom-heavy, dyslexia-friendly font. Below the card are three minimalist multiple-choice option buttons (A, B, C) with wide padding. On the correct choice selection, show a visual representation of haptic ripple feedback and confetti particles bursting around the card. Tone is warm, encouraging, and game-like.
```

---

## 4. 溫柔召回頁 (Re-engagement Screen)
* **設計要點**：用溫馨插畫與同理心文案，避免警告色，提供一鍵「只學1個字」的超低心理阻力按鈕。

```text
A gentle re-engagement screen for FocusLingua app, shown after a user has been away for 2+ days. Features a soft pastel illustration of a cute flashcard character "napping" cozy under a blanket (no sad faces, no red warning colors). Warm copy in dark slate: "Your flashcards missed you. It's okay to take breaks." Shows a message about their previous 7-day streak with encouraging reframe: "Ready to start again? No pressure." A single large primary button at the bottom says "Just Learn 1 Word". Calming cozy aesthetic.
```

---

## 5. 進度統計頁 (Progress Screen)
* **設計要點**：使用圓環圖表呈現，並列展示「歷史最佳紀錄」與「目前天數」，三色區塊分明。

```text
A high-fidelity mobile app progress dashboard UI for FocusLingua. In the upper half, it features a clean circular donut progress chart displaying "75% Complete" in the center. Below the chart, three cards show progress metrics with light colored progress bars: "Learned: 120 words" with a teal bar, "To Review: 15 words" with a soft yellow bar, and "Mastered: 90 words" with a green bar. Under the stats, show two columns: "Best Streak: 14 Days" and "Current Streak: 7 Days" with small flame icons. Slate, white, and teal colors. Premium clean design.
```

---

## 6. 設定偏好頁 (Settings Screen)
* **設計要點**：自訂偏好開關，開關按鈕圓潤大顆防誤觸，字體大且間距寬。

```text
A clean mobile settings screen UI for FocusLingua app. Contains option lists with large toggle switches and segmented controls: "Daily Word Count" (shows input selector), "Daily Reminder Time", and a segment selector for "Translation Explanations" (English-Chinese / English Only). Below are sensory toggles: "Haptic Vibration Strength" (Light / Medium / Off) and "Focus Background Noise" (Binaural 40Hz / Pink Noise / Off). Standard slate and white premium clean theme, large easy-to-tap targets.
```
