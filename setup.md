# AI Tutor Setup Guide

Follow these simple steps to set up and run the AI Tutor backend.

### 1. Prerequisites
*   Python 3.8 or higher installed.

### 2. Setup Virtual Environment
It is recommended to use a virtual environment.
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required packages using pip.
```bash
pip install -r requirements.txt
```

### 4. Run the Server
Start the FastAPI server using Uvicorn.
```bash
python main.py
```
*   The server will start at `http://127.0.0.1:8000`.

### 5. API Usage
**Generate a Question**
*   **Endpoint:** `POST /api/generate-question`
*   **Body:**
    ```json
    {
      "source": "Your topic or URL here"
    }
    ```
*   **Example (cURL):**
    ```bash
    curl -X POST http://127.0.0.1:8000/api/generate-question \
    -H "Content-Type: application/json" \
    -d '{"source": "https://en.wikipedia.org/wiki/Computer_science"}'
    ```
