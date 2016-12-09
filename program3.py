import datetime

def print_header():
    print('**********************************************')
    print('             Birthday APP                      ')
    print('**********************************************')
    print('')


def get_birthday_from_user():
    name1 = input('Whats your Name: ')
    print('Tell us when you are Born')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))
    birthday = datetime.datetime(year, month, day)
    return birthday
    name= name1();
    return name

def compute_days_between_dates(origninal_date , now):
    date1 = now
    date2 = datetime.datetime(now.year, origninal_date.month, origninal_date.day)
    dt = date1 - date2
    dt.total_seconds()
    days = int(dt.total_seconds () /60 /60 /24)
    return days

# def print_birthday_information(days):
#         if days < 0:
#             print('Your birthday is in {} days!'.format(-days))
#         elif days > 0:
#             print('You had your birthday already this year! {} days ago'.format(days))
#         else:
#             print('Happy birthday!!!')

def print_birthday_information(days):
   if days < 0:
        print('Birthday is in {1} days {2} '.format(-days, name))
   elif days > 0:
        print(' Birthday is in {} days'.format(days))
   else:
       print(' Happy  Birthday !!! ')


def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)

main()

