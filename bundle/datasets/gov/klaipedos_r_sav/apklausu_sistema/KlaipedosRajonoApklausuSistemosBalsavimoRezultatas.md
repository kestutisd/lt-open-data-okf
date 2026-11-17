---
type: Table
title: "KlaipedosRajonoApklausuSistemosBalsavimoRezultatas — Klaipėdos rajono apklausų sistemos rezultatai"
description: "Informacija apie Klaipėdos rajono gyventojų apklausų sistemoje apklausa.klaipedos-r.lt rezultatus nuo 2022 m."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_r_sav/apklausu_sistema/KlaipedosRajonoApklausuSistemosBalsavimoRezultatas"
tags: [gov, klaipedos_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_r_sav/apklausu_sistema.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/apklausu_sistema.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# KlaipedosRajonoApklausuSistemosBalsavimoRezultatas — Klaipėdos rajono apklausų sistemos rezultatai

Informacija apie Klaipėdos rajono gyventojų apklausų sistemoje apklausa.klaipedos-r.lt rezultatus nuo 2022 m.

- **Model:** `datasets/gov/klaipedos_r_sav/apklausu_sistema/KlaipedosRajonoApklausuSistemosBalsavimoRezultatas`[^manifest]
- **Dataset:** [Klaipėdos rajono apklausų sistemos rezultatai](../apklausu_sistema.md) (`datasets/gov/klaipedos_r_sav/apklausu_sistema`)
- **Manifest CSV:** [datasets/gov/klaipedos_r_sav/apklausu_sistema.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/apklausu_sistema.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_r_sav/apklausu_sistema/KlaipedosRajonoApklausuSistemosBalsavimoRezultatas`
- **Primary Key (`ref`):** `balsavimo_identifikatorius`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `balsavimo_identifikatorius` | `string` | — | `4` | `open` | — | Balsavimo identifikatorius | — |
| `respondento_identifikatorius` | `string` | — | `4` | `open` | — | Respondento identifikatorius | — |
| `respondento_ip_adresas` | `string` | — | `4` | `open` | — | Šifruotas respondento IP adresas nustatytas balsavimo metu | — |
| `tiketina_valstybe_pagal_ip` | `string` | — | `4` | `open` | — | Užfiksuota apytikslė respondento lokacija (valstybė) balsavimo metu pagal IP adresą pagal trečiųjų šalių duomenis | — |
| `tiketinas_miestas_pagal_ip` | `string` | — | `4` | `open` | — | Užfiksuota apytikslė respondento lokacija (miestas) balsavimo metu pagal IP adresą pagal trečiųjų šalių duomenis | — |
| `respondento_vardas_ir_pavarde` | `string` | — | `4` | `open` | — | Šifruotas respondento vardas ir pavardė | — |
| `respondento_amzius` | `integer` | `yr` | `4` | `open` | — | Respondento amžius | — |
| `apklausos_identifikatorius` | `string` | — | `4` | `open` | — | Apklausos identifikatorius | — |
| `apklausos_pavadinimas` | `string` | — | `4` | `open` | — | Apklausos pavadinimas | — |
| `aprasymas_lt` | `string` | — | `4` | `open` | — | Apklausos aprašas | — |
| `pradzia` | `date` | `D` | `4` | `open` | — | Apklausos pradžia | — |
| `pabaiga` | `date` | `D` | `4` | `open` | — | Apklausos pabaiga | — |
| `klausimo_identifikatorius` | `string` | — | `4` | `open` | — | Apklausos klausimo identifikatorius | — |
| `klausimas_lt` | `string` | — | `4` | `open` | — | Apklausos klausimas | — |
| `klausimo_tipas` | `string` | — | `4` | `open` | — | Apklausos klausimo tipas | — |
| `atsakymo_identifikatorius` | `string` | — | `4` | `open` | — | Atsakymo identifikatorius | — |
| `atsakymas_lt` | `string` | — | `4` | `open` | — | Apklausos atsakymas | — |
| `reitingo_atsakymo_identifikatorius` | `string` | — | `4` | `open` | — | Reitingo atsakymo/įvertinimo identifikatorius | — |
| `reitingo_atsakymas_lt` | `string` | — | `4` | `open` | — | Reitingo atsakymas/įvertinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `klausimo_tipas` | `"Likerto skalė"` | — | — | — | — |
| `klausimo_tipas` | `"Keli pasirinkimai iš sąrašo"` | — | — | — | — |
| `klausimo_tipas` | `"Vienas pasirinkimas iš sąrašo"` | — | — | — | — |
| `klausimo_tipas` | `"Nuoroda"` | — | — | — | — |
| `klausimo_tipas` | `"Įvedimo laukas"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas_lt` | `update(property: "aprasymas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `klausimas_lt` | `update(property: "klausimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `atsakymas_lt` | `update(property: "atsakymas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `reitingo_atsakymas_lt` | `update(property: "reitingo_atsakymas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_r_sav/apklausu_sistema.csv
