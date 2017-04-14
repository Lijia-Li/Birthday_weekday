

### define sevral function that can be used in this main function
# leap year function
# define the function to test if y is leap year.
def is_leap_year(y):
    if y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    else:
        return True

# define the function Gregorian date:
# if before the date september, 14, 1752 then it is not a gregorian date.
def is_gregorian_date(y, m, d):
    if 0 <= y < 1752:
        return False
    elif y == 1752 and 0 <= m < 9:
        return False
    elif y == 1752 and m == 9 and 0 <= d < 14:
        return False
    else:
        return True

# define valid date function
def is_valid_date(y, m, d):
    months_thirtyone_day = [1, 3, 5, 7, 8, 10, 12]
    months_thirty_day = [4, 6, 9, 11]
    # prerequisite: if it is a geogian date and year bigger than 0 and month within 1-12
    if is_gregorian_date(y, m, d) and 0 < y and 1 <= m <= 12:
        if m in months_thirtyone_day and 1 <= d <= 31:          # if 31 days/ month
            return True
        elif m in months_thirty_day and 1 <= d <= 30:           # if 30 day/ month
            return True
        elif m == 2:
            if is_leap_year(y) and 1 <= d <= 29:                # if leap-year for feb, 29 days
                return True
            elif not is_leap_year(y) and 1 <= d <= 28:          # if not leap-year feb, 28 days
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# define the function of weekday:
import math
def weekday_of(y, m, d):
    year_last_two_digit = int(str(y)[2:4])

    if 3 <= m <= 12:
        zm = m
        c = int(str(y)[0:2])
        zy = year_last_two_digit
        mod = (d + math.floor((13 * (zm + 1)) / 5) + zy + math.floor(zy / 4) + math.floor(c / 4) + (5 * c)) % 7
        return mod

    elif 1 <= m <= 2:
        zm = m + 12
        if year_last_two_digit == 0:                 # if year = 0, zy to 99, century - 1
            c = int(str(y)[0:2]) - 1
            zy = 99
        elif year_last_two_digit != 0:               # if year != 0, zy - 1, century constant
            c = int(str(y)[0:2])
            zy = year_last_two_digit - 1
        mod = (d + math.floor((13 * (zm + 1)) / 5) + zy + math.floor(zy / 4) + math.floor(c / 4) + (5 * c)) % 7
        return mod
    # print out variables
    # print(zy, zm)
    # print(year_last_two_digit, y, m, d)



# define function of weekday name
def weekday_name(mod):
    if mod == 0:
        return "Saturday"
    elif mod == 1:
        return "Sunday"
    elif mod == 2:
        return "Monday"
    elif mod == 3:
        return "Tuesday"
    elif mod == 4:
        return "Wednesday"
    elif mod == 5:
        return "Thursday"
    elif mod == 6:
        return "Friday"
    else:
        return False



# running the program
def main():
    birthday = input("Enter your birthday in YYYY-MM-DD format:")
    # store the birthday into year, month, and day and convert them into a integer
    y = int(birthday[0:4])
    m = int(birthday[5:7])
    d = int(birthday[8:])
    weekname = weekday_name(weekday_of(y, m, d))

    if not is_valid_date(y, m, d):
        print("The date you entered is invalid.")
    else:
        print("You were born on a " + weekname + "!")


if __name__ == "__main__": main()