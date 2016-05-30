from datetime import date


def years(age):
    remaining_years = 100 - age
    future_date = date.today().year + remaining_years
    return future_date


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    number = int(input("Please enter a number: "))
    hundred_years = years(age)
    for i in range(0, number):
        print("Hi {0} you will be 100 years old in {1}".format(name, hundred_years))
    # return


if __name__ == '__main__':
    main()
