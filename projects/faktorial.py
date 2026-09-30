import math


def faktorial_cyklus(n):
    skontroluj(n)
    vysledok = 1
    for i in range(2, n + 1):
        vysledok *= i
    return vysledok


def faktorial_rekurzia(n):
    """Rekurzívna verzia"""
    skontroluj(n)
    if n <= 1:
        return 1
    return n * faktorial_rekurzia(n - 1)


def skontroluj(n):
    if not isinstance(n, int):
        raise TypeError("Faktoriál je definovaný pre celé čísla.")
    if n < 0:
        raise ValueError("Faktoriál záporného čísla neexistuje.")


def main():
    print("Faktoriál")
    print("Pre ukončenie napíš 'q'.\n")

    while True:
        text = input("Zadaj celé číslo: ").strip()
        if text.lower() == "q":
            print("Maj sa!")
            break

        try:
            n = int(text)
        except ValueError:
            print("Chyba: zadaj celé číslo.\n")
            continue

        try:
            a = faktorial_cyklus(n)
            # Rekurzia má v Pythone limit hĺbky (~1000), pri veľkých n ju preskočíme
            if n <= 900:
                b = faktorial_rekurzia(n)
                assert a == b == math.factorial(n)
            print(f"{n}! = {a}\n")
        except ValueError as chyba:
            print(f"Chyba: {chyba}\n")


if __name__ == "__main__":
    main()