import streamlit as st
import pandas as pd
from joblib import load
import io

# Set page configuration
st.set_page_config(
    page_title="Star Type Classifier",
    page_icon="⭐",
    layout="wide"
)

# Streamlit App Title
st.title("Star Type Classifier")

# Load the ML pipeline locally
pipeline = load('pipeline/pipeline_for_startypepredictor.joblib')

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Single Star Prediction", "Batch Prediction"])

# Single Star Prediction
if page == "Single Star Prediction":
    st.header("Predict a Single Star's Type")

    # Input fields
    temperature = st.number_input("Temperature (K)", min_value=0.0, value=6000.0)
    luminosity = st.number_input("Luminosity (L/Lo)", min_value=0.0, value=1.0)
    radius = st.number_input("Radius (R/Ro)", min_value=0.0, value=1.0)
    absolute_magnitude = st.number_input("Absolute Magnitude (Mv)", value=4.83)

    if st.button("Predict"):
        # Create a DataFrame for the single input
        single_data = pd.DataFrame([{
            "Temperature (K)": temperature,
            "Luminosity(L/Lo)": luminosity,
            "Radius(R/Ro)": radius,
            "Absolute magnitude(Mv)": absolute_magnitude
        }])

        # Perform prediction locally
        predictions = pipeline.predict(single_data)
        probabilities = pipeline.predict_proba(single_data)

        st.success(f"Predicted Star Type: {predictions[0]}")
        st.write("Probabilities:")
        prob_dict = {pipeline.classes_[i]: probabilities[0][i] for i in range(len(pipeline.classes_))}
        st.json(prob_dict)

# Batch Prediction
elif page == "Batch Prediction":
    st.header("Predict Star Types in Bulk")

    # File upload
    uploaded_file = st.file_uploader("Upload a CSV File", type=["csv"])

    if uploaded_file:
        st.subheader("Uploaded Data")
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

        if st.button("Predict Batch"):
            # Perform predictions locally
            predictions = pipeline.predict(df)
            probabilities = pipeline.predict_proba(df)

            # Combine predictions and probabilities into a DataFrame
            results = pd.DataFrame({
                "Index": range(len(predictions)),
                "Predicted Type": predictions
            })
            for i, class_name in enumerate(pipeline.classes_):
                results[class_name] = probabilities[:, i]

            st.subheader("Predictions")
            st.dataframe(results)

            # Option to download predictions
            csv_output = results.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Predictions as CSV",
                data=csv_output,
                file_name="star_predictions.csv",
                mime="text/csv"
            )
