---
type: Table
title: "IstaigaMenuo — Kompensacijos Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo švietimo įstaigoms"
description: "Spręsdama vietų trūkumo Vilniaus ikimokyklinio ir priešmokyklinio švietimo įstaigose klausimą, Vilniaus miesto savivaldybė nuo 2015 m. moka mėnesines kompensacijas, pasirinkusiems leisti vaikus į Vilniaus mieste veikiančius privačius..."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/kompensacijos/IstaigaMenuo"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/kompensacijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/kompensacijos.csv#L12"
    last_modified: "2026-11-11T14:39:20Z"
---

# IstaigaMenuo — Kompensacijos Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo švietimo įstaigoms

Spręsdama vietų trūkumo Vilniaus ikimokyklinio ir priešmokyklinio švietimo įstaigose klausimą, Vilniaus miesto savivaldybė nuo 2015 m. moka mėnesines kompensacijas, pasirinkusiems leisti vaikus į Vilniaus mieste veikiančius privačius darželius (2025 m. rugpjūčio duomenimis, kompensacijos dydis yra 120 eurų). Kompensacija skiriama tuo atveju, jei vienas iš vaiko tėvų (globėjų) deklaruoja gyvenamąją vietą Vilniaus savivaldybės teritorijoje, ir yra mokama tiesiogiai nevalstybinei ugdymo įstaigai. Daugiau informacijos apie kompensacijų skyrimą galima rasti tvarkos apraše (https://aktai.vilnius.lt/document/30400626).

Rinkinyje skelbiami mėnesinių kompensacijų ataskaitų duomenys pagal švietimo įstaigą ir ataskaitinį mėnesį nuo 2018 m. Taip pat nurodomas atmestų, laukiančių patvirtinimo ir patvirtintų kompensacijų prašymų skaičius.

- **Model:** `datasets/gov/vilniaus_m_sav/kompensacijos/IstaigaMenuo`[^manifest]
- **Dataset:** [Kompensacijos Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo švietimo įstaigoms](../kompensacijos.md) (`datasets/gov/vilniaus_m_sav/kompensacijos`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/kompensacijos.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/kompensacijos.csv#L12)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/kompensacijos/IstaigaMenuo`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `ataskaitine_data` | `date` | `D` | `4` | `open` | — | Ataskaitinio mėnesio paskutinė diena | — |
| `istaiga` | `string` | — | `4` | `open` | — | Švietimo įstaigos pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įstaigos juridinio asmens kodas | — |
| `atmesta` | `integer` | — | `4` | `open` | — | Atmestų kompensacijų apmokėjimo prašymų skaičius. | — |
| `laukiama` | `integer` | — | `4` | `open` | — | Kompensacijų prašymų, kurių apmokėjimas laukia Vilniaus miesto savivaldybės administracijos patvirtinimo, skaičius | — |
| `patvirtinta` | `integer` | — | `4` | `open` | — | Kompensacijų prašymų, kurių apmokėjimas buvo patvirtintas Vilniaus miesto savivaldybės administracijos, skaičius | — |
| `atnaujinimas` | `date` | `D` | `4` | `open` | — | Ataskaitos duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/kompensacijos.csv
