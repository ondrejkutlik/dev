<a href="https://ondrejkutlik.github.io/kodev/">
  <img src="banner.svg" alt="Moje projekty" width="100%">
</a>

<p align="center"><a href="https://ondrejkutlik.github.io/kodev/">▶ Otvoriť interaktívnu verziu (bodky reagujú na myš)</a></p>


Zbierka malých programov v **Pythone** a **čistom HTML/CSS/JavaScripte**. Webové projekty nepotrebujú žiadne knižnice ani inštaláciu – stačí otvoriť súbor v prehliadači.

## 🐍 Python

| Súbor | Popis |
|-------|-------|
| [`faktorial.py`](python/faktorial.py) | Výpočet faktoriálu cyklom aj rekurziou, s kontrolou vstupu a porovnaním s `math.factorial`. |
| [`generator_hesiel.py`](python/generator_hesiel.py) | Generátor bezpečných hesiel cez modul `secrets`. Voliteľná dĺžka (4–128) a typy znakov. |
| [`kalkulacka.py`](python/kalkulacka.py) | Konzolová kalkulačka (`+ - * / ** %`) s desatinnou čiarkou a pokračovaním od posledného výsledku. |

### Spustenie

Vyžaduje Python pre spustenie.

```bash
python python/faktorial.py
python python/generator_hesiel.py
python python/kalkulacka.py
```

## 🌐 Web (HTML + CSS + JavaScript)

| Súbor | Popis |
|-------|-------|
| [`generator-hesiel.html`](web/generator-hesiel.html) | Generátor hesiel s posuvníkom dĺžky, odhadom sily a kopírovaním do schránky. Používa `crypto.getRandomValues`. |
| [`kalkulacka.html`](web/kalkulacka.html) | Kalkulačka bez `eval()`, ovládateľná myšou aj klávesnicou. |
| [`piskvorky3x3.html`](web/piskvorky3x3.html) | Klasické piškvorky 3×3 – dvaja hráči alebo proti počítaču, so skóre. |
| [`piskvorky5x5.html`](web/piskvorky5x5.html) | Piškvorky 15×15, 5 v rade – proti počítaču alebo dvaja hráči, vrátenie ťahu, skóre. |

### Spustenie

Stačí dvojklikom otvoriť súbor v prehliadači, alebo z terminálu:

```bash
open web/kalkulacka.html        # macOS
xdg-open web/kalkulacka.html    # Linux
start web\kalkulacka.html       # Windows
```