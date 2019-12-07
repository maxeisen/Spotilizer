import spotipy
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
token = "BQDLUpQ12NsxxjH7il4QRu0UMnC6My8_WLthPghR6_V6kdwm029WYKT6JKMvSCWhEH0_giyS0NKX05q3UQ5dkayrUOYyVFkXGZVdVuHB"
spotify = spotipy.Spotify(auth=token)

results = spotify.artist_albums(birdy_uri, album_type='album')
print(results)
username = "12165810876"
