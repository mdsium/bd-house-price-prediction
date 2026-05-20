import joblib
import pandas as pd
import os
import numpy as np

# Correct Model Path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'bangladesh_house_price_model.pkl')

model = None

def load_model():
    global model
    if model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at: {MODEL_PATH}")
        model = joblib.load(MODEL_PATH)
        print(f"✅ Model loaded successfully from: {MODEL_PATH}")
    return model

def predict_house_price(data: dict):
    load_model()
    
    df = pd.DataFrame([data])
    
    # Expected columns
    expected_cols = [
        'area_sqft', 'city', 'thana', 'bedrooms', 'bathrooms', 'floor_level',
        'total_floors', 'building_age', 'lift', 'gas_line', 'airco', 'generator',
        'security', 'parking', 'garagepl', 'road_width_ft', 'distance_main_road_m',
        'near_school', 'near_hospital', 'near_market', 'driveway', 'fullbase', 'prefarea'
    ]
    
    for col in expected_cols:
        if col not in df.columns:
            if col in ['lift','gas_line','airco','generator','security','parking',
                      'garagepl','near_school','near_hospital','near_market',
                      'driveway','fullbase','prefarea']:
                df[col] = 0
            else:
                df[col] = 0
                
    pred_log = model.predict(df)
    pred_price = float(np.expm1(pred_log[0]))
    return round(pred_price)