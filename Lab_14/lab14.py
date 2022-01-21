from textblob import TextBlob
from typing import List
from numpy import linalg, array

def hello(name):
    return f'Hello {name}'

def extract_sentiment(text):
    text=TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word:str,text:str):
    return word in text

def hurwitz_coefficients(list_of_coefficients:List):
    if list_of_coefficients[0] <0:
        for x in range(len(list_of_coefficients)):
            list_of_coefficients[x]=-1*list_of_coefficients[x]
    valid=True
    for elem in list_of_coefficients:
        if elem<=0:
            valid=False
    return valid


def hurwitz_necessery_and_suffient(list_of_coefficients:List):
    if len(list_of_coefficients) == 3 and hurwitz_coefficients(list_of_coefficients)is True:
        return True
    else:
        return False


print(linalg.det(array([[10,2,3],[4,5,6],[7,8,9]])))


