---
type: Table
title: "Individ2016 — Asmens duomenys 2016 m."
description: "Amžius, lytis, giminystės ryšiai, išsilavinimas, ekonominio aktyvumo statusas ir kt."
resource: "https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Individ2016"
tags: [gov, lsd, individ2016, deployed, cadence-quadrennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L1354"
    title: "atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L1354"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1630/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Individ2016 — Asmens duomenys 2016 m.

Amžius, lytis, giminystės ryšiai, išsilavinimas, ekonominio aktyvumo statusas ir kt.[^manifest]

- **Model:** `datasets/gov/lsd/namu_ukio_biudzetas/Individ2016`[^manifest]
- **Dataset:** [Namų ūkių biudžeto statistinio tyrimo duomenys](../namu_ukio_biudzetas.md) (`datasets/gov/lsd/namu_ukio_biudzetas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/namu_ukio_biudzetas.csv#L1354](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L1354)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Individ2016` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUADRENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh_ident` | `integer` | — | — | `open` | — | Namų ūkio identifikatorius | — |
| `line` | `integer` | — | — | `open` | — | Namų ūkio nario eilės Nr. | — |
| `age` | `integer` | — | — | `open` | — | Sukakusių metų skaičius | — |
| `sex` | `integer` | `sex` | — | `open` | — | Lytis | — |
| `relation` | `integer` | — | — | `open` | — | Ryšys su namų ūkio galva | — |
| `partner` | `integer` | — | — | `open` | — | Sutuoktinio (-ės) sugyventinio (-ės) asmens numeris | — |
| `father` | `integer` | — | — | `open` | — | Tėvo (įtėvio patėvio globėjo) asmens numeris | — |
| `mother` | `integer` | — | — | `open` | — | Motinos (įmotės pamotės globėjos) asmens numeris | — |
| `marital` | `integer` | — | — | `open` | — | Šeiminė padėtis | — |
| `study2` | `integer` | — | — | `open` | — | Mokymosi įstaiga kurioje mokosi namų ūkio narys | — |
| `educat2` | `integer` | — | — | `open` | — | Namų ūkio nario išsilavinimas | — |
| `act_st` | `integer` | — | — | `open` | — | Namų ūkio nario ekonominio aktyvumo statusas | — |
| `profes` | `integer` | — | — | `open` | — | Profesija (pareigos atliekamas darbas) pagrindinėje darbovietėje ar užsiimant individualiąja veikla | — |
| `work_day` | `integer` | — | — | `open` | — | Darbo laikas | — |
| `uzimt_st` | `integer` | — | — | `open` | — | Užimtumo statusas pagrindinėje darbovieteje | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `relation` | `1` | — | — | Namų ūkio galva | — |
| `relation` | `2` | — | — | Sutuoktinis (-ė) | — |
| `relation` | `3` | — | — | Sugyventinis (-ė) | — |
| `relation` | `4` | — | — | Sūnus, duktė, įsūnis, įdukra, posūnis, podukra, globotinis (-ė) | — |
| `relation` | `5` | — | — | Tėvas, motina, įtėvis, įmotė, patėvis, pamotė, globėjas (-a) | — |
| `relation` | `6` | — | — | Sutuoktinio (-ės), sugyventinio (-ės) tėvas, motina | — |
| `relation` | `7` | — | — | Brolis , sesuo | — |
| `relation` | `8` | — | — | Žentas , marti | — |
| `relation` | `9` | — | — | Senelis, senelė | — |
| `relation` | `10` | — | — | Vaikaitis (-ė) | — |
| `relation` | `11` | — | — | Kitas (-a) giminaitis (-ė) | — |
| `relation` | `12` | — | — | Ne giminė | — |
| `marital` | `1` | — | — | Niekada nebuvo vedęs (ištekėjusi) | — |
| `marital` | `2` | — | — | Vedęs (ištekėjusi) | — |
| `marital` | `3` | — | — | Neregistruota santuoka | — |
| `marital` | `4` | — | — | Našlys (-ė) | — |
| `marital` | `5` | — | — | Išsituokęs (-usi) | — |
| `study2` | `1` | — | — | Bendrojo ugdymo mokykla | — |
| `study2` | `2` | — | — | Profesinio mokymo įstaiga | — |
| `study2` | `3` | — | — | Kolegija | — |
| `study2` | `4` | — | — | Universitetas | — |
| `educat2` | `1` | — | — | Pradinis, nebaigė pradinės mokyklos | — |
| `educat2` | `2` | — | — | Pagrindinis, pradinis su profesine kvalifikacija | — |
| `educat2` | `3` | — | — | Vidurinis su profesine kvalifikacija, vidurinis, pagrindinis su profesine kvalifikacija | — |
| `educat2` | `4` | — | — | Specialus vidurinis, povidurinis | — |
| `educat2` | `5` | — | — | Aukštasis, aukštesnysis | — |
| `act_st` | `1` | — | — | Dirbantis asmuo | — |
| `act_st` | `2` | — | — | Bedarbis | — |
| `act_st` | `3` | — | — | Senatvės ar išankstinės senatvės pensininkas | — |
| `act_st` | `4` | — | — | Moksleivis, studentas | — |
| `act_st` | `5` | — | — | Darbingo amžiaus namų šeimininkas (-ė), kitas ekonomiškai neaktyvus asmuo | — |
| `act_st` | `6` | — | — | Dėl negalios nedirbantis asmuo | — |
| `profes` | `0` | — | — | Ginkluotųjų pajėgų profesijos | — |
| `profes` | `1` | — | — | Vadovai | — |
| `profes` | `2` | — | — | Specialistai | — |
| `profes` | `3` | — | — | Technikai ir jaunesnieji specialistai | — |
| `profes` | `4` | — | — | Įstaigų tarnautojai | — |
| `profes` | `5` | — | — | Paslaugų sektoriaus darbuotojai ir pardavėjai | — |
| `profes` | `6` | — | — | Kvalifikuoti žemės, miškų ir žuvininkystės ūkio darbuotojai | — |
| `profes` | `7` | — | — | Kvalifikuoti darbininkai ir amatininkai | — |
| `profes` | `8` | — | — | Įrenginių ir mašinų operatoriai ir surinkėjai | — |
| `profes` | `9` | — | — | Nekvalifikuoti darbininkai | — |
| `profes` | `99` | — | — | Nenurodė | — |
| `work_day` | `1` | — | — | Visas darbo dienos ar savaitės laikas | — |
| `work_day` | `2` | — | — | Ne visas darbo dienos ar savaitės laikas | — |
| `uzimt_st` | `1` | — | — | Samdomasis darbuotojas | — |
| `uzimt_st` | `2` | — | — | Savarankiškai su samdomaisiais darbuotojais dirbantis asmuo | — |
| `uzimt_st` | `3` | — | — | Savarankiškai be samdomuųjų darbuotojų dirbantis asmuo | — |
| `uzimt_st` | `4` | — | — | Dirbantis be atlyginimo šeimos versle, asmeniniame žemės ūkyje asmuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L1354 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L1354)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas (https://data.gov.lt/datasets/1630/)
