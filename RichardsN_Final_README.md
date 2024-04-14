# Dalhousie Reference Checker
Reference Checker (RC) is a web application that helps Dalhousie Undergraduate and Graduate students improve their references. It is designed to help students correct common reference errors with feedback provided by the GenAI application ChatGPT 3.5 Turbo. RC can offer feedback based on three common reference styles: APA, MLA, and Chicago. Students must select one of these three styles from a dropdown menu prior to inputting their references. The feedback provided could include the highlighting of missing DOIs or URLs, as well as incorrect punctuation. 

## Table of Contents
File Structure
Configuring an Open API Key
How to run RC
File Types
    pycache files
    app.py
    database.db
    db_test.py
    init_db.py
    LICENSE
    requirements.txt
    schema.sql
    static files
        main.css
        DAL_icon.png
        DAL_logo.png
    index.html

## File Structure
Reference_Checker (folder)
    app.py
    database.db
    db_test.py
    init_db.py
    LICENSE
    README.md
    requirements.txt
    schema.sql
    static (folder)
        main.css
        DAL_icon.png
        DAL_logo.png
    templates (folder)
        index.html
    _pycache_ (folder)
        app.cpython-39.pyc
        app.cpython-312.pyc

## Configuring an OpenAI API Key
OpenAI is the organization that created ChatGPT. RC uses ChatGPT 3.5 Turbo to assess the student input references. To allow for this, you must configure an API Key. API stands for Application Programming Interface, and using an API Key from OpenAI authenticates your computer and allows it to access OpenAI applications. To configure the API key, you will need to either work in Terminal (Mac) or Command Prompt (Windows). 

    To begin you will need to install python and download the OpenAI library by entering "pip install --upgrade openai" or maybe "pip3 install --upgrade openai" into either the Terminal or Command Prompt.

    For further details on setting up an API key, see here: https://platform.openai.com/docs/quickstart?context=python

    It is recommended that you set up your API key for all projects, rather than just for a single project. Doing this means that your computer will remember the API key and you won't have to set up it up again. 

    Make sure to verify that the API key is set up correctly using either "echo $OPENAI_API_KEY" (for Mac) or "echo %OPENAI_API_KEY%" (for Windows).

## How to Run RC
The first step to running RC is to install the python library Flask using the command "pip install flask" or "pip3 install flask" in either Terminal or Command Prompt. 

To initiate the database run "python init_db.py" or "python3 init_db.py".

To run RC as a Flask applicatiton, use this command "python -m flask --app app run" (for Windows) or "python3 -m flask --app app run" (for Mac). The second "app" refers to the name of the python file app.py. This should produce a url "http://127.0.0.1:5000" which can be used to navigate to the RC web page. This launches the web server on your personal computer. 

## File types

### pycache files
These files are specific to each individual computer, not to RC and have no real bearing on how it works. 

### app.py
This file connects to ChatGPT 3.5 Turbo through an API request. This code tells ChatGPT what information it can expect to receive and respond to, which in this case is the selection of reference style as well as the input references. It also provides ChatGPT with the prompt to which it responds. In this case, the prompt indicates that ChatGPT will be recieving references from Dalhousie students. It provides ChatGPT with the three different styles of references that it could receive and provides it with a few examples of common errors to watch out for. This code also tells ChatGPT how it will respond, i.e. on the html website itself. App.py connects to the index.html through Flask. 

It also connects to the SQL database and provides instructions about information to put into that database.

### database.db
This file contains the information in the database that is initialized by init_db.py and structured by schema.sql

### db_test.py
This code can be executed in either Terminal or Command Prompt to test the database created by init_db.py and structured by schema.sql. This would allow you to check the contents of the database. 

### init_db.py
The code in this file will initialize an SQL database, the structure of which will be determined by the schema.sql file. It connects to both schema.sql as well as SQLite which is a simple database library. 

### LICENSE
This file contains the licensing and copyright information for RC. RC is licensed under an MIT License. See license for further details. 

### requirements.txt
This text file contains all of the requirements needed for your computer's python environment. This details the packages of code plus the versions of each required package necessary to run the python code. 

### schema.sql 
This is an SQL file that contains the code which specifies the structure of the database initiation by the init_db.py file. This code is why two tables will be created once information has been input into the html webpage. The first table contains an primary ID key (student ID key), a timestamp, the student's name and email. The second table contains a different primary ID key, plus that of the first table in addition to a timestamp, the chosen reference style, the inputted references, and the feedback provided by the Reference Checker. These two databases are connected through the student ID key, and create a database. 

### static files
These files influence the aesthetics of the HTML webpage portion of RC.

#### main.css
This file supplements an HTML document (in this case a webpage) with visual content and aesthetic information. It contents information about the font colour, style, as well as if the text is bolded or italicized. This file also contains information regarding photo dimensions. 

#### DAL_icon.png
This file provides a static image of the Dalhousie Unviersity icon.

#### DAL_logo.png
This file provides a static image of the Dalhousie Unviersity logo.

### index.html
This file is the main structural element for the webpage. It contains all of the text that is displayed on the webpage and is responsible for the text input boxes and buttons. It is made up of tags that are interpreted by a web browser. 

