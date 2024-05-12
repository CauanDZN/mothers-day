import datetime
import locale

def wish_happy_mothers_day():
    locale.setlocale(locale.LC_TIME, '')

    today = datetime.date.today()
    
    if today.month == 5 and today.weekday() == 6 and 8 <= today.day <= 14:
        language = locale.getlocale()[0]
        if language.startswith('pt'):
            print("Feliz Dia das Mães!")
        elif language.startswith('es'):
            print("¡Feliz Día de la Madre!")
        else:
            print("Happy Mother's Day!")
    else:
        print("Today is not Mother's Day.")

wish_happy_mothers_day()
