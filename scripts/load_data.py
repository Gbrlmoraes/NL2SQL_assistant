import pandas as pd
from sqlalchemy import create_engine
import os

os.chdir(os.getcwd())


# Reads the csv fle and outputs as a sqllite database
def load_data(csv_path, db_path):
    """
    Reads the csv file and outputs as a SQLite database.
    Args:
    - csv_path: str: Path to the CSV file to be read.
    - db_path: str: Path to the SQLite database to be created.
    """
    try:
        pd.read_csv(csv_path).to_sql(
            "supermarket_sales",
            create_engine(f"sqlite:///{db_path}"),
            index=False,
        )

        print("SQLite database created successfully!")
    except Exception as e:
        print("Could not create the SQLite database", e)


if __name__ == "__main__":
    load_data(
        csv_path=os.path.join("data", "supermarket_sales.csv"),
        db_path=os.path.join("data", "supermarket_sales.db"),
    )
