import pandas as pd
from bs4 import BeautifulSoup as bs
import nltk
import re

filepath = "your file path to the kindle csv file"
data = pd.read_csv(filepath)
textlist = data["reviewText"]

# cleaned_list is a list of lists, and each list represents a tokenized words from each review.
cleaned_list = []
for i in range(len(textlist)):
    temp = textlist[i]
    if type(temp) != str:
        cleaned_list.append([])
    else:
        cleaned = bs(temp, "html.parser").get_text()
        tokens = nltk.word_tokenize(cleaned)
        cleaned_list.append(tokens)

# cleaned_list_nosw is the same as cleaned_list, but punctuations and stopwords are removed.
stop_words = nltk.corpus.stopwords.words('english')
cleaned_list_nosw = []
for eachlist in cleaned_list:
    newlist = []
    for token in eachlist:
        token = token.lower()
        if re.search(r"[a-zA-Z]", token) is not None and token not in stop_words:
            newlist.append(token)
    cleaned_list_nosw.append(newlist)