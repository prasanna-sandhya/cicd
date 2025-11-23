# Family Info FastAPI Service

A simple FastAPI project that provides parent information for a given name. Designed for CI/CD demonstration and easy deployment with Docker.

## Features

- **POST** `/get-parents`: Returns father and mother names for a given person.
- **GET** `/health`: Health check endpoint.
- Returns `404` if the name is not found.

## Example Data

- `sandhya`: father - Govindh, mother - padma
- `akash`: father - krishna reddy, mother - Jyothi

## Usage

### Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the API:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Test the API:
   ```bash
   curl -X POST "http://127.0.0.1:8000/get-parents" -H "Content-Type: application/json" -d '{"name": "sandhya"}'
   ```

### Run with Docker

1. Build the Docker image:
   ```bash
   docker build -t family-api .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 family-api
   ```

## Environment Variables

- See `.env` for examples (not required for basic usage, included for best practices).

## Project Structure

```
cicd/
├── app/
│   └── main.py
├── .env
├── requirements.txt
├── Dockerfile
└── README.md
```
