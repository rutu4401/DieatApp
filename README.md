# 🥗 DieatApp

DieatApp is a machine learning-based web application that recommends personalized diet plans using clustering and label encoding. Users can input their data and receive suitable diet recommendations based on predefined data models and plans.

---

## 🚀 Features

- 📊 Machine learning-based diet recommendation system
- 🧠 Clustering and label encoding models for prediction
- 🧪 Jupyter notebook for experimentation
- 🌐 Web interface built with Flask and HTML templates
- 📁 Supports CSV-based diet data for model training and predictions

---

## 🗂️ Project Structure
|── app.py # Main Flask application
├── check_csv.py # Utility to validate CSV structure 
├── demo.py # Sample/test script 
├── diet_clustering.pkl # Saved ML clustering model 
├── diet_plans_updated.csv # Dataset for diet plans
├── diet_recommendation.ipynb # Jupyter notebook for model creation 
├── label_encoder.pkl # Encoded labels for prediction 
├── scaler.pkl # Scaler used in preprocessing 
├── tempCodeRunnerFile.py # Temporary script (can be ignored) 
├── templates │ 
    ├── index.html # Input page for the app 
    ├── result.html # Output page showing the result


yaml
---

## ⚙️ How to Run

1. *Clone the repository:*

   ```bash
   git clone https://github.com/rutu4401/DieatApp.git
   cd DieatApp
   
2. *Set up the environment:*

Make sure you have Python 3.7+ installed. Install required libraries:

bash
Copy code
pip install flask pandas scikit-learn

3. *Start the Flask server:*

bash
Copy code
python app.py

4. *Access the application:*

Open your browser and navigate to http://127.0.0.1:5000

🧠 **Machine Learning Workflow**
The dataset is processed using encoders and scalers.

Clustering models group users based on dietary needs.

The app uses these clusters to suggest appropriate diet plans from the dataset.

📄 **Files to Know**
diet_recommendation.ipynb – Notebook where all the preprocessing and model training happens.

diet_clustering.pkl – Pre-trained KMeans or clustering model used for prediction.

label_encoder.pkl, scaler.pkl – Stored preprocessing objects for consistent predictions.


📬 **Feedback or Contributions?**
If you have suggestions or want to contribute, feel free to open a pull request or contact me via GitHub.


