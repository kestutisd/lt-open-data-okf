---
type: Table
title: "Darbuotojas — Darbuotojų duomenys pagal spalio mėn. darbo užmokesčio dydį"
description: "Spinta table datasets/gov/lsd/darbuotoju_darbo_uzmokestis/Darbuotojas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/darbuotoju_darbo_uzmokestis/Darbuotojas"
tags: [gov, lsd, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/darbuotoju_darbo_uzmokestis/darbuotoju_darbo_uzmokestis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/darbuotoju_darbo_uzmokestis/darbuotoju_darbo_uzmokestis.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Darbuotojas — Darbuotojų duomenys pagal spalio mėn. darbo užmokesčio dydį

- **Model:** `datasets/gov/lsd/darbuotoju_darbo_uzmokestis/Darbuotojas`[^manifest]
- **Dataset:** [Darbuotojų duomenys pagal spalio mėn. darbo užmokesčio dydį](../darbuotoju_darbo_uzmokestis.md) (`datasets/gov/lsd/darbuotoju_darbo_uzmokestis`)
- **Manifest CSV:** [datasets/gov/lsd/darbuotoju_darbo_uzmokestis/darbuotoju_darbo_uzmokestis.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/darbuotoju_darbo_uzmokestis/darbuotoju_darbo_uzmokestis.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/darbuotoju_darbo_uzmokestis/Darbuotojas`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | `yr` | `4` | `open` | — | Ataskaitiniai metai | — |
| `key_l` | `integer` | — | `3` | `open` | — | Suteiktas įmonei kodas | — |
| `key_e` | `integer` | — | `3` | `open` | — | Darbuotojo kodas | — |
| `evrk` | `string` | — | `4` | `open` | — | Ekonominės veiklos rūšies kodas (EVRK 2 red., sekcijos) | — |
| `apsk_kodas` | `string` | — | `3` | `open` | — | Apskrities kodas | — |
| `apsk` | `string` | — | `3` | `open` | — | Apskrities pavadinimas | — |
| `sav_kodas` | `string` | — | `3` | `open` | — | Savivaldybės kodas | — |
| `sav` | `string` | — | `3` | `open` | — | Savivaldybės pavadinimas | — |
| `bdu_spalio` | `number` | — | `2` | `open` | — | Bruto darbo užmokestis spalio mėn. | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `apsk_kodas` | — | `1'` | — | Alytaus apskritis | — |
| `apsk_kodas` | — | `'2'` | — | Kauno apskritis | — |
| `apsk_kodas` | — | `'3'` | — | Klaipėdos apskritis | — |
| `apsk_kodas` | — | `'4'` | — | Marijampolės apskritis | — |
| `apsk_kodas` | — | `'5'` | — | Panevėžio apskritis | — |
| `apsk_kodas` | — | `'6'` | — | Šiaulių apskritis | — |
| `apsk_kodas` | — | `'7'` | — | Tauragės apskritis | — |
| `apsk_kodas` | — | `'8'` | — | Telšių apskritis | — |
| `apsk_kodas` | — | `'9'` | — | Utenos apskritis | — |
| `apsk_kodas` | — | `'10'` | — | Vilniaus apskritis | — |
| `sav_kodas` | — | `'11'` | — | Alytaus m. sav. | — |
| `sav_kodas` | — | `'12'` | — | Birštono sav. | — |
| `sav_kodas` | — | `'13'` | — | Vilniaus m. sav. | — |
| `sav_kodas` | — | `'15'` | — | Druskininkų sav. | — |
| `sav_kodas` | — | `'18'` | — | Marijampolės sav. | — |
| `sav_kodas` | — | `'19'` | — | Kauno m. sav. | — |
| `sav_kodas` | — | `'21'` | — | Klaipėdos m. sav. | — |
| `sav_kodas` | — | `'23'` | — | Neringos sav. | — |
| `sav_kodas` | — | `'25'` | — | Palangos m. sav. | — |
| `sav_kodas` | — | `'27'` | — | Panevėžio m. sav. | — |
| `sav_kodas` | — | `'29'` | — | Šiaulių m. sav. | — |
| `sav_kodas` | — | `'30'` | — | Visagino m. sav. | — |
| `sav_kodas` | — | `'32'` | — | Akmenės r. sav. | — |
| `sav_kodas` | — | `'33'` | — | Alytaus r. sav. | — |
| `sav_kodas` | — | `'34'` | — | Anykščių r. sav. | — |
| `sav_kodas` | — | `'36'` | — | Biržų r. sav. | — |
| `sav_kodas` | — | `'38'` | — | Varėnos r. sav. | — |
| `sav_kodas` | — | `'39'` | — | Vilkaviškio r. sav. | — |
| `sav_kodas` | — | `'41'` | — | Vilniaus r. sav. | — |
| `sav_kodas` | — | `'42'` | — | Elektrėnų sav. | — |
| `sav_kodas` | — | `'43'` | — | Zarasų r. sav. | — |
| `sav_kodas` | — | `'45'` | — | Ignalinos r. sav. | — |
| `sav_kodas` | — | `'46'` | — | Jonavos r. sav. | — |
| `sav_kodas` | — | `'47'` | — | Joniškio r. sav. | — |
| `sav_kodas` | — | `'48'` | — | Kalvarijos sav. | — |
| `sav_kodas` | — | `'49'` | — | Kaišiadorių r. sav. | — |
| `sav_kodas` | — | `'52'` | — | Kauno r. sav. | — |
| `sav_kodas` | — | `'53'` | — | Kėdainių r. sav. | — |
| `sav_kodas` | — | `'54'` | — | Kelmės r. sav. | — |
| `sav_kodas` | — | `'55'` | — | Klaipėdos r. sav. | — |
| `sav_kodas` | — | `'56'` | — | Kretingos r. sav. | — |
| `sav_kodas` | — | `'57'` | — | Kupiškio r. sav. | — |
| `sav_kodas` | — | `'58'` | — | Kazlų Rūdos sav. | — |
| `sav_kodas` | — | `'59'` | — | Lazdijų r. sav. | — |
| `sav_kodas` | — | `'61'` | — | Mažeikių r. sav. | — |
| `sav_kodas` | — | `'62'` | — | Molėtų r. sav. | — |
| `sav_kodas` | — | `'63'` | — | Pagėgių sav. | — |
| `sav_kodas` | — | `'65'` | — | Pakruojo r. sav. | — |
| `sav_kodas` | — | `'66'` | — | Panevėžio r. sav. | — |
| `sav_kodas` | — | `'67'` | — | Pasvalio r. sav. | — |
| `sav_kodas` | — | `'68'` | — | Plungės r. sav. | — |
| `sav_kodas` | — | `'69'` | — | Prienų r. sav. | — |
| `sav_kodas` | — | `'71'` | — | Radviliškio r. sav. | — |
| `sav_kodas` | — | `'72'` | — | Raseinių r. sav. | — |
| `sav_kodas` | — | `'73'` | — | Rokiškio r. sav. | — |
| `sav_kodas` | — | `'74'` | — | Rietavo sav. | — |
| `sav_kodas` | — | `'75'` | — | Skuodo r. sav. | — |
| `sav_kodas` | — | `'77'` | — | Tauragės r. sav. | — |
| `sav_kodas` | — | `'78'` | — | Telšių r. sav. | — |
| `sav_kodas` | — | `'79'` | — | Trakų r. sav. | — |
| `sav_kodas` | — | `'81'` | — | Ukmergės r. sav. | — |
| `sav_kodas` | — | `'82'` | — | Utenos r. sav. | — |
| `sav_kodas` | — | `'84'` | — | Šakių r. sav. | — |
| `sav_kodas` | — | `'85'` | — | Šalčininkų r. sav. | — |
| `sav_kodas` | — | `'86'` | — | Švenčionių r. sav. | — |
| `sav_kodas` | — | `'87'` | — | Šilalės r. sav. | — |
| `sav_kodas` | — | `'88'` | — | Šilutės r. sav. | — |
| `sav_kodas` | — | `'89'` | — | Širvintų r. sav. | — |
| `sav_kodas` | — | `'91'` | — | Šiaulių r. sav. | — |
| `sav_kodas` | — | `'94'` | — | Jurbarko r. sav. | — |
| `sav_kodas` | — | `'100'` | — | Alytaus apskrities savivaldybės | — |
| `sav_kodas` | — | `'200'` | — | Kauno apskrities savivaldybės | — |
| `sav_kodas` | — | `'300'` | — | Klaipėdos apskrities savivaldybės | — |
| `sav_kodas` | — | `'400'` | — | Marijampolės apskrities savivaldybės | — |
| `sav_kodas` | — | `'500'` | — | Panevėžio apskrities savivaldybės | — |
| `sav_kodas` | — | `'600'` | — | Šiaulių apskrities savivaldybės | — |
| `sav_kodas` | — | `'700'` | — | Tauragės apskrities savivaldybės | — |
| `sav_kodas` | — | `'800'` | — | Telšių apskrities savivaldybės | — |
| `sav_kodas` | — | `'900'` | — | Utenos apskrities savivaldybės | — |
| `sav_kodas` | — | `'1000'` | — | Vilniaus apskrities savivaldybės | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bdu_spalio` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/darbuotoju_darbo_uzmokestis/darbuotoju_darbo_uzmokestis.csv
