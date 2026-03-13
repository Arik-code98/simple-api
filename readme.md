# FastAPI Text Analyzer API

## Overview

This is a simple **FastAPI-based REST API** that analyzes text input. The API allows users to submit text and receive basic information such as the **word count** and the **first 100 characters** of the text. It also provides endpoints to check if the API is running and to verify the health status of the service.

This project is useful for learning the basics of **FastAPI**, **Pydantic request models**, and **building simple REST endpoints**.

---

## Features

* Check if the API is running
* Submit text and get:

  * Word count
  * First 100 characters of the text
* Health check endpoint with timestamp
* Input validation using **Pydantic**

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn (ASGI server)

---

## Project Structure

```
.
├── main.py
└── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create a virtual environment (recommended)

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the API

Start the server using **uvicorn**:

```
uvicorn main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

---

## Interactive API Docs

FastAPI automatically generates documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

Alternative docs:

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### 1. Root Endpoint

Check if the API is running.

**Endpoint**

```
GET /
```

**Response**

```json
{
  "message": "api is running"
}
```

---

### 2. Summarize Text

Accepts text input and returns word count and the first 100 characters.

**Endpoint**

```
POST /summarize/
```

**Request Body**

```json
{
  "text": "Your text goes here"
}
```

**Response**

```json
{
  "Word Count": 10,
  "Hundred": "First 100 characters of the text..."
}
```

---

### 3. Health Check

Returns the API health status and current timestamp.

**Endpoint**

```
GET /health
```

**Response**

```json
{
  "status": "OK",
  "timestamp": "2026-03-13T20:00:00"
}
```

---

## Example Request (cURL)

```
curl -X POST "http://127.0.0.1:8000/summarize/" \
-H "Content-Type: application/json" \
-d '{"text":"This is a simple FastAPI example that counts words and returns the first hundred characters."}'
```

---

## Future Improvements

* Add text summarization using NLP
* Add authentication
* Deploy the API using Docker
* Add unit tests

---

## License

This project is for learning and educational purposes.
