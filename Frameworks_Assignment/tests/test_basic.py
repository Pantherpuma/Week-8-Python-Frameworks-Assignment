import os
import pandas as pd
import importlib


def test_sample_data_exists():
    p = os.path.join(os.path.dirname(__file__), '..', 'data', 'metadata_sample.csv')
    assert os.path.exists(p), f"Sample data not found at {p}"
    df = pd.read_csv(p)
    assert not df.empty


def test_app_load_prepare():
    # Import the streamlit app module and run its helper functions
    app_mod = importlib.import_module('app.streamlit_app')
    df = app_mod.load_data()
    assert isinstance(df, pd.DataFrame)
    df2 = app_mod.prepare(df)
    assert 'year' in df2.columns


def test_sklearn_import():
    import sklearn
    assert hasattr(sklearn, '__version__')
