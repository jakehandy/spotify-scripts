# Spotify Scripts
Quick Python scripts to search Spotify. Nothing fancy.

## Get Spotify Producers
get_spotify_producers.py

Currently broken. This attempts to retrieve producers from the Spotify API using the artist roles, but the producer artist role does not exist yet.

## Get Track Credits
get_track_credits.py

Currently broken. This attempts to access Spotify's experimental API endpoint that holds credits information. It is not currently accessible by standard API access.

## Search Producer Names
spotify_search_producer_names.py

Searches Spotify via API for a defined producer name.
**Usage:** `python script_name.py [producer_name]`

Searches track titles for `Prod. by` and `Produced by` (and some variations) and the producer name specified. Returns ISRC, Track Title, and Track URL for matches.
