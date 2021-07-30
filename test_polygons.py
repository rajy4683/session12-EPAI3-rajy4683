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
    "ConvexPolygon",
    "get_vertices",
    "get_edges",
    "get_circumradius",
    "get_length_of_side",
    "get_apothem",
    "get_area",
    "get_perimeter",
    "__eq__",
    "__gt__",
    "__getitem__",
    "get_max_efficiency_poly"   
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

# def test_readme_proper_description():
#     READMELOOKSGOOD = True
#     f = open("README.md", "r", encoding="utf-8")
#     content = f.read()
#     f.close()
#     for c in README_CONTENT_CHECK_FOR:
#         if c not in content:
#             READMELOOKSGOOD = False
#             pass
#     assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

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

def test_poly_shape_limits():
    try:
        fake_poly = ConvexPolygon(2, 10)
        assert False, ('Invalid number of sides', 'Exception should have been raised')
    except ValueError:
        pass
    
    tri_poly = ConvexPolygon(3, 10)
    assert tri_poly.get_interior_angle == 60,  (f'Actual Interior Angle: {tri_poly.get_interior_angle}, Expected: {60}')
    square_poly = ConvexPolygon(4, 10)
    assert square_poly.get_interior_angle == 90,  (f'Actual Interior Angle: {square_poly.get_interior_angle}, Expected: {90}')
    
def test_poly_properties(input_edges = 5, circumradius = 2):
    '''
    Verifies for a given class of polygons if all properties are returned as expected
    '''
    def get_poly_values(input_edges, circumradius):
        '''
        Returns expected values of all measurements for a polygon
        '''
        interior_angle = (input_edges - 2) * 180 / input_edges
        side_length = 2*circumradius*math.sin(math.pi / input_edges)
        apothem = circumradius * math.cos(math.pi / input_edges)
        area = 0.5 * input_edges  * side_length * apothem
        perimeter = side_length * input_edges
        
        return apothem, area,interior_angle, side_length, perimeter
    
    input_edges = 5
    circumradius = 2
    all_getters = ['get_apothem',
                   'get_area',
                   'get_interior_angle',
                   'get_length_of_side',
                   'get_perimeter',
                   ]
    poly = ConvexPolygon(input_edges, circumradius)
    assert str(poly) == f'ConvexPolygon Object: Edges:{input_edges} Radius:{circumradius}', f'actual: {str(poly)}'
    
#     interior_angle, side_length, apothem, area, perimeter 
    test_values= get_poly_values(input_edges, circumradius)
    for idx, i in enumerate(all_getters):
        out_val = poly.__getattribute__(i)

        print(i, type(out_val).__name__, out_val)
        if type(out_val).__name__ == "float":
            assert (check_numerical_similarity(out_val, test_values[idx])), (f'Invalid value for {i}. Expected: {test_values[idx]} Got: {out_val}')
        elif type(out_val).__name__ == "int":
            assert (out_val == test_values[idx]), (f'Invalid value for {i}. Expected: {test_values[idx]} Got: {out_val}')
        else:
            print("Bad horrible type found")

def test_decagon():
    '''
    Verifies for a given class of polygons if all properties are returned as expected
    '''
    test_poly_properties(10,20)

def test_octagon():
    '''
    Verifies for a given class of polygons if all properties are returned as expected
    '''
    test_poly_properties(8,2.22)
    
def test_dodecaagon():
    '''
    Verifies for a given class of polygons if all properties are returned as expected
    '''
    test_poly_properties(12,2.22)

def test_equality():
    
    tri = ConvexPolygon(3, 10)
    deca = ConvexPolygon(10, 10)
    poly1_22 = ConvexPolygon(22, 54)
    poly2_large = ConvexPolygon(22, 22.34)
    poly3_large = ConvexPolygon(22, 22.34)
    
    assert deca > tri
    assert deca < poly1_22 
    assert poly1_22 != poly2_large
    assert tri != poly2_large
    assert poly2_large == poly3_large
    print("All checks passed!")
