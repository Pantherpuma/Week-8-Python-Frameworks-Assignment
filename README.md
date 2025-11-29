# CORD-19 Data Explorer — Frameworks_Assignment

A beginner-friendly starter project for the Week 8 Python Frameworks assignment. This repository contains exploratory analysis (Jupyter notebook), a small sample of the CORD-19 metadata CSV for quick testing, and an interactive Streamlit app for visual exploration.

This starter is intentionally lightweight and designed so you can get up and running quickly using a small sample dataset. When ready, add the full `metadata.csv` (from the official CORD-19 dataset) to `data/metadata.csv` and the notebook + app will automatically use it.

Key features
- Exploratory notebook with data loading, cleaning, visualizations, TF-IDF and a basic LDA topic modeling demo (`notebooks/analysis.ipynb`).
- Interactive Streamlit app to filter and visualize publications by year, source, journals, and title word cloud (`app/streamlit_app.py`).
- Minimal tests and CI workflow to validate the environment and basic functions.

Contents
- data/metadata_sample.csv — small sample CSV to run the app & notebook locally
- notebooks/analysis.ipynb — exploratory analysis, plots, TF-IDF + LDA demo
- app/streamlit_app.py — Streamlit app for interactive exploration
- scripts/check_env.py — simple environment check helper
- tests/ — pytest tests verifying sample data and app loading
- .github/workflows/ci.yml — basic CI to run tests on push / PR
- requirements.txt — Python dependencies

Prerequisites
- Python 3.8+ (3.10 recommended)
- pip

Quick start (Windows PowerShell)
1. Clone this repo and change into the project folder. For example:

```powershell
git clone https://github.com/<your-username>/Week-8-Python-Frameworks-Assignment.git
cd Week-8-Python-Frameworks-Assignment/Frameworks_Assignment
```

2. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run a quick environment check:

```powershell
python scripts\check_env.py
```

5a. Run the Streamlit app (recommended for quick interactive exploration):

```powershell
streamlit run app/streamlit_app.py
```

5b. Or open the notebook for deeper analysis:

```bash
jupyter notebook notebooks/analysis.ipynb
```

Using the full CORD-19 metadata CSV
1. Download `metadata.csv` from the CORD-19 dataset (Kaggle: https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) and place it in `data/metadata.csv`.
2. The notebook and app prefer `data/metadata.csv` and will automatically fall back to `data/metadata_sample.csv` when the full file is not present.

Running tests
This project contains a small set of tests using pytest. To run them locally:

```powershell
pytest -q
```

Continuous integration (GitHub Actions)
This repository includes a CI workflow: `.github/workflows/ci.yml`. The workflow installs the requirements and runs pytest on pushes and pull requests to `main`.

Deploy to Streamlit Cloud
1. Push the repository to GitHub (make sure requirements.txt, app/streamlit_app.py and streamlit.toml are in the repo).
2. Sign in to Streamlit Cloud (https://streamlit.io/cloud) and create a new app connected to your GitHub repository. Set the app file path to `app/streamlit_app.py`.
3. Click **Deploy**. Streamlit Cloud will install dependencies and run your app. Once deployed you will receive a public URL that you can share.

Notes & recommendations
- The TF-IDF/LDA demo in `notebooks/analysis.ipynb` is intentionally small to run on the sample dataset. For the full metadata CSV you should tune parameters (min_df/max_df, n_components), and consider sampling or more scalable algorithms (gensim, incremental LDA).
- Add more tests to improve CI coverage (data quality checks, notebook execution tests, app endpoints).

Repository structure
```
Frameworks_Assignment/
├─ app/streamlit_app.py
├─ data/metadata_sample.csv
├─ notebooks/analysis.ipynb
├─ scripts/check_env.py
├─ tests/test_basic.py
├─ requirements.txt
├─ .github/workflows/ci.yml
├─ streamlit.toml
└─ README.md
