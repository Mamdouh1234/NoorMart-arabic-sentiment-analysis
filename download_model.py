from huggingface_hub import hf_hub_download
import os

def download_model():
    print("⏳ Downloading model from Hugging Face...")
    repo_id = "Mamdouh-Alaa12/Arabic-Sentiment-Analysis"
    filename = "arabic_sentiment_model.keras"
    
    # This downloads the file to your current directory
    path = hf_hub_download(repo_id=repo_id, filename=filename, local_dir=".")
    print(f"✅Model downloaded successfully to: {path}")

if __name__ == "__main__":
    download_model()