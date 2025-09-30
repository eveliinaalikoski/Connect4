# Viikkoraportti 3

työaika: 15.5h

Mitä olen tehnyt tällä viikolla?

- heuristiikkafunktiota, missä tutkitaan neljän ikkunoita
  - aluksi laski count() metodin avulla, montako kenenkin nappulaa ikkunassa oli
  - vaihdoin tekoälyn merkinnäksi 5 (ennen 2), jotta heuristiikkafunktiossa voidaan laskea ikkunan summa ja apulistan avulla saada pistemäärä
  - tämä nopeuttaa jonkin verran laskentaa (if-lauseita paljon vähemmän, eikä tarvitse erillistä funktiota laskemiseen)
- minimaxin alkuun voittotarkistuksen ja tasapelin tarkistuksen
  - voittotarkastus tutkii voittoa vain edellisen siirron sisältäviltä riveiltä
  - tasapeli todetaan, jos pelilauta on täynnä
- kun minimaxin sisällä haetaan sarakkeet joihin on mahdollista tehdä siirtoja, ne käydään läpi keskeltä sivuille
- eriyttänyt käyttöliittymän ja pelilogiikan (ui luokassa oli connect4 luokkaan kuuluvia funktioita)
- tehnyt lisää testejä & testausdokumentti
- siistinyt koodia pylintillä ja autopep8lla

Miten ohjelma on edistynyt?

- peliä pystyy pelaamaan, ja tekoäly pisteyttää heuristiikkafunktion avulla pelitilanteita siten, että tekoäly tekee järkeviä siirtoja
- peli tarkistaa voittoja ja tasapelejä (eli onko game over)
  - ei pysty tehdä enää siirtoja jos game over
  - tällä hetkellä vielä pelilauta jää näkyviin ja pelin päättymisestä tulee ilmoitus komentoriville

Mitä opin tällä viikolla?

- heuristiikoista, ja kuinka monimutkaisia niistä voisi tehdä (jos otetaan huomioon esim. erilaiset 3-rivit, onko avoin molemmilta puolilta, vain toiselta tai kokonaan suljettu)
- opin ohjauksen avulla myös seuraavalla viikolla aloitettavasta iteratiivisesta syvenemisestä, miten implemoin sen projektiini ja miten se voi nopeuttaa laskentaa

Mikä jäi epäselväksi tai tuottanut vaikeuksia?

- alkuviikosta heuristiikat, mutta sain siihen ohjausta mikä selvensi paljon

Mitä teen seuraavaksi?

- aloitan iteratiivisen syvenemisen iplemoinnin minimaxiin
- lisää testausta
