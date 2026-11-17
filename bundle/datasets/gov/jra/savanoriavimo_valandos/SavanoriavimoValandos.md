---
type: Table
title: "SavanoriavimoValandos — Savanoriavimo valandos"
description: "Jaunimo reikalų agentūros jaunimo savanoriškos tarnybos savanorių savanoriautos valandos priimančiose organizacijose"
resource: "https://get.data.gov.lt/datasets/gov/jra/savanoriavimo_valandos/SavanoriavimoValandos"
tags: [gov, jra, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/jra/savanoriavimo_valandos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/savanoriavimo_valandos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# SavanoriavimoValandos — Savanoriavimo valandos

Jaunimo reikalų agentūros jaunimo savanoriškos tarnybos savanorių savanoriautos valandos priimančiose organizacijose

- **Model:** `datasets/gov/jra/savanoriavimo_valandos/SavanoriavimoValandos`[^manifest]
- **Dataset:** [Savanoriavimo valandos](../savanoriavimo_valandos.md) (`datasets/gov/jra/savanoriavimo_valandos`)
- **Manifest CSV:** [datasets/gov/jra/savanoriavimo_valandos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/savanoriavimo_valandos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/jra/savanoriavimo_valandos/SavanoriavimoValandos`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `val_id` | `string` | — | `4` | `open` | — | Savanorio savanoriavimo dienos valandos ID | — |
| `ataskaitos_id` | `string` | — | `4` | `open` | — | Savanoriavimo valandų registravimo ataskaitos ID | — |
| `role` | `string` | — | `4` | `open` | — | Naudotojo rolė | — |
| `savanorio_id` | `string` | — | `4` | `open` | — | Savanorio identifikatorius | — |
| `dedikuota_lytis` | `string` | — | `4` | `open` | — | Iš vardo pavardės nustatyta lytis | — |
| `gimimo_metai` | `date` | `D` | `4` | `open` | — | Savanorio gimimo metai | — |
| `sutarties_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Savanoriavimo sutarties pasirašymo mėnuo | — |
| `sutarties_ikelimo_data` | `date` | `D` | `4` | `open` | — | Sutarties įkėlimo į sistemą mėnuo | — |
| `savanorystes_pradzia` | `date` | `D` | `4` | `open` | — | Savanoriavimo pradžios mėnuo | — |
| `savanorystes_pabaiga` | `date` | `D` | `4` | `open` | — | Savanoriavimo pabaigos mėnuo | — |
| `savan_men_nr` | `integer` | — | `4` | `open` | — | Savanoriavimo mėnesio eilės numeris | — |
| `savan_val_suma` | `integer` | — | `4` | `open` | — | Savanoriavimo valandų suma per mėnesį | — |
| `savan_pradzios_data` | `date` | `D` | `4` | `open` | — | Savanoriavimo, už kurį suvestos valandos, laikotarpio pradžia | — |
| `savan_pabaigos_data` | `date` | `D` | `4` | `open` | — | Savanoriavimo, už kurį suvestos valandos, laikotarpio pabaiga | — |
| `savan_val_trukme` | `integer` | — | `4` | `open` | — | Savanoriavimo valandų suma už vedamą laikotarpį | — |
| `mentoriaus_id` | `string` | — | `4` | `open` | — | Savanorišką veiklą organizuojančios organizacijos savanoriui paskirto mentoriaus ID | — |
| `mentoriaus_org` | `string` | — | `4` | `open` | — | Paskirto mentoriaus organizacijos pavadinimas | — |
| `svo_id` | `string` | — | `4` | `open` | — | Savanorišką veiklą organizuojančios organizacijos ID | — |
| `svo_pavadinimas` | `string` | — | `4` | `open` | — | Savanorišką veiklą organizuojančios organizacijos pavadinimas | — |
| `svo_veiklos_sritis` | `string` | — | `4` | `open` | — | Savanorišką veiklą organizuojančios organizacijos veiklos sritis | — |
| `po_id` | `string` | — | `4` | `open` | — | Priimančios organizacijos ID | — |
| `po_pavadinimas` | `string` | — | `4` | `open` | — | Priimančios organizacijos pavadinimas | — |
| `po_adresas` | `string` | — | `4` | `open` | — | Priimančios organizacijos veiklos adresas | — |
| `po_veiklos_sritis` | `string` | — | `4` | `open` | — | Priimančios organizacijos veiklos sritis | — |
| `val_suvedimo_data` | `date` | `D` | `4` | `open` | — | Savanoriavimo valandų įvedimo į sistemą data | — |
| `val_modifikavimo_data` | `date` | `D` | `4` | `open` | — | Savanoriavimo valandų modifikavimo data | — |
| `val_versija` | `string` | — | `4` | `open` | — | Savanoriavimo valandų įvedimo versija, skaičiuojama nuo 0 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/jra/savanoriavimo_valandos.csv
