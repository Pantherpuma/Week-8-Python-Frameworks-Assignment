# Frameworks_Assignment — CORD-19 Data Explorer

This repository is a starter project for the Week 8 assignment: a beginner-friendly exploration of the CORD-19 metadata file with a Jupyter notebook and a Streamlit app.

What I added for you:

- small sample dataset `data/metadata_sample.csv` so the app + notebook are runnable without the full dataset
- `notebooks/analysis.ipynb` — a notebook with exploration, cleaning, and visualizations
- `app/streamlit_app.py` — a Streamlit app showing interactive charts
- `requirements.txt` and `.gitignore`

How to use:

1. Put the full `metadata.csv` (if you have it) into the `data/` folder — the app/notebook will prefer `data/metadata.csv` and fall back to `data/metadata_sample.csv`.
2. Create a Python environment and install requirements:

   pip install -r requirements.txt

3. Run the Jupyter notebook or start the Streamlit app:

   # Jupyter
   jupyter notebook notebooks/analysis.ipynb

   # Streamlit app
   streamlit run app/streamlit_app.py

Notes
- The complete CORD-19 metadata file is large; you can download the CSV from Kaggle: https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge
- This starter focuses on core tasks from the assignment (exploration, cleaning, visualization, Streamlit UI). Feel free to extend the analyses.

Quick checks and recommended commands (PowerShell)

```powershell
# Create a venv (PowerShell)
python -m venv .venv; .\.venv\Scripts\Activate.ps1
# Install requirements
pip install -r requirements.txt
# Run the environment-check helper
python scripts\check_env.py
# Run the Streamlit app
streamlit run app/streamlit_app.py
```

Tip: If you have the full `metadata.csv` place it in `data/metadata.csv`. The notebook and app will automatically prefer the full file and fall back to the sample if necessary.

Continuous Integration (GitHub Actions)

This repository includes a basic CI workflow (.github/workflows/ci.yml) that will install requirements and run pytest on pushes and pull requests to `main`.

Deploying to Streamlit Cloud (quick guide)

1. Push this repository to GitHub. Make sure `requirements.txt` and `app/streamlit_app.py` are at the repo root (they are in this starter).  
2. Visit https://streamlit.io/cloud and sign in with your GitHub account.  
3. In Streamlit Cloud, click **New app** and select this repository and branch. For the app path enter `app/streamlit_app.py`.  
4. Click **Deploy** — Streamlit Cloud will create the app and run it.  

Limitations / notes: I can't deploy from this environment on your behalf. To get a live link, connect your GitHub repo to Streamlit Cloud and follow the steps above — once deployed Streamlit Cloud will give you the public URL.
