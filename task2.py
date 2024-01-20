from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
import numpy as np
import io
app = FastAPI()

@app.post("/calculate_volatility")
async def compute_volatility_endpoint(file: UploadFile = File(...)):
    # Check file extension
    if not file.filename.endswith(('.csv', '.xlsx')):
        raise HTTPException(status_code=400, detail="Unsupported file format")

    # Read the file
    content = file.file.read()
    file_data = io.BytesIO(content)

    data = pd.read_csv(file_data) if file.filename.endswith('.csv') else pd.read_excel(file_data)

    data['Daily Returns'] = (data['Close '] / data['Close '].shift(1)) - 1
    # print(data)

    # Calculate daily volatility
    daily_volatility = data['Daily Returns'].std()

    # Calculate annualized volatility
    length_of_data = len(data)
    annualized_volatility = daily_volatility * np.sqrt(length_of_data)

    result = {
        'daily_volatility': daily_volatility,
        'annualized_volatility': annualized_volatility
    }

    return result
