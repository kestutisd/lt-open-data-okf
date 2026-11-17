---
type: Table
title: "Isrinktas"
description: "Spinta table datasets/gov/vrk/isrinkti/Isrinktas (30 columns)."
tags: [gov, vrk, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/isrinkti.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/isrinkti.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Isrinktas

- **Model:** `datasets/gov/vrk/isrinkti/Isrinktas`[^manifest]
- **Dataset:** [datasets/gov/vrk/isrinkti](../isrinkti.md) (`datasets/gov/vrk/isrinkti`)
- **Manifest CSV:** [datasets/gov/vrk/isrinkti.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/isrinkti.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `kandidato_id, rink_kandidato_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `isrinktu_id` | `integer` | — | `4` | `open` | — | Unikalus ID | — |
| `rinkimu_rusis` | `string` | — | `4` | `open` | — | Rinkimų rūšis | EP, SEI, SAV, PRE |
| `kadencijos_nr` | `integer` | — | `4` | `open` | — | Kadencijos eilės numeris | Kadencijos, kurios metu asmuo ėjo pareigas (buvo išrinktas rinkimuose arba užėmė laisvą vietą po rinkimų), eilės numeris |
| `rinkimu_id` | `integer` | — | `4` | `open` | — | Rinkimų identifikatorius | Rinkimų, kuriuose asmuo kandidatavo ir dėl kurių eina arba ėjo pareigas, ID |
| `rinkimu_pavad` | `string` | — | `4` | `open` | — | Rinkimų pavadinimas | Rinkimų, kuriuose asmuo kandidatavo ir dėl kurių eina arba ėjo pareigas, pavadinimas |
| `sav_kodas` | `integer` | — | `4` | `open` | — | Savivaldybės identifikavimo kodas | sav_kodas sutampa su Adresų registro atvertuose rinkiniuose esančiu "Savivaldybės identifikavimo kodas" |
| `sav_nr` | `integer` | — | `4` | `open` | — | Savivaldybės numeris | Savivaldybės, kurioje kandidatas buvo išrinktas, numeris. (Aktualu savivaldybių tarybų narių (merų) rinkimams) - rinkimų apygardos numeris savivaldos rinkimuose |
| `sav_pavadinimas` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | Savivaldybės, kurioje kandidatas buvo išrinktas, pavadinimas. (Aktualu savivaldybių tarybų narių (merų) rinkimams |
| `kandidato_id` | `integer` | — | `4` | `open` | — | Kandidato identifikatorius | — |
| `rink_kandidato_id` | `integer` | — | `4` | `open` | — | Kandidato identifikatorius rinkimuose | — |
| `vardas` | `string` | — | `4` | `open` | — | Kandidato vardas | — |
| `pavarde` | `string` | — | `4` | `open` | — | Kandidato pavardė | — |
| `isrinkimo_budas` | `string` | — | `4` | `open` | — | Apygardos, kurioje kandidatas buvo išrinktas arba užėmė laisvą vietą, tipas | Apygardos, kurioje kandidatas buvo išrinktas arba užėmė laisvą vietą, tipas: 1 - išrinktas vienmandatėje apygardoje pirmajame ture; 2 - išrinktas vienmandatėje apygardoje antrajame ture; D - išrinktas daugiamandatėje apygardoje arba užėmė laisvą vietą. |
| `kandidata_iskele` | `string` | — | `4` | `open` | — | Kandidatą vienmandatėje apygardoje iškėlusios (-ių) organizacijos (-ų) pavadinimas (-ai) ir/ar kandidatas išsikėlė pats | *atskiriama kabliataškiais |
| `apyg_id` | `integer` | — | `4` | `open` | — | Apygardos identifikatorius | — |
| `rink_apyg_id` | `integer` | — | `4` | `open` | — | Rinkimų apygardos identifikatorius | — |
| `apyg_nr` | `integer` | — | `4` | `open` | — | Apygardos numeris | Vienmandatės rinkimų apygardos Nr. |
| `apyg_pavad` | `string` | — | `4` | `open` | — | Apygardos pavadinimas | Vienmandatės rinkimų apygardos pavadinimas |
| `saraso_id` | `integer` | — | `4` | `open` | — | Kandidatą daugiamandatėje apygardoje iškėlusio sąrašo identifikatorius | Kandidatą daugiamandatėje apygardoje iškėlusio sąrašo ID |
| `saraso_nr` | `integer` | — | `4` | `open` | — | Kandidatą daugiamandatėje apygardoje iškėlusio sąrašo numeris | Kandidatą daugiamandatėje apygardoje iškėlusio sąrašo numeris |
| `saraso_pavad` | `string` | — | `4` | `open` | — | Kandidatą daugiamandatėje apygardoje iškėlusio sąrašo pavadinimas | Kandidatą daugiamandatėje apygardoje iškėlusio sąrašo pavadinimas |
| `kand_porink_nr` | `integer` | — | `4` | `open` | — | Kandidato eilės numeris kandidatų sąraše po rinkimų | Porinkiminis Nr. sąraše (daugiamandatėje apygardoje) |
| `ar_isrinktas` | `string` | — | `4` | `open` | — | Požymis, nurodantis ar kandidatas buvo išrinktas rinkimų dieną (T/N) | Požymis, nurodantis ar kandidatas buvo išrinktas rinkimų dieną (T/N) |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Įgaliojimų pradžios data | Data, nuo kurios kandidatas eina/ėjo pareigas |
| `data_iki` | `date` | `D` | `4` | `open` | — | Įgaliojimų pabaigos data | Data, iki kurios kandidatas ėjo pareigas |
| `nutrauk_priezast_kodas` | `string` | — | `4` | `open` | — | Įgaliojimų nutraukimo priežasties kodas | — |
| `nutrauk_priezast_pavad` | `string` | — | `4` | `open` | — | Įgaliojimų nutraukimo priežasties pavadinimas | — |
| `pareigybes_kodas` | `integer` | — | `4` | `open` | — | Asmens pareigybės kodas | — |
| `pareigybes_pavad` | `string` | — | `4` | `open` | — | Asmens pareigybės pavadinimas | 510 Respublikos Prezidentas 502 Europos Parlamento nariai, išrinkti nuo Lietuvos Respublikos 506 Lietuvos Respublikos Seimo nariai 511 Savivaldybių tarybų nariai |
| `ja_pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens, kuriame einamos pareigos, pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rinkimu_rusis` | `"EP"` | — | — | Rinkimai į Europos parlamentą | — |
| `rinkimu_rusis` | `"SEI"` | — | — | Seimo rinkimai | — |
| `rinkimu_rusis` | `"SAV"` | — | — | Savivaldybių tarybų rinkimai | — |
| `rinkimu_rusis` | `"PRE"` | — | — | Prezidento rinkimai | — |
| `isrinkimo_budas` | `"1"` | — | — | Išrinktas vienmandatėje apygardoje pirmajame ture | — |
| `isrinkimo_budas` | `"2"` | — | — | Išrinktas vienmandatėje apygardoje antrajame ture | — |
| `isrinkimo_budas` | `"D"` | — | — | Išrinktas daugiamandatėje apygardoje arba užėmė laisvą vietą | — |
| `ar_isrinktas` | `"T"` | — | — | Taip - išrinktas rinkimų dieną; | — |
| `ar_isrinktas` | `"N"` | — | — | Ne - užėmė laisvą mandatą, atsiradusį kadencijos metu | — |
| `pareigybes_kodas` | `510` | — | — | 510 Respublikos Prezidentas | — |
| `pareigybes_kodas` | `502` | — | — | 502 Europos Parlamento nariai, išrinkti nuo Lietuvos Respublikos | — |
| `pareigybes_kodas` | `506` | — | — | 506 Lietuvos Respublikos Seimo nariai | — |
| `pareigybes_kodas` | `511` | — | — | 511 Savivaldybių tarybų nariai | — |
| `pareigybes_pavad` | `"Respublikos Prezidentas"` | — | — | Respublikos Prezidentas | — |
| `pareigybes_pavad` | `"Europos Parlamento nariai, išrinkti nuo Lietuvos Respublikos"` | — | — | Europos Parlamento nariai, išrinkti nuo Lietuvos Respublikos | — |
| `pareigybes_pavad` | `"Lietuvos Respublikos Seimo nariai"` | — | — | Lietuvos Respublikos Seimo nariai | — |
| `pareigybes_pavad` | `"Savivaldybių tarybų nariai"` | — | — | Savivaldybių tarybų nariai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gpv/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `property` | `4` | `open` | — | — | — |
| `sav_nr` | `update(property: "savivaldybe.sav_nr", type: "")` | `property` | `4` | `open` | — | — | — |
| `sav_pavadinimas` | `update(property: "savivaldybe.sav_pavadinimas", type: "")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/isrinkti.csv
