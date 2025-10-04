# Testausdokumentti

## Testikattavuus

![Kattavuusraportti](./coverage_report.png)

## Yksikkötestaus

Yksikkötestaus on tehty Unittest-kirjastoa käyttäen. Testeissä testataan luokkien Connect4 ja AI toimintoja, sillä nämä sisältävät ohjelmalogiikan funktioita. Käyttöliittymä ei ole mukana testauksessa.

Testauksessa syötteinä on käytetty pelilaudan eri tilanteita: tyhjää lautaa, täyttä lautaa sekä erilaisia osin täytettyjä lautoja.

AI-luokan testeissä testattu, että

- winning_move palauttaa oikean tuloksen kun ei ole voittoa ja kun on voitto
- heuristic_value laskee oikean arvon pelilaudalle, jossa on yksi siirto ja laudalle mikä on osittain täytetty
- get_moves palauttaa oikeat sarakkeet oikeassa järjestyksessä tyhjällä, puoliksi täytetyllä ja täydellä laudalla
- simulate_move simuloi laudan oikein, kun sille annetaan alkuperäinen lauta, kolumni johon siirto tehdään ja pelaaja jonka siirto on
- minimax näkee voittotilanteen 5 siirron päässä ja osaa tehdä oikeat siirrot, kun 5 siirron päässä on varma voitto, lisäksi siirroille palautuu oikea voittoarvo 100000

Connect4-luokan testeissä testattu, että

- make_move osaa tehdä oikean pelaajan siirron haluttuun sarakkeeseen, palauttaa Truen sekä rivi-sarake -arvot
- make_move osaa todeta, että siirto ei ole mahdollinen tilanteessa jossa haluttu sarake on jo täynnä, tällöin ei palauta rivi-sarake -arvoja
- full_board osaa tutkia onko annettu pelilauta täynnä / on vielä tilaa

## Manuaalinen testaus

Käyttöliittymän ja pelilogiikan toimimista yhdessä on testattu manuaalisesti. On testattu, tekeekö tekoäly hyviä siirtoja pelaajaa vastaan (eli osaa rakentaa omia suoria ja myös estää pelaajan suoria). Testattu myös että oikeat tekstit tulevat näkyviin voitoista/tasapelistä.
