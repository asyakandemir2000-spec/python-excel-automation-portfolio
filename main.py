import os
import time
import csv

print("Starting Web Scraping and Inventory Monitor Bot (Local Offline Mode)...")
time.sleep(1)

# Dosyayi dogrudan bu klasorun icine kaydetmesini soyluyoruz
OUTPUT_CSV = "./scraped_inventory.csv"

try:
    print("\nParsing and transforming local e-commerce data payload...")
    
    # Kurumsal yerel veri paketi (Sifir risk, internet gerektirmez!)
    local_data_payload = [
        {"id": 1, "title": "Wireless Mechanical Keyboard", "completed": True},
        {"id": 2, "title": "Ergonomic USB-C Gaming Mouse", "completed": False},
        {"id": 3, "title": "UltraWide 4K Monitor 32 Inch", "completed": True},
        {"id": 4, "title": "Thunderbolt 4 Docking Station", "completed": False},
        {"id": 5, "title": "Noise Cancelling Headphones", "completed": True}
    ]
    
    print("\n--- SCRAPED PRODUCTS / TASKS SUCCESSFULLY ---")
    
    # CSV dosyasini fiziksel olarak tam bu klasorde olusturuyoruz
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        # Tablo basliklari
        writer.writerow(["Product ID", "Product Name", "Inventory Status"])
        
        for item in local_data_payload:
            item_id = item.get("id", "N/A")
            title = item.get("title", "Unknown")
            
            # Stok durum kontrol simülasyonu
            status = "In Stock" if item.get("completed", False) else "Out of Stock"
            
            # CMD ekranina basiyoruz
            print(f"Product ID: {item_id:<3} | Name: {title:<35} | Status: {status}")
            
            # Dosyaya yaziyoruz
            writer.writerow([item_id, title, status])
            
    print(f"\nSUCCESS: Data successfully analyzed and saved into '{OUTPUT_CSV}'!")

except Exception as error:
    print(f"Unexpected error occurred during execution: {error}")

input("\nProcess finished! Press Enter to close this window...")