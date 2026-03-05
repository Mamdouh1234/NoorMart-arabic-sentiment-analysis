# 🚀 NoorMart: Production-Ready Arabic Sentiment Analysis

AI-powered Arabic sentiment analysis system for multiclass customer feedback classification (positive, negative, neutral) enabling data-driven business insights.

## Business Scenario
In the fast-paced world of e-commerce, NoorMart, a rapidly scaling platform operating across the MENA region receives over 150,000 customer interactions daily. This feedback is scattered across App Store reviews, Twitter (X) mentions, and direct support tickets. Currently, analyzing this localized, dialect-heavy Arabic feedback is a highly manual, slow, and expensive process. By the time a human agent spots a viral complaint regarding a delayed delivery, the PR damage is already done.

Imagine a scenario where a state-of-the-art AI system automatically reads, cleans, and categorizes every single customer message in real-time. By leveraging advanced Deep Learning (Stacked Bi-LSTMs) and robust Arabic word embeddings (AraVec), this project aims to develop an automated sentiment analysis microservice.

This system can be seamlessly integrated into NoorMart's backend architecture. As soon as a tweet or review is posted, the API instantly classifies the sentiment as Positive, Negative, or Neutral. This AI-powered solution offers significant advantages:

- Immediate Escalation: Instantly routes "Negative" complaints to the VIP Customer Support team to prevent customer churn.

- Automated Marketing: Aggregates "Positive" reviews for promotional campaigns.

- Resource Optimization: Reduces the need for manual ticket tagging, allowing human agents to focus on resolving actual complex issues.

Evaluation Metric: In customer service, missing a negative complaint is a catastrophic failure. Because the "Neutral" class naturally dominates everyday interactions, standard Accuracy is a misleading metric (a model could guess "Neutral" every time and score highly). Therefore, this project strictly optimizes for the F1-Score, ensuring the model heavily penalizes False Negatives and maintains high precision and recall across all customer emotions.

## Dataset

## Model Architecture
The core engine is a Deep Recurrent Neural Network designed specifically to understand the sequential context of Arabic text. It utilizes the following architecture:

- Input Layer: TextVectorization layer configured for a customized vocabulary size of 107,884 tokens (covering 95% of the dataset) and padded to 512 sequence length.

- Embedding Layer: Pre-trained AraVec (Word2Vec CBOW 300-d Twitter model) weights are injected here and set to be trainable for fine-tuning.

- SpatialDropout1D: Set to 0.3 for robust regularization on the embedding vectors.

- First Bi-LSTM Layer: Bidirectional LSTM (64 units) returning full sequences.

- Dropout Layer: Set to 0.4 to prevent overfitting.

- Second Bi-LSTM Layer: Bidirectional LSTM (64 units) returning the final summarized context vector.

- Dense Layer: 64 neurons with a ReLU activation function and L2 Regularization (1e-4).

- Dropout Layer: Set to 0.3.

- Output Layer: Dense layer with 3 neurons and a Softmax activation function (for multi-class classification: Positive, Neutral, Negative).


## Model compilation 
The model is compiled using the following setup:

- **Optimizer**: Adam optimizer (with an initial learning rate set to 0.0001 and weight decay of 0.005).

- **Loss Function**: Categorical Crossentropy.

- **Metric**: F1-Score (to handle class imbalances).

## Model Training
The model was trained using a highly optimized tf.data pipeline (.cache(), .prefetch(), .batch(64)) with the following callbacks:

- **Early Stopping**: Applied with patience set to 5 epochs (restoring the best weights).

- **Learning Rate Scheduler**: ReduceLROnPlateau applied to monitor validation loss, reducing the learning rate by a factor of 0.5 if no improvement is seen for 2 epochs.

- **Epochs**: 50 (Training halted optimally at Epoch 14).

Results
After evaluating on the unseen holdout test set, the final model achieved the following performance:

- **Test F1-Score**: 0.7307 (73.07%)

- **Test Loss**: 0.6531


## ⚙️ Deployment & MLOps Pipeline
This project is prepared as a production-ready, containerized microservice using FastAPI and Docker. The heavy model weights are hosted externally on a Model Registry (Hugging Face) to keep the source code repository lightweight and professional.

1- Download the Pre-trained Model
The trained .keras model is hosted on Hugging Face. To fetch it, run the included automated download script:

Hugging Face Hub: Mamdouh-Alaa12/Arabic-Sentiment-Analysis

2- Build the Docker Image
Instead of worrying about library versions and local environments, build the self-contained Docker image:

`docker build -t arabic-sentiment-api .`

3- Run the Container
Start the API server on your local machine:

`docker run -p 8000:8000 arabic-sentiment-api`

4- Test the model
Once the server is running, you can test it by running the client integration script:

`python client.py`
