---
type: Table
title: "Tikrinimas — Pasienio kontrolės punktų fitosanitarijos postų (skyrių) tikrinimų duomenys"
description: "Spinta table datasets/gov/vat/fitosanitarijos_kontrole/Tikrinimas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_kontrole/Tikrinimas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/fitosanitarijos_kontrole.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/fitosanitarijos_kontrole.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tikrinimas — Pasienio kontrolės punktų fitosanitarijos postų (skyrių) tikrinimų duomenys

- **Model:** `datasets/gov/vat/fitosanitarijos_kontrole/Tikrinimas`[^manifest]
- **Dataset:** [Pateikiama informacija apie iš viso atliktų patikrinimų skaičių pagal kontroliuojamas sritis, nurodomas neatitikusių reikalavimus siuntų skaičius, dažniausiai pasitaikantys neatitikimai (patikrintų siuntų ir iš jų...](../fitosanitarijos_kontrole.md) (`datasets/gov/vat/fitosanitarijos_kontrole`)
- **Manifest CSV:** [datasets/gov/vat/fitosanitarijos_kontrole.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/fitosanitarijos_kontrole.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_kontrole/Tikrinimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | — | — |
| `pradzia` | `date` | `D` | `4` | `open` | — | Tikrinimo pradžios data | — |
| `pabaiga` | `date` | `D` | `4` | `open` | — | Tikrinimo pabaigos data | — |
| `metodine_sritis` | `string` | — | `4` | `open` | — | Tikrinimo metodinė sritis | — |
| `tikrinimo_sritis` | `string` | — | `4` | `open` | — | Tikrinimo rūšis | — |
| `paimtas_meginys` | `boolean` | — | `4` | `open` | — | Nuoroda, ar tikrinimo metu buvo paimtas mėginys | — |
| `punkto_fitosanitarijos_postas` | `string` | — | `4` | `open` | — | Pasienio kontrolės fitosanitarijo postas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `metodine_sritis` | `"Fitosanitarija"` | — | — | — | — |
| `metodine_sritis` | `"Agrochemija"` | — | — | — | — |
| `metodine_sritis` | `"Dauginamoji medžiaga"` | — | — | — | — |
| `tikrinimo_sritis` | `"Fitosanitarinis tikrinimas"` | — | — | — | — |
| `tikrinimo_sritis` | `"Šviežių vaisių ir daržovių atitikties prekybos standartams tikrinimas"` | — | — | — | — |
| `tikrinimo_sritis` | `"Tręšiamųjų produktų priežiūra"` | — | — | — | — |
| `tikrinimo_sritis` | `"Augalų apsaugos produktų priežiūra"` | — | — | — | — |
| `tikrinimo_sritis` | `"GMO stebėsena"` | — | — | — | — |
| `tikrinimo_sritis` | `"Dauginamosios medžiagos tikrinimas pasienyje"` | — | — | — | — |
| `tikrinimo_sritis` | `"GMO kontrolė"` | — | — | — | — |
| `punkto_fitosanitarijos_postas` | `"Klaipėdos jūrų uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `punkto_fitosanitarijos_postas` | `"Medininkų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `punkto_fitosanitarijos_postas` | `"Šalčininkų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `punkto_fitosanitarijos_postas` | `"Raigardo kelio pasienio kontrolės punkto fitosanitarijos postas"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/fitosanitarijos_kontrole.csv
