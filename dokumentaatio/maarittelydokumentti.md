# Määrittelydokumentti

Projektityö Helsingin yliopiston kurssille TKT20010 Aineopintojen harjoitustyö: Algoritmit ja tekoäly, syksy 2025 tietojenkäsittelytieteen kandiohjelmassa (TKT).

Projektin ohjelmointikieli on Python ja dokumentointi suomeksi.

- pythonin lisäksi pystyn vertaisarvioimaan Javalla tehtyjä projekteja

## Aihe

Aiheeni on Connect4 pelin tekoäly. Tekoäly tutkii sen mahdolliset siirrot minimax-algoritmin avulla ja etsii parhaimman siirron. Laskentaa nopeuttamaan käytetään alfa-beta karsintaa.

Lisävaatimuksina:

- Siirtojen järjestäminen (aloitetaan siirtojen tutkiminen pelilaudan keskeltä)
- Iteratiivinen syveneminen (minimax ensin pienellä syvyydellä, sitten yhä suuremmalla, tietyllä aikarajalla)
- Tarkistetaan voittoa tutkimalla vain edellisen siirron 'koskettavat' suorat
- Mielekäs heuristiikkafunktio arvioimaan pelitilannetta

Pelilauta tulostetaan konsoliin ja peliä pelataan komentoriviltä. Syötteenä pelaaja antaa sarakkeen numeron, mihin pelaajan pelinappula tiputetaan.

## Lähteet
