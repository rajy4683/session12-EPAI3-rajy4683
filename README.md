# Iterables and Iterators (Part 2)

Lazy iterables is an important concept that allow objects to be created only when the need arises i.e only when requested for the next object in the collection. This mechanism i.e lazy evaluation prevents pre-allocation of  memory, thereby saving memory and CPU time unless the need arises for using them explicitly. Generators are the simplest example of lazy iteration. 

```
Sample:
def generate_numbers(min_value, max_value):
    while min_value < max_value:
        yield min_value
        min_value += 1

numbers = generate_numbers(10, 20)
print(type(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers)
```

**[Colab Link](https://colab.research.google.com/drive/1W8XivyHSMq1OxkOncD6qPXHzwNVvxtZK?usp=sharing)**

## TASKS

### 1. Refactor the `ConvexPolygon` class so that all the calculated properties are lazy properties

To achieve this we convert all the class variables in to property methods that are calculated when they are called.

    @property
    def get_vertices(self):
        '''
        Property: number of vertices of the polygon
        '''
    @property
    def get_edges(self):
        '''
        Property: number of edges of the polygon
        return self._n_sides    
    @property
    def get_circumradius(self):
        '''
        Property: circumradius of the polygon
        '''
    @property
    def get_interior_angle(self):
        '''
        Property: number of interior angles of the polygon
        '''
    @property
    def get_length_of_side(self):
        '''
        Property: length of one side of the polygon
        '''
    @property
    def get_apothem(self):
        ''''
        Property: Length of apothem of the polygon
        '''
    @property
    def get_area(self):
        ''''
        Property: Area of the polygon
        '''        
    @property
    def get_perimeter(self):
        '''
        Property: Perimeter of the polygon
        '''

### 2. Refactor the `PolygonSequences` (sequence) type, into an **iterable**  and the elements in the iterator must be computed lazily

To achieve lazy evaluation, we do the following:

1. All the precomputation is removed from the `__init__` function and only the max length/count for the iterable object is stored
2. From` __getitem__` method we invoke memoized static method `_polygonator`based on the index/slice requested

```
class PolygonSequences():
    '''
    Polygons Iterable class that generates all polygons for a given circumradius and upto the max edges specified by n_sides.
    E.g: If input radius = 4 and n_sides = 10, polygons starting from sides = 3,4,...10 of size 4 will be generated
    Returns Iterable of ConvexPolygon class.
    '''
```

```
    def __getitem__(self, s):
        '''
        Allows for proper iteration of the sequence.
        '''
        if isinstance(s, int):
            if s < 0:
                s = self.__len__() + s
            if s < 0 or s >=self.__len__():
                raise IndexError(f"Invalid Index.")
            else:
                return PolygonSequences._polygonator(s+3, self.__circumradius)
#                 return self._offset_to_polysides[s]
        else:
#             print(type(s))
            start, stop, step = s.indices(self.__len__())
            return [PolygonSequences._polygonator(i+3, self.__circumradius) for i in range(start, stop, step)]     
```

We make the class PolygonSequences **iterable** by implementing an *iterator* within the PolygonSequences class and by implementing an `__iter__()` method that returns a new iterator.

    class PolygonSqIterator:
        '''
        The iterator class over Polygon sequence that converts it into an iterable.
        Implements __next__ and __iter__ functions.
        '''
        def __init__(self, n_sides, circumradius):
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

Further we modify the `get_max_efficiency_poly` function to evaluate lazily based on loop/request.

```
    def get_max_efficiency_poly(self):
        '''
        Returns the max efficient polygon. We can make a simple hack to use the one with largest number of edges.
        '''
        self_poly_iter = iter(self)
        sorted_polygons = sorted(self_poly_iter, 
                                 key=lambda x: x.get_area/x.get_perimeter,
                                reverse=True)
        return sorted_polygons[0] 
```



## User Details:

Submitted by: Rajesh Y(github: rajy4683)
Email ID: st.hazard@gmail.com
