def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"

    is_leap_year = False

    if year <= 1917:
        is_leap_year = year % 4 == 0

    else:
        is_leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    return f"12.09.{year}" if is_leap_year else f"13.09.{year}"

print(dayOfProgrammer(2016))
print(dayOfProgrammer(2017))
print(dayOfProgrammer(2018))

