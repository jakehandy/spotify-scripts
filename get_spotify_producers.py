import requests

class InvalidTrackIDError(Exception):
    pass

class InvalidAccessTokenError(Exception):
    pass

def get_producer_names(spotify_track_id, spotify_access_token):
    if not spotify_track_id or not spotify_access_token:
        raise ValueError("Both spotify_track_id and spotify_access_token must be provided.")
    
    track_url = f"https://api.spotify.com/v1/tracks/{spotify_track_id}"
    
    headers = {
        "Authorization": f"Bearer {spotify_access_token}"
    }
    
    response = requests.get(track_url, headers=headers)
    
    if response.status_code == 400 or response.status_code == 404:
        raise InvalidTrackIDError("The provided track ID is invalid.")
    elif response.status_code == 401:
        raise InvalidAccessTokenError("The provided access token is invalid.")
    elif response.status_code == 200:
        track_info = response.json()
        album_id = track_info['album']['id']
        album_url = f"https://api.spotify.com/v1/albums/{album_id}"
        album_response = requests.get(album_url, headers=headers)

        if album_response.status_code == 401:
            raise InvalidAccessTokenError("The provided access token is invalid.")
        elif album_response.status_code == 200:
            album_info = album_response.json()
            producers = [credit['name'] for credit in album_info['credits']['personnel'] if 'Producer' in credit['role']]
            return producers
    return []

track_id = "11dFghVXANMlKmJXsNCbNl"
access_token = "your_access_token_here"

try:
    producer_names = get_producer_names(track_id, access_token)
    print("Producers of the track:")
    for producer in producer_names:
        print(producer)
except InvalidTrackIDError as e:
    print(e)
except InvalidAccessTokenError as e:
    print(e)
