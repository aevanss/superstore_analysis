from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parent / "Sample - Superstore.csv"


def main() -> None:
    df = pd.read_csv(DATA_PATH, encoding="latin-1")

    print("Shape:", df.shape)
    print("\nColumn names:")
    print(list(df.columns))
    print("\nData types:")
    print(df.dtypes)
    print("\nNulls per column:")
    print(df.isna().sum())
    print("\nFirst 5 rows:")
    print(df.head())

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    print("\nDate column types (after conversion):")
    print(df[["Order Date", "Ship Date"]].dtypes)

    print("\nSummary stats (Sales, Quantity, Discount, Profit):")
    print(df[["Sales", "Quantity", "Discount", "Profit"]].describe())


if __name__ == "__main__":
    main()
