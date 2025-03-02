
# Car Price Prediction

## Project Overview

This project is designed to predict car prices based on various input features such as manufacturer, model, category, fuel type, mileage, gear box type, and other relevant attributes. The model is built using machine learning techniques and deployed as a web application using Streamlit.

## Features

- Interactive web application for predicting car prices.
- User-friendly interface for selecting car attributes.
- Machine learning model trained on historical car price data.

## Files Description

1. **Model Building.ipynb**: Jupyter Notebook containing the process of data preprocessing, model training, and evaluation.
2. **Model deployment.py**: Python script that deploys the trained model using Streamlit.

## Installation and Setup

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- Required libraries: `streamlit`, `pandas`, `pickle`, `sklearn`

### Steps to Run the Project

1. Clone or download the project files.
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv car_price_env
   source car_price_env/bin/activate  # On macOS/Linux
   car_price_env\Scripts\activate  # On Windows
   ```
3. Install required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is not available, install manually:
   ```bash
   pip install streamlit pandas scikit-learn pickle5
   ```
4. Ensure that the trained model file (`model1.sav`) is available in the correct directory.
5. Run the Streamlit app:
   ```bash
   streamlit run "Model deployment.py"
   ```

## Usage

- Select the relevant car features from the dropdown lists in the web interface.
- Click the `Predict Price` button to get the estimated car price.

## Model Details

- The model was trained using historical car price data.
- Features used include manufacturer, model, fuel type, mileage, gear box type, and more.
- The model predicts the price based on these input parameters.

## Future Enhancements

- Improve model accuracy by incorporating more features.
- Deploy the model using cloud services like AWS or Azure.
- Implement a database for storing user inputs and predictions.
