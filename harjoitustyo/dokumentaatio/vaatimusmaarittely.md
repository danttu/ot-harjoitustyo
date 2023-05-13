# Vaatimusmäärittely

## Pelin tarkoitus
Peli on *reaaliaikainen Tower Defence* peli, jossa puolustetaan omaa tukikohtaa vihollisilta rakentamalla erilaisia puolustusaseita.

## Perusversion tarjoama toiminnallisuus

### Päävalikko
- Kun käynnistää pelin niin peli näyttää päävalikon *Tehty*
- Päävalikossa on seuraavat kohdat:
  - Aloita peli *Tehty*
    - *Tämän valittua pelaaja pääsee aloittamaan pelin*
  - Asetukset *Tehty*
    - *Tässä näkymässä tulee olemaan pelin asetukset, jossa voi säätää esimerkiksi äänenvoimakkuutta tai vaihtaa ikkunan resoluutiota*
  - Poistu pelistä *Tehty*
    - *Sulkee pelin*

### Peli
- Kun pelaaja aloittaa pelin:
  - Pelaaja on **suunnitteluvaiheessa**, jossa pelaaja pääsee suunnittelemaan omaa puolustusta *Tehty*
    - *Tässä vaiheessa viholliset eivät tule*
  - Näytöllä näkyy pelikenttä, tukikohdan elämät, nykyinen kierros ja rahamäärä *Tehty*
  - Näytöllä on myös valikko, mistä pelaaja voi valita puolustusaseet ja *Valmis*-nappi, jota painetaan siirtyäkseen **puolustusvaiheeseen** *Tehty*
- Kun *Valmis*-nappi on painettu:
  - Pelaaja on **puolustusvaiheessa** ja vihollisten hyökkäys alkaa *Tehty*
  - Jos nykyisen kierroksen kaikki viholliset ovat päihitetty siirtyy pelaaja takaisin **suunnitteluvaiheeseen** suunnittelemaan puolustusta seuraavaa kierrosta varten
  - Jos vihollinen onnistuu tuhoamaan pelaajan tukikohdan niin pelaaja siirtyy **lopputulosruutuun** *Tehty*
- Lopputulosruutu:
  - Näytetään kierros, jossa epäonnistuttiin puolustamaan omaa tukikohtaa, rahamäärä, tuhottujen vihollisten määrä ja kaksi nappia: *Aloita uusi peli* ja *Poistu päävalikkoon*
  - Jos pelaaja painaa *Aloita uusi peli*-nappia, peli nollaa pelikentän ja palauttaa arvot aloitusarvoihin. Pelin kulku alkaa alusta,
  - Jos pelaaja painaa *Poistu päävalikkoon*-nappia, pelaaja siirtyy **päävalikkoon**.

## Jatkokehitysideoita
- Paremmat tekstuurit
- Lisää karttoja
- Lisää vihollisia ja puolustusaseita
- Paremmat äänet
- Musiikkia
