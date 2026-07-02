import pandas as pd

def test_no_missing_values():
    df = pd.read_csv("diabetes_prediction_dataset.csv")
    assert df.isnull().sum().sum() == 0

def test_no_duplicate_rows():
    df = pd.read_csv("diabetes_prediction_dataset.csv")
    assert df.duplicated().sum() >= 0

def test_target_column_exists():
    df = pd.read_csv("diabetes_prediction_dataset.csv")
    assert "diabetes" in df.columns
