# Määrittelydokumentti

Projektityö Helsingin yliopiston kurssille TKT20010 Aineopintojen harjoitustyö: Algoritmit ja tekoäly, syksy 2025 tietojenkäsittelytieteen kandiohjelmassa (TKT).

Projektin ohjelmointikieli on Python ja dokumentointi suomeksi.

- pythonin lisäksi pystyn vertaisarvioimaan Javalla tehtyjä projekteja

## Aihe

Aiheeni on Connect4 pelin tekoäly. Tekoäly tutkii sen mahdolliset siirrot minimax-algoritmin avulla ja etsii parhaimman siirron. Projektin tavoitteena on minimax-algoritmin tehostaminen. Laskentaa nopeuttamaan käytetään alfa-beta karsintaa sekä lisävaatimuksissa lueteltuja optimointeja.

Tekoälyn vuorolla alogoritmi tutkii mahdollisia liikkeitä ja antaa niille tietyn arvon. Arvojen avulla arvioidaan, mikä on optimaalisin liike voiton kannalta. Tekoäly tekee tämän mukaan siirtonsa ja vuoro siirtyy pelaajalle, joka valitsee kolumnin mihin hän haluaa tiputtaa pelinappulansa. Tämän jälkeen on taas tekoälyn vuoro laskea sille paras siirto.

Lisävaatimuksina:

- Siirtojen järjestäminen (aloitetaan siirtojen tutkiminen pelilaudan keskeltä)
- Iteratiivinen syveneminen (minimax ensin pienellä syvyydellä, sitten yhä suuremmalla, tietyllä aikarajalla)
- Tarkistetaan joka vuoron jälkeen, muodostaako tämä siirto neljän suoran eli voiton
- Mielekäs heuristiikkafunktio arvioimaan pelitilannetta (esimerkiksi tekoälyn kolmen suorista hyvät pisteet, kun taas vastustajan kolmen suorasta miinuspisteitä)

Pelilauta tulostetaan konsoliin ja peliä pelataan komentoriviltä. Syötteenä pelaaja antaa sarakkeen numeron, mihin pelaajan pelinappula tiputetaan.

Alfa-beta karsinnalla minimax algoritmin aikavaatimus on hitaimmillaan O(b^d) ja nopeimmillaan O(sqrt(b^d)), missä d on haun syvyys ja b on haarautumisluku eli vaihtoehtojen määrä. Alfa-beta karsinta sekä lisävaatimuksissa luetellut optimoinnit lisäävät algoritmin tehokkuutta. Ilman niitä varsinkin alussa (kun ladalla on vähän nappuloita) laskentaan menisi paljon aikaa, eikä olisi niin mielekästä pelata tätä tekoälyä vastaan.

## Lähteet

[Wikipedia, Alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
[Youtube, Minimax algorithm with Alpha-Beta pruning with Connect 4](https://www.youtube.com/watch?v=DV5d31z1xTI&list=WL&index=1&t=196s)
