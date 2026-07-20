# Data Science & Machine Learning Portfolio

A comprehensive collection of machine learning projects showcasing data analysis, model building, and web deployment with Python.

## 📋 Projects Included

### 1. 🛍️ Ecommerce Customer Spending Predictor
**Linear Regression Model** - Predicts customer yearly spending based on user behavior metrics.
- **Algorithm:** Linear Regression
- **Features:** Avg. Session Length, Time on App, Time on Website, Length of Membership
- **Target:** Yearly Amount Spent
- **Deployment:** Streamlit Web App

**Files:**
- `app.py` - Streamlit web interface
- `Linear Regression Project.py` - Model training script
- `Ecommerce Customers` - Dataset

---

### 2. 🏦 Bank Note Authentication (Deep Learning)
**Neural Network Classification** - Identifies counterfeit bank notes using a 3-layer deep neural network.
- **Algorithm:** TensorFlow Deep Neural Network (10-20-10 architecture)
- **Task:** Binary Classification
- **Accuracy:** Achieved high precision on test set
- **Model:** Saved as `perceptron_model.keras`

**Files:**
- `Tensor Flow and Deep Learning.py` - Model training and evaluation
- `bank_note_data.csv` - Training dataset

---

### 3. 🏠 Quebec Housing Market EDA
**Exploratory Data Analysis** - Comprehensive visualization dashboard for housing market analysis.
- **Analysis:** Price distribution, feature correlations, categorical insights
- **Visualizations:** 4-plot dashboard (histogram, scatter, box plot, heatmap)
- **Output:** `eda_summary.png`

**Files:**
- `house_pricing_eda.py` - EDA script with professional visualizations
- `quebec_housing_sales_v2.csv` - Housing dataset

---

### 4 🚨 Emergency Services Analysis
**Data Processing & Visualization** - Analysis of 911 emergency call data.
- `911.csv` - Emergency services dataset

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/meghansh07-tech/Data-Science-And-ML.git
cd Data-Science-And-ML
```

2. **Create virtual environment (optional but recommended):**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env with your MySQL credentials (if using database logging)
```

---

## 📌 Running the Projects

### Option 1: Run the Streamlit Web App
```bash
streamlit run app.py
```
- Access at `http://localhost:8501`
- Input customer metrics to get spending predictions
- Results logged to MySQL (requires database setup)

### Option 2: Train Linear Regression Model
```bash
python "Linear Regression Project.py"
```
- Generates visualizations
- Saves model as `Linear regression_model.pkl`

### Option 3: Train Deep Learning Model
```bash
python "Tensor Flow and Deep Learning.py"
```
- Builds and trains neural network
- Saves model as `perceptron_model.keras`
- Displays confusion matrix and classification metrics

### Option 4: Run Housing EDA
```bash
python house_pricing_eda.py
```
- Generates comprehensive 4-plot visualization dashboard
- Saves output as `eda_summary.png`

---

## 📊 Tech Stack

| Category | Tools |
|----------|-------|
| **Languages** | Python 3.8+ |
| **ML Frameworks** | scikit-learn, TensorFlow 2.13, Keras |
| **Data Processing** | pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **Web Framework** | Streamlit |
| **Database** | MySQL (optional) |
| **Utilities** | joblib (model serialization) |

---

## 🔒 Security

- Database credentials are stored in `.env` file (never committed)
- See `.env.example` for configuration template
- Sensitive files excluded via `.gitignore`

**To set up database logging:**
1. Copy `.env.example` to `.env`
2. Fill in your MySQL credentials
3. Install mysql-connector: `pip install mysql-connector-python`

---

## 📁 Project Structure

```
Data-Science-And-ML/
├── app.py                              # Streamlit web app
├── Linear Regression Project.py        # Linear regression training
├── Tensor Flow and Deep Learning.py   # Deep learning model
├── house_pricing_eda.py               # Housing market EDA
├── requirements.txt                   # Python dependencies
├── .env.example                       # Environment template
├── .gitignore                         # Git ignore rules
├── Ecommerce Customers               # Ecommerce dataset
├── bank_note_data.csv                # Bank note dataset
├── quebec_housing_sales_v2.csv       # Housing dataset
├── 911.csv                           # Emergency calls dataset
├── Linear regression_model.pkl       # Trained linear model
└── perceptron_model.keras            # Trained neural network
```

---

## 📈 Model Performance

### Linear Regression (Ecommerce)
- **Mean Absolute Error (MAE):** ~$7.23
- **Root Mean Squared Error (RMSE):** ~$9.05
- **R² Score:** ~0.98

### Deep Learning (Bank Notes)
- **Accuracy:** 99.5%+
- **Precision:** High across both classes
- **Architecture:** Input(4) → Dense(10) → Dense(20) → Dense(10) → Output(1, sigmoid)

### Housing EDA
- **Dataset Size:** 5000+ properties
- **Features Analyzed:** Price, bedrooms, bathrooms, living area, year built
- **Key Insight:** Strong correlation between living area and sale price

---

## 🛠️ Development

### Adding New Models
1. Create a new `.py` file for your model
2. Follow the existing project structure
3. Update `requirements.txt` with new dependencies
4. Document in this README

### Running Tests
Currently no automated test suite. Recommend adding `pytest` for future enhancements.

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Meghansh Singh**
- GitHub: [@meghansh07-tech](https://github.com/meghansh07-tech)
- LinkedIn: [meghansh-singh](https://linkedin.com/in/meghansh-singh)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## 📧 Contact & Support

For questions or issues:
- Open an issue on GitHub
- Check existing documentation
- Review model comments in source code

---

## 🔄 Recent Updates

- ✅ Added environment variable support for secure credential management
- ✅ Pinned dependency versions for reproducibility
- ✅ Created `.env.example` template
- ✅ Enhanced `.gitignore` for better file management
- ✅ Added comprehensive README documentation

---

**Last Updated:** July 20, 2026  
**Status:** Active Development
