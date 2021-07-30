# Iterables and Iterators (Part 1)

In Python, iterables are objects that allow retrieval of its members one element at a time. Upon passing an iterable to built-in `iter()` method in Python, the iterable object returns an iterator. The most important property of an iterable is that it should not get exhausted upon completing iteration.

Iterators on the other hand are objects that represent a batch or group of elements. These elements can be iterated over by calling `__next__()` method.  Iterators will exhaust upon completing iteration over the elements and must raise __StopIteration__ error upon exhausting all the elements.

To prevent exhaustion of __iterables__, it is necessary that such containers/objects must return a new iterator when iterables are passed to an *iter()* function.

```
Sample:
list_s = [0,2.9, 30]
l_iter = iter(list_s)
while True:
    try:
        print(next(l_iter))
    except StopIteration:
        break
```

**[Colab Link](https://colab.research.google.com/drive/1W8XivyHSMq1OxkOncD6qPXHzwNVvxtZK?usp=sharing)**

## TASKS

### Implement a Custom Polygon sequence type

1. Implement a Custom Polygon sequence type:
   1. where initializer takes in:
      1. number of vertices for largest polygon in the sequence
      2. common circumradius for all polygons
   2. that can provide these properties:
      1. max efficiency polygon: returns the Polygon with the highest **area to perimeter** ratio
   3. that has these functionalities:
      1. functions as a sequence type (`__getitem__`)
      2. supports the len() function (`__len__`)
      3. has a proper representation (`__repr__`)
      4. Is also an iterable and implements an iterator.

### Solution

```
class PolygonSequences():
    '''
    Polygons Iterable class that generates all polygons for a given circumradius and upto the max edges specified by n_sides.
    E.g: If input radius = 4 and n_sides = 10, polygons starting from sides = 3,4,...10 of size 4 will be generated
    Returns Iterable of ConvexPolygon class.
    '''
```

This is the primary class  whose `__init__` function takes two arguments the number of edges and the circumradius. Here number of edges will be used to generate a sequence of all the *ConvexPolygon* objects between 3 and number of max edges. Each object will have ofcourse use the same circumradius. To support indexing and slicing, `__getitem__` method is explicitly implemented. 

```
    def __getitem__(self, s):
        '''
        Allows for proper iteration of the sequence.
        '''
     
```

Another important function that is implemented is the `get_max_efficiency_poly`. This function returns the polygon with the maximum ratio of area to perimeter amongst all the polygons in the sequence.

```
    def get_max_efficiency_poly(self):
        '''
        Returns the max efficient polygon. We can make a simple hack to use the one with largest number of edges.
        '''
```

We make the class PolygonSequences **iterable** by implementing an *iterator* within the PolygonSequences class and by implementing an `__iter__()` method that returns a new iterator.

    class PolygonSqIterator:
        '''
        The iterator class over Polygon sequence that converts it into an iterable.
        Implements __next__ and __iter__ functions.
        '''
        def __init__(self, polygon_sq_obj):
        #print("Calling PolygonSqIterator __init__")
            self.polygon_sq_obj = polygon_sq_obj
            self._index = 0

```class PolygonSqIterator:
    '''
    The iterator class over Polygon sequence that converts it into an iterable.
    Implements __next__ and __iter__ functions.
    '''
    def __iter__(self):
    	'''
        Iterator function that returns a new iterator on every call
        '''
        return self.PolygonSqIterator(self) 
```

## User Details:

Submitted by: Rajesh Y(github: rajy4683)
Email ID: st.hazard@gmail.com
