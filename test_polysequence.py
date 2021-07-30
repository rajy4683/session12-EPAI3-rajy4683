from polygonlib import check_numerical_similarity
from functools import lru_cache
import math
import numbers
import decimal
import sys
from polygonlib import ConvexPolygon
from polygonsequence import PolygonSequences

from polygonlib import check_numerical_similarity
from functools import lru_cache
import math
import numbers
import decimal
import sys
from polygonlib import ConvexPolygon
import polygonlib
from datetime import datetime
import pytest
from io import StringIO
import sys
import time
import inspect
import os
#import polygonlib
import re

README_CONTENT_CHECK_FOR = [
    "PolygonSequences",
    "PolygonSqIterator",
    "__getitem__",
    "__iter__",
    "get_max_efficiency_poly"   
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

# def test_indentations():
#    ''' Returns pass if used four spaces for each level of syntactically \
#    significant indenting.'''
#    lines = inspect.getsource(polygonlib)
#    spaces = re.findall('\n +.', lines)
#    for space in spaces:
#        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
#        # if (len(space) % 4 == 2):
        #     print("Your script contains misplaced indentations", space)
#        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(polygonlib, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_poly_sequence():
    '''
    Check basic length, access and size of the returned iterator
    '''
    try:
        poly_gen = PolygonSequences(2, 5)
        assert False, ('Seriously! A polygon must have atleast 3 sides')
    except ValueError:
        pass
    
    poly_gen = PolygonSequences(10, 5)
    assert len(poly_gen) == 8, f'Invalid length of sequence: {len(poly_gen)}, Expected:8'
    
    for idx,i in enumerate(range(3,10)):
        edge_count = poly_gen[idx].get_edges
        c_radius = poly_gen[idx].get_circumradius
        assert poly_gen[idx].get_edges == i, f'Expected number of edges = {i} Got: {edge_count}'
        assert c_radius == 5, f'Expected circumradius = 5 Got: {c_radius}'
    
    max_eff_poly = poly_gen.get_max_efficiency_poly.get_edges
    assert max_eff_poly == 10, f'Expected Max Efficiency Polygon: {10}, Got:{max_eff_poly}'
    try:
        _ = poly_gen[100]
        assert False, "Invalid Index allowed for access"
    except IndexError:
        pass
    sliced_val = poly_gen[1:-1:2]
    assert len(sliced_val) == 3, f'Slicing failed. Expected length={3}, Got:{len(sliced_val)}'
    expected_edges = [4,6,8]
    for idx,elem in enumerate(sliced_val):
        assert elem.get_edges == expected_edges[idx], f'Wrong slice returned'
    
    sliced_val = poly_gen[-4::-1]
    assert len(sliced_val) == 5, f'Slicing failed. Expected length={5}, Got:{len(sliced_val)}'
    expected_edges = [7,6,5,4,3]
    for idx,elem in enumerate(sliced_val):
        assert elem.get_edges == expected_edges[idx], f'Wrong slice returned'

def test_poly_length():
    '''
    Verify boundary conditions for all the sequence lengths 
    '''
    poly_gen_20 = PolygonSequences(20, 5)
    poly_gen_21 = PolygonSequences(21, 5)

    assert len(poly_gen_20) != len(poly_gen_21), f'Max Boundary checks failed'

    poly_gen_3 = PolygonSequences(3, 5)
    poly_gen_4 = PolygonSequences(4, 5)

    assert len(poly_gen_3) != len(poly_gen_4), f'Max Boundary checks failed'


def test_poly_iterators():
    '''
    Verify iterator/iterable handling in PolygonSequence class
    '''
    assert '__iter__' in dir(PolygonSequences), f'__iter__ not defined in PolygonSequences'
    assert '__iter__' in dir(PolygonSequences.PolygonSqIterator), f'__iter__ not defined in PolygonSequences.PolygonSqIterator'
    assert  (not '__next__' in dir(PolygonSequences)), f'__next__ should not be defined in PolygonSequences'
    assert '__next__' in dir(PolygonSequences.PolygonSqIterator), f'__next__ not defined in PolygonSequences.PolygonSqIterator'
    
    poly_gen_10 = PolygonSequences(10, 5)
    iter_one = iter(poly_gen_10)
    iter_two = iter(poly_gen_10)
    assert (id(iter_one) != id(iter_two)), (f'Iterator objects must be unique')
    
    poly_gen_20 = PolygonSequences(20, 5)
    poly_len = len([ poly for poly in poly_gen_20])
    
    assert (poly_len== 18), (f'Iterator failed Expected len:{18} Got: {poly_len}')
    try:
        a = next(iter(poly_gen_20))
    except StopIteration:
        assert False, f'Iterable shouldnt have exhausted'
    
    count = 0
    poly_iter = iter(poly_gen_20)
    while True:
        try:
            a = next(poly_iter)
            count += 1
        except StopIteration:
            break
#             assert False, f'Expected an iterable which shouldnt have exhausted'
    assert (count == 18), (f'Wrong length for iterator Expected:{18} Got: {count}')
    my_iter = iter(poly_gen_20)
    my_iter2 = iter(poly_gen_20)
    for i in zip(my_iter, my_iter2):
        assert id(i[0]) == id(i[1]), "Polygon object should have been immutable despite separate iterators"
