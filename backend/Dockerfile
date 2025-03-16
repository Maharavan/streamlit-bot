# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . . 

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
