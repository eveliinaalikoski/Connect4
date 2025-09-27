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

Voit suorittaa testit komennolla

```bash
poetry run invoke test
```

ja saat testikattavuusraportin komennolla

```bash
poetry run invoke coverage
```
