from datetime import date # importuje biblioteke czasu do pozniejszej funkcji

# funckja od sprawdzania czy podany rok urodzenia jest poprawny
def correct_age(year_born):
    try:
        year_born = int(year_born)
    except ValueError as e:
        print('Your year is not an integer!!!')
        return False
    if year_born <= 0:
        print("You couldn't born this year!!!")
        return False

    return year_born

# wykorzystujac biblioteke importuje akrualny czas
todays_date = date.today()
# prosze o rok
year_born = input('Enter year you were born: ')
# wykorzystuja funkcje correct_age
year_born = correct_age(year_born)
# jesli wartosc zwrocona w funkcji corract_age = False to nie wyswietli wieku. Jesli nie zwroci False to wykona
if year_born:
    print(todays_date.year - int(year_born))