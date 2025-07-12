# 📊 Linear Regression – Ad Budget Sales Prediction

This project uses **Linear Regression** to predict product sales based on advertising budgets for **TV**, **Radio**, and **Newspaper**.  
It includes full **EDA**, data cleaning, model building, evaluation, and **deployment using Streamlit** with bilingual (Arabic/English) UI.

---

## 📁 Project Structure

linear-regression-ad-sales-prediction/
├── data/
│ └── Advertising Budget and Sales.csv
├── notebooks/
│ └── eda_and_model.ipynb
├── app/
│ ├── streamlit_app.py
│ └── linear_model.pkl
├── requirements.txt
└── README.md

---

## 🧪 Dataset

- **File:** `Advertising Budget and Sales.csv`
- **Target:** `Sales ($)`
- **Features:**
  - `TV Ad Budget ($)`
  - `Radio Ad Budget ($)`
  - `Newspaper Ad Budget ($)`

---

## 🧠 Project Workflow

1. **EDA (Exploratory Data Analysis)**
   - Info, describe, nulls, types
   - Correlation heatmap
   - Boxenplots, histograms, pairplot

2. **Data Preprocessing**
   - Removed duplicates and irrelevant column (`Unnamed: 0`)
   - Splitting into train/test sets (80/20)

3. **Modeling**
   - Linear Regression using `scikit-learn`
   - Evaluated with MAE, RMSE, R²
   - Saved model using `joblib`

4. **Deployment**
   - Web app built with **Streamlit**
   - Dual-language interface (🇺🇸 English & 🇪🇬 Arabic)

---

## 📈 Results

| Metric     | Value |
|------------|-------|
| **MAE**    | 1.46  |
| **RMSE**   | 1.78  |
| **R² Score** | 0.90  |

---

## 💻 Run Locally

```bash
# Clone the repository
git clone https://github.com/<YOUR-USERNAME>/linear-regression-ad-sales-prediction.git
cd linear-regression-ad-sales-prediction

# (Optional) Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app/streamlit_app.py
☁️ Deploy on Streamlit Cloud
Push this repository to GitHub.

Go to streamlit.io → New app → connect your repo.

Set main file to: app/streamlit_app.py

Click Deploy – done! 🎉

🌐 Streamlit App UI
User selects language (Arabic / English)

Enters ad budget for each channel

App predicts sales instantly with LinearRegression model

Clean, centered, and responsive layout

🛠️ Tech Stack
Languages: Python

Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, joblib, streamlit

Tools: Jupyter Notebook, Streamlit, GitHub

✨ Author
Ahmed Osama
Data Science Practitioner & CS Student