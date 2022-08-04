# Import packages 
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components 
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import pinecone

# Text
st.title('Sneezed on These Beats')
st.markdown('This app allows you to input a Spotify playlist URL and get song recommendations based on the playlist.')

# Step 1: Get user to input the playlist url/spotify ID
playlist_id = st.text_input("Your playlist ID/URI/URL", key="playlist_id")
if not playlist_id:
    st.stop()

msg = 'Thank you for inputting a playlist, getting your recommendations now...'
    
if playlist_id:
    with st.spinner(msg):
        
# Step 2: Create playlist vector 
        # Connect to Spotify API
        client_credentials_manager = SpotifyClientCredentials(client_id=st.secrets["cid"], client_secret=st.secrets["secret"])
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
        # Set up authorization for Pinecone API
        pinecone.init(api_key=st.secrets["api_key"], 
                      environment="us-west1-gcp")
        index = pinecone.Index("spotifyv1")

        # Def function that takes in a playlist id/url
        # Returns a list of track_ids for songs in playlist 
        def song_lst(playlist_id):
            songs = sp.playlist_tracks(playlist_id)['items']
            lst = []
            for song in songs:
                track_id = song['track']['id']
                lst.append(track_id)
            return lst 
        
        id_list = song_lst(st.session_state.playlist_id)
        vec_list = []
        
        for song in id_list:
            try: 
                res = index.query(id=song, top_k=1, include_values=True)
                vec_list.append(res['matches'][0]['values'])
            except:
                pass
            
        # Playlist vector created! 
        playlist_vec = pd.DataFrame(vec_list).mean().tolist()


# Step 3: Query vector database with playlist vector 
        recs_dict = index.query(
            vector=playlist_vec, #vector to find similar vectors for 
            top_k=15, #number of results to return 
            filter={ 
                "track_id" : {"$nin" : id_list} #filter for songs that are NOT in the playlist already
            },
            include_metadata = True
        )
        recid_list = [song['id'] for song in recs_dict['matches']]
        
        msg = 'Here are your recommendations!'
        st.success(msg)
        
# Step 4: Show the recommended songs
track_info = sp.tracks(recid_list)['tracks']
img_lst = [track['album']['images'][2]['url'] for track in track_info]
name_lst = [track['name'] for track in track_info]
artist_lst = [artist[0]['name'] for artist in [track['artists'] for track in track_info]]
render_tracks = [{'artist':artist_lst[i], 
  'img' : img_lst[i], 
  'name' : name_lst[i]} for i in range(15)]

for song in render_tracks:
    st.image(song['img'])
    st.write(f"{song['name']}, {song['artist']}")
                







