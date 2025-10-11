# Viikkoraportti 6

työaika: 7 h

Mitä olen tehnyt tällä viikolla?

- lisää testejä winning_move:lle (joka suuntaan testattu) ja heuristic_value:lle (testattu useammalla pelitilanteella)
- tein muokkauksia vertaispalautteen ehdotuksien mukaan (iteratiivinen syveneminen)
- poistin luokasta UI funktion update_topbar, koska se sisälsi vain yhden rivin, jota pystyy kutsumaan suoraan app.py:ssä
- olen päivittänyt dokumentaatioita
- olen käynyt läpi koodia ja siivoillut sitä

Miten ohjelma on edistynyt?

- muutama testi lisää
- iteratiivinen syveneminen lopettaa laskennan jos sille palautetaan arvo 100000 tai -100000 (voittotilanne), jotta se ei käytä turhaa aikaa laskentaan kun jo tiedetään varma voitto
- yläpalkin tekstien päivitys kutsutaan suoraan funktioissa handle_click ja ai_turn, eikä ui luokassa erillisen funktion avulla

Mikä jäi epäselväksi tai tuottanut vaikeuksia?

- mietin vertaisarvioinnista saatua ehdotusta luokkajaosta, mutta sain siihen apua ohjaajalta, ja päätin, että en nyt enää muokkaa projektin rakennetta

Mitä teen seuraavaksi?

- vertaisarvioinnin ja muokkaan tarvittaessa omaa projektiani saamani vertaisarvion avulla
- viimeistelyä ja siistimistä
