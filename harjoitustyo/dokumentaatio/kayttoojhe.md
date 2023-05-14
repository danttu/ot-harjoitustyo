# Käyttöohje

## Pelin asennus
Asenna kaikki pelin tarvittavat riippuvuudet seuraavalla komennolla:
```
poetry install
```
Sen jälkeen kun kaikki riippuvuudet on asennettu suoritetaan alustustoimenpiteet:
```
poetry run invoke build
```
## Pelin käynnistäminen
Pelin käynnistät seuraavalla komennolla:
```
poetry run invoke start
```
## Päävalikko
![Kuva pelin päävalikosta](https://github.com/danttu/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/kuvat/paavalikko.png)

Päävalikossa on kolme nappia: **Aloita peli**, **Asetukset** ja **Poistu pelistä**.
### Aloita peli
Vaihtaa näkymää *suunnitteluvaiheeseen*.
### Asetukset
Avaa *asetukset*.
### Poistu pelistä
Sulkee pelin.

## Asetukset
![Kuva pelin asetuksista](https://github.com/danttu/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/kuvat/asetukset.png)

Asetuksissa voit säätää:
- Musiikin voimakkuutta
- Ääniefektien voimakkuutta
- Ikkunan resoluutiota
Muutokset tulevat toimeen kun painat **Käytä**-nappia. Poistuaksesi takaisin päävalikkoon paina **Takaisin**-nappia.

## Suunnitteluvaihe
![Kuva suunnitteluvaiheesta](https://github.com/danttu/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/kuvat/suunnitteluvaihe.png)

Ikkunan yläreunasta löytyy tukikohdan elämät, nykyinen kierros ja pelaajan rahamäärä. Ikkunan oikealla reunalla on kauppa, mistä voi ostaa puolustusaseet.
Keskellä on kartta. Puolustusaseet ostetaan painamalla haluttu puolustusase ja sen jälkeen **Osta**-nappia. Kun ollaan valmiita puolustamaan, painetaan
**Valmis**-nappia siirtyäkseen puolustusvaiheeseen.

## Puolustusvaihe
![Kuva puolustusvaiheesta](https://github.com/danttu/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/kuvat/puolustusvaihe.png)

Ikkunan yläreunassa edelleen näkyy tukikohdan elämät, nykyinen kierros ja pelaajan rahamäärä. Vihollisia alkaa tulemaan tietyin aikavälein. 
Vihollisten nopeus ja elämät riippuvat nykyisestä kierroksesta, mitä pidemmälle päästään, sitä vaikeampi on tuhota vihollisia. Jos vihollinen
pääsee lähelle tukikohtaa (kuvassa laatikko, jossa lukee "HQ") tekee vihollinen vahinkoa joka kaksi sekunttia. Samalla vihollinen ottaa vahinkoa joka
kaksi sekunttia. Peli päättyy kun pelaajan tukikohta tuhoutuu tai pelaaja painaa **ESC**-näppäintä joko suunnitteluvaiheessa tai puolustusvaiheessa.
Pelin päätyttyä näytetään tulosruutu.

## Tulosruutu
![Kuva tulosruudusta](https://github.com/danttu/ot-harjoitustyo/blob/main/harjoitustyo/dokumentaatio/kuvat/tulokset.png)

Tulosruudulla näytetään kierros, jossa tukikohta tuhoutui, tuhottujen vihollisten määrä ja jäljelle jäänyt rahamäärä. Tulosruudulla
näkyy myös kaksi nappia: **Aloita uusi peli** ja **Poistu päävalikkoon**. Jos pelaaja haluaa aloittaa uuden pelin hänen pitää
painaa **Aloita uusi peli**-nappia, jolloin peli alustetaan uutta pelikertaa varten. Jos pelaaja haluaa poistua päävalikkoon niin
hänen pitää painaa **Poistu päävalikkoon**-nappia.
