# Import packages 
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components 
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import pinecone
from key import cid, secret

# Text
st.title('Sneezed on These Beats')

# Step 1: Get user to input the playlist url/spotify ID
playlist_id = st.text_input("Your playlist ID/URI/URL", key="playlist_id")
if not playlist_id:
    st.stop()

msg = 'Thank you for inputting a playlist, getting your recommendations now...'
    
if playlist_id:
    with st.spinner(msg):
        
# Step 2: Load Spotify dataset 
        st.cache(show_spinner=False, suppress_st_warning=True)
        def load_data(): 
            return pd.read_pickle("./data/all_song_ft.pkl")
        
        all_song_ft = load_data()

# Step 3: Access playlist info using Spotify API
        scope = "playlist-modify-public"
        redirect_uri = "https://github.com/karinakong"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, 
                                                       client_secret=secret, 
                                                       redirect_uri=redirect_uri, 
                                                       scope=scope))
        # client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # Function that takes in a playlist id/url
        # Returns a list of dict (dict=song) 
        def song_lst(playlist_id):
            return sp.playlist_tracks(playlist_id)['items']

        # Define a function that takes in a list of dict where each dict is a song that a user listened to
        # Returns a summarized vector for the songs that exist in the original Spotify dataset
        # song_lst = sp.playlist_tracks(<playlist_url>)['items']
        def song_vec(song_lst):
                # Store all track_ids in a list 
            lst = [] 
            for song in song_lst:
                track_id = song['track']['id']
                lst.append(track_id)

            # Create a df for all songs in the playlist that exist in the Spotify dataset     
            song_df = all_song_ft[all_song_ft['track_id'].isin(lst)] 
            # Summarize the playlist into a single vector by taking the mean of all songs in the playlist 
            playlist_vec = song_df.iloc[:, 1:].mean().tolist()
            playlist_songids = lst

            return playlist_vec, playlist_songids

        song_list = song_lst(st.session_state.playlist_id)
        playlist_vec = song_vec(song_list)[0]
        playlist_songids = song_vec(song_list)[1]

# Step 4: Query vector database 
        pinecone.init(api_key='3b9bd9d9-88f0-4911-a7e9-d589e7447fa1', 
                     environment="us-west1-gcp")
        index = pinecone.Index("spotifyv1")
        recs_dict = index.query(
            vector=playlist_vec, #vector to find similar vectors for 
            top_k=15, #number of results to return 
            filter={ 
                "track_id" : {"$nin" : playlist_songids} #filter for songs that are NOT in the playlist already
            },
            include_metadata = True
        )
        recid_list = [song['id'] for song in recs_dict['matches']]
        
        msg = 'Check out Spotify for your newly created playlist!'
        st.success(msg)
        
# Step 5: Show the recommended songs
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
        
# Step 6: Create playlist and add recommended tracks 
        profile = sp.me()
        name = 'Sneezed on These Beats'
        des = 'Test'
        rec_playlist = sp.user_playlist_create(user=profile['id'], 
                                name=name, 
                                public=True, 
                                collaborative=False, 
                                description=des)
        
        sp.user_playlist_add_tracks(user=profile['id'], 
                                    playlist_id=rec_playlist['id'], 
                                    tracks=recid_list, 
                                    position=None)
                



