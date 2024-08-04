import praw
import json

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id='f3O-dcB13qSqoMxKh_XkcA',
    client_secret='wqPqVtgyCs8kC7fsdbY1oJ8dph8PBQ',
    user_agent='NLPArgumentMiningBot/0.1'
)

def collect_top_posts(subreddit_name, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for submission in subreddit.top(limit=limit):
        post_info = {
            "title": submission.title,
            "score": submission.score,
            "url": submission.url,
            "id": submission.id,
            "created": submission.created,
            "body": submission.selftext,
        }
        posts.append(post_info)
    return posts

if __name__ == "__main__":
    top_posts = collect_top_posts('PoliticalDiscussion', limit=10)
    with open('data/raw/top_posts.json', 'w') as f:
        json.dump(top_posts, f, indent=4)
    print("Data saved to data/raw/top_posts.json")
