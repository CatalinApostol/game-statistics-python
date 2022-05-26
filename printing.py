from reports import *
import sys


def print_questions():
    g=input('Hello. What is the folder you would like to access? ')
    while True:
        f=input('''
          
          
          
        What would you like to know?
        1. How many games are in the file?
        2. Is there a game from a given year?
        3. Which is the latest game?
        4. How many games are in the file by genre?
        5. What is the line number of a given title?
        6. Can you give me the alphabetically ordered list of the titles?
        7. Which genres occur in the data files?
        8. What is the release year of the top sold first-person shooter game?
        
        
        ''')
        if f== '1':
            print(count_games(g))
        elif f== '2':
            year=input ('What is the year you\'re looking for?')
            print(decide(g, year))
        elif f=='3':
            print(get_latest(g))
        elif f=='4':
            genre=input('What is the genre you\'re looking for?')
            print(count_by_genre(g, genre))
        elif f=='5':
            title=input('What is the title you\'re looking for?')
            print(get_line_number_by_title(g, title))
        elif f=='6':
            print(sort_abc(g))
        elif f=='7':
            print(get_genres(g))
        elif f=='8':
            print(when_was_top_sold_fps(g))
        elif f=='quit':
            sys.exit[0]
            
print_questions()
    
