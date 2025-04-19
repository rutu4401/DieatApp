import pickle
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

# Load trained models
with open("diet_classifier.pkl", "rb") as f:
    rf_model = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoders = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template("index.html") 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Validate form data
        calories = request.form.get("calories")
        protein = request.form.get("protein")
        calcium = request.form.get("calcium")
        fats = request.form.get("fats")

        # Ensure values are not None and convert to float
        if not all([calories, protein, calcium, fats]):
            return "Error: Missing input fields. Please fill in all values."

        input_data = {
            'Calories': float(calories),
            'Protein': float(protein),
            'Calcium': float(calcium),
            'Fats': float(fats)
        }
        
        # Convert input data to dataframe
        input_df = pd.DataFrame([input_data])
        
        # Scale input data
        input_scaled = scaler.transform(input_df)
        
        # Predict meals using trained model
        predictions = rf_model.predict(input_scaled)
        
        # Decode predictions
        diet_plan = {
            "breakfast": label_encoders['Breakfast'].inverse_transform([predictions[0][0]])[0],
            "lunch": label_encoders['Lunch'].inverse_transform([predictions[0][1]])[0],
            "dinner": label_encoders['Dinner'].inverse_transform([predictions[0][2]])[0]
        }
        
        return render_template("result.html", diet_plan=diet_plan)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
