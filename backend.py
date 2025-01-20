from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pandas as pd
from joblib import load
import io

# Load the ML pipeline
pipeline = load('pipeline/pipeline_for_startypepredictor.joblib')

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input schema for a single star
class StarInput(BaseModel):
    temperature: float = Field(..., description="Temperature in Kelvin (K)")
    luminosity: float = Field(..., description="Luminosity in terms of L/Lo")
    radius: float = Field(..., description="Radius in terms of R/Ro")
    absolute_magnitude: float = Field(..., description="Absolute Magnitude (Mv)")

@app.get("/")
def check_status():
    return {"message": "The Star Type Classifier API is running!"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    # Ensure required columns are present
    required_columns = ['Temperature (K)', 'Luminosity(L/Lo)', 'Radius(R/Ro)', 'Absolute magnitude(Mv)']
    if not all(col in df.columns for col in required_columns):
        return {"error": f"Invalid file format. Required columns are: {', '.join(required_columns)}"}

    # Predict star types
    predictions = pipeline.predict(df)
    probabilities = pipeline.predict_proba(df)

    # Build response
    results = []
    for i, prediction in enumerate(predictions):
        prob_dict = {pipeline.classes_[j]: probabilities[i][j] for j in range(len(pipeline.classes_))}
        results.append({
            "index": i,
            "predicted_type": prediction,
            "probabilities": prob_dict
        })

    return {"predictions": results}
