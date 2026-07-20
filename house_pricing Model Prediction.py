import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Model imports
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score


def main():
    # 1. DYNAMICALLY LOCATE THE CSV FILE IN THE SCRIPT'S OWN FOLDER
    script_directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_directory, "quebec_housing_sales_v2.csv")

    print(f"\n[1/4] Looking for CSV file at: {filename}")

    if not os.path.exists(filename):
        print("\n❌ Error: Still could not find the file automatically.")
        print(f"Current terminal directory: {os.getcwd()}")
        print("Please double check that 'quebec_housing_sales_v2.csv' sits in the exact same folder as this script.")
        return

    df = pd.read_csv(filename)
    print("--> File loaded successfully! Total records:", len(df))

    # 2. SIMPLE PREPROCESSING (Explicitly mapping your columns)
    print("\n[2/4] Preprocessing columns and handling missing values...")

    # Fill missing values using the median value of that column (much better for accuracy than 0)
    df['lot_size_sqft'] = df['lot_size_sqft'].fillna(df['lot_size_sqft'].median())
    df['living_area_sqft'] = df['living_area_sqft'].fillna(df['living_area_sqft'].median())
    df['year_built'] = df['year_built'].fillna(df['year_built'].median())

    # Features explicitly listed
    feature_columns = ['bedrooms', 'bathrooms', 'living_area_sqft', 'lot_size_sqft', 'year_built', 'sale_year']

    X = df[feature_columns]
    y = df['sale_price']

    # Split into 80% training data and 20% testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. INITIALIZE AND TRAIN ALL 3 MODELS
    print("\n[3/4] Training Linear Regression, Random Forest, and XGBoost...")
    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1),
        'XGBoost': XGBRegressor(n_estimators=100, learning_rate=0.08, random_state=42, n_jobs=-1)
    }

    predictions = {}
    metrics = {}

    for name, model in models.items():
        print(f"  ⚡ Training {name}...")
        model.fit(X_train, y_train)
        predictions[name] = model.predict(X_test)

        # Performance metrics
        rmse = np.sqrt(mean_squared_error(y_test, predictions[name]))
        r2 = r2_score(y_test, predictions[name])
        metrics[name] = {'RMSE': rmse, 'R2': r2}

    # 4. GENERATE, SAVE, AND DISPLAY THE PLOT
    print("\n[4/4] Creating comparison chart image...")
    plt.figure(figsize=(18, 5))
    color_map = {'Linear Regression': 'royalblue', 'Random Forest': 'teal', 'XGBoost': 'crimson'}

    for i, (name, preds) in enumerate(predictions.items(), 1):
        plt.subplot(1, 3, i)

        # Scatter actual vs estimated prices
        plt.scatter(y_test, preds, alpha=0.4, color=color_map[name], s=20)

        # Diagonal reference line showing perfect predictions
        ideal_line = np.linspace(min(y_test), max(y_test), 100)
        plt.plot(ideal_line, ideal_line, color='black', linestyle='--', linewidth=2, label='Perfect Fit')

        plt.title(f"{name}\n$R^2$: {metrics[name]['R2']:.3f} | RMSE: ${metrics[name]['RMSE']:,.0f}")
        plt.xlabel('Actual Price ($)')
        plt.ylabel('Estimated Price ($)')
        plt.legend()
        plt.grid(True, alpha=0.3)

    plt.tight_layout()

    # Save chart to the same folder as the script
    output_image = os.path.join(script_directory, "model_comparison.png")
    plt.savefig(output_image, dpi=300)
    print(f"--> Graphical plot saved successfully as: {output_image}")

    # Print final text output matrix table
    print("\n" + "=" * 55)
    print("           FINAL MODEL PERFORMANCE METRICS")
    print("=" * 55)
    print(f"{'Model Name':<22} | {'R² Score':<12} | {'RMSE':<15}")
    print("-" * 55)
    for name, score in metrics.items():
        print(f"{name:<22} | {score['R2']:<12.4f} | ${score['RMSE']:<14,.2f}")
    print("=" * 55 + "\n")

    # Force the interactive pop-up window to display on your monitor
    print("--> Opening graphical display window. Close the chart window to finish execution.")
    plt.show()


if __name__ == "__main__":
    main()