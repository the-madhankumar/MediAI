# 🩺 MediAI — Intelligent Health Diagnosis & Report Analysis App (status - in progress....)

## 📘 Problem Statement

In today’s fast-paced world, most people struggle to interpret complex medical reports, lab results, or numeric health metrics. Although AI assistants exist, they usually fail to understand **structured medical data** (like tables and numerical test results) and lack **personalization** — providing generic replies that don’t reflect a person’s unique health history.

**MediAI** bridges this gap by combining **document understanding**, **AI-driven health diagnosis**, and **personal health insights** — all inside a secure and user-friendly mobile application built for the public good.

---

## 🎯 Objective

To create a mobile application that enables users to:

* Upload and interpret health reports automatically.
* Receive personalized, data-driven health insights based on real test values.
* Diagnose potential health conditions from natural language symptom inputs.
* Securely store, analyze, and visualize their health progress over time.

---

## 💡 Key Features

### 🧾 1. Document Upload & Analysis

* Upload health documents (PDFs, images, or scanned reports).
* Automatic text and **table extraction** using OCR and parsing models.
* Identify key metrics like glucose, hemoglobin, cholesterol, etc.
* Generate **human-friendly explanations** of abnormal values.

**Example:**

> A user uploads a blood test report.
> MediAI identifies “Glucose – 190 mg/dL” as high and explains:
> “Your sugar level is above the normal range. Reduce sugar intake and retest in 7 days.”

---

### 🧠 2. Intelligent Query Agent

* Users can ask questions like:

  > “Was my cholesterol higher last month than this month?”
* The agent internally runs **Pandas + SQL logic** on extracted report data.
* Produces **accurate, context-aware answers**, not generic replies.

---

### 🤒 3. Symptom-Based Diagnosis

* User describes symptoms in plain language, e.g., “I feel dizzy and tired.”
* MediAI’s AI model maps symptoms to possible diseases.
* Provides severity level (mild/moderate/severe) and first-aid recommendations.

---

### 📊 4. Personalized Health Insights

* All user reports are securely stored in Firebase.
* MediAI visualizes **health trends** (e.g., blood pressure, sugar, cholesterol) over time.
* Highlights improvement or decline in any metric.

---

### 🔐 5. Secure Data Handling

* All personal medical data is encrypted and stored in the user’s Firebase account.
* No third-party API or external storage is used.
* Ensures privacy, transparency, and trustworthiness.

---

## ⚙️ Tech Stack

| Layer              | Technology                                                                 |
| ------------------ | -------------------------------------------------------------------------- |
| **Frontend**       | Flutter (Cross-platform UI Framework)                                      |
| **Backend**        | FastAPI (Python-based high-performance backend framework)                  |
| **Database**       | SQLite (Lightweight local relational database for structured medical data) |
| **AI/ML Models**   | Symptom Classifier, Health Insight Agent, Table Parser (Pandas + LLM)      |
| **PDF Extraction** | pdfplumber (Accurate extraction of tabular and textual data from reports)  |
| **Authentication** | Custom User Authentication (JWT-based or local credential system)          |

---

## 🌍 Innovation Highlights

| Challenge in Existing Systems    | How MediAI Solves It                                  |
| -------------------------------- | ----------------------------------------------------- |
| Generic chatbot answers          | Context-aware responses based on real health data     |
| Inability to read tables or PDFs | Parses structured & unstructured medical reports      |
| Lack of numeric reasoning        | Uses Pandas & SQL-based agents for calculations       |
| No personalization               | Maintains user-specific health memory securely        |
| Privacy concerns                 | Full local encryption — user controls their own data  |
| Confusing medical reports        | Converts results into easy-to-understand explanations |

---

## 🧩 Example User Flow

1. **Upload Report:** User uploads their blood test (PDF).
2. **Extraction:** MediAI reads values like:

   * Blood Sugar → 190 mg/dL
   * Cholesterol → 250 mg/dL
3. **Analysis:** AI agent compares with standard medical ranges and responds:

   > “Your sugar level is high — possible prediabetes. Consult your doctor for lifestyle advice.”
4. **Visualization:** User sees a chart comparing past and current results.
5. **Symptom Input:** User types “frequent urination, fatigue” → MediAI predicts possible conditions and gives recommendations.

---

## 📈 Impact

MediAI empowers users to **understand their health without relying on medical jargon**.
It democratizes healthcare analytics by making **AI-assisted diagnosis and interpretation accessible to everyone**, especially those without frequent access to medical professionals.

By turning raw data into meaningful health insights, MediAI promotes **preventive care**, awareness, and long-term well-being for the general public.

---

## 🧑‍💻 Contributor

**👤 Madhan Kumar M.**
*Independent Developer (AI & Backend Engineer)*


## ⚙️ Constraints for Perfect Table & Text Extraction (Using pdfplumber)

To ensure accurate and consistent data extraction from medical reports, follow the below guidelines and limitations while using **pdfplumber**. These rules help maintain clean, reliable, and structured data before storing it in the SQLite database.

---

### 🧾 1. PDF Quality Constraints

* Use **digitally generated PDFs** instead of scanned or camera-captured images.
* Avoid **handwritten or blurred text**, as pdfplumber cannot accurately detect characters or grid lines.
* If you must use scanned PDFs, perform **OCR preprocessing** using tools like `pytesseract` before extraction.

---

### 📄 2. Layout and Table Structure

* Ensure **clearly defined table grid lines** or consistent spacing between columns.
* Each row must represent a **single record** (e.g., `Test | Result | Unit | Normal Range`).
* Keep **column headers** in the first row of each table.
* Avoid merged cells, multi-line headers, or irregular spacing.
* Maintain **consistent alignment** of columns across pages for accurate parsing.

---

### 🧠 3. Extraction Process Guidelines

* Extract data **page-by-page** to handle multi-page reports efficiently.
* Choose the correct detection mode:

  * **Lattice Mode:** for tables with borders.
  * **Stream Mode:** for tables separated by spaces.
* If multiple tables exist on a single page, process them separately and combine later.
* Skip empty or invalid pages to improve performance.

---

### 📏 4. Data Formatting Standards

* Always clean and standardize extracted values by removing extra spaces or special symbols.
* Replace missing entries such as “N/A” or “—” with blank or null values.
* Store extracted data using a **uniform structure** with consistent column names like:
  **Test Name**, **Result Value**, **Unit**, **Normal Range**.
* Remove duplicate entries, headers repeated on each page, and irrelevant footer text.

---

### 📅 5. Multi-Page Report Handling

* Extract and validate each page individually, then combine all pages into a single dataset.
* Identify logical boundaries such as “End of Report” or doctor signatures.
* Merge repeating table structures seamlessly to avoid data fragmentation.

---

### 🧩 6. Error & Exception Handling

* Handle blank pages, unreadable tables, or layout errors gracefully.
* Log skipped pages for review instead of halting the entire extraction.
* Verify that all extracted tables contain the expected columns before saving.

---

### 🧪 7. Post-Processing & Validation

* Normalize column names for consistency across reports.
* Merge similar test names (e.g., “RBC” and “RBC Count”) using text-matching logic.
* Drop incomplete or invalid rows before inserting data into the database.
* Run basic validation checks:

  * Numeric results are correctly parsed.
  * Normal ranges follow standard numeric or symbol formats (e.g., “4.2–5.9”).

---

### 🧰 8. Performance Recommendations

* Process each PDF **page by page** to reduce memory usage.
* Close the file properly after parsing to release system resources.
* Define expected columns beforehand to maintain consistency across extractions.

---

### 🧠 9. Insight Preparation Rules

* Store data in SQLite with columns like **Test**, **Result**, **Unit**, **Normal Range**, and **Report ID**.
* Generate insights or health summaries **only after validation** is completed.
* Maintain consistent naming for all fields to allow accurate AI-driven queries later.

---

### 🔐 10. Privacy and Security Guidelines

* Do not log or expose full patient details in debugging or console output.
* Mask sensitive fields like patient ID, age, or location before saving.
* Delete temporary files immediately after extraction.
* Keep all data processing strictly local to maintain patient confidentiality.

---

### ⚠️ PDF Limitations

* Handwritten, scanned, or low-resolution PDFs are **not supported** directly.
* Complex layouts with **merged cells or nested tables** may reduce extraction accuracy.
* Reports with **unstructured paragraphs** instead of tables may require manual review or OCR post-processing.
* Ensure that each uploaded report follows a **consistent structure** for optimal results.
