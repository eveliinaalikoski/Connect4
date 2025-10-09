# Toteutusdokumentti

## Ohjelman rakenne

Connect 4 -pelissä käyttäjä pelaa tekoälyä vastaan tavoitteena neljän suora vaakaan, pystyyn tai diagonaalisesti. Tekoäly laskee minimax algoritmin avulla parhaan siirron (tekoälyn kannalta) käyttäen alfa-beta -karsintaa.

Algoritmi käy liikkeitä läpi sille annetulla syvyydellä, pisteyttää syvyydellä saadut pelitilanteet ja palauttaa niistä parhaimman arvon sekä siirron sijainnin. Alfa-beta -karsintaa käytetään laskennan nopeuttamisessa, sillä se ei käy niitä solmuja läpi, jotka eivät vaikuta lopputulokseen. Lisäksi laskentaa tehostamaan käytetään iteratiivista syvenemistä, eli tutkitaan ensin syvyydellä kolme paras liike, sitten syvyydellä neljä jne. kunnes aikaraja (2s) täyttyy. Jokaisella algoritmin kierroksella otetaan ylös pelitilanne ja tutkitaan ollaanko sellaisessa aikaisemmin oltu. Jos ollaan, tutkitaan ensiksi sitä kolumnia, jossa oli silloin paras liike (usein se on ainakin hyvä liike myös tällä iteraatiolla). Jokainen syvyys käydään kokonaan läpi (aikarajoitteen ylittymistä tutkitaan aina iteraatioiden väleissä), joten parhaan liikkeen löytämiseen menee noin 2-10s.

Pelilaudan ja pelinappuloiden piirtämisestä sekä ilmoitusviestien piirtämisestä vastaa UI-luokka. Connect4-luokka vastaa pelilogiikasta, kuten siirron merkkaamisesta lautaan sekä pelaajan ja tekoälyn vuoroista. Luokka AI koostuu algoritmista sekä siihen vaadittavista apufunktioista kuten voittotarkistuksesta ja heuristiikkafunktiosta.

Pelin käynnistyessä alustetaan tkinter:in avulla graafinen pelilauta, mikä on aluksi tyhjä. Pelaaja (käyttäjä) aloittaa pelin painamalla haluamaansa saraketta, johon pelinappula (punainen) tiputetaan. Onnistunut pelaajan siirto käynnistää tekoälyn vuoron, milloin lasketaan algoritmilla paras liike, ja piirretään tekoälyn pelinappula (keltainen) laudalle. Onnistunut tekoälyn vuoro johtaa siihen, että pelaaja voi taas napauttaa haluamaansa saraketta ja näin peli jatkuu kunnes jompi kumpi voittaa tai tulee tasapeli (eli pelilauta on täysi).

## Aikavaativuudet

Alfa-beta karsinnalla minimax algoritmin aikavaatimus on hitaimmillaan O(b^d) ja nopeimmillaan O(sqrt(b^d)), missä d on haun syvyys ja b on haarautumisluku eli vaihtoehtojen määrä. Alfa-beta karsinta sekä optimoinnit, kuten iteratiivinen syveneminen ja siirtojen järjestäminen, lisäävät algoritmin tehokkuutta.

## Laajojen kielimallien käyttö

Käytin ChatGPT:tä joidenkin bugitilanteiden ymmärtämiseen ja ratkaisemiseen. Käytin sitä myös selittämään kahden vaihtoehtoisen tavan välillä, kumpi on tehokkaampi tai hyödyllisempi juuri siihen tilanteeseen.

## Lähteet

[Wikipedia, Alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

[Youtube, Minimax algorithm with Alpha-Beta pruning with Connect 4](https://www.youtube.com/watch?v=DV5d31z1xTI&list=WL&index=1&t=196s)

[Minimax ja alfa-beta-karsinta, Jaakko Karhunen](https://jyx.jyu.fi/bitstreams/991dbfe7-5ba5-4c0e-9c8d-5ad4fc2022e7/download)
