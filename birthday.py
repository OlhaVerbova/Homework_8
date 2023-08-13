from datetime import datetime, timedelta
users = [
    {'Olha':datetime(1992, 3, 10)},
    {'Anna': datetime(1993, 8, 13)},
    {'Joy': datetime(1989, 8, 14)},
    {'Kern': datetime(2000, 8, 17)},
    {'Lui': datetime(1999, 8, 15)},
    {'Sofi': datetime(1998, 8, 15)},
    {'Dory': datetime(1985, 9, 1)},
    {'Sam': datetime(1987, 10, 16)},
    {'Bill': datetime(1994, 12, 1)}
]
def get_birthdays_per_week(users:dict):
    actual_year:int = datetime.now().year
    now_day = datetime.now().date()
    seven_days =  timedelta(days = 7)
    last_week_day = now_day + seven_days

    birthday_dict = dict()
    for values in users:
        for keys, value in values.items():
            convert_str_to_date = value.date()
            value = convert_str_to_date.replace(year=actual_year) # Changing the year of birth to the current year
            
            #Select only those birthdays that fall within the range of the task (today + 7 days)
            if value >= now_day and value <= last_week_day:
                if value.weekday() == 5: # If the day of the week is Saturday, add 2 days
                    two_days = timedelta(days=2)
                    value += two_days 
                elif value.weekday() == 6: # If the day of the week is Sunday - add 1 day
                    one_day = timedelta(days=1)
                    value += one_day
                birthday_dict.update({keys:value})

    result_list = {}
    for keys, value in birthday_dict.items():
        if value not in result_list:
            result_list[value] = []
        result_list[value].append(keys)
    sorted_result_list = sorted(result_list.items())
    

    for keys, values in sorted_result_list:        
        result_date = datetime.strftime(keys, '%A')
        print(f'{result_date}: {", ".join(values)}')
        

def main():
    get_birthdays_per_week(users)

if __name__ == "__main__":
    main()