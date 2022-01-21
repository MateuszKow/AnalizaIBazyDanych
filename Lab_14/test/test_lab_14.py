from lab14 import hello,extract_sentiment,text_contain_word,hurwitz_coefficients,hurwitz_necessery_and_suffient

import pytest

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


test_data_hurwitz_coefficients=[([1,2,3,4,5,6],True),
([4,5,6,9],True),([-5,1,2,3],False),([2,1,0,3],False),([-1,-2,-3,-4,-5,-6],True)]

@pytest.mark.parametrize('sample_coefficient,expected_output',test_data_hurwitz_coefficients)

def test_hurwitz_coefficients(sample_coefficient,expected_output):
    assert hurwitz_coefficients(sample_coefficient)==expected_output


test_data_necessery_and_suffient=[([2,3,1],True),([4,5,6,7],False),([4,5,-6,-7],False),([4,-5,6],False)]

@pytest.mark.parametrize('sample_n_a_s,expected_output',test_data_necessery_and_suffient)

def test_hurwitz_necessery_and_suffient(sample_n_a_s,expected_output):
    assert hurwitz_necessery_and_suffient(sample_n_a_s) == expected_output


test_data_stable=[([[10,2,3],[4,5,6],[7,8,9]],False)]


@pytest.mark.parametrize('sample_stable,expected_output',test_data_stable)

def test_hurwitz_stable(sample_stable,expected_output):
    assert hurwitz_stable(sample_stable) == expected_output