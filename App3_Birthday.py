import datetime

def print_header():
    print('---------------------------')
    print('      BIRTHDAY APP')
    print('---------------------------')
    print()


def get_birthday_from_user():
    print("Tell us when you were born: ")
    year = input('Year [yyyy]: ')
    month = input('Month [MM]: ')
    Day = input('DAy [DD]: ')
    Day = input('DAy [DD]: ')

    Birthday = datetime.datetime(year, month, Day)
    return Birthday

def compute_days_between_dates():
    pass

def print_birthday_information():
    pass

def main():
    print_header()
    bday = get_birthday_from_user()
    now = None
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)

main()

