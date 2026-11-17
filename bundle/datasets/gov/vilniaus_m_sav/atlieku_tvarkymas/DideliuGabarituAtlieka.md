---
type: Table
title: "DideliuGabarituAtlieka — Didelių gabaritų atliekos"
description: "Rinkinio lentelėje pateikiami SĮ „Vilniaus atliekų sistemos administratoriaus“ (VASA) gaunami užsakymai išvežti didelių gabaritų atliekas Vilniaus miesto savivaldybės teritorijoje."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/DideliuGabarituAtlieka"
tags: [gov, vilniaus_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L50"
    last_modified: "2026-11-11T14:39:20Z"
---

# DideliuGabarituAtlieka — Didelių gabaritų atliekos

Rinkinio lentelėje pateikiami SĮ „Vilniaus atliekų sistemos administratoriaus“ (VASA) gaunami užsakymai išvežti didelių gabaritų atliekas Vilniaus miesto savivaldybės teritorijoje. Vienas užsakymas gali apimti kelias skirtingas daiktų grupes, todėl jie išdėstyti atskirose lentelės eilutėse. Nurodyta išvežimo paslaugos kaina kartais gali nesutapti su nemokamos ar mokamos paslaugos tipu, nes klientui užsisakius papildomą mokamą paslaugą, klientas moka tiesiai vežėjui, informacija gali pasikeisti paslaugos teikimo metu., pvz., kai atvykusiam paimti daiktų vežėjui klientas atiduoda daugiau daiktų ar kitos rūšies daiktų nei buvo iš anksto užsakyta. Klientai gali patys teikti užsakymus s savitarnoje <https://savitarna.vasa.lt/>, arba užsakymo informaciją gali užpildyti VASA darbuotojai. Iš adreso išgautos koordinatės, bet klaidingai aptiktomis laikytinos su patikimumo balu 86 ir mažesniu. Koordinatės susiskirstytos pagal H3 gardelių (angl. H3 grid) sistemą septintojo lygio smulkumu, plačiau apie H3 gardeles ir „H3 index“ žr. <https://h3geo.org/> svetainėje.

- **Model:** `datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/DideliuGabarituAtlieka`[^manifest]
- **Dataset:** [Vilniaus atliekų sistemos administratoriaus atliekų tvarkymas](../atlieku_tvarkymas.md) (`datasets/gov/vilniaus_m_sav/atlieku_tvarkymas`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L50](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L50)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/DideliuGabarituAtlieka`
- **Primary Key (`ref`):** `vda_id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `uzsakymo_id` | `string` | — | `4` | `open` | — | Didelių gabaritų atliekų išvežimo užsakymo identifikatorius | — |
| `ismetamas_daiktas` | `string` | — | `4` | `open` | — | Išmetamo daikto pavadinimas | — |
| `daiktu_sk` | `integer` | — | `4` | `open` | — | Išmetamų daiktų skaičius | — |
| `paslaugos_kaina` | `number` | — | `4` | `open` | — | Paslaugos kaina | — |
| `paslaugos_tipas` | `string` | — | `4` | `open` | — | Paslaugos tipas | — |
| `kada_sukurtas_uzsakymas` | `datetime` | `L` | `4` | `open` | — | Užsakymo užduoties sukūrimo laikas | — |
| `kada_paimami_daiktai` | `datetime` | `H` | `4` | `open` | — | Daiktų paėmimo data | — |
| `busena` | `string` | — | `4` | `open` | — | Užsakymo užduoties būsena | — |
| `vda_koordinaciu_patikimumas` | `number` | — | `4` | `open` | — | Valstybės Duomenų Agentūros pagal adresą nustatytų koordinačių patikimumas (patikimi > 86) | — |
| `vda_adreso_h3_l7` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros iš adreso nustatytų koordinačių „H3 index“ gardelė (septinto lygio) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paslaugos_tipas` | `"ATKS - DGA - Nemokama Individuali atliekų paėmimo paslauga"` | — | — | Nemokama individuali atliekų paėmimo paslauga | — |
| `paslaugos_tipas` | `"ATKS - DGA - Mokama Individuali atliekų paėmimo paslauga"` | — | — | Mokama individuali atliekų paėmimo paslauga | — |
| `busena` | `"Užregistruota"` | — | — | Užregistruota | — |
| `busena` | `"Tikslinama"` | — | — | Tikslinama | — |
| `busena` | `"Perduota vykdymui"` | — | — | Perduota vykdymui | — |
| `busena` | `"Atlikta DGA paslauga"` | — | — | Atlikta | — |
| `busena` | `"Atšaukta DGA paslauga"` | — | — | Atšaukta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv
