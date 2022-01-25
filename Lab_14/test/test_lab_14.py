from lab14 import hello,extract_sentiment,text_contain_word,hurwitz_coefficients,hurwitz_necessery_and_suffient,hurwitz_matrix,hurwitz_stability,hurwitz

import pytest
import numpy as np

def test_hello():
    got = hello("Mateusz")
    want= "Hello Mateusz"

    assert got == want

#testdata=["I think today will be a great day","I do not think this will turn well"]
testdata=["I think today will be a great day"]


@pytest.mark.parametrize('sample',testdata)
def test_extract_sentiment(sample):
    sentiment=extract_sentiment(sample)
    assert sentiment>0

test_data_word=[("There is a duck in this sentence","duck",True),
("There is void here","duck",False)]

@pytest.mark.parametrize('sample_duck,word,expected_output',test_data_word)

def test_text_contain_word(sample_duck,word,expected_output):
    assert text_contain_word(word,sample_duck) == expected_output


test_data_hurwitz_coefficients=[([1,2,3,4,5,6],(True,[1,2,3,4,5,6])),
([4,5,6,9],(True,[4,5,6,9])),([-5,1,2,3],(False,[5,-1,-2,-3])),([2,1,0,3],(False,[2,1,0,3])),([-1,-2,-3,-4,-5,-6],(True,[1,2,3,4,5,6]))]

@pytest.mark.parametrize('sample_coefficient,expected_output',test_data_hurwitz_coefficients)

def test_hurwitz_coefficients(sample_coefficient,expected_output):
    assert hurwitz_coefficients(sample_coefficient)==expected_output


test_data_necessery_and_suffient=[([2,3,1],True),([4,5,6,7],False),([4,5,-6,-7],False),([4,-5,6],False)]

@pytest.mark.parametrize('sample_n_a_s,expected_output',test_data_necessery_and_suffient)

def test_hurwitz_necessery_and_suffient(sample_n_a_s,expected_output):
    assert hurwitz_necessery_and_suffient(sample_n_a_s) == expected_output


test_matrix=[([1,2,3,4,5],np.array([[2,4,0,0],[1,3,5,0],[0,2,4,0],[0,1,3,5]])),([10,2,3],np.array([[2,0],[10,3]])),([1,6,4,7,11,2],np.array([[6,7,2,0,0],[1,4,11,0,0],[0,6,7,2,0],[0,1,4,11,0],[0,0,6,7,2]]))]

@pytest.mark.parametrize('matrix_stable,expected_output',test_matrix)

def test_hurwitz_matrix(matrix_stable,expected_output):
    assert np.all(hurwitz_matrix(matrix_stable) == expected_output)

test_stability=[(np.array([[1,30,0],[1,4,0],[0,1,30]]),False),(np.array([[9,6,0],[2,4,0],[0,9,6]]),True)]

@pytest.mark.parametrize('hurwitz_stable,expected_output',test_stability)

def test_hurwitz_stability(hurwitz_stable,expected_output):
    assert hurwitz_stability(hurwitz_stable)== expected_output


test_hurwitz=[([4,5,6],True),([-5,-8,-5,-5],True),([5,-2,0,5],False),([1,2,3,4,5],False)]

@pytest.mark.parametrize('hurwitz_sample,expected_output',test_hurwitz)

def test_hurwitz(hurwitz_sample,expected_output):
    assert hurwitz(hurwitz_sample)== expected_output