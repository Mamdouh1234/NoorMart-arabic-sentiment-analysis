# Use an official, lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements first (to leverage Docker caching)
COPY requirements.txt .

# Install dependencies (no-cache-dir keeps the image size small)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your files into the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# The command to start the server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]