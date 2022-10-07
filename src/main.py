from datetime import date
import holidays

def main():
    # Select country
    uk_holidays = holidays.UnitedKingdom()
    # Print all the holidays in UnitedKingdom in year 2018
    # Print all the holidays in UnitedKingdom in year 2018
for ptr in holidays.UnitedStates(years = 2022).items():
	print(ptr)

for ptr in holidays.UnitedStates(years = 2023).items():
	print(ptr)


if __name__ == "main":
    main()