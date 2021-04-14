import pandas as pd
import numpy as np

#returns dataframe cotaining lexicon
def getLexicon():
    return pd.read_csv("politics.tsv",sep='\t')

def test():
    lex = getLexicon()
    print("Test Executed")

if __name__ == '__main__':
    test()