# Spotify Music Recommender System

## Summary
The objective of this project is to create a full stack Spotify music recommender system that recommends a user songs based on an existing Spotify playlist. The scope of this project covers 
- Data cleaning
- EDA
- Data preprocessing (scaling, TF-IDF, vectorizing) 
- Spotify API (to retrieve Spotify data)
- Pinecone (vector search database for recommender systems)
- Streamlit (platform for building FE web apps for data science projects)

## Data
The original data files used in the working_code notebooks are taken from this [Kaggle dataset](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks). All the associated data files are too large to be uploaded to GitHub so they are not included in this repository. 

## Try it!
Check out the web app [here](https://karinakong-young-gr-spotify-music-recommenderapp-codeapp-ljtr4p.streamlitapp.com/)! A version of the web app that automatically creates a playlist with the recommended songs is currently under development. You can find the code for the web app in the app_code folder.

## References 
- [Pinecone](https://www.pinecone.io/semantic-search/)
    - An online vector search database used to store and query the Spotify dataset
- [Spotipy documentation](https://spotipy.readthedocs.io/en/master/#)
    - Spotify API, used to get user, track and playlist informationb
- [Streamlit](https://streamlit.io/)
    - Used to create the web app