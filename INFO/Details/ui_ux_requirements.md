# 🎨 UI / UX Requirements Document

### for *MediScan AI – Intelligent Health Diagnosis and Report Insight App*

---

## 🧭 1. UI Design Philosophy

* **Goal:** The app must look professional, modern, and easy to use for users aged 18–65.
* **Design Approach:** Minimalist medical theme — clean typography, plenty of whitespace, and trust-focused color palette.
* **Primary Colors:**

  * Light Theme: Light Aqua Blue (`#B2EBF2`)
  * Accent: Light Green (`#C8E6C9`)
  * Text: Dark Gray / Black (`#212121`)
  * Dark Mode: Deep Blue / Black (`#000`) with White Text
* **Fonts:** Sans-serif (e.g., *Poppins*, *Roboto*) for clarity.
* **Layout Type:** Card-based with rounded edges (`rounded-2xl` style) and subtle shadows.

---

## 🏗️ 2. Core Screens & Their Requirements

| Screen                       | Purpose                        | UI Elements                                                                                                         | Key Actions                                 |
| ---------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Splash Screen**            | App intro                      | App logo animation, tagline, progress indicator                                                                     | Auto-redirect to login                      |
| **Login / Register**         | Authentication                 | Google & Email sign-in buttons, simple form                                                                         | Login / Register user                       |
| **Home Dashboard**           | Overview of user’s health data | Welcome text, upload button, previous reports list, summary cards (Health Status, Risk Score, Recommendations)      | Upload report / Enter symptoms              |
| **Report Upload Screen**     | Upload PDF or image            | Upload button, drag-and-drop zone, progress bar, AI extraction loader                                               | Upload, analyze, and view extracted results |
| **Extracted Data View**      | Show extracted table & results | Dynamic data table (pandas/SQL-like grid), test charts, abnormal value highlights (red)                             | Tap row → see AI insight                    |
| **AI Insights Screen**       | Health interpretation          | Cards for “Summary,” “Risk Factors,” “Doctor Suggestions,” “Next Steps”                                             | Share or download summary                   |
| **Symptom Diagnosis Screen** | User inputs symptoms           | Text input box (multi-symptom), “Analyze Symptoms” button, results displayed as condition cards (with confidence %) | Diagnose, View Recommendations              |
| **Chat Assistant Screen**    | Conversational query           | Chat bubbles (user left, AI right), voice input button (optional), context persistence                              | Ask questions like “Is my BP high?”         |
| **History Screen**           | Past reports & comparisons     | Timeline view, small charts comparing past tests                                                                    | View, export, or delete old reports         |
| **Profile Screen**           | User details                   | Profile image, email, total reports analyzed, logout button                                                         | Edit / Delete account                       |
| **Settings Screen**          | App preferences                | Dark mode toggle, notification preferences, privacy policy                                                          | Save preferences                            |

---

## 🧩 3. Component-Level Requirements

### **A. Report Upload Component**

* Supports drag-and-drop or file picker.
* Progress bar during upload.
* File preview with name, size, and type.
* Error state: “Invalid file format. Please upload a PDF or image.”

### **B. Extracted Data Component**

* Auto-generated table view for report data.
* Highlight abnormal readings in **red**.
* Tooltip on hover → “Normal Range: 13.0–17.0 g/dL.”
* Button → “Generate Insights” triggers AI backend.

### **C. Insights Cards**

* 3–4 cards per result page:

  * **Overall Status**
  * **Detected Conditions**
  * **Doctor’s Suggestion**
  * **Next Steps**
* Color-coded:

  * 🟢 Normal
  * 🟡 Slightly Abnormal
  * 🔴 Critical

### **D. Symptom Diagnosis Component**

* Multi-input symptom field with autocomplete (e.g., “fever,” “fatigue,” “headache”).
* AI output card showing:

  * Probable condition
  * Confidence percentage
  * Precautions / suggestions

### **E. Chat Interface**

* Floating input box with microphone icon.
* User queries appear on left; AI answers on right.
* AI responses include emoji-based friendliness (💬🩺).
* Scroll to latest message automatically.

---

## 📊 4. Visualization Requirements

| Feature                | Visualization Type | Description                                    |
| ---------------------- | ------------------ | ---------------------------------------------- |
| Test Result Comparison | Line Chart         | Compare current vs previous test values        |
| Report Summary         | Pie Chart          | Proportion of Normal vs Abnormal readings      |
| Health Trend           | Bar Graph          | Changes over time (cholesterol, glucose, etc.) |
| Confidence Scores      | Progress Bar       | Visual indication of AI prediction confidence  |

---

## 📱 5. Responsiveness Requirements

* Fully responsive across **mobile (Flutter)** screens:

  * Small (5.5") to large tablets (10").
* Support for both **portrait** and **landscape** modes.
* Dynamic resizing of cards and charts.
* All text readable without horizontal scrolling.

---

## 🧭 6. Navigation Flow

**Login → Dashboard → Upload → Extracted Data → AI Insights → Chat / History / Profile**

Floating bottom navigation bar:

* 🏠 Home
* 📄 Reports
* 💬 Chat
* ⚙️ Settings

---

## ⚡ 7. Accessibility Requirements

* Support text-to-speech for visually impaired users (optional).
* Large font toggle option.
* High-contrast mode for better visibility.
* Buttons labeled with ARIA-style alt text.

---

## 💬 8. Feedback & Error States

* On successful analysis: ✅ “Report analyzed successfully.”
* On failure: ❌ “Could not process the document. Please retry.”
* AI error fallback: “We couldn’t interpret this test. Try re-uploading a clearer version.”
* Each insight card can be rated 👍 / 👎 by user to improve suggestions.

---

## 🧠 9. UI Example (User Journey)

1. **User opens app** → sees logo & tagline:
   *“Your health, decoded by AI.”*
2. **Uploads report** → sees animated progress bar.
3. **After analysis** → health table + colored insights appear.
4. **Enters symptoms** → gets quick probable diagnosis (e.g., “Dehydration likely, drink fluids”).
5. **Chats with AI assistant** → asks: “Is dehydration serious?”
6. **Downloads report summary** → saves as PDF.

---

## 🧩 10. Design Deliverables

1. High-fidelity mockups (Figma or Flutter UI).
2. UI component library (buttons, cards, modals).
3. Color palette & typography guide.
4. Sample animations for transitions (using Flutter’s `AnimatedContainer` or `Lottie`).

