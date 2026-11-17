---
type: Table
title: "Patikrinimas — Pateikiama informacija apie atliktus agrochemijos srities patikrinimus (tikrinimą atlikęs teritorinis padalinys; tikrinimo data; metodinė sritis; tikrinimo sritis; tikrinimo pobūdis..."
description: "Spinta table datasets/gov/vat/agrochemija/Patikrinimas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/agrochemija/Patikrinimas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r11_agrochemijos_patikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r11_agrochemijos_patikrinimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patikrinimas — Pateikiama informacija apie atliktus agrochemijos srities patikrinimus (tikrinimą atlikęs teritorinis padalinys; tikrinimo data; metodinė sritis; tikrinimo sritis; tikrinimo pobūdis...

- **Model:** `datasets/gov/vat/agrochemija/Patikrinimas`[^manifest]
- **Dataset:** [datasets/gov/vat/agrochemija](../agrochemija.md) (`datasets/gov/vat/agrochemija`)
- **Manifest CSV:** [datasets/gov/vat/r11_agrochemijos_patikrinimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r11_agrochemijos_patikrinimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/agrochemija/Patikrinimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis stulpelis | — |
| `tikrinimo_pradzia` | `date` | `D` | `4` | `open` | — | Tikrinimo pradžios data | — |
| `tikrinimo_pabaiga` | `date` | `D` | `4` | `open` | — | Tikrinimo pabaigos data | — |
| `pobudis` | `string` | — | `4` | `open` | — | Tikrinimo pobūdis | — |
| `sritis` | `string` | — | `4` | `open` | — | Tikrinimo sritis | — |
| `rusis` | `string` | — | `4` | `open` | — | Tikrinimo rūšis | — |
| `objektas` | `string` | — | `3` | `open` | — | Tikrinamas objektas | — |
| `paimtas_meginys` | `boolean` | — | `4` | `open` | — | Nuoroda, ar buvo paimtas mėginys | — |
| `tikrinta_turgavieteje` | `boolean` | — | `4` | `open` | — | Nuoroda, ar tikrinimas vyko turgavietėje | — |
| `padalinys` | `string` | — | `4` | `open` | — | Tikrinimą vykdęs padalinys | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pobudis` | `"Augalų apsaugos produktų naudojimo patikra"` | — | — | — | — |
| `pobudis` | `"Tręšiamųjų produktų naudojimo patikra"` | — | — | — | — |
| `pobudis` | `"Krovinių ir (ar) prekių tikrinimas dėl TP"` | — | — | — | — |
| `pobudis` | `"Augalų apsaugos produktų tiekimo rinkai patikra"` | — | — | — | — |
| `pobudis` | `"Tręšiamųjų produktų saugojimo, pateikimo ir (ar) tiekimo rinkai patikra"` | — | — | — | — |
| `pobudis` | `"Augalų apsaugos produktų saugojimo patikra"` | — | — | — | — |
| `pobudis` | `"Krovinių ir (ar) prekių tikrinimas dėl AAP"` | — | — | — | — |
| `pobudis` | `"TP produktų gaminių bandinių ėmimas"` | — | — | — | — |
| `pobudis` | `"Apdorojimo įrangos tikrintojų patikra"` | — | — | — | — |
| `pobudis` | `"Tręšiamųjų produktų patikra pasienio poste"` | — | — | — | — |
| `pobudis` | `"Augalų, jų dalių arba dirvožemio ėminių ėmimas"` | — | — | — | — |
| `pobudis` | `"Augalų apsaugos produktų ėminių ėmimas"` | — | — | — | — |
| `sritis` | `"Augalų apsaugos produktų priežiūra"` | — | — | — | — |
| `sritis` | `"Tręšiamųjų produktų priežiūra"` | — | — | — | — |
| `sritis` | `"Augalų apsaugos produktų apdorojimo įrangos tikrintojų priežiūra"` | — | — | — | — |
| `rusis` | `"neplaninis"` | — | — | — | — |
| `rusis` | `"planinis"` | — | — | — | — |
| `rusis` | `"planinis+neplaninis"` | — | — | — | — |
| `padalinys` | `"Kauno regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Šiaulių regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Panevėžio regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Marijampolės regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Vilniaus regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Klaipėdos regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Medininkų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Utenos regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Telšių regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Alytaus regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Tauragės regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Šalčininkų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Klaipėdos jūrų uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Agrochemijos skyrius"` | — | — | — | — |
| `padalinys` | `"Kybartų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Kauno oro uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r11_agrochemijos_patikrinimai.csv
