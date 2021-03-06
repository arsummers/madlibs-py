Create a file called madlib.py at root of madlib_cli folder, which will contain all of the Python code that you will write relating to your Madlib game.
Create a file called test_madlib.py in root of tests folder which will be used to test your executable command line script.
Keeping in mind the concept of Single Responsibility Principle{:target="_blank"}, build a command line tool which will perform the following:
Print a welcome message to the user, explaining the Madlib process and command line interactions
Read a template Madlib file (Example{:target="_blank"}), and parse that file into usable parts.
You need to decide what components of this file are useful, and how to break those useful pieces apart
Once you know what parts of the template need user input, such as Adjective, prompt the user to submit a series of words to fit each of the required components of the Madlib template.
With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
Write the completed template (Example{:target="_blank"})to a new file on your file system (in the repo).