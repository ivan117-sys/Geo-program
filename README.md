# Geo Program

#### Video Demo: https://www.youtube.com/shorts/DjbBz0IA7AU

#### Description: Geo Program is used to gain interesting knowledge about any country in the world.

### It uses country info API to get the data about countries, and than asks the user
### what he wants to know about specefic country.

### As a quizz fan I think this is great program to brush on the knowledge before going to the quizz.

### Program utilizes 5 functions wich are: getCountryName, getCountry, additionalInfo, getChoice and run program.

### getCountry name function takes an input from command line and returns country

### getCountry functions takes arguments and returns capital of a given country

### additionalInfo function is called to ask the user what else he wants to know about

### country that he choose he have 7 options and return value of this function is calling next function

### getChoice function takes in a number and country and returns what the user asked for,
### it can return country currencies, languages, size, borders, calling codes, population or the user can sipmly exit the program

### runProgram takes in country and runs program in a loop until user decides to exit the program.

### test_project file also tests almost all given functions so it ensures that programm is running correctly.

### This is how to use the program:

### Overview
### This Python program provides detailed information about countries using the countryinfo library. Users can input a country name, and the program retrieves its capital. Additionally, users can explore various details such as currency, languages spoken, size, borders, calling codes, and population.

### Usage
### Run the Program:

### Execute the program using a Python interpreter.
### Ensure the countryinfo library is installed (pip install countryinfo).
### Input Country Name:

### Enter the name of the country you want information about.
### Retrieve Capital:

### The program fetches and displays the capital of the specified country.
### Additional Information:

### Choose a number (1-7) to get more details:
### 1: Currency
### 2: Languages
### 3: Size
### 4: Borders
### 5: Calling Codes
### 6: Population
### 7: Exit program
### Explore Details:

### If a number between 1 and 6 is selected, the program retrieves and prints corresponding information.
### Continue or Exit:

### Decide whether to continue exploring more details (option 1) or exit the program (option 2).
### Note: Ensure that the countryinfo library is installed before running the program (pip install countryinfo).

### Country Information Program - Testing
### This set of pytest tests is designed to ensure the proper functionality of the functions within the country information program. The tests cover input validation, retrieval of country information, and the correct handling of choices for additional details.

### Testing getCountry
### Scenario 1: Valid Country Name

### Input: "United States"
### Expected Output: Country information is successfully retrieved.
### Scenario 2: Another Valid Country Name

### Input: "Croatia"
### Expected Output: Country information is successfully retrieved.
### Scenario 3: Yet Another Valid Country Name

### Input: "Italy"
### Expected Output: Country information is successfully retrieved.
### Scenario 4: Empty Country Name

### Input: ""
### Expected Output: Invalid input; an exception is raised.
### Testing getCountryName
### Scenario 1: Valid User Input
### Input: "United States"
### Expected Output: User input is correctly formatted ("united states").
### Testing additionalInfo
### Scenario 1: Valid User Input
### Input: "3"
### Expected Output: User input is correctly converted to an integer (3).
### Testing getChoice
### Scenario 1: Valid Choice for Currency
### Input: Choice number 1
### Expected Output: The currencies information of the mock country is retrieved.
### How to Run Tests
### Install pytest: pip install pytest
### Run the tests: pytest test_country_info.py
### Ensure that the necessary dependencies are installed, and the program is functioning as expected based on the outlined scenarios.
