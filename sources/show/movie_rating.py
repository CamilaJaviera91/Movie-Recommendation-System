from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import sys
sys.path.append('./sources/queries/')
from query_movies_rating import query_movies_rating

folder = "download"

# Get the data
df = query_movies_rating()

# Check if the DataFrame is valid
if df is None or df.empty:
    raise ValueError("query_movies_rating did not return valid data.")

# Define columns and rows
columns = ['movie', 'year', 'genre', 'minutes', 'users', 'rating']
rows = df.values.tolist()

# Add headers to the rows
data = [columns] + rows

# Create the PDF file
output_pdf = "movie_ratings.pdf"
pdf = SimpleDocTemplate(folder+"/"+output_pdf, pagesize=letter)

# Create the table
table = Table(data)

# Style the table
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Grey background for header
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # White text for header
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center all text
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Header spacing
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Beige background for cells
    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Black grid lines
])

table.setStyle(style)

# Add the table to the PDF and build it
elements = [table]
pdf.build(elements)

print(f"The table has been saved in {folder}/{output_pdf}")
