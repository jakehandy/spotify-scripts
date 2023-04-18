import requests

# Replace this value with your own access token
ACCESS_TOKEN = 'your_access_token_here'

# Replace this value with the track ID for which you want to get credits
TRACK_ID = '11dFghVXANMlKmJXsNCbNl'

def get_track_credits(access_token, track_id):
    """
    Function to get track credits from the experimental credits endpoint.
    """
    # URL for the experimental credits endpoint
    url = f'https://spclient.wg.spotify.com/track-credits-view/v0/experimental/{track_id}'
    
    # Headers for the request
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    # Send GET request to the URL
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the response content
        return response.json()
    else:
        # Raise an error if unable to obtain track credits
        response.raise_for_status()

if __name__ == '__main__':
    try:
        # Get track credits using the provided access token
        track_credits = get_track_credits(ACCESS_TOKEN, TRACK_ID)
        
        # Print track credits
        print(track_credits)
        
    except requests.exceptions.HTTPError as err:
        print(f'An error occurred: {err}')
