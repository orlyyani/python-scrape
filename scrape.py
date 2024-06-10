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
url = os.getenv('REDDIT_URL')

# Check if URL is provided
if url is None:
    print("Reddit URL is not provided in the .env file.")
    sys.exit(1)

# Get the submission object
submission = reddit.submission(url=url)

# Fetch comments
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)

