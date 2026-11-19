---
type: Table
title: "SavanoriavimoValandos — Savanoriavimo valandos"
description: "Jaunimo reikalų agentūros jaunimo savanoriškos tarnybos savanorių savanoriautos valandos priimančiose organizacijose"
resource: "https://get.data.gov.lt/datasets/gov/jra/savanoriavimo_valandos/SavanoriavimoValandos"
tags: [gov, jra, savanoriavimovalandos, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/savanoriavimo_valandos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/jra/savanoriavimo_valandos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3863/"
    title: "data.gov.lt DCAT-AP — datasets/gov/jra/savanoriavimo_valandos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# SavanoriavimoValandos — Savanoriavimo valandos

Jaunimo reikalų agentūros jaunimo savanoriškos tarnybos savanorių savanoriautos valandos priimančiose organizacijose[^manifest]

- **Model:** `datasets/gov/jra/savanoriavimo_valandos/SavanoriavimoValandos`[^manifest]
- **Dataset:** [Savanoriavimo valandos](../savanoriavimo_valandos.md) (`datasets/gov/jra/savanoriavimo_valandos`)[^manifest]
- **Manifest CSV:** [datasets/gov/jra/savanoriavimo_valandos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/savanoriavimo_valandos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/jra/savanoriavimo_valandos/SavanoriavimoValandos` (`deployed`)[^manifest]
- **Provider:** `jra` — Jaunimo reikalų agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/jra/savanoriavimo_valandos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/savanoriavimo_valandos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/jra/savanoriavimo_valandos (https://data.gov.lt/datasets/3863/)
