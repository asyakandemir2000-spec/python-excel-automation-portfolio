import os
import csv

try:
    import openpyxl
except ImportError:
    print("Required dependency missing! Please run 'pip install openpyxl' in your terminal.")
    input("\nPress Enter to close...")
    exit()

CSV_FILE = "./inventory.csv"
OUTPUT_EXCEL = "./inventory_report.xlsx"

print("Initializing Inventory Automation & Reporting Engine...")

if os.path.exists(CSV_FILE):
    print("Reading inventory data from CSV...")
    
    products = []
    in_stock_count = 0
    out_of_stock_count = 0
    
    try:
        with open(CSV_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
                status = row.get("Inventory Status", "").strip()
                if status == "In Stock":
                    in_stock_count += 1
                elif status == "Out of Stock":
                    out_of_stock_count += 1

        # Create Excel Report
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Inventory Status"
        
        # Headers
        sheet.append(["Product ID", "Product Name", "Inventory Status"])
        
        # Data Rows
        for p in products:
            sheet.append([p["Product ID"], p["Product Name"], p["Inventory Status"]])
            
        # Summary rows
        sheet.append([])
        sheet.append(["Total Products", len(products)])
        sheet.append(["In Stock", in_stock_count])
        sheet.append(["Out of Stock", out_of_stock_count])
        
        workbook.save(OUTPUT_EXCEL)
        
        print("\n--- INVENTORY ANALYSIS REPORT ---")
        print(f"Total Products Processed: {len(products)}")
        print(f"In Stock: {in_stock_count} | Out of Stock: {out_of_stock_count}")
        print(f"\nSUCCESS: Summary report generated successfully at '{OUTPUT_EXCEL}'!")
        
    except Exception as error:
        print(f"Error processing CSV data: {error}")
else:
    print(f"Error: '{CSV_FILE}' not found. Please create the CSV file first.")

input("\nProcess finished! Press Enter to close this window...")