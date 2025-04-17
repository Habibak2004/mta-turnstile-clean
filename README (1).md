# 🚇 NYC MTA Turnstile Data Pipeline & Heatmap Visualization

This project takes raw MTA subway turnstile data and transforms it into an interactive heatmap that visualizes ridership across NYC. It showcases skills in data engineering, cleaning, merging external metadata, SQL querying, and geospatial visualization.

---

## 📁 Project Structure

```
transit-pipeline/
├── data/
│   ├── raw/                    # Original CSVs (e.g., Turnstile2022.csv)
│   ├── external/               # Metadata: booth mapping, coordinates, etc.
│   ├── processed/              # Cleaned + merged datasets
│   └── turnstile.db            # Optional SQLite database for SQL queries
│
├── scripts/                    # Modular Python scripts
│   ├── extract.py              # (Placeholder) Script to fetch/download data
│   ├── transform.py            # Cleans and processes raw turnstile data
│   ├── load.py                 # (Placeholder) To load data into a DB or export
│   └── merge_and_enrich.py     # Merges booth + station + coordinate data
│
├── notebooks/
│   ├── heatmap_visualization.ipynb   # Creates interactive folium heatmap
│   └── hourly_analysis_sql.ipynb     # Hourly trends using SQL + plotly
│
├── visuals/                   # Exported visualizations (HTML format)
│   ├── turnstile_heatmap.html
│   └── hourly_entries_chart.html
│
├── requirements.txt           # Python packages needed
├── README.md                  # Project overview + usage
├── .gitignore                 # Ignore large files, .DS_Store, temp files, etc.
└── LICENSE (optional)
```

---

## ✨ Features

- Cleaned 10M+ rows of NYC subway turnstile data using pandas
- Merged multiple datasets using SQL-style joins and geospatial metadata
- Linked booth IDs to station names and added latitude/longitude coordinates
- Built an interactive Folium heatmap to visualize ridership patterns
- Used SQL queries to analyze hourly subway usage via SQLite
- Created interactive charts with Plotly and exported them as HTML

---

## 📊 Sample Visualizations

- 🗺️ [Interactive Subway Heatmap](./visuals/turnstile_heatmap.html)
- 📈 [Hourly Entries Chart](./visuals/hourly_entries_chart.html)

---

## 🛠️ Tech Stack

- Python 3.x
- pandas
- folium
- plotly
- SQLite (for SQL queries)
- Jupyter Notebook

---

## 🙋🏽‍♀️ Built by

**Habiba Khan**  
First-gen student passionate about robotics, data visualization, and building tech that makes cities more intuitive to navigate.

---

## ✅ To Run

1. Clone the repo
2. Install dependencies from `requirements.txt`
3. Run the notebooks inside the `notebooks/` folder
4. Open any `.html` files inside `visuals/` to view outputs

