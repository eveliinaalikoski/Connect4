# Viikkoraportti 2

työaika: 13 h

Mitä olen tehnyt tällä viikolla?

- päätin, että teen ohjelman käyttöliittymän tkinterillä
- tein tkinterillä pelilaudan piirtämisen, missä on kaksi pelaajaa punainen ja keltainen
- aloittanut ohjelman perustoimintoja (piirretään lauta, voi napauttaa haluamaansa saraketta ja siihen tiputetaan pelinappula)
- aloittanut tekoälyn tekemistä (minimax algoritmin pohja tehtynä [Wikipedian pseudokoodin](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) avulla ja muutama funktio mitä algoritmi tarvitsee)
- yksikkötestaus aloitettu app.py ja ai.py tiedostoista ja coverage report tehty
- olen lisännyt docstringejä funktioihin
- olen siistinyt koodia pylintin ja autopep8in avulla

Miten ohjelma on edistynyt?

- ohjelman teko aloitettu pelilaudan piirtämisellä ja siihen nappuloiden piirrolla
- peliä pystyy 'pelata' eli voit napauttaa haluamaasi saraketta ja pelinappulasi (punainen) piirretään sen sarakkeen alimmalle mahdolliselle riville
- peli vuorottelee pelaajan ja tekoälyn vuoroilla siten, että sen jälkeen kun pelaaja on onnistuneesti saanut pelinappulan tiputettua laudalle, tulee tekoälyn vuoro
  - tällä hetkellä tekoälyn vuorolla, nappula tiputetaan ensimmäiseen sarakkeeseen
  - algoritmi, minkä avulla tekoäly laskisi parhaan siirron on aloitettu, mutta tällä hetkellä kaikille liikkeille annetaan sama arvo
- ohjelman testaus aloitettu

Mitä opin tällä viikolla?

- lisää minimax algoritmista alfa-beta-karsinnalla, ja olen tutkinut lisää miten käyttää sitä projektissani
- opin erilaisia tkinterin elementtejä ja miten niistä voi koota erilaisia pelilautoja (halusin tehdä klassisen näköisen sinisen Connect4 pelilaudan, niin opin siihen tarvittavien elementtien käytöstä)

Mikä jäi epäselväksi tai tuottanut vaikeuksia?

- hieman oli aluksi vaikeuksia algoritmin kanssa rekursioon liittyen ja miten rekursiokutsulle annetaan pelilauta ilman että alkuperäinen lauta muuttuu, mutta sain tämän mielestäni ratkaistua copy kirjaston avulla (deepcopy)

Mitä teen seuraavaksi?

- jatkan algoritmin kehittämistä
- teen mielekkään heuristiikkafunktion, jotta eri liikkeet saavat eri arvoja
- jatkan testausta
