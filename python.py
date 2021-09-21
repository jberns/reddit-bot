import praw
import os
from dotenv import load_dotenv

load_dotenv()

tags = ["python", "react", "javascript", "developer"]

def main():
  reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent="desktop:com.reddit-botv0.0.0"
  )

  subreddit = reddit.subreddit("gaming")

  # for submission in subreddit.hot(limit=5):
  #   print("Title: ", submission.title)
  #   print("--------------\n")


  for submission in subreddit.stream.submissions():
    normalized_title = submission.title.lower()
    print(submission.id)
    print(submission.title)
    print(submission.author)
    print(submission.created_utc)
    print(submission.selftext)
    print("-" * 30)
    # for tag in tags:
    #   if tag in normalized_title:
    #     print(submission.title)

if __name__ == "__main__":
  main()