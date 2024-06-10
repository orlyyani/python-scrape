import praw
import sys
import io
from dotenv import load_dotenv
import os

# Load environment variables from .env fil
load_dotenv()

# Set encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Initialize PRAW with your credentials
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

# URL of the Reddit thread
url = 'https://www.reddit.com/r/musicsuggestions/comments/188acwv/give_me_songs_about_not_being_worried/'

# Get the submission object
submission = reddit.submission(url=url)

# Fetch comments
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)

