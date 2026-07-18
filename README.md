# Superstore Analysis

Exploratory analysis of retail sales data using Python, pandas, and matplotlib.

## What this project does

`explore_superstore.py` loads the Superstore dataset and runs a short analysis pipeline:

1. **Data overview** — shape, column names, data types, null counts, and first 5 rows
2. **Date parsing** — converts `Order Date` and `Ship Date` to datetime
3. **Summary statistics** — descriptive stats for Sales, Quantity, Discount, and Profit
4. **Loss analysis** — groups negative-profit orders by Category and Sub-Category, showing loss count and average discount
5. **Visualization** — bar chart of total profit by Sub-Category, saved as `profit_by_subcategory.png`

## Dataset

**File:** `Sample - Superstore.csv`  
**Source:** Tableau's sample Superstore dataset (fictional U.S. office supply retailer, 2014–2017)

| | |
|---|---|
| Rows | 9,994 |
| Columns | 21 |
| Missing values | None |

Key columns include order and ship dates, customer and location fields, product category/sub-category, and financial metrics (Sales, Quantity, Discount, Profit).

The CSV uses `latin-1` encoding (not UTF-8), which is handled in the script.

## How to run

```bash
python explore_superstore.py
```

Requires **pandas** and **matplotlib**.

## Key findings

### Binders and heavy discounting

**Binders** (Office Supplies) have the highest number of loss-making orders of any sub-category — **613 orders** with negative profit. Those loss-making binder orders carry an average discount of about **74%**, far above most other sub-categories. Heavy discounting appears to be a major driver of individual binder orders losing money.

Despite that, Binders remain **net profitable overall** (~$30k total profit) because enough orders still earn margin at lower discounts.

### Tables and Bookcases profitability

**Tables** and **Bookcases** (both Furniture) are the only sub-categories with **net negative total profit**:

| Sub-Category | Total Profit |
|---|---:|
| Tables | −$17,725 |
| Bookcases | −$3,473 |

These show up as red bars on the left side of `profit_by_subcategory.png`. Tables in particular combine a large number of loss-making orders with deep enough losses to make the sub-category unprofitable overall — a different pattern from Binders, where high discounting hurts many line items but does not wipe out the category total.

## Output files

| File | Description |
|---|---|
| `explore_superstore.py` | Main analysis script |
| `Sample - Superstore.csv` | Source data |
| `profit_by_subcategory.png` | Bar chart of total profit by sub-category |
