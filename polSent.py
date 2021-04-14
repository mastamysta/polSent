import pandas as pd
import numpy as np

#returns dataframe cotaining lexicon
def getLexicon():
    return pd.read_csv("politics.tsv",sep='\t')

def createHash(lex):
    h = {}
    for i in range(0, lex.shape[0]):
        h[lex["word"][i]] = lex["score"][i]
    return h

def findSumScore(tweet, h):
    tokenList = tweet.split()
    sum = 0
    for tok in tokenList:
        if tok in h:
            sum += h[tok]
    
    return sum

def findAverageScore(tweet, h):
    tokenList = tweet.split()
    sum = 0
    for tok in tokenList:
        if tok in h:
            sum += h[tok]
    
    return sum/len(tokenList)

def analyse(tweets):
    scores = [findAverageScore for tweet in tweets]

def test():
    lex = getLexicon()
    h = createHash(lex)
    print(findAverageScore("I am a giant loser", h))

if __name__ == '__main__':
    test()