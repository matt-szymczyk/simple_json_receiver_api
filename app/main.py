from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
from datetime import datetime
import os

app = FastAPI()

@app.post("/store-json")
async def store_json(data: dict):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"stored_json_{timestamp}.json"
        
        os.makedirs("data", exist_ok=True)
        file_path = os.path.join("data", filename)
        
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
            
        return JSONResponse(
            content={
                "message": "JSON data stored successfully",
                "file": filename
            },
            status_code=200
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
