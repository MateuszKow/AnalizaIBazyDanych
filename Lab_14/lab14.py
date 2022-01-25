from textblob import TextBlob
from typing import List
import numpy as np

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
    return valid,list_of_coefficients


def hurwitz_necessery_and_suffient(list_of_coefficients:List):
    if len(list_of_coefficients) == 3 and hurwitz_coefficients(list_of_coefficients)[0] is True:
        return True
    else:
        return False

def hurwitz_matrix(list_of_coefficients:List):
    n=len(list_of_coefficients)-1
    h_matrix=np.zeros((n,n))
    p=0
    for x in range(n):
        if (x!=0 and x%2==0):
            p+=1
        for y in range(n):
            if x%2==0:
                if (2*y+1<=n):
                    h_matrix[x,y+p]=list_of_coefficients[2*y+1]
            if x%2==1:
                if (2*y<=n):
                    h_matrix[x,y+p]=list_of_coefficients[2*y]


    return h_matrix


def hurwitz_stability(matrix):
    for x in range(1,len(matrix)):
        mat=matrix[:x,:x]
        if np.linalg.det(mat)<=0:
            return False
    return True

def hurwitz(list_of_coefficients:List):
    valid,list_coeff=hurwitz_coefficients(list_of_coefficients)
    if valid is False:
        return False
    else:
        list_of_coefficients=list_coeff
    if hurwitz_necessery_and_suffient(list_of_coefficients) is True:
        return True
    matrix=hurwitz_matrix(list_of_coefficients)
    if hurwitz_stability(matrix) is False:
        return False
    else:
        return True

