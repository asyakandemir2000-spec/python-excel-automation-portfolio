import os
import time

try:
    import openpyxl
    from pypdf import PdfReader
except ImportError:
    print("Required dependencies missing! Please run 'pip install pypdf openpyxl' in your terminal.")
    input("\nPress Enter to close...")
    exit()

print("Initializing PDF Invoice Parser System...")
print("Scanning target directory for invoice_summary.pdf...")
time.sleep(1)

FILE_PATH = "./invoice_summary.pdf"

if os.path.exists(FILE_PATH):
    print("File found! Starting secure data extraction pipeline...\n")
    
    try:
        reader = PdfReader(FILE_PATH)
        page = reader.pages[0]
        content = page.extract_text()
        
        invoice_no = "Not Found"
        client_name = "Not Found"
        total_amount = "Not Found"
        
        for line in content.split("\n"):
            if "Invoice Number:" in line:
                invoice_no = line.split("Invoice Number:")[1].strip()
            if "Name:" in line:
                client_name = line.split("Name:")[1].strip()
            if "GRAND TOTAL:" in line:
                total_amount = line.split("GRAND TOTAL:")[1].strip()

        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Invoices"
        
        sheet.append(["Invoice No", "Client Name", "Total Amount"])
        sheet.append([invoice_no, client_name, total_amount])
        
        workbook.save("./extracted_invoices.xlsx")
        
        print("--- EXTRACTED INVOICE DATA PIPELINE ---")
        print(f"Successfully read from: {FILE_PATH}")
        print(f"Data Extracted -> ID: {invoice_no} | Client: {client_name} | Total: {total_amount}")
        print("\nSUCCESS: Data successfully converted and saved into 'extracted_invoices.xlsx'!")
        
    except Exception as error:
        print(f"Critical error during data extraction workflow: {error}")
else:
    print(f"Error: '{FILE_PATH}' not found in the directory.")
    print("Please make sure 'invoice_summary.pdf' exists in this folder from your previous project.")

input("\nProcess finished! Press Enter to close this window...")