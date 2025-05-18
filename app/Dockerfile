# Use Python 3.13 Alpine
FROM python:3.13-alpine

# Set working directory
WORKDIR /app

# Copy only what's needed
COPY requirements.txt app.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run as non-root (Alpine's adduser is simpler than useradd)
RUN adduser -D myuser && chown -R myuser /app
USER myuser

# Run the app
EXPOSE 5000
CMD ["python", "app.py"]
