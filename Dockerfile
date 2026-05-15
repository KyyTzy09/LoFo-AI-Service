# Base image python
FROM python:3.11-slim

# Working directory dalam container
WORKDIR /app

# Copy dependency dulu (biar docker cache efisien)
COPY requirements.txt .

# Install dependency
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua source code
COPY . .

# Expose port FastAPI
EXPOSE 8080

# Jalankan server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]