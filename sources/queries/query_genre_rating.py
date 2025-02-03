# Import the connection function from the 'connection' file
import sys
sys.path.append('./sources/connection/')

from connection import connection

# Import necessary libraries
import psycopg2
import locale
import pandas as pd

def query_genre_rating():
    """
    Queries the movie recommendation database to retrieve genre-based statistics,
    including the number of movies, number of users, and average rating per genre.
    """
    # Set the locale to Spanish (Spain) to ensure proper formatting
    try:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    except locale.Error:
        print("Error: Could not establish the regional settings.")
    
    # Establish a connection using the connection function from 'connection.py'
    con = connection()
    if con is None:
        print("Error: Could not establish a connection to the database.")
        return

    try:
        cursor = con.cursor()  # Create a cursor to interact with the database

        # Execute the SQL query to retrieve the genre-based statistics
        cursor.execute('''
                        SELECT 
                            genre,
                            movies,
                            users, 
                            rating
                        FROM 
                        (SELECT 
                            m.genre AS genre,
                            COUNT(DISTINCT m.title) AS movies,  -- Count distinct movie titles per genre
                            COUNT(DISTINCT u.user_id) AS users, -- Count distinct users who rated movies
                            ROUND(AVG(r.rating), 1) AS rating  -- Calculate the average rating rounded to 1 decimal
                        FROM postgres.movie_recommendation.movies m 
                        JOIN postgres.movie_recommendation.ratings r ON r.movie_id = m.movie_id 
                        JOIN postgres.movie_recommendation.users u ON u.user_id = r.user_id 
                        GROUP BY m.genre)
                        WHERE users > 10  -- Filter out genres with less than 10 users
                        ORDER BY rating DESC;  -- Sort genres by average rating in descending order
        ''')

        records = cursor.fetchall()  # Fetch all the results from the query

        # Convert results into a DataFrame for better visualization and manipulation.
        columns = [desc[0] for desc in cursor.description]  # Extract column names from query result
        df = pd.DataFrame(records, columns=columns)  # Create DataFrame

        return df  # Return DataFrame

    except psycopg2.Error as e:
        print(f"Error executing the query: {e}")  # Handle query execution errors
        return None

    finally:
        # Close cursor and connection safely to avoid resource leaks
        cursor.close()
        con.close()
        print("Connection closed successfully.")