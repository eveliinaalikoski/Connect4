# Viikkoraportti 2

työaika: 10,5h

Mitä olen tehnyt tällä viikolla?

- testejä minimax algoritmille
- iteratiivinen syvenemishaku kutsuessa minimaxia
  - aloitetaan syvyydestä 3 ja määritetään aikarajaksi 2s
  - minimaxissa talletetaan avaimeksi str(board) ja arvoksi minimaxin parhaan arvon kolumni
  - myöhemmällä kierroksella katsotaan ollaanko oltu kyseisessä tilanteessa aikasemmin --> jos ollaan niin järjestetään possible_moves siten että avaimen arvona oleva kolumni käydään läpi ensimmäisenä (alfa-beta-karsinta tehostuu)
- tein tkinterin Labelilla ilmoitukset voitosta/häviöstä/tasapelistä
- siistin koodia pylintin ja autopep8 avulla
- tutkin eri tekniikoita testaukseen yksikkötestien lisäksi

Miten ohjelma on edistynyt?

- käyttää iteratiivista syvenemistä --> tekoälyn vuorossa kestää yleensä 2-10s
- lisää testausta & testausdokumentti päivitetty
- peli-ikkunan alareunaan tulee ilmoitus voitosta / häviöstä / tasapelistä

Mitä opin tällä viikolla?

- iteratiivisen syvenemisen minimaxissa
- eri testaustekniikoita

Mikä jäi epäselväksi tai tuottanut vaikeuksia?

- en ole onnistunut testaamaan luokan Connect4 funktioita handle_click() ja ai_turn(), koska ne käyttävät käyttöliittymää, niin en tiedä millä tavalla sitä kannattaisi testata
- lisäksi testaukseen liittyen, olen miettinyt mitä muita testeja kuin yksikkötestausta teen projektissani, ehkä integraatiotestausta nimenomaan Connect4 luokan funktioille

Mitä teen seuraavaksi?

- testausta
