
# Reddit Music Suggestions Crawler

This Python script utilizes PRAW (Python Reddit API Wrapper) to crawl a specific Reddit thread in search of music suggestions. It fetches comments from the specified thread URL and prints them out. It's a handy tool for discovering songs based on a particular theme or topic discussed within a Reddit community.

## Prerequisites

- Python 3.x
- PRAW (Python Reddit API Wrapper)
- dotenv

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory of the project and add your Reddit API credentials:
    ```
    REDDIT_CLIENT_ID=your_client_id
    REDDIT_CLIENT_SECRET=your_client_secret
    REDDIT_USER_AGENT=your_user_agent
    ```

## Usage

1. Modify the `url` variable in the script to point to the Reddit thread from which you want to fetch music suggestions.
2. Run the script using `python reddit_music_crawler.py`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs, feature requests, or questions.
