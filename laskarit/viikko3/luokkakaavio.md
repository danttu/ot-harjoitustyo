## Monopoly

Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi. Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa.

```mermaid
 classDiagram
      Pelilauta <.. "2..8" Pelaaja
      Pelilauta <.. Ruutu
      Pelilauta <.. "2" Noppa
      Pelaaja <.. Ruutu
      class Noppa{
          silmaluku
      }
      class Pelaaja{
          pelinappula
          pelinappulanSijainti
      }
      class Pelilauta{
          pelaajat
          ruudut
          nopat
      }
      class Ruutu{
          nykyinen
          seuraava
      }
```