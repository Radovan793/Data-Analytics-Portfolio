# test_covid_etl.py
import pandas as pd
from Covid_etl import CovidETL  # Import your ETL class

def test_transform():
    """Test if Active = cases - deaths - recovered is calculated correctly."""
    # Arrange
    data = pd.DataFrame({
        "cases": [100, 200],
        "deaths": [10, 20],
        "recovered": [50, 100]
    })
    etl = CovidETL("dummy")
    etl.df = data

    # Act
    etl.transform()

    # Assert
    expected = [40, 80]
    assert etl.df["Active"].tolist() == expected





