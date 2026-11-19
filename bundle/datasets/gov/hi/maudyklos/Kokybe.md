---
type: Table
title: "Kokybe — Maudyklų vandens kokybės duomenys"
description: "Stebimų Lietuvos maudyklų sąrašas, pateikiama informacija apie: maudymosi sezono metus, maudyklos identifikavimo unikalų kodą, maudymosi sezono pradžią ir pabaigą, vandens kokybės klasę, nuorodos į maudyklos charakteristikų aprašus, maudyklos stebėjimo vietos koordinates..."
resource: "https://get.data.gov.lt/datasets/gov/hi/maudyklos/Kokybe"
tags: [gov, hi, kokybe, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/maudyklos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/hi/maudyklos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2644/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/maudyklos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kokybe — Maudyklų vandens kokybės duomenys

Stebimų Lietuvos maudyklų sąrašas, pateikiama informacija apie: maudymosi sezono metus, maudyklos identifikavimo unikalų kodą, maudymosi sezono pradžią ir pabaigą, vandens kokybės klasę, nuorodos į maudyklos charakteristikų aprašus, maudyklos stebėjimo vietos koordinates, mėginio ėmimo datą, parametrų: žarninių enterokokų ir žarninių lazdelių vertes.[^manifest]

- **Model:** `datasets/gov/hi/maudyklos/Kokybe`[^manifest]
- **Dataset:** [Maudyklų vandens kokybės duomenys](../maudyklos.md) (`datasets/gov/hi/maudyklos`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/maudyklos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/maudyklos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/maudyklos/Kokybe` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `season` | `date` | `Y` | `4` | `open` | — | Sezonas (metai) | — |
| `period_type` | `string` | — | `4` | `open` | — | Stebėsenos laikotarpis | — |
| `start_date` | `date` | `D` | `4` | `open` | — | Stebėsenos pradžia | — |
| `end_date` | `date` | `D` | `4` | `open` | — | Stebėsenos pabaiga | — |
| `bathing_water_id` | `string` | — | `4` | `open` | — | Maudyklos identifikavimo kodas | — |
| `name` | `string` | — | `4` | `open` | — | Maudyklos pavadinimas | — |
| `geometry` | `geometry(point,3346)` | `m` | `4` | `open` | — | Maudyklos stebėjimo vietos koordinatės | — |
| `sample_status` | `string` | — | `4` | `open` | — | Mėginio statusas | shortTermPollutionSample – mėginys, rodantis trumpalaikę taršą (E.coli nustatyta daugiau nei 1000 ksv/100 ml), t.y. viršijantis pagal senąją direktyvą 76/160/EEB nustatytas gairines vertes |
| `sample_date` | `date` | `D` | `4` | `open` | — | Mėginio paėmimo data | — |
| `escherichia_coli_status` | `string` | — | `4` | `open` | — | Žarninių enterokokų statusas | — |
| `escherichia_coli_value` | `number` | — | `3` | `open` | — | Žarniniai enterokokai (ksv/100 ml) | — |
| `intestinal_enterococci_status` | `string` | — | `4` | `open` | — | Žarninių lazdelių statusas | — |
| `intestinal_enterococci_value` | `number` | — | `3` | `open` | — | Žarninės lazdelės (ksv/100 ml) | — |
| `link` | `url` | — | `4` | `open` | — | Nuoroda į maudyklų charakteristikas pdf formatu | Pateikiamos nuorodos į HI svetainę |
| `quality_class` | `string` | — | `4` | `open` | — | Kokybės klasė | Maudyklos kokybė nevertinama kuomet nėra pilnas duomenų rinkinys (mažiausiai 16 mėginių, 4 stebėsenos sezonai) |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `period_type` | `"bathingSeason"` | — | — | Sezonas | — |
| `period_type` | `"shortTermPollution"` | — | — | Trumpalaikė tarša | — |
| `period_type` | `"delisted"` | — | — | Nebestebima - išbraukta iš sąrašo | — |
| `sample_status` | `"preSeasonSample"` | — | — | Prieš maudymosi sezoną paimtas mėginys | — |
| `sample_status` | `"missingSample"` | — | — | Prieš maudymosi sezoną nebuvo paimtas mėginys arba praleistas mėginys | — |
| `sample_status` | `"shortTermPollutionSample"` | — | — | Mėginys, rodantis trumpalaikę taršą | — |
| `sample_status` | `"confirmationSample"` | — | — | Mėginys, patvirtinantis taršos pabaigą | — |
| `sample_status` | `"replacementSample"` | — | — | Mėginys, kurio reikšmėmis bus pakeitos trumpalaikio mėginio reikšmėmis | — |
| `escherichia_coli_status` | `"limitOfDetectionValue"` | — | — | Žemiau aptikimo ribo | — |
| `escherichia_coli_status` | `"confirmedValue"` | — | — | Mėginio reikšmė patvirtinta | — |
| `escherichia_coli_status` | `"missingValue"` | — | — | Mėginys nepaimtas | — |
| `intestinal_enterococci_status` | `"limitOfDetectionValue"` | — | — | Žemiau aptikimo ribo | — |
| `intestinal_enterococci_status` | `"confirmedValue"` | — | — | Mėginio reikšmė patvirtinta | — |
| `intestinal_enterococci_status` | `"missingValue"` | — | — | Mėginys nepaimtas | — |
| `quality_class` | `"0"` | — | — | Nevertinta | — |
| `quality_class` | `"1"` | — | — | Puiki kokybė | — |
| `quality_class` | `"2"` | — | — | Gera kokybė | — |
| `quality_class` | `"3"` | — | — | Patenkinama kokybė | — |
| `quality_class` | `"4"` | — | — | Prasta kokybė | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/maudyklos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/maudyklos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/maudyklos (https://data.gov.lt/datasets/2644/)
