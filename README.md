# 🚀 Production-Ready Python & Data Automation Portfolio

Welcome to my professional automation portfolio. This repository contains a curated collection of production-ready Python scripts engineered to optimize business workflows, automate database/spreadsheet manipulation, and establish secure data pipelines.

---

## 🛠️ Portfolio Systems & Features

### 1. 📄 Automated PDF Invoice Generation Engine (`invoice_generator_2.py`)
*   **Core Functionality:** Dynamically parses corporate dictionaries/payloads and compiles them into clean, client-ready PDF invoice documents using `reportlab`.
*   **Technical Highlights:** Granular font styling, custom corporate layout spacing, and automated local deployment.
*   **Live Output:** Generates `invoice_summary.pdf` instantly upon execution.

### 2. 🔍 PDF Invoice Parser & Ingestion Engine (`pdf_parser_2.py`)
*   **Core Functionality:** Establishes a downstream pipeline that reads structural layout schemas from binary PDF invoices and extracts critical data patterns.
*   **Technical Highlights:** Integrated with `pypdf` and `openpyxl` for seamless extraction and structured schema mapping.
*   **Live Output:** Formats and saves target fields directly into `extracted_invoices.xlsx`.

### 3. 📦 Web Scraping & Inventory Monitor Bot (`main.py`)
*   **Core Functionality:** Simulates localized e-commerce inventory monitoring by parsing data structures and evaluating real-time availability logistics.
*   **Technical Highlights:** Implements production-grade error mapping, matrix layout formatting, and secure local file writes.
*   **Live Output:** Compiles inventory records into a clean, spreadsheet-compatible `scraped_inventory.csv`.

### 4. 📊 Advanced Inventory & Excel Reporting Engine (`excel_main.py` / `inventory_processor_2.py`)
*   **Core Functionality:** Processes inventory data, generates beautifully styled professional Excel workbooks with custom headers, conditional stock status color-coding, and automated summary counts.
*   **Technical Highlights:** Built using `pandas` and `openpyxl` for high-precision spreadsheet design and error management.
*   **Live Output:** Generates professional reports like `inventory_report.xlsx`.

### 5. 🔀 JSON API Data Transformer (`api_transformer_2.py`)
*   **Core Functionality:** Parses localized raw JSON data streams, evaluates individual user statuses, and normalizes them into structured system logs.
*   **Technical Highlights:** Robust exception handling, formatting alignment, and cross-platform log generation.

---

## 💻 Tech Stack & Dependencies

*   **Language:** Python 3.x
*   **Libraries Used:** `pandas` (Data processing), `openpyxl` (Excel automation), `pypdf` (PDF manipulation), `reportlab` (PDF generation), `csv` (Data logging)

---

## ⚙️ How To Run Locally

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
   ```bash
   pip install pandas openpyxl pypdf reportlab
