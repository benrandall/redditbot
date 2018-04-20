# Imports
import praw                 # For reddit API
import time                 # For sleep function
import sys                  # For stderr message output
import configparser         # For reading ini file for authentication
import certifi              # 
from pytube import YouTube  # For downloading YouTube videos
import moviepy.editor

# Read the config filea
config = configparser.ConfigParser()
config.read('authentication.ini')
USERNAME = config.get('redditbot', 'username')
PASSWORD = config.get('redditbot', 'password')
CLIENTID = config.get('redditbot', 'client_id')
SECRET = config.get('redditbot', 'client_secret')
USER_AGENT = config.get('redditbot', 'user_agent')


def main():
    
	# Initialize Reddit instance
    reddit = praw.Reddit(user_agent=USER_AGENT,
                      client_id=CLIENTID,
                      client_secret=SECRET,
                      username=USERNAME,
                      password=PASSWORD)
    reddit.config._ssl_url = None
    print("Logged in.", file=sys.stderr)

    # Get top videos of the day
    subreddit = reddit.subreddit('youtubehaiku')
    limit = 25
    i = 0
    for submission in subreddit.top('day'):
        if "[Announcement]" or "[NSFW]" not in submission.title:
            url = submission.url
            if "youtu" in url:
                print("Downloading:", submission.title, file=sys.stderr)
                ''' yt = YouTube(submission.url)
                
                stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
                #TODO: check if stream is valid
                stream.download('./clips/')'''
                i = i + 1
        if i >= limit:
            break



main()
