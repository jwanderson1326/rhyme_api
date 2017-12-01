from nose.tools import *
from .. import python

def test_random_return():
    normal = python.random_return.return_random('Hello goodbye')
    punctuated = python.random_return.return_random('hello, goodbye,')
    assert((normal == 'Hello' or normal == 'goodbye'))
    assert((punctuated =='hello' or punctuated == 'goodbye'))

def test_rhyme():
    normal = python.rhyme.get_rhymes('big')
    capitalized = python.rhyme.get_rhymes('BiG')
    gibberish = python.rhyme.get_rhymes('asdfasdf')
    number = python.rhyme.get_rhymes(1)
    punctuated = python.rhyme.get_rhymes('good!')
    assert(type(normal) == list)
    assert(type(capitalized) == list)
    assert(type(gibberish) == str)
    assert(type(number) == str)
    assert(type(punctuated) == list)


    
