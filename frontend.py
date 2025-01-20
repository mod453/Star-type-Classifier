import streamlit as st
import pandas as pd
import requests
import base64

# Set the API base URL
API_BASE_URL = "http://127.0.0.1:8000"  # Update if running FastAPI on a different host/port

# Add background to the app with starry theme
def add_background():
    starry_background_url = "https://source.unsplash.com/1920x1080/?stars,space"  # Background image URL

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{starry_background_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        .css-1d391kg .css-1v3fvcr {{
            background-color: rgba(0, 0, 0, 0.7);  /* Sidebar with semi-transparent black */
            color: #F5F5F5;
        }}
        .stMarkdown, .stTitle, .stSubheader, .stText, .stCaption {{
            color: #FFD700; /* Golden star color */
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.8); /* Glowing effect */
        }}
        .stTitle {{
            font-size: 3.5rem; /* Larger font size for titles */
            font-weight: bold;
        }}
        .stSubheader {{
            font-size: 2rem; /* Slightly larger font for subheaders */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the background function
add_background()

# Page 1: Introduction
def introduction():
    st.title("Star Type Predictor")
    st.markdown(
        """
        ## Welcome to the Star Type Predictor! 🌌
        Use this app to predict the type of stars based on their properties.
        
        **Features:**
        - Predict a single star type.
        - Predict star types for multiple stars via a CSV upload.
        
        Navigate to the desired feature using the sidebar. 🚀
        """
    )

# Page 2: Single Star Predictor
def single_star_predictor():
    st.title("Single Star Type Predictor")

    # Input fields for star properties
    st.subheader("Enter Star Properties:")
    temperature = st.number_input("Temperature (K)", min_value=0.0, value=6000.0)
    luminosity = st.number_input("Luminosity (L/Lo)", min_value=0.0, value=1.0)
    radius = st.number_input("Radius (R/Ro)", min_value=0.0, value=1.0)
    absolute_magnitude = st.number_input("Absolute Magnitude (Mv)", value=4.83)

    if st.button("Predict"):
        # Call the FastAPI backend
        payload = {
            "temperature": temperature,
            "luminosity": luminosity,
            "radius": radius,
            "absolute_magnitude": absolute_magnitude
        }
        response = requests.post(f"{API_BASE_URL}/predict/single/", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Star Type: {result['predicted_type']}")
            st.write("Probabilities:")
            st.json(result['probabilities'])
        else:
            st.error("Error: Unable to get predictions. Please try again.")

# Page 3: Multiple Star Predictor
def multiple_star_predictor():
    st.title("Multiple Star Type Predictor")

    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV File", type=["csv"])

    if uploaded_file is not None:
        # Display the uploaded file
        st.subheader("Uploaded Data:")
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

        # Call the FastAPI backend
        response = requests.post(
            f"{API_BASE_URL}/predict/multiple/",
            files={"file": uploaded_file.getvalue()}
        )

        if response.status_code == 200:
            results = response.json()
            predictions_df = pd.DataFrame([
                {
                    "Index": r["index"],
                    "Predicted Type": r["predicted_type"],
                    **r["probabilities"]
                } for r in results
            ])

            st.subheader("Predictions:")
            st.dataframe(predictions_df)
        else:
            st.error("Error: Unable to get predictions. Please check your file and try again.")

# Streamlit App Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Introduction", "Single Star Predictor", "Multiple Star Predictor"])

if page == "Introduction":
    introduction()
elif page == "Single Star Predictor":
    single_star_predictor()
elif page == "Multiple Star Predictor":
    multiple_star_predictor()
