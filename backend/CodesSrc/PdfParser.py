import pdfplumber
import pandas as pd

pdf_path = r"D:/projects/Project MediAI/Data/Medical_Report.pdf"

all_clean_text = []
all_tables = []

with pdfplumber.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        tables = page.extract_tables()
        if tables:
            for t_idx, table in enumerate(tables):
                df = pd.DataFrame(table)
                all_tables.append({
                    "page": page_number,
                    "table_index": t_idx,
                    "data": df
                })

        table_bboxes = [table_obj.bbox for table_obj in page.find_tables()]

        words = page.extract_words()

        non_table_words = []
        for w in words:
            x0, top, x1, bottom = w["x0"], w["top"], w["x1"], w["bottom"]
            inside_table = any(
                (x0 >= bbox[0] and x1 <= bbox[2] and top >= bbox[1] and bottom <= bbox[3])
                for bbox in table_bboxes
            )
            if not inside_table:
                non_table_words.append(w)

        clean_text = " ".join([w["text"] for w in non_table_words])
        all_clean_text.append({
            "page": page_number,
            "text": clean_text
        })

print("\n================ TABLES ================\n")
for tbl in all_tables:
    print(f"Page {tbl['page']} - Table {tbl['table_index']}")
    print(tbl["data"], "\n")

print("\n================ TEXT CONTENT ================\n")
for page_text in all_clean_text:
    print(f"\n----- Page {page_text['page']} Text -----\n")
    print(page_text["text"])
