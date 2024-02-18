from countryinfo import CountryInfo
import requests
import sys

def main():

    # Get country
    country = getCountryName()

    # Get capital of country
    capital = getCountry(country)
    this_country = CountryInfo(country)

    print(f"Capital of {country} is {capital}\n")

    # Get Additional info
    number = additionalInfo()

    choice = getChoice(number, this_country)
    print(choice)

    # Keep the program running until the exit
    runProgram(this_country)


def getCountryName():

    name = input("\nWhat country do you want to know about? ").lower().strip()
    return name


def getCountry(name):

    try:
         country = CountryInfo(name)
         capital = country.capital()

    except requests.exceptions.RequestException as e:
         raise SystemExit(e)


    return capital


def additionalInfo():

    while True:
        number = int(input(("\nType number for additional info: \n 1: Currency \n 2: Languages \n 3: Size \n 4: Borders, \n 5: Calling Codes, \n 6: Population \n 7: Exit program \n Please enter a number: ")))

        if number > 0 and number < 8:
             break

    return number


def getChoice(number, country):

    if number == 1:
        return country.currencies()

    if number == 2:
        return country.languages()

    elif number == 3:
        return country.area()

    elif number == 4:
        return country.borders()

    elif number == 5:
        return country.calling_codes()

    elif number == 6:
        return country.population()

    elif number == 7:
        sys.exit("Thank you for using the program")


def runProgram(country):

    while True:

       try:
        go = int(input("\nDo you Want to know about Something more? Press one or two \n 1. Yes \n 2. No \n"))

        if go == 1:

            number = additionalInfo()
            choice = getChoice(number, country)
            print(choice)

        elif go == 2:
           sys.exit("\nThank you for your time")

       except ValueError:
           sys.exit("\nInput is not an number")



if __name__ == "__main__":
    main()

