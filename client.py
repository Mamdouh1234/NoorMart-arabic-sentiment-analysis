import requests
import time

# The URL of your local Docker container
URL = "http://localhost:8000/predict"

# A batch of sentences to test
payload = {
    "text": [
        "المنتج ممتاز جدا وسريع",
        "خدمة العملاء سيئة للغايه",
        "تطبيق رائع شكرا لكم",
        "لا يعمل بشكل جيد وتجربة محبطة"
    ]
}

def test_api():
    print("🚀 Sending batch request to Arabic Sentiment API...")
    
    start_time = time.time()
    try:
        response = requests.post(URL, json=payload)
        response.raise_for_status() # Check for HTTP errors
        
        end_time = time.time()
        results = response.json().get("results", [])
        
        print(f"✅ Success! Processed {len(payload['text'])} sentences in {end_time - start_time:.4f} seconds.\n")
        
        for res in results:
            print(f"Text: {res['original_text']}")
            print(f"Sentiment: {res['sentiment']} (Confidence: {res['confidence']:.2f})\n")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ API Connection Failed: {e}")

if __name__ == "__main__":
    test_api()