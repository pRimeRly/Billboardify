# Billboardify
 
### A web scraper application for creating Spotify playlist from Billboard top 100 songs of a specific year.
 
## Project Description
This project creates a Spotify playlist of the top 100 songs from the Billboard chart of a user-specified year. The project uses the BeautifulSoup and requests libraries to scrape the Billboard website and retrieve the song names of the top 100 songs of a given year. Then, using the Spotify API and spotipy library, the project searches for the songs in the Spotify database and adds them to a new or existing playlist on the user's Spotify account.

## Prerequisites
1. You need to have Python 3 installed on your machine.
2. You need to have a Spotify developer account, and Spotify API credentials, including the Spotify client ID and Spotify client secret.
3. You also need to have a Spotify account to which you want to add the playlist.


## Installation
1. Clone this repository
2. Create a virtual environment and activate it using your preferred method.
3. Install the required libraries using pip install -r requirements.txt.
4. Create a new file named .env in the project root directory, and set your Spotify credentials as environmental variables:
```
SPOTIFY_CLIENT-ID = "your Spotify client ID"
SPOTIFY_CLIENT-SECRET = "your Spotify client secret"
SPOTIFY_REDIRECT_URI = "your Spotify redirect URI"
```
 
5. Run the program using python main.py.
 
## Usage
```
Run the program using python main.py.
Input the year in the YYYY-MM-DD format when prompted.
The program will then scrape the Billboard website for the top 100 songs of the year and search for the songs in the Spotify database.
If the playlist already exists in your Spotify account, the program will add the songs to the existing playlist.
If the playlist does not exist, the program will create a new playlist and add the songs to the playlist.
The program will display the playlist information after it has been created or updated.
```
