print("Starting JSON API Data Transformer...")

# Simulating a raw JSON API response payload
raw_api_payload = [
    {"user": "alpha_dev", "status": "active", "access_level": "admin"},
    {"user": "beta_user", "status": "suspended", "access_level": "guest"},
    {"user": "gamma_tester", "status": "active", "access_level": "developer"}
]

try:
    print("\n--- TRANSFORMING UNSTRUCTURED JSON TO SYSTEM LOGS ---")
    for user_data in raw_api_payload:
        log_entry = f"STATUS CHECK -> User: {user_data['user']:<15} | Flag: {user_data['status'].upper():<10} | Role: {user_data['access_level']}"
        print(log_entry)
    print("\nLog transformation process completed without data leaks.")
except Exception as error:
    print(f"Transformation failed: {error}")

