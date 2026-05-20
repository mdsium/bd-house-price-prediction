# backend/retrain_model.py
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
import xgboost as xgb
import os

# Load data
df = pd.read_csv('bd_house_price.csv')   # Put this file in backend folder

print("Dataset Shape:", df.shape)

# Prepare data
df['price_log'] = np.log1p(df['price'])
X = df.drop(['price', 'price_log'], axis=1)
y = df['price_log']

categorical_cols = ['city', 'thana']
numerical_cols = [col for col in X.columns if col not in categorical_cols]

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_cols)
])

# Train model
xgb_model = xgb.XGBRegressor(n_estimators=200, learning_rate=0.1, random_state=42)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', xgb_model)
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# Save model
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'model')
os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(pipeline, os.path.join(MODEL_DIR, 'bangladesh_house_price_model.pkl'))

print("✅ Model retrained and saved successfully!")