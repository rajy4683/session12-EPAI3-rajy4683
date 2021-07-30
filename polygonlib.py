import math
import numbers
import decimal

def check_numerical_similarity(lhs, rhs, upper=0.001, lower=0.001):
    '''
    Checks if two floats are numerically similar within a given bound
    '''
    return math.isclose(lhs, rhs, rel_tol=upper, abs_tol=lower)
class ConvexPolygon():
    ''' 
    A regular strictly convex polygon is a polygon that has the following characteristics:
        all interior angles are less than 180
        all sides have equal length
    '''
    def check_number_type(self, x):
        if isinstance(x, bool):
            return False
        if isinstance(x, complex):
            return False
        return isinstance(x, numbers.Number)
    
    def __init__(self, n_sides, circumradius):
        ''' 
        n_sides and circumradius are expected to be numbers
        ''' 
        if (self.check_number_type(n_sides) == False or
            self.check_number_type(circumradius) == False):
            raise TypeError
                
        if n_sides < 3:
            raise ValueError
        self._n_sides = n_sides
        self._circumradius = circumradius
    @property
    def get_vertices(self):
        '''
        Property: number of vertices of the polygon
        '''
        return self._n_sides    
    @property
    def get_edges(self):
        '''
        Property: number of edges of the polygon
        '''
        return self._n_sides    
    @property
    def get_circumradius(self):
        '''
        Property: circumradius of the polygon
        '''
        return self._circumradius    
    @property
    def get_interior_angle(self):
        '''
        Property: number of interior angles of the polygon
        '''
        return (self._n_sides - 2) * 180 / self._n_sides
    @property
    def get_length_of_side(self):
        '''
        Property: length of one side of the polygon
        '''
        return 2 * self._circumradius * math.sin(math.pi / self._n_sides)
    @property
    def get_apothem(self):
        ''''
        Property: Length of apothem of the polygon
        '''
        return self._circumradius * math.cos(math.pi / self._n_sides)
    @property
    def get_area(self):
        ''''
        Property: Area of the polygon
        '''        
        return self._n_sides / 2 * self.get_length_of_side * self.get_apothem
    @property
    def get_perimeter(self):
        '''
        Property: Perimeter of the polygon
        '''
        return self._n_sides * self.get_length_of_side
    def return_polybase(self):
        '''
        Returns the circumradius and number of sides of the polygon
        '''
        return self._n_sides, self._circumradius
    def __str__(self):
        '''
        String representation of ConvexPolygon object
        '''
        return f'ConvexPolygon Object: Edges:{self._n_sides} Radius:{self._circumradius}'
    def __repr__(self):
        '''
        String describing the ConvexPolygon object
        '''
        return f'Instance of ConvexPolygon class. Edges:{self._n_sides} Radius:{self._circumradius}'
    def __eq__(self, rhs_poly):
        '''
        Implementation of equality function for ConvexPolygon class.
        Returns True when both circumradius and the number of sides both match.
        '''
        if (rhs_poly is None) or not (isinstance(rhs_poly, ConvexPolygon)):                
            raise TypeError(f"unsupported operand type(s) for __eq__: 'ConvexPolygon' and '{type(rhs_poly).__name__}'")
        return (self._n_sides, self._circumradius) == rhs_poly.return_polybase()
    def __gt__(self, rhs_poly):
        '''
        Implementation of greater than function for ConvexPolygon class.
        Returns True when LHS has greater number of vertices/sides than RHS.
        '''
        if (rhs_poly is None) or (not isinstance(rhs_poly, ConvexPolygon)):               
            raise TypeError(f"unsupported operand type(s) for __gt__: 'ConvexPolygon' and '{type(rhs_poly).__name__}'")
        return self._n_sides  > rhs_poly.return_polybase()[0]
