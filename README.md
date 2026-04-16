# MindTrace-Cognitive-Load-Focus-Prediction-System
MindTrace is a behavioral analytics system that predicts user focus and mental fatigue based on typing patterns and interaction data.

## Features
- Keystroke-based data collection  
- Feature extraction (speed, pauses)  
- ML-based focus prediction  
- Interactive dashboard  

## Tech Stack
- Python  
- Scikit-learn  
- Streamlit  
- Pynput  

## Project Structure
collect.py – data collection  
train.py – model training  
app.py – UI and prediction  

## Installation
pip install -r requirements.txt


## Run the Project
1. Collect data:
python collect.py

2. Train model:
python train.py

3. Run app:
streamlit run app.py


## How It Works
- Tracks typing intervals  
- Extracts behavioral features  
- Uses ML model to predict focus  


## Future Improvements
- Add webcam-based attention detection  
- Use deep learning models  
- Real-time tracking  
