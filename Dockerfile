# Base Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /usr/local/app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY src ./src

# Expose application port
EXPOSE 8000

# Switch to a non-root user for better security
RUN useradd app
USER app

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
