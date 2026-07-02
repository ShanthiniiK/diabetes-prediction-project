import pandas as pd

def test_dataset_exists():
    df = pd.read_csv("diabetes_prediction_dataset.csv")
    assert len(df) > 0

def test_no_missing_values():
    df = pd.read_csv("diabetes_prediction_dataset.csv")
    assert df.isnull().sum().sum() == 0
