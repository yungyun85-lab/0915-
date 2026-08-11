# 📘 FocusLingua | 項目六：素材清單 (Asset Inventory)

> 資料與內容從哪裡來、怎麼整理。

---

### 6.1 視覺素材 (Visual Assets)

* **Logo 與品牌識別**：
  * `logo_focus_calm.svg`：向量標誌，使用莫蘭迪灰綠色調（減壓視覺色彩），不使用高飽和度色彩。
* **字型檔 (Fonts)**：
  * `OpenDyslexic-Regular.ttf`、`OpenDyslexic-Bold.ttf`：閱讀障礙專用字型，下載自 OpenDyslexic 官網，並託管於本地前端目錄下。
* **動畫與視覺回饋**：
  * `success_celebration.json`：Lottie 格式灑花動畫，用於 90 秒通關結算時。
  * HTML5 Canvas 動態粒子引擎：答對題目時的本地即時碰撞擴散效果，避免遠端資源載入造成的反饋延遲。

---

### 6.2 音訊素材 (Audio Assets)

* **發音音訊檔**：
  * 結合 Web Speech API 進行語音合成 (TTS) 與離線發音。
* **背景白噪音 (BGM)**：
  * `binaural_40hz_focus.mp3`：雙耳 40Hz 專注波形，由專業聲學產生器合成，並轉為 Seamless Loop 格式以確保無縫循環播放。
* **系統音效 (Sound Effects)**：
  * `success_pop.wav`：點擊成功啵啵音效，高頻、極短（<0.5s），取自 ASMR 減壓音效庫。
  * `error_buzz.wav`：低頻沉悶的錯誤提示聲，無尖銳刺耳感，減少挫敗焦慮。

---

### 6.3 觸覺素材 (Haptic Profiles)

* **Vibe patterns**：
  * `success_pattern.json`：對應 iOS CoreHaptics 與 Android AAudio API 的自訂震動設定檔（雙重輕微觸碰回饋，80ms-50ms-80ms）。
