# Käyttöohje

## Asennus ja käynnistys

Kloonaa repositorio omalle koneellesi, siirry projektin juurihakemistoon, ja lataa projektin riippuvuudet:

```bash
poetry install
```

Käynnistä sovellus komennolla

```bash
poetry run invoke start
```

## Sovelluksen käyttö

Kun käynnistät projektin, tyhjä pelilauta aukeaa tkinter-ikkunaan ja konsoliin printataan ilmoitus 'Start the game'. Peli ottaa syötteinä käyttäjän klikkaukset pelilaudalla. Kun olet klikannut vuorollasi, vaihtuu tekoälyn vuoro, josta ilmoitetaan konsolissa 'AI calculating...'. Tekoälyn laskettua konsoliin ilmoitetaan mihin syvyyteen asti tekoäly laski ja kuinka kauan siinä meni. Sitten ilmoitetaan olevan taas pelaajan vuoro 'Make your move'. Näin peli pyörii kunnes jompi kumpi voittaa. Tällöin pelilaudalle sekä konsoliin ilmoitetaan voitosta 'AI WINS'/'YOU WIN'. Tasapelitilanteessa ilmoitetaan myös pelilaudalle ja konsoliin 'No more moves!'.

## Testien ajo

Voit suorittaa testit komennolla

```bash
poetry run invoke test
```

ja saat testikattavuusraportin komennolla

```bash
poetry run invoke coverage
```
