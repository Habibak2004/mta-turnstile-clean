# MTA Turnstile Data Pipeline 🚇

This project processes and analyzes NYC subway turnstile data from 2022. Using Python, I built a modular pipeline to clean, transform, and visualize over 10 million data points representing station entries across time.

---

## 📁 Project Structure


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
