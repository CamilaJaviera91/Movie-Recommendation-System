# Import the connection function from the 'connection' file
import sys
sys.path.append('./sources/connection/')

from connection import connection

# Import necessary libraries
import psycopg2
import locale
import pandas as pd

def query_movies_rating():
    """
    Queries the movie recommendation database to retrieve movie-specific statistics,
    including title, release year, genre, duration, number of users, and average rating.
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

        # Execute the SQL query to retrieve movie-specific statistics
        cursor.execute('''
                        select
                            m.title as movies,
                            m.release_year as release,
                            m.genre as genre,
                            sum(case when r.rating  > 3 then 1 else 0 end) as positive_reviews,
                            sum(case when r.rating <= 3 then 1 else 0 end) as negative_reviews,
                            count(r.rating_id) as total_reviews
                        from postgres.movie_recommendation.movies m
                        left join postgres.movie_recommendation.ratings r on r.movie_id = m.movie_id
                        group by 
                            m.title, 
                            m.release_year, 
                            m.genre
                        order by 
                            count(r.rating_id) desc;

        ''')

        records = cursor.fetchall()  # Fetch all query results

        # Convert results into a DataFrame for better visualization and analysis
        columns = [desc[0] for desc in cursor.description]  # Extract column names from query result
        df = pd.DataFrame(records, columns=columns)  # Create DataFrame

        print(df)  # Print DataFrame to console

        return df  # Return DataFrame for further use

    except psycopg2.Error as e:
        print(f"Error executing the query: {e}")  # Handle query execution errors
        return None

    finally:
        # Close cursor and connection safely to prevent resource leaks
        cursor.close()
        con.close()
        print("Connection closed successfully.")