while True:
    try:
        user_input = input("Podaj liczbę rzeczywistą (wpisz 'stop' aby zakończyć): ")

        if user_input.lower() == 'stop':
            break

        x = float(user_input)
        x_cubed = x ** 3

        print(f"x = {x}, x^3 = {x_cubed}")

    except ValueError:
        print("Błąd: Wprowadź liczbę rzeczywistą lub wpisz 'stop' aby zakończyć.")