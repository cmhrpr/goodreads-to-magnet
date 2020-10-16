#!/bin/env python
import os
import sqlite3
import string
# Set config variables 
GOODREADS_DB = os.environ['GOODREADS_DB']
GOODREADS_SHELF = os.environ['GOODREADS_SHELF']

# Read the SQLite DB
conn = sqlite3.connect(GOODREADS_DB)
c = conn.cursor()
to_read_shelf_id =  None
# Identify the to-read shelf ID
for row in c.execute("SELECT id FROM shelves WHERE name = \"{}\"".format(GOODREADS_SHELF)):
    to_read_shelf_id = row[0]
print(to_read_shelf_id)
 
# Get all the review IDs on this review shelf
to_read_reviews = []

for row in c.execute("select reviews_id from reviews_shelves where shelves_id = {}".format(to_read_shelf_id)):
    # book id is the second item
    to_read_reviews.append(row[0])

# Get the book IDs from each of the review IDs 
to_read_book_ids = []

for review_id in to_read_reviews:
    for row in c.execute("SELECT book_id FROM reviews WHERE id = {}".format(review_id)):
        to_read_book_ids.append(row[0])

# Get the book titles
for book_id in to_read_book_ids:
    for row in c.execute("SELECT title FROM books WHERE id = {}".format(book_id)):
        
        book_name = row[0]
        book_name = book_name.translate(str.maketrans('', '', string.punctuation))
        print(book_name)

# Output list