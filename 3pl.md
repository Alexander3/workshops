1. Zaimplementuj grę w wisielca bazując na poniższym kodzie (zmień miejsca zawierające komentarze TODO).
```python
maksymalna_liczba_prob = 9
liczba_zyc = maksymalna_liczba_prob
haslo = 'pythoniczny kod'
wyswietlane_slowo = ['_'] * len(haslo)

def powitanie():
    print("Witaj w grze wisielec. Masz {} zyc.".format(liczba_zyc))

def wczytaj_litere():
    pass
    # TODO: funkcja powinna pobierać literę od użytkownika

def nie_zgadles():
    pass
    # TODO: wyświetl informację że użytkownik wpisał złą literę i odejmij jedno życie
    # hint: trzeba użyć słowa kluczowego `global`

def wyswietl_slowo():
    wiadomosc = "Slowo ktore zgadujesz: {} ({} znakow)"
    slowo = ''.join(wyswietlane_slowo)
    print(wiadomosc.format(slowo, len(wyswietlane_slowo)))

def odkryj_litere(litera):
    pass
    # TODO: odkryj wszystkie wystąpienia `litera` z `haslo` w `wyswietlane_slowo`
    # hint: `enumerate` może się przydać

def gra():
    odkryj_litere(' ')
    powitanie()

    while liczba_zyc > 0 and ''.join(wyswietlane_slowo) != haslo:
        wyswietl_slowo()
        litera = wczytaj_litere()

        if litera in haslo:
            odkryj_litere(litera)
        else:
            nie_zgadles()

    # skoro liczba_zyc != 0, to znaczy ze gracz wygral
    if liczba_zyc:
        print("Wygrales! Slowo to: {}".format(haslo))
        print("Udalo ci sie tego dokonac w {} probach!".format(maksymalna_liczba_prob - liczba_zyc))
    else:
        print("Przegrales! Szukane slowo to: {}".format(haslo))

gra()
```
+ napraw bug podający złą ilość prób (tak naprawdę gracz stracił 2 życia, a nie dokonał 2 próby)
+ rozszerz grę tak, żeby wielkość liter podanych przez użytkownika nie miała znaczenia (hint: metoda lower() na stringu)
+ dodaj walidację wejścia - jeśli użytkownik poda więcej niż jeden znak, wypisz komunikat o błędzie i poproś jeszcze raz o podanie litery (hint: funkcja wbudowana len(...))
+ rozszerz grę tak, żeby pokazać inny komunikat, jeśli gracz poda tę samą literę kolejny raz

2. Gra w kółko i krzyżyk. (zmień miejsca zawierające komentarze TODO).
```python
import random

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
player = random.choice(['X', 'O'])

def print_board():
    print('  0 1 2')
    for i, row in enumerate(board):
        print(str(i) + ' ' + '|'.join(row))
        if i < 2:
            print('  ' + '-' * 5)

def make_move():
    # TODO: wczytaj pozycję xy od użytkownika
    # hint: board[y][x] - tak można dostać się do odpowiedniej komórki 
    pass

def game_over():
    # TODO: Sprawdź czy gracz wygrał ostatnim ruchem
    # Użyj return True lub False
    # Wypisz informację czy był remis czy wygrana
    # Jest 8 możliwości na wygraną,
    # sprawdzanie pionowych i poziomych można zrobić pętlą 
    return False

while not game_over():
    # TODO: zmień gracza na przeciwnego
    print_board()
    make_move()
print('#' * 7)
print_board()
print('#' * 7)
```

+ Jeśli gracz zrobi zły ruch (pole jest już zajęte) wyświetl komunikat i pozwól mu spróbować jeszcze raz

