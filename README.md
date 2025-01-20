**# Star Type Classifier**

**Star Type Classifier** is an interactive application that uses a machine learning model to classify stars into different types based on their properties such as **Temperature (K)**, **Luminosity (L/Lo)**, **Radius (R/Ro)**, and **Absolute Magnitude (Mv)**. The app provides both single and bulk star type prediction capabilities, along with probabilistic outputs for each prediction.

**## Features**

- **Single Star Prediction**: Predict the type of a single star by inputting its properties.
- **Bulk Prediction via CSV**: Upload a CSV file containing multiple stars' properties to predict their types.
- **Classification Probabilities**: Get probabilistic outputs for each prediction.
- **Interactive Interface**: A user-friendly Streamlit interface for easy interaction.

**## Deployed Application**

Access the deployed application here:
[**Star Type Classifier App**](https://your-streamlit-app-url.streamlit.app)  
(Note: Replace the placeholder URL with the actual deployed app URL.)

**## Project Structure**

```
|-- backend.py               # FastAPI backend for handling predictions
|-- frontend.py              # Streamlit frontend for user interaction
|-- Star_type_Classifier_completed.ipynb  # Jupyter Notebook with ML model development
|-- requirements.txt         # List of dependencies
|-- sidebar_image.png        # Sidebar image for the frontend
|-- image.png                # Additional image for the app
|-- star_type_(1) copy.csv   # Sample CSV file for bulk predictions
```

**### Backend (`backend.py`):**
- **Endpoints**:
  - `/predict/single/`: Accepts star properties and returns the predicted type with probabilities.
  - `/predict/multiple/`: Accepts a CSV file and returns predictions for all stars in the file.
- **Libraries**: FastAPI, Pandas, Joblib.
- **Model**: The backend uses a pre-trained machine learning pipeline stored as a `.joblib` file.

**### Frontend (`frontend.py`):**
- **Pages**:
  - **Introduction**: Overview of the application.
  - **Single Star Predictor**: Input fields for single-star prediction.
  - **Multiple Star Predictor**: File uploader for bulk predictions.
- **Libraries**: Streamlit, Pandas, Requests.
- **Styling**: Custom background and sidebar styling for a starry theme.

**### Jupyter Notebook (`Star_type_Classifier_completed.ipynb`):**
- **Model Development**:
  - The notebook outlines the process of training the machine learning model used for star classification.
  - Explains feature selection, model training, evaluation, and export.
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib.

**## Installation**

**### Prerequisites**
- Python 3.8 or higher

**### Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url/star-type-classifier.git
   cd star-type-classifier
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend server:
   ```bash
   uvicorn backend:app --reload
   ```
4. Run the frontend app:
   ```bash
   streamlit run frontend.py
   ```

**## Usage**

1. Open the Streamlit app in your browser.
2. Use the **Single Star Predictor** to predict the type of a star by entering its properties.
3. Upload a CSV file in the **Multiple Star Predictor** to classify multiple stars at once.
4. View the predicted types and associated probabilities for each star.

**## Technologies Used**

- **Python**: Programming language.
- **FastAPI**: Backend framework for API development.
- **Streamlit**: Frontend for interactive web applications.
- **Pandas**: Data manipulation.
- **NumPy**: Numerical computations.
- **Scikit-learn**: Machine learning library.
- **Matplotlib**: Data visualization.

**## Deployed Application**

The application is deployed on Streamlit Cloud. Access it here:
[**Star Type Classifier App**](https://your-streamlit-app-url.streamlit.app)  


