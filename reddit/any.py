import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import csv


f=pd.read_csv("iphone11.csv")
keep_col = ['clean']
new_f = f[keep_col]
new_f.to_csv("iphone11.csv", index=False)

with open('iphone11.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    for row in read :
        makeitastring = ''.join(map(str, row))
        sentence = makeitastring
        analysisPol = TextBlob(sentence).polarity
        analysisSub = TextBlob(sentence).subjectivity
        plt.scatter(analysisPol,analysisSub,color='red')
#        print(analysis)

plt.title("Sentiment Analysis Iphone11", fontsize = 20)
plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
plt.show()
# Creating a textblob objectw and assigning the sentiment property


f=pd.read_csv("galaxys10.csv")
keep_col = ['clean']
new_f = f[keep_col]
new_f.to_csv("galaxys10.csv", index=False)

with open('galaxys10.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    for row in read :
        makeitastring = ''.join(map(str, row))
        sentence = makeitastring
        analysisPol = TextBlob(sentence).polarity
        analysisSub = TextBlob(sentence).subjectivity
        plt.scatter(analysisPol,analysisSub,color='blue')
#        print(analysis)

plt.title("Sentiment Analysis Galaxys10", fontsize = 20)
plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
plt.show()

f=pd.read_csv("iphone11Pro.csv")
keep_col = ['clean']
new_f = f[keep_col]
new_f.to_csv("iphone11Pro.csv", index=False)

with open('iphone11Pro.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    for row in read :
        makeitastring = ''.join(map(str, row))
        sentence = makeitastring
        analysisPol = TextBlob(sentence).polarity
        analysisSub = TextBlob(sentence).subjectivity
        plt.scatter(analysisPol,analysisSub,color='green')
#        print(analysis)

plt.title("Sentiment Analysis Iphone11 Pro", fontsize = 20)
plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
plt.show()

f=pd.read_csv("iphone11ProMax.csv")
keep_col = ['clean']
new_f = f[keep_col]
new_f.to_csv("iphone11ProMax.csv", index=False)

with open('iphone11ProMax.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    for row in read :
        makeitastring = ''.join(map(str, row))
        sentence = makeitastring
        analysisPol = TextBlob(sentence).polarity
        analysisSub = TextBlob(sentence).subjectivity
        plt.scatter(analysisPol,analysisSub,color='red')
#        print(analysis)

plt.title("Sentiment Analysis iphone11ProMax", fontsize = 20)
plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
plt.show()

f=pd.read_csv("k20pro.csv")
keep_col = ['clean']
new_f = f[keep_col]
new_f.to_csv("k20pro.csv", index=False)

with open('k20pro.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    for row in read :
        makeitastring = ''.join(map(str, row))
        sentence = makeitastring
        analysisPol = TextBlob(sentence).polarity
        analysisSub = TextBlob(sentence).subjectivity
        plt.scatter(analysisPol,analysisSub,color='blue')
#        print(analysis)

plt.title("Sentiment Analysis k20pro", fontsize = 20)
plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
plt.show()

f=pd.read_csv("OnePlus7Pro.csv")
keep_col = ['clean']
new_f = f[keep_col]
new_f.to_csv("OnePlus7Pro.csv", index=False)

with open('OnePlus7Pro.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    for row in read :
        makeitastring = ''.join(map(str, row))
        sentence = makeitastring
        analysisPol = TextBlob(sentence).polarity
        analysisSub = TextBlob(sentence).subjectivity
        plt.scatter(analysisPol,analysisSub,color='green')
#        print(analysis)

plt.title("Sentiment Analysis OnePlus7Pro", fontsize = 20)
plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
plt.show()

f=pd.read_csv("OnePlus7tPro.csv")
keep_col = ['clean']
new_f = f[keep_col]
new_f.to_csv("OnePlus7tPro.csv", index=False)

with open('OnePlus7tPro.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    for row in read :
        makeitastring = ''.join(map(str, row))
        sentence = makeitastring
        analysisPol = TextBlob(sentence).polarity
        analysisSub = TextBlob(sentence).subjectivity
        plt.scatter(analysisPol,analysisSub,color='red')
#        print(analysis)

plt.title("Sentiment Analysis OnePlus7tPro", fontsize = 20)
plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
plt.show()

f=pd.read_csv("SamsungNote10.csv")
keep_col = ['clean']
new_f = f[keep_col]
new_f.to_csv("SamsungNote10.csv", index=False)

with open('SamsungNote10.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    for row in read :
        makeitastring = ''.join(map(str, row))
        sentence = makeitastring
        analysisPol = TextBlob(sentence).polarity
        analysisSub = TextBlob(sentence).subjectivity
        plt.scatter(analysisPol,analysisSub,color='blue')
#        print(analysis)

plt.title("Sentiment Analysis SamsungNote10", fontsize = 20)
plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
plt.show()

f=pd.read_csv("XiaomiMi9.csv")
keep_col = ['clean']
new_f = f[keep_col]
new_f.to_csv("XiaomiMi9.csv", index=False)

with open('XiaomiMi9.csv', "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    for row in read :
        makeitastring = ''.join(map(str, row))
        sentence = makeitastring
        analysisPol = TextBlob(sentence).polarity
        analysisSub = TextBlob(sentence).subjectivity
        plt.scatter(analysisPol,analysisSub,color='green')
#        print(analysis)

plt.title("Sentiment Analysis XiaomiMi9", fontsize = 20)
plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
plt.show()

#
#f=pd.read_csv("lgg7.csv")
#keep_col = ['Title ']
#new_f = f[keep_col]
#new_f.to_csv("lgg7.csv", index=False)

#with open('lgg7.csv', "rt") as infile:
#    read = csv.reader(infile)
#    for row in read :
#        makeitastring = ''.join(map(str, row))
#        sentence = makeitastring
#        analysisPol = TextBlob(sentence).polarity
#        analysisSub = TextBlob(sentence).subjectivity
#        plt.scatter(analysisPol,analysisSub)
##        print(analysis)
#
#plt.title("Sentiment Analysis Lgg7", fontsize = 20)
#plt.xlabel("← Negative — — — — — — Positive →", fontsize=15)
#plt.ylabel("← Facts — — — — — — — Opinions →", fontsize=15)
#plt.show()
