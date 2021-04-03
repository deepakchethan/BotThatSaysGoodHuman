import praw

trigger_text = "Good bot"
reply_text = "Good human"

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('BotThatSaysGoodHuman')

for comment in subreddit.stream.comments():

    # check for Good bot in each comment
    if trigger_text in comment.body:

        # respond with Good Human
        comment.reply(reply_text)
        print('Replied to ' + comment.body)
