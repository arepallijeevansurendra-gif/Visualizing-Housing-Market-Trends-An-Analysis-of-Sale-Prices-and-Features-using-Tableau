# Housing Market Analysis Project

This Tableau-focused data analysis project explores key housing market drivers, including renovation impact, house age, bathrooms, bedrooms, and floors.

## Project Contents

- `data/` - project dataset and exported artifacts.
- `notebooks/` - Python notebook for data preparation, cleaning, and analysis.
- `web/` - Flask app to embed Tableau dashboards.

## Getting Started

1. Place the housing dataset CSV into `data/` as `housing_data.csv`.
2. Open `notebooks/housing_analysis.ipynb` to inspect and clean the data.
3. Build Tableau visualizations and dashboards using the prepared dataset.
4. Publish the dashboard to Tableau Public or Tableau Server.
5. Update `web/app.py` with the published Tableau embed URL.
6. Run the Flask app:
   - `python -m venv venv`
   - `venv\Scripts\Activate`
   - `pip install -r requirements.txt`
   - `python web/app.py`

## Dashboard Scope

- Data Collection & Preparation
- Clean and validate fields
- Calculated fields: house age, years since renovation, renovation status
- Visualizations: price distribution, sales trends, renovation impact, feature comparisons
- Storyboard and responsive dashboard design
- Web embedding in Flask UI
