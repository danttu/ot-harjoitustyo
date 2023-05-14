# Tower Defence
Tower Defence on reaaliaikainen tornipuolustuspeli, eli siinä puolustetaan omaa tukikohtaa vihollisilta.

##Huomautukset
Varmista, että sinulla on asennettuna **Python** vähintään versio `3.8`. 
Peli saattaa toimia vanhemmalla versiolla, mutta en voi taataa toimivuuden.
Muista myös asentaa poetry ja päivittää se viimeisimpään versioon.
Kaikki komennot pitää suorittaa "**harjoitustyo**"-kansiossa, eikä juurikansiossa eli ei "ot-harjoitustyo"-kansiossa.

## Dokumentaatio
- [Työaikakirjanpito](https://github.com/danttu/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/danttu/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/danttu/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/changelog.md)
- [Arkkitehtuuri (kesken)](https://github.com/danttu/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/danttu/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/kayttoojhe.md)

## Releaset
- [Release 1](https://github.com/danttu/ot-harjoitustyo/releases/tag/viikko5)
- [~~Release 2~~]()
  - Viikko 6:n palautus unohtui.
- [Release 3](https://github.com/danttu/ot-harjoitustyo/releases/tag/viikko7)

## Pelin asennus
Asenna kaikki pelin tarvittavat riippuvuudet seuraavalla komennolla:
```
poetry install
```
Sen jälkeen kun kaikki riippuvuudet on asennettu pelin voi käynnistää.

## Pelin käynnistäminen
Pelin käynnistät seuraavalla komennolla:
```
poetry run invoke start
```
## Pelin testaus
Peliä testataan suorittamalla seuraava komento:
```
poetry run invoke test
```
Testikattavuuden näkee kun suorittaa seuraava komento:
```
poetry run invoke coverage-report
```
*Huom.* Testikattavuus löytyy *htmlcov*-hakemistosta. 


Pylintin tarkistus voi suorittaa seuraavalla komennolla:
```
poetry run invoke pylint
```

