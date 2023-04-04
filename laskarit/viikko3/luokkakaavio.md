## Monopoly

Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi. Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa.

```mermaid
classDiagram
    Pelilauta <.. "2..8" Pelaaja
    Pelilauta <.. "40" Ruutu
    Pelilauta <.. "2" Noppa
    Pelaaja <.. Ruutu
    Pelaaja <.. Katu
    SattumaJaYhteismaa <.. Kortti
    Ruutu <.. AloitusRuutu
    Ruutu <.. Vankila
    Ruutu <.. SattumaJaYhteismaa
    Ruutu <.. AsematJaLaitokset
    Ruutu <.. Katu
    class Noppa{
        silmaluku
    }
    class Pelaaja{
        pelinappula
        pelinappulanSijainti
        kadut
        raha
    }
    class Pelilauta{
        pelaajat
        ruudut
        nopat
    }
    class Ruutu{
        tyyppi
        sijainti
        seuraava
    }
    class AloitusRuutu{
        sijainti
    }
    class Vankila{
        sijainti
    }
    class SattumaJaYhteismaa{
        tyyppi
        sijainti
        kortit
    }
    class AsematJaLaitokset{
        tyyppi
        sijainti
    }
    class Katu{
        nimi
        sijainti
        talot
        hotelli
        
    }
    class Kortti{
        toiminto
    }
```