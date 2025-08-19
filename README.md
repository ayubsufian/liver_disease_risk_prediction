# Liver Disease Risk Prediction

This project contains a machine learning model to predict the risk of liver disease based on patient data. It includes a Jupyter Notebook for the complete data analysis and model training process, and a desktop application for making real-time predictions.

## Project Structure

```
├── .ipynb_checkpoints
│   └── liver_disease_risk_prediction-checkpoint.ipynb
├── data/
│   └── Indian Liver Patient Dataset (ILPD).csv
├── app.py
├── liver_disease_rf_model.pkl
├── liver_disease_risk_prediction.ipynb 
└── requirements.txt
```

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

-   Python 3.8+
-   Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ayubsufian/liver_disease_risk_prediction.git
    cd liver_disease_risk_prediction
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    
## How to Run

This is a two-step process: first train the model, then run the application.

### Step 1: Train the Model

1.  Launch Jupyter Notebook or JupyterLab:
    ```bash
    jupyter notebook
    ```
2.  Open and run all cells in `liver_disease_risk_prediction.ipynb`.
3.  This will generate the model file `liver_disease_rf_model.pkl` in the root directory.

### Step 2: Run the Prediction App

Once the model file (`.pkl`) exists, run the desktop application:
```bash
python app.py
```
The application window will open, allowing you to input patient data and get a prediction.

## Technologies Used

-   **Data Analysis & Modeling**: `pandas`, `numpy`, `scikit-learn`
-   **Data Visualization**: `matplotlib`, `seaborn`
-   **Desktop GUI**: `tkinter`, `ttkbootstrap`
-   **Model Persistence**: `joblib`
