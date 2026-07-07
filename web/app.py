from pathlib import Path

import pandas as pd
from flask import Flask, render_template

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "housing_data_cleaned.csv"
TABLEAU_EMBED_URL = "https://public.tableau.com/app/profile/arepalli.jeevan.surendra/viz/HousingData_17834384352300/Dashboard2?publish=yes"

app = Flask(__name__, template_folder=str(BASE_DIR / "web" / "templates"), static_folder=str(BASE_DIR / "web" / "static"))


def load_dashboard_summary():
    try:
        df = pd.read_csv(DATA_PATH)
        return {
            "total_homes": int(len(df)),
            "avg_price": round(float(df["price"].mean()), 2),
            "max_price": round(float(df["price"].max()), 2),
            "avg_sqft": round(float(df["sqft_living"].mean()), 2),
        }
    except Exception:
        return {
            "total_homes": 0,
            "avg_price": 0,
            "max_price": 0,
            "avg_sqft": 0,
        }


@app.route('/')
def home():
    summary = load_dashboard_summary()
    return render_template('index.html', tableau_url=TABLEAU_EMBED_URL, summary=summary)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
