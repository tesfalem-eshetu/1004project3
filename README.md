Total Points: 100

You are welcome to discuss the problem with other students but the program you submit must be your own work. Please review the academic honesty policy for this course (see the syllabus). Please ask the instructor and IA for help if you get stuck. 

Upload the following two files to Courseworks:

problem1.py
problem2.py

Important: If you re-submit your assignment you need to re-upload all files, even if you change just one of them. Otherwise, any files you uploaded previously will be lost if you submit a second time.

Problem 1: Farmers Market Database (60 pts)

In this assignment, you will implement a simple database that lets the user discover farmers markets in their town or zip code. The database prompts the user for a town or zip code. It then outputs all farmers markets in the town or zip code. The database prompts the user repeatedly until they enter "quit".

Download the file markets.txt. The file contains geographic information for more than 7000 farmers markets in the U.S. (source: https://catalog.data.gov/dataset/farmers-markets-directory-and-geographic-dataLinks to an external site.). Each line contains information about one farmers market. Data fields are separated by a single "@" character. The fields are in the following order: state, market name, street address, city, zip code, longitude, latitude.

Download the skeleton file problem1.py. Save the skeleton file in the same folder as markets.txt.

(1) Create the function read_market_data(). The function takes the filename as a parameter. The file contains the market data in the format described above. The function opens the file, reads in the data, and converts each line into a tuple of five strings describing a single farmers market. Please ignore the longitude and latitude fields.

The function read_market_data() returns two objects (i.e., it returns a tuple of two objects). The first object is a dictionary mapping zip codes to lists of farmers market tuples. In other words, the keys in the dictionary are zip codes (in string format) and the values are lists of farmers market tuples.

The second object is a dictionary mapping towns to sets of zip codes. In other words, this dictionary has the strings from the "city" field for keys and sets of zip codes (in string format) for values. Think about why the values in this dictionary are sets and not lists.

(2) Create the function format_market_data(). The function takes a single farmers market tuple as a parameter and returns a human-readable string. Use string formatting to create the string. The function should return a human-readable string that looks as follows:

Columbia University Greenmarket
E. Side of Broadway between 114th & 115th Streets
New York, New York 10027
(3) Create a main program that first reads in the markets.txt file once using the function from (1), then asks the user repeatedly for a zip code or a town name in a while loop until the user types “quit”.

For each input, the program shows all farmers markets for the town or zip code using the function from (2). If the user enters a zip code, the program looks up the farmers markets in the zip code using the first dictionary returned by read_market_data(). If the user enters a town name, the program first translates the town to a set of zip codes using the second dictionary returned by read_market_data(). It then looks up all farmers markets for each zip code and prints them all.

If a town or zip code does not exist, the program prints "Not found."

Hints:  

Verify if the user input is a zip code by checking if it only consists of numbers. If so, simply print all farmers markets in that zip code. If the user typed in the name of a town, loop over all zip codes for this town name and then use a nested loop to print all farmers markets for each zip code.
The data set is messy. There are entries with missing zip codes or other information. If you find an entry with a missing zip code, town name, or other information, ignore it in the read_market_data() function.
In the dictionary that has town names for keys, make sure the keys are all lower-case, i.e., convert the town name to lower case with the .lower() string method before you use it as key. When the user enters a town name, also convert it to lower case before you look up the corresponding key. 
Submit your program in a file called problem1.py.

Problem 2: Hangman (40 pts)

In this assignment, you will implement the classic word-guessing game HangmanLinks to an external site.. The computer selects a random word that the player must guess. Instead of guessing the entire word at once, the player guesses individual letters. If the user guesses a letter that appears in the word, the computer reveals where in the word the guessed letter appears. If the user guesses a letter that does not appear in the word, the computer increases a variable value that keeps track of the number of incorrect guesses. If the player gets more than five guesses wrong, they loose. If the player uncovers the entire word, they win.

Write a Python program that plays Hangman:

(1) Download file dictionary.txt. Save it in the same folder as your program (problem2.py).

(2) At the start, your program reads all the words from the file and stores them in a list. Then it randomly selects one word from the list.

(3) The program prints '_' (underscore) for each letter in the word. Separate underscores with a space. For example, if the word is "college", the program prints:

_ _ _ _ _ _ _
(4) The main loop lets the player make repeated letter guesses. If the guessed letter appears in the word, the program uncovers the letter. If the letter appears multiple times, all occurrences are uncovered. For example, if the word is "college" and the user guesses "e", the output should be:

_ _ _ _ e _ e
I If the user guesses "l" in the next turn, the output should be:

_ _ l l e _ e
and so on. If the players guesses a letter that does NOT appear in the word, the program simply prints the previous output. For example, if the player guesses "k" next, the program outputs:

_ _ l l e _ e
(5) If the player guesses the entire word, the program prints a winning message and terminates. If the user makes more than five incorrect guesses, the program prints a losing message and terminates.

Hints:

Think about how can you store the letters that have already been guessed? What's the most suitable data structure from those covered in class?
How do you display the word with these letters uncovered?
Submit your program in a file called problem2.py. 
