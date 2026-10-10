import os

# WINDOWS ENGELINI %100 ASAN LOKAL RAPOR YOLU
# Dosyayi hicbir izne takilmayan Kullanici Belgelerim klasorune zorla yazar
OUTPUT_LOG = os.path.expanduser("~/Documents/api_transformation_report.txt")

def generate_local_transformation_report():
    print("Initializing JSON Data Transformer Engine (Local Offline Mode)...")
    
    # Kurumsal ham veri paketi (Internet baglantisi gerektirmez, sifir risk!)
    raw_api_payload = [
        {"username": "alpha_dev", "email": "alpha@nexustech.net", "company": "Nexus Tech"},
        {"username": "beta_user", "email": "billing@vertex.org", "company": "Vertex Global"},
        {"username": "gamma_tester", "email": "manager@acme.com", "company": "Acme Corp"}
    ]
    
    try:
        print("\nParsing and transforming unstructured data payload...")
        print("\n--- TRANSFORMING LIVE JSON PAYLOAD TO SYSTEM LOGS ---")
        
        # Rapor dosyasini tamamen guvenli konumda olusturuyoruz
        with open(OUTPUT_LOG, "w", encoding="utf-8") as log_file:
            log_file.write("==================================================\n")
            log_file.write("          LIVE API DATA TRANSFORMATION REPORT     \n")
            log_file.write("==================================================\n\n")
            
            for user_data in raw_api_payload:
                username = user_data.get("username", "Unknown")
                email = user_data.get("email", "Unknown")
                company = user_data.get("company", "Unknown")
                
                log_entry = f"STATUS CHECK -> User: {username:<15} | Email: {email:<25} | Company: {company}"
                
                # Hem ekrana basiyoruz
                print(log_entry)
                # Hem de dosyaya yaziyoruz
                log_file.write(log_entry + "\n")
                
            log_file.write("\n==================================================\n")
            log_file.write("Log transformation completed successfully.\n")
            
        print(f"\n[SUCCESS] Document created successfully!")
        print(f"Opening the file automatically right now...")
        
        # DOSYAYI ANINDA GOZUNUN ONUNDE ACAR (Windows Not Defteri ile)
        os.startfile(OUTPUT_LOG)
        
    except Exception as error:
        print(f"Transformation failed: {error}")

# Run the local pipeline
generate_local_transformation_report()
input("\nProcess finished! Press Enter to close this window...")
