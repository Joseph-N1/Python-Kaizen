from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
import io
import base64
from mainhard import randomize_image_grid as hard_randomize
from maineasy import randomize_image_grid as easy_randomize

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def process_and_encode_image(img_array):
    # Convert numpy array to PIL Image
    img = Image.fromarray(img_array.astype('uint8'))
    
    # Save to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # Encode to base64
    return base64.b64encode(img_byte_arr).decode()

@app.post("/api/process")
async def process_image(file: UploadFile = File(...), mode: str = "easy"):
    try:
        # Read image file
        contents = await file.read()
        img = Image.open(io.BytesIO(contents))
        img_array = np.array(img)
        
        # Process based on mode
        if mode == "easy":
            processed_array = easy_randomize(img_array)
        else:
            processed_array = hard_randomize(img_array)
            
        # Convert result to base64
        result_base64 = process_and_encode_image(processed_array)
        
        return {
            "status": "success",
            "processingTime": 1.5,  # You can add actual timing if needed
            "resultImage": f"data:image/png;base64,{result_base64}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)