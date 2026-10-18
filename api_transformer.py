import os
import platform

# Cross-platform safe report path in user documents
OUTPUT_LOG = os.path.expanduser("~/Documents/api_transformation_report.txt")

def generate_local_transformation_report() -> None:
    """Parses raw payload data, formats system logs, and writes them to a local report file."""
    print("Initializing JSON Data Transformer Engine (Local Offline Mode)...")
    
    # Sample raw API payload (Offline mode, zero external dependencies)
    raw_api_payload = [
        {"username": "alpha_dev", "email": "alpha@nexustech.net", "company": "Nexus Tech"},
        {"username": "beta_user", "email": "billing@vertex.org", "company": "Vertex Global"},
        {"username": "gamma_tester", "email": "manager@acme.com", "company": "Acme Corp"}
    ]
    
    try:
        print("\nParsing and transforming unstructured data payload...")
        print("\n--- TRANSFORMING LIVE JSON PAYLOAD TO SYSTEM LOGS ---")
        
        with open(OUTPUT_LOG, "w", encoding="utf-8") as log_file:
            log_file.write("==================================================\n")
            log_file.write("         LIVE API DATA TRANSFORMATION REPORT      \n")
            log_file.write("==================================================\n\n")
            
            for user_data in raw_api_payload:
                username = user_data.get("username", "Unknown")
                email = user_data.get("email", "Unknown")
                company = user_data.get("company", "Unknown")
                
                log_entry = f"STATUS CHECK -> User: {username:<15} | Email: {email:<25} | Company: {company}"
                
                print(log_entry)
                log_file.write(log_entry + "\n")
                
            log_file.write("\n==================================================\n")
            log_file.write("Log transformation completed successfully.\n")
            
        print(f"\n[SUCCESS] Document created successfully at: {OUTPUT_LOG}")
        
        # Safely open the file on Windows
        if platform.system() == "Windows":
            print("Opening the file automatically...")
            os.startfile(OUTPUT_LOG)
            
    except Exception as error:
        print(f"Transformation failed: {error}")

if __name__ == "__main__":
    generate_local_transformation_report()
    input("\nProcess finished! Press Enter to close this window...")