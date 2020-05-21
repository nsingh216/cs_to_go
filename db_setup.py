import sqlite3
import csv


def load_data_into_db():
    # connect to database
    conn = sqlite3.connect('charades.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS movie_chars;")
    # create a table for the movie characters
    cur.execute(""" CREATE TABLE movie_chars (code integer, 
                                              movie text, 
                                              character text);
                """
                )

    # read the csv file and convert to
    with open('characters.csv', 'r') as file:
        reader = csv.DictReader(file)  # comma is default delimiter

        # create a list for each row (3 columns of each row are stored as tuple
        to_db = [(row["code"], row["movie"], row["character"]) for row in reader]

    # insert all the rows from the csv file to the database
    cur.executemany("""INSERT INTO movie_chars (code, movie, character) 
                       VALUES (?,?,?);
                    """,
                    to_db
                    )

    # save inserts
    conn.commit()

    # close connection to database
    conn.close()


def read_data_from_db(selected_movie):
    # connect to database
    conn = sqlite3.connect('charades.db')
    cur = conn.cursor()

    # query the table
    cur.execute("SELECT character FROM movie_chars WHERE code=?",
                (selected_movie,)
               )

    # get the list of characters from the selected movie
    characters = cur.fetchall()

    # a list of tuples is returned, but we only want the first column
    char_list = [row[0] for row in characters]

    # close connection to database
    conn.close()

    return char_list


if __name__ == "__main__":
    load_data_into_db()