import praw
import csv
reddit = praw.Reddit(client_id='sujSjYzYUV5WqA',
                     client_secret='tGJ1QvmiY4XaFEhSW0W7wL7jEw8',
                     user_agent='my user agent')
f = open('iphone11.csv','w')
f.write("Title \n")
#print(reddit.read_only
for submission in reddit.subreddit('iphone11').top(limit=50):
    print(submission.title)
    f.write(submission.title)
    f.write("\n")
f.close()

f = open('k20pro.csv','w')
f.write("Title \n")
#print(reddit.read_only
for submission1 in reddit.subreddit('RedmiK20Pro').top(limit=50):
    print(submission1.title)
    f.write(submission1.title)
    f.write("\n")
f.close()

f = open('XiaomiMi9.csv','w')
f.write("Title \n")
#print(reddit.read_onlyR
for submission12 in reddit.subreddit('XiaomiMi9').top(limit=50):
    print(submission12.title)
    f.write(submission12.title)
    f.write("\n")
f.close()

f = open('galaxys10.csv','w')
f.write("Title \n")
#print(reddit.read_onlyR
for submission13 in reddit.subreddit('galaxys10').top(limit=50):
    print(submission13.title)
    f.write(submission13.title)
    f.write("\n")
f.close()

f = open('OnePlus7tPro.csv','w')
f.write("Title \n")
#print(reddit.read_onlyR
for submission1 in reddit.subreddit('OnePlus7tPro').top(limit=50):
    print(submission1.title)
    f.write(submission1.title)
    f.write("\n")
f.close()

f = open('OnePlus7Pro.csv','w')
f.write("Title \n")
#print(reddit.read_onlyR
for submission1 in reddit.subreddit('OnePlus7Pro').top(limit=50):
    print(submission1.title)
    f.write(submission1.title)
    f.write("\n")
f.close()

f = open('HuaweiP30.csv','w')
f.write("Title \n")
#print(reddit.read_onlyR
for submission1 in reddit.subreddit('HuaweiP30').top(limit=50):
    print(submission1.title)
    f.write(submission1.title)
    f.write("\n")
f.close()

f = open('lgg7.csv','w')
f.write("Title \n")
#print(reddit.read_onlyR
for submission1 in reddit.subreddit('lgg7').top(limit=50):
    print(submission1.title)
    f.write(submission1.title)
    f.write("\n")
f.close()

f = open('SamsungNote10.csv','w')
f.write("Title \n")
#print(reddit.read_onlyR
for submission1 in reddit.subreddit('SamsungNote10').top(limit=50):
    print(submission1.title)
    f.write(submission1.title)
    f.write("\n")
f.close()

f = open('iPhone11Pro.csv','w')
f.write("Title \n")
#print(reddit.read_onlyR
for submission1 in reddit.subreddit('iPhone11Pro').top(limit=50):
    print(submission1.title)
    f.write(submission1.title)
    f.write("\n")
f.close()

f = open('iPhone11ProMax.csv','w')
f.write("Title \n")
#print(reddit.read_onlyR
for submission1 in reddit.subreddit('iPhone11ProMax').top(limit=50):
    print(submission1.title)
    f.write(submission1.title)
    f.write("\n")
f.close()

