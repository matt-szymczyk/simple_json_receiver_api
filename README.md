
# JSON Storage API

A FastAPI application that stores JSON data with timestamps in a data directory.

## Features

- Accepts JSON data via POST requests
- Automatically creates timestamped files
- Stores files in a dedicated data directory
- Returns success message with filename

## Installation

1. Create and activate virtual environment:

```bash
virtualenv venv
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the application:
```bash
uvicorn app.main:app --reload
```

