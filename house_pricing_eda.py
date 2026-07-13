import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    # 1. SET UP PATHS
    script_directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_directory, "quebec_housing_sales_v2.csv")

    print(f"\n[1/3] Loading dataset for EDA from: {filename}")
    if not os.path.exists(filename):
        print(f"❌ Error: Could not find 'quebec_housing_sales_v2.csv' in this directory.")
        return

    df = pd.read_csv(filename)

    # Quick terminal data health printout
    print("\n" + "=" * 45)
    print("         DATASET OVERVIEW & SUMMARY")
    print("=" * 45)
    print(f"Total Rows: {df.shape[0]} | Total Columns: {df.shape[1]}")
    print("\nMissing Values Per Numeric Column:")
    numeric_cols = ['bedrooms', 'bathrooms', 'living_area_sqft', 'lot_size_sqft', 'year_built', 'sale_year',
                    'sale_price']
    print(df[numeric_cols].isnull().sum())
    print("=" * 45)

    # Clean missing values using column medians for accurate plotting
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # 2. CREATE THE EDA VISUALIZATION DASHBOARD
    print("\n[2/3] Generating comprehensive visual analytics grid...")

    # Create a 2x2 grid of subplots
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    sns.set_theme(style="whitegrid")

    # Plot A: Histplot (Target Variable Distribution)
    print("  📊 Rendering Price Distribution Histogram...")
    sns.histplot(df['sale_price'], kde=True, ax=axes[0, 0], color='purple', edgecolor='black', alpha=0.6)
    axes[0, 0].set_title('Distribution of Sale Prices', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('Sale Price ($)', fontsize=12)
    axes[0, 0].set_ylabel('Count', fontsize=12)

    # Plot B: Scatterplot (Living Area vs. Sale Price)
    print("  🔵 Rendering Space vs Price Scatter Plot...")
    sns.scatterplot(data=df, x='living_area_sqft', y='sale_price', ax=axes[0, 1], color='teal', alpha=0.5,
                    edgecolor='none', s=25)
    axes[0, 1].set_title('Living Area vs Sale Price', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('Living Area (sqft)', fontsize=12)
    axes[0, 1].set_ylabel('Sale Price ($)', fontsize=12)

    # Plot C: Boxplot (Bedrooms vs. Sale Price Distribution)
    print("  📦 Rendering Bedroom Categorical Distribution...")
    sns.boxplot(data=df, x='bedrooms', y='sale_price', ax=axes[1, 0], palette='viridis')
    axes[1, 0].set_title('Sale Price Variance by Bedroom Count', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('Number of Bedrooms', fontsize=12)
    axes[1, 0].set_ylabel('Sale Price ($)', fontsize=12)

    # Plot D: Correlation Heatmap Matrix
    print("  🔥 Computing Linear Feature Correlation Heatmap...")
    correlation_matrix = df[numeric_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=axes[1, 1], cbar=True)
    axes[1, 1].set_title('Correlation Matrix of Numeric Features', fontsize=14, fontweight='bold')

    plt.tight_layout()

    # 3. SAVE AND DISPLAY
    output_image = os.path.join(script_directory, "eda_summary.png")
    plt.savefig(output_image, dpi=300)
    print(f"\n[3/3] EDA Summary dashboard successfully saved to: {output_image}")

    print("--> Opening graphical display window now...")
    plt.show()


if __name__ == "__main__":
    main()