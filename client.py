import requests
import time

# The URL of your local Docker container
URL = "http://localhost:8000/predict"

# A batch of sentences to test
payload = {
    "text": [
        "المنتج ممتاز جدا وسريع",
        "خدمة العملاء سيئة للغايه",
        
        """إن الشعور بالإلهام يتدفق في داخلي كالنهر الجارف، يدفعني نحو تحقيق أهدافي بكل قوة وثبات. أشعر وكأنني اكتشفت سر الطاقة الكامنة في أعماقي، وهي طاقة لا تعرف الكلل أو الملل. كل تحدٍ أواجهه هو مجرد خطوة صاعدة على سلم النجاح، وفرصة لإثبات قدرتي على التميز والتفوق. لقد أصبحت أنظر إلى العقبات ليس كحواجز، بل كفرص ثمينة للتعلم والنمو.

اليوم هو يوم رائع للشروع في مشاريع جديدة؛ فالعقل متقد بالأفكار المبتكرة، والروح مفعمة بالحماس للمغامرة والإبداع. أجد متعة خالصة في عملية البناء والتطوير، وفي رؤية النتائج الإيجابية لعملي الجاد وتفانيّ. إن النجاح ليس مجرد نقطة وصول، بل هو رحلة مستمرة من التحسن والتطور الذاتي، وأنا أستمتع بكل تفاصيل هذه الرحلة المدهشة.

أشعر بامتنان عظيم لكل شخص وثق بي وشجعني. هذا الدعم هو الوقود الذي يجعل شعلة طموحي تزداد اشتعالًا. أنا أؤمن بأن كل شيء ممكن عندما تمتزج الرغبة الصادقة بالتخطيط المحكم والعمل الدؤوب. العالم ينتظر أن يرى ما لدي لأقدمه، وأنا على استعداد تام لأترك بصمتي الإيجابية وأحدث فرقًا حقيقيًا. المستقبل مشرق، وها أنا أستقبله بكل ثقة وإشراق!""",

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