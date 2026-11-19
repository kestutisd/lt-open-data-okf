---
type: Table
title: "Patikrinimas — Saugos reikalavimų vykdymo patikrinimai"
description: "Spinta table datasets/gov/rsc/saugos_reikalavimai/Patikrinimas (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rsc/saugos_reikalavimai/Patikrinimas"
tags: [gov, rsc, patikrinimas, deployed, level-2, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/saugos_reikalavimai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rsc/saugos_reikalavimai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/458/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rsc/saugos_reikalavimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Patikrinimas — Saugos reikalavimų vykdymo patikrinimai

- **Model:** `datasets/gov/rsc/saugos_reikalavimai/Patikrinimas`[^manifest]
- **Dataset:** [Radiacinės saugos centro atlikti radiacinės saugos reikalavimų vykdymo patikrinimai](../saugos_reikalavimai.md) (`datasets/gov/rsc/saugos_reikalavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rsc/saugos_reikalavimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/saugos_reikalavimai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsc/saugos_reikalavimai/Patikrinimas` (`deployed`)[^manifest]
- **Provider:** `rsc` — Radiacinės saugos centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `akto_data` | `date` | `D` | `4` | `open` | — | Patikrinimo akto data | — |
| `skyriaus_id` | `string` | — | `2` | `open` | — | Patikrinimą atlikusio RSC skyriaus identifikatorius | — |
| `akto_nr` | `string` | — | `4` | `open` | — | Patikrinimo akto pilnas numeris | — |
| `tipas` | `string` | — | `2` | `open` | — | Patikrinimo tipas | — |
| `ar_planinis` | `boolean` | — | `4` | `open` | — | Požymis, ar patikrinimas planinis | — |
| `parengta` | `date` | `D` | `4` | `open` | — | Patikrinimo akto parengimo data | — |
| `radiologinis` | `boolean` | — | `4` | `open` | — | Patikrinimo atlikimo su radiologiniais tyrimais požymis | — |
| `veiklos_id` | `string` | — | `2` | `open` | — | Asmens padalinio veiklos identifikatorius | — |
| `rusies_id` | `string` | — | `2` | `open` | — | Asmens padalinio veiklos rūšies identifikatorius | — |
| `sritis` | `string` | — | `3` | `open` | — | Veiklos srities pavadinimas | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens kodas | — |
| `org_pav` | `string` | — | `1` | `open` | — | Juridinio asmens pavadinimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Pilnas adresas | — |
| `miesto_pozymis` | `boolean` | — | `4` | `open` | — | Požymis ar miestas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `salis` | `string` | — | `4` | `open` | — | Valstybės pavadinimas | — |
| `koord` | `geometry(point, 3346)` | — | `3` | `open` | — | Juridinio asmens koordinatės | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `skyriaus_id` | `"33"` | — | — | Vilnius | — |
| `skyriaus_id` | `"34"` | — | — | Kaunas | Aktyvus iki 2019-12-30 |
| `skyriaus_id` | `"35"` | — | — | Klaipėda | Aktyvus iki 2019-12-31 |
| `skyriaus_id` | `"36"` | — | — | Panevėžys | — |
| `skyriaus_id` | `"37"` | — | — | Šiauliai | Aktyvus iki 2019-12-31 |
| `skyriaus_id` | `"38"` | — | — | VATESI | Nebegalioja |
| `skyriaus_id` | `"43"` | — | — | AVMS | Aktyvus nuo 2022-01-01 |
| `tipas` | `"1"` | — | — | Operatyvinis | — |
| `tipas` | `"2"` | — | — | Tikslinis | — |
| `tipas` | `"3"` | — | — | Kompleksinis | — |
| `tipas` | `"10"` | — | — | Planinis - Pranešta | — |
| `tipas` | `"11"` | — | — | Planinis - Nepranešta | — |
| `tipas` | `"12"` | — | — | Neplaninis - Pranešta | — |
| `tipas` | `"13"` | — | — | Neplaninis - Nepranešta | — |
| `veiklos_id` | `"36"` | — | — | Medicina | — |
| `veiklos_id` | `"37"` | — | — | Pramonė | — |
| `veiklos_id` | `"38"` | — | — | Mokslas ir mokymas | — |
| `veiklos_id` | `"39"` | — | — | Kita | — |
| `veiklos_id` | `"40"` | — | — | Mišri | — |
| `veiklos_id` | `"41"` | — | — | Nežinoma | — |
| `rusies_id` | `"74"` | — | — | Rentgenodiagnostika | — |
| `rusies_id` | `"75"` | — | — | Spindulinė terapija | — |
| `rusies_id` | `"76"` | — | — | Branduolinė medicina | — |
| `rusies_id` | `"77"` | — | — | Gamyba | — |
| `rusies_id` | `"78"` | — | — | Radiografija | — |
| `rusies_id` | `"79"` | — | — | Matavimai, bandymai ir tyrimai | — |
| `rusies_id` | `"80"` | — | — | Branduolinė energetika | — |
| `rusies_id` | `"81"` | — | — | Paslaugos | — |
| `rusies_id` | `"82"` | — | — | Kontrolė | — |
| `rusies_id` | `"83"` | — | — | Kita | — |
| `rusies_id` | `"84"` | — | — | Mišri | — |
| `rusies_id` | `"85"` | — | — | Nežinoma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ja_kodas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `base` | `4` | `open` | — | — | — |
| `ja_kodas` | `update(type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rsc/saugos_reikalavimai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/saugos_reikalavimai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rsc/saugos_reikalavimai (https://data.gov.lt/datasets/458/)
