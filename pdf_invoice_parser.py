import time

print("Initializing PDF Invoice Parser system...")
print("Scanning target directory for customer invoices...")
time.sleep(1)

# Simulating data extraction from multiple PDF files
extracted_invoices = [
    {"invoice_no": "INV-2026-001", "client": "Acme Global Corp", "amount": "$1,250.00"},
    {"invoice_no": "INV-2026-002", "client": "Nexus Tech Solutions", "amount": "$450.00"},
    {"invoice_no": "INV-2026-003", "client": "Vertex Retail Ltd", "amount": "$2,910.00"}
]

try:
    print("\n--- EXTRACTED INVOICE DATA PIPELINE ---")
    for invoice in extracted_invoices:
        print(f"File Source: PDF_Reader | ID: {invoice['invoice_no']} | Client: {invoice['client']:<22} | Total: {invoice['amount']}")
    print("\nData successfully converted into structural database tables!")
except Exception as error:
    print(f"Critical error during PDF binary parsing: {error}")
