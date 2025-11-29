import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud
import re

st.set_page_config(page_title='CORD-19 Data Explorer', layout='wide')

@st.cache_data
def load_data():
    base = os.path.join(os.path.dirname(__file__), '..')
    paths = [
        os.path.join(base, 'data', 'metadata.csv'),
        os.path.join(base, 'data', 'metadata_sample.csv'),
    ]
    for p in paths:
        if os.path.exists(p):
            df = pd.read_csv(p, low_memory=False)
            return df
    st.error('No metadata file found. Add metadata.csv or use the provided metadata_sample.csv in the data/ folder.')
    return pd.DataFrame()

@st.cache_data
def prepare(df):
    df = df.copy()
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract'] = df['abstract'].fillna('')
    df['abstract_word_count'] = df['abstract'].str.split().apply(len)
    return df

# Simple tokenizer
_stopwords = set(["the","and","a","of","in","to","for","on","is","with","by","as","from"]) 

def simple_tokens(text, stop_words=_stopwords):
    text = (text or '').lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = [t for t in text.split() if t and t not in stop_words]
    return tokens

# App layout
st.title('CORD-19 Data Explorer')
st.write('Simple exploration of the CORD-19 metadata (title/abstract + basic metadata).')

# Load data
with st.spinner('Loading data...'):
    df = load_data()

if df.empty:
    st.stop()

df = prepare(df)

# Sidebar controls
st.sidebar.header('Filters')
min_year = int(df['year'].min() or 2019)
max_year = int(df['year'].max() or 2022)
year_range = st.sidebar.slider('Select year range', min_year, max_year, (min_year, max_year))
selected_sources = st.sidebar.multiselect('Source (source_x)', sorted(df['source_x'].dropna().unique()), default=sorted(df['source_x'].dropna().unique()))

# Apply filters
mask = df['year'].between(year_range[0], year_range[1]) & df['source_x'].isin(selected_sources)
df_filt = df[mask]

# Summary cards
col1, col2, col3 = st.columns(3)
col1.metric('Papers (selected)', len(df_filt))
col2.metric('Unique journals', df_filt['journal'].nunique())
col3.metric('Avg. abstract words', round(df_filt['abstract_word_count'].mean() or 0, 1))

# Plots
st.header('Publications by Year')
if df_filt['year'].notna().any():
    year_counts = df_filt['year'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8,3))
    sns.barplot(x=year_counts.index.astype('Int64'), y=year_counts.values, palette='Blues_d', ax=ax)
    ax.set_title('Publications by year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    st.pyplot(fig)
else:
    st.info('No publication years present in the selected subset.')

st.header('Top journals')
top_j = df_filt['journal'].value_counts().nlargest(10)
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x=top_j.values, y=top_j.index, palette='viridis', ax=ax)
ax.set_xlabel('Number of papers')
ax.set_ylabel('Journal')
st.pyplot(fig)

st.header('Title word cloud')
all_title_tokens = []
for t in df_filt['title'].fillna(''):
    all_title_tokens += simple_tokens(t)
text_for_wc = ' '.join(all_title_tokens) or 'empty'
wc = WordCloud(width=800, height=300, background_color='white').generate(text_for_wc)
fig, ax = plt.subplots(figsize=(10,3))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

st.header('Sample papers')
st.dataframe(df_filt[['publish_time','year','title','authors','journal','source_x']].sort_values('publish_time', ascending=False).head(50))

st.write('---')
st.write('Tips: Add the full `metadata.csv` to data/metadata.csv to explore the entire dataset. The app will automatically prefer the full dataset if present.')
