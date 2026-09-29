import urllib.request
import json

print("Starting web scraping bot...")

# Target test URL for e-commerce simulation
url = "https://typicode.com"

try:
    # Connecting to the website and fetching data safely with custom User-Agent
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode())
    
    # Processing and listing the scraped data
    print("\n--- SCRAPED PRODUCTS / TASKS SUCCESSFULLY ---")
    for item in data[:10]: # Listing the first 10 items
        status = "In Stock" if item['completed'] else "Out of Stock"
        print(
            f"Product ID: {item['id']} | "
            f"Product Name: {item['title'][:30]}... | "
            f"Status: {status}"
        )
    print("\nData successfully analyzed and displayed!")

except Exception as error:
    print(f"Error occurred during execution: {error}")

