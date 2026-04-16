import streamlit as st
import pickle
import pandas as pd

st.title("MindTrace – Focus Prediction System")

model = pickle.load(open("model.pkl", "rb"))

file = st.file_uploader("Upload typing data (CSV)")

if file:
    data = pd.read_csv(file, header=None)
    data.columns = ["interval"]
    data["pause"] = data["interval"].apply(lambda x: 1 if x > 1 else 0)

    prediction = model.predict(data)

    focus_score = prediction.mean()

    st.subheader("Focus Level")
    st.write("High" if focus_score > 0.7 else "Low")

    st.line_chart(data["interval"])
