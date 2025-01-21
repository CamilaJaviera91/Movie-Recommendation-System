from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Set the number of entries to generate
num_entries = 200

# Generate unique data in advance
userid = random.sample(range(1000, 9999), num_entries)  # Pre-generate unique IDs
name = [fake.name_nonbinary().capitalize() for _ in range(num_entries)]
email = [fake.email().lower() for _ in range(num_entries)]
password = [fake.password() for _ in range(num_entries)]
joindate = [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_entries)]

# Combine the data into products
users = [
    (userid[i], name[i], email[i], password[i], joindate[i])
    for i in range(num_entries)
]

# Print the data in SQL format
print("INSERT INTO movie_recommendation.users (user_id, username, email, password, join_date) VALUES")
values = ",\n".join(
    [f"    ({u[0]}, '{u[1]}', '{u[2]}', '{u[3]}', '{u[4]}')" for u in users]
)
print(values + ";")