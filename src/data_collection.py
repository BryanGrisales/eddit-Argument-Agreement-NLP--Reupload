import praw
import json
from dotenv import load_dotenv
import os

load_dotenv()

# initialize Reddit instance
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

def collect_top_posts(subreddit_names, limit=10):
    all_posts = []
    for subreddit_name in subreddit_names:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.top(limit=limit):
            post_info = {
                "subreddit": subreddit_name,
                "title": submission.title,
                "score": submission.score,
                "url": submission.url,
                "id": submission.id,
                "created": submission.created,
                "body": submission.selftext,
            }
            all_posts.append(post_info)
    return all_posts

if __name__ == "__main__":
    subreddits = ['PoliticalDiscussion', 'ChangeMyView', 'AskReddit']
    top_posts = collect_top_posts(subreddits, limit=10)
    os.makedirs('data/raw', exist_ok=True)
    with open('data/raw/top_posts.json', 'w') as f:
        json.dump(top_posts, f, indent=4)
    print("Data saved to data/raw/top_posts.json")
