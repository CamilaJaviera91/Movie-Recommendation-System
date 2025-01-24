# Import the connection function from the 'query_movies_rating' file
import sys
sys.path.append('./sources/queries/')
from query_movies_rating import query_movies_rating

import matplotlib.pyplot as plt

#data for the table
df = query_movies_rating()