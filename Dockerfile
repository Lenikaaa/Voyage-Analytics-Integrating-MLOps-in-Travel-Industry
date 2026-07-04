FROM python:3.10-slim

WORKDIR /app

# Install system dependencies

RUN apt-get update && apt-get install -y \
gcc \
g++ \
&& rm -rf /var/lib/apt/lists/*

# Install Python dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy project files

COPY app ./app
COPY src ./src
COPY model ./model
COPY data ./data

# Streamlit port

EXPOSE 8501

# Start Streamlit app

CMD ["streamlit", "run", "app/regression.py", "--server.address=0.0.0.0", "--server.port=8501"]
