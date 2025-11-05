# StudentStress

A machine learning project to predict student stress levels based on survey data and provide visual analytics.

## Features

- Data cleaning and exploratory data analysis (EDA) using Jupyter Notebook
- Machine learning models for stress prediction
- Interactive dashboard built with Streamlit
- Simple instructions to run and experiment locally

## Project Structure

```
.
├── Stress.ipynb                        # Jupyter notebook for EDA and model building
├── streamlit_app.py                    # Streamlit web app for predictions & visualization
├── Student Attitude and Behavior.csv   # Dataset
├── stress_prediction_models.pkl        # Saved ML models
├── model_evaluation_results.pkl        # Model evaluation results
├── .gitignore
├── LICENSE
└── requirements.txt
```

## Requirements

- Python 3.8 or higher
- Jupyter Notebook
- Streamlit
- Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, joblib

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/JeevanKaliregowda/StudentStress.git
    cd StudentStress
    ```

2. **Create a virtual environment (recommended)**
    ```bash
    python -m venv venv
    # On Linux/Mac
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Explore the Notebook

Open and run the Jupyter notebook for EDA and model building:
```bash
jupyter notebook Stress.ipynb
```

### 2. Run the Streamlit App

Launch the webapp:
```bash
streamlit run streamlit_app.py
```
Then, open the local address shown in the terminal (usually `http://localhost:8501`) in your browser.

### 3. Customization

- To use your own dataset, replace `Student Attitude and Behavior.csv` and update the notebook accordingly.
- Retrain models in the notebook, export as `.pkl` files, and update the app to use these new files if needed.

## Notes

- The app uses pre-trained models from `stress_prediction_models.pkl`.
- If you encounter errors, check library versions or file paths.

## Contributing

Pull requests, bug reports, and suggestions are welcome!

## License

This project is licensed under the MIT License.
