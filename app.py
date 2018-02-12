#   Copyright 2018

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import praw            # For reddit API
import time            # For sleep function
import sys             # For stderr message output
import configparser    # For reading ini file for authentication

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
    bot = praw.Reddit(user_agent=USER_AGENT,
                      client_id=CLIENTID,
                      client_secret=SECRET,
                      username=USERNAME,
                      password=PASSWORD)
    print("Logged in.", file=sys.stderr)

    subreddit = bot.subreddit('youtubehaiku')
    comments = subreddit.stream.comments()

    # Fetch videos

main()
