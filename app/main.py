
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

import os
import logging
from dotenv import load_dotenv


load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

app = FastAPI()

# Example data
FAMILY_DATA = {
    "sandhya": {"father": "Govindh", "mother": "Padma"},
    "nagesh": {"father": "Govindh", "mother": "Padma"},
    "akash": {"father": "Krishna reddy", "mother": "Jyothi"},
    "hasini": {"father": "Krishna reddy", "mother": "Jyothi"},
    "srushti": {"father": "Krishna", "mother": "Nandhini"}
}
class NameRequest(BaseModel):
    name: str



@app.get("/health")
async def health():
    logging.info("Health check requested.")
    return {"status": "I am healthy"}

@app.post("/get-parents")
async def get_parents(request: NameRequest):
    name = request.name.lower()
    logging.info(f"Received request for name: {name}")
    if name in FAMILY_DATA:
        response = FAMILY_DATA[name]
        logging.info(f"Found: {response}")
        return response
    logging.warning(f"Name not found: {name}")
    return JSONResponse(status_code=404, content={"error": "Name not found"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
