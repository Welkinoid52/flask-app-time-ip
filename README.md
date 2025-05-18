# Flask IP and Timestamp Microservice

A simple Flask application that returns the current UTC timestamp and the client's IP address in JSON format.

## Features

- Returns current UTC timestamp in ISO format
- Detects client IP address (handles proxies via X-Forwarded-For header)
- Returns pretty-printed JSON response
- Lightweight Docker container based on Alpine Linux

# Flask IP & Timestamp Microservice

[![Docker Pulls](https://img.shields.io/docker/pulls/welkinoid/flaskapp-ip-time)](https://hub.docker.com/r/welkinoid/flaskapp-ip-time)

A lightweight microservice that returns the client's IP address and current UTC timestamp in JSON format.

## Quick Start

Run the pre-built image from Docker Hub:

```bash
docker run --name my-con -p 5000:5000 welkinoid/flaskapp-ip-time:latest
```
## Access the service:

```bash
curl http://localhost:5000
```

# Features
🕒 Current UTC timestamp in ISO-8601 format

🔍 Client IP detection (supports X-Forwarded-For header)

🎨 Pretty-printed JSON responses

🐳 Optimized Docker image (~50MB)

🔒 Runs as non-root user

# Example Response

```json
{
  "timestamp": "2023-11-15T14:25:36.123456Z",
  "ip": "203.0.113.42"
}
```

# Configuration Options
## Port Mapping
Map to a different host port:

```bash
docker run -p 8080:5000 welkinoid/flaskapp-ip-time:latest
```


## Environment Variables
The service supports these environment variables:

Variable	  Default  	Description
FLASK_PORT	5000	    Container listening port

## Example:
```bash
  docker run -e FLASK_PORT=6000 -p 5000:6000 welkinoid/flaskapp-ip-time:latest
```

# Docker Compose Example
```yaml
yaml
version: '3.8'
services:
  ip-time:
    image: welkinoid/flaskapp-ip-time:latest
    ports:
      - "5000:5000"
    restart: unless-stopped
```

    
# Building Locally
Clone the repository

## Build the image:

```bash
docker build -t flaskapp-ip-time .
```
## Run:

```bash
docker run -p 5000:5000 flaskapp-ip-time
```

# License
MIT License - Free for personal and commercial use

## 📦 Docker Hub: [welkinoid/flaskapp-ip-time](https://hub.docker.com/repository/docker/welkinoid/flaskapp-ip-time/tags/latest/sha256-8841c21420ff14a5c70e6b90117fc2fa477dc52c1f95ba29b894e9c0bfc9302c)
