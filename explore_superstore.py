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

    losses = df[df["Profit"] < 0]
    loss_by_group = (
        losses.groupby(["Category", "Sub-Category"])
        .agg(
            loss_order_count=("Profit", "count"),
            avg_discount=("Discount", "mean"),
        )
        .sort_values("loss_order_count", ascending=False)
    )

    print("\nLoss-making orders by Category and Sub-Category:")
    print(loss_by_group)


if __name__ == "__main__":
    main()
