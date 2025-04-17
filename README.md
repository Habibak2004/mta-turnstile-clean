# MTA Turnstile Data Pipeline 🚇

This project processes and analyzes NYC subway turnstile data from 2022. Using Python, I built a modular pipeline to clean, transform, and visualize over 10 million data points representing station entries across time.

---

## 📁 Project Structure

transit-pipeline/
├── data/
│   ├── raw/                        # Original CSVs (e.g., Turnstile2022.csv)
│   ├── external/                   # Metadata: booth mapping, coordinates, etc.
│   ├── processed/                  # Cleaned + merged datasets
│   └── turnstile.db                # Optional SQLite database for SQL queries
│
├── scripts/                        # Modular Python scripts
│   ├── extract.py                  # (Placeholder) Script to fetch/download data
│   ├── transform.py                # Cleans and processes raw turnstile data
│   ├── load.py                     # (Placeholder) To load data into a DB or export
│   └── merge_and_enrich.py         # Merges booth + station + coordinate data
│
├── notebooks/
│   ├── heatmap_visualization.ipynb    # Creates interactive folium heatmap
│   └── hourly_analysis_sql.ipynb      # Hourly trends using SQL + plotly
│
├── visuals/                       # Exported visualizations (HTML format)
│   ├── turnstile_heatmap.html
│   └── hourly_entries_chart.html
│
├── requirements.txt              # Python packages needed
├── README.md                     # Project overview + usage
├── .gitignore                    # Ignore large CSVs, .DS_Store, etc.
└── LICENSE (optional)

---

## 🚀 Features

- Cleaned and filtered 10M+ rows of MTA turnstile data
- Calculated hourly ridership using cumulative entry counts
- Filtered out anomalies (e.g. counter resets, large jumps)
- Visualized ridership trends over time in a Jupyter notebook

---

## 📊 Sample Visualization

📈 *Notebook includes plots of average hourly entries across the MTA system.*

---

## 📓 Notebook

Explore the notebook here 👉 [`MTA_Turnstile_Analysis.ipynb`](notebooks/MTA_Turnstile_Analysis.ipynb)

---

## 📦 Technologies Used

- Python (Pandas, Matplotlib)
- Git + GitHub for version control
- Jupyter Notebooks
- Data from: [NYC Open Data - MTA Turnstile](https://catalog.data.gov/dataset/turnstile-usage-data-2022)

---

## 💡 Future Plans

- Join with station metadata to analyze ridership by location
- Build an Airflow pipeline for scheduled ETL
- Deploy a Streamlit dashboard for interactive visualization

---

## 👩‍💻 Author

**Habiba Khan**  
[LinkedIn](https://linkedin.com/in/Habibak2004) · [GitHub](https://github.com/Habibak2004)
