# Movie Reports

This is a small Python program for my assignment. It reads a movies CSV file
and prints different reports from it. The data is old movies from 1892 to
1915, taken from this Google Sheet:

https://docs.google.com/spreadsheets/d/1SvoN2m96SkFDE7zALEsHnnELrZmzn1cDVqEXMgq-qoM/edit#gid=610360206

## How to run it

First download the sheet as a CSV file. Then set the file path in an
environment variable. On Windows PowerShell:

    $env:MOVIES_CSV_PATH = "C:\path\to\movies.csv"

Then run the program from the same folder:

    python movies_parser.py -r 1903
    python movies_parser.py -g Comedy
    python movies_parser.py -y 1892

You can also ask for more than one report in one command:

    python movies_parser.py -r 1903 -g Comedy -y 1895

## Reports

-r year

    Shows the highest rated movie of that year, the lowest rated movie,
    and the average runtime in minutes.

-g genre

    Shows how many movies are in that genre and their average rating.

-y year

    Shows the top 10 movies of that year by votes, with a circle chart.
    One circle stands for a fixed number of votes, and the top movie
    never gets more than 80 circles.

If a year or genre has no movies, the program just prints a message
instead of crashing. If you type a wrong year, like a word instead of
a number, it shows an error and stops.

## Files

models.py - the data structures for a movie and for the results
parser.py - reads the CSV file and makes Movie objects
reports.py - calculates the reports and prints them
movies_parser.py - the main program, reads the commands and runs everything
sample_movies.csv - a small file with a few movies, just for quick testing

## Requirements

Python 3.10 or newer. No other libraries are needed, only the ones that
come with Python.
