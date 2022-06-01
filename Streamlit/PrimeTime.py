
import pandas as pd
import streamlit as st
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

st.sidebar.title('PrimeTime: Amazon Prime Movie & Show Recommendation System')

st.sidebar.caption('By [Jawwad A. Siddiqui](https://www.linkedin.com/in/jsiddiqui85/)')

meta_df = pd.read_csv('./Data/meta_df.csv')

model_df = pd.read_csv('./Data/model_df.csv')

title = st.text_input('Movie Title: ')
n_recs = st.number_input('How many recommendations? ', min_value=1, max_value=30)
m_or_s = st.multiselect('Would you like MOVIE or SHOW recommendations? ',
                          options=['MOVIE', 'SHOW'])


def cos_movie_recommend(title, n_recs, m_or_s):
    
    movie2 = meta_df.index[meta_df['title'] == title]
    
    y = np.array(model_df.loc[movie2]).reshape(1, -1)
    cos_sim = cosine_similarity(model_df, y)
    cos_sim = pd.DataFrame(data=cos_sim, index=model_df.index)
    cos_sim.sort_values(by = 0, ascending = False, inplace=True)
    results = cos_sim.index.values[1:n_recs+50]
    results_df = meta_df.loc[results]
    results_df.reset_index(inplace=True)
    
    # Rename and capitalize columns
    results_df.rename(columns={'title':'Movie Title',
                              'type':'Type',
                              'release_year':'Release Year',
                              'runtime':'Runtime (minutes)',
                              'genres':'Genres',
                              'imdb_score':'IMDB Score',
                              'name':'Cast Name'}, inplace=True)
    
    # Filter on the type (movie or show)
    results_df  = results_df[results_df['Type'] == m_or_s[0]]
    
    # Convert Release Year and Runtime columns to display as an integer instead of a float
    results_df[['Release Year','Runtime (minutes)','IMDB Score']] = results_df[['Release Year','Runtime (minutes)', 'IMDB Score']]
    
#    results_df = results_df.astype(str)
    
    # Only display relevant columns
    return (results_df[['Movie Title','Type','Release Year','Runtime (minutes)','Genres','IMDB Score','Cast Name']]).head(n_recs)

run = st.button('Click To Get Results!')

if run:
    movie_results = cos_movie_recommend(title, n_recs, m_or_s)
    st.table(movie_results)
