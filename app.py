from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
from typing import List  # <-- Added to support lists
from utils import clean_arabic

# 1. Initialize the FastAPI app
app = FastAPI(title="Arabic Sentiment API", version="1.0")

# 2. Load the model ONCE when the server starts
# We use the end-to-end model that includes the vectorizer
MODEL_PATH = "arabic_sentiment.keras"
try:
    model = tf.keras.models.load_model(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

# The labels exactly as defined in your notebook
LABELS = ['neutral', 'positive', 'negative']

# 3. Define the expected request payload format
class SentimentRequest(BaseModel):
    text: List[str]  # <-- Changed to List[str] to support multiple texts in one request

@app.get("/")
def home():
    return {"message": "Arabic Sentiment API is running! Go to /docs for testing."}

# 4. Create the prediction endpoint
@app.post("/predict")
async def predict_sentiment(request: SentimentRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    # Clean the text using your custom logic
    cleaned_text = [clean_arabic(t) for t in request.text if t.strip()]
    
    # Predict (model expects a batch, so we wrap it in a list/numpy array)
    input_data = tf.constant(cleaned_text, dtype=tf.string)
    predictions = model.predict(input_data, verbose=0)
    
    # Extract results for the whole batch
    results = []
    for i, pred_probs in enumerate(predictions):
        class_idx = np.argmax(pred_probs)
        predicted_class = LABELS[class_idx]
        confidence = float(pred_probs[class_idx])
        
        results.append({
            "original_text": request.text[i],
            "sentiment": predicted_class,
            "confidence": round(confidence, 4),
            "probabilities": {
                "neutral": float(pred_probs[0]),
                "positive": float(pred_probs[1]),
                "negative": float(pred_probs[2])
            }
        })
    
    return {"results": results}