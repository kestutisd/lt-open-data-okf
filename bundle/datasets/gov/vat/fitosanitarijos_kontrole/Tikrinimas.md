---
type: Table
title: "Tikrinimas — Pasienio kontrolės punktų fitosanitarijos postų (skyrių) tikrinimų duomenys"
description: "Spinta table datasets/gov/vat/fitosanitarijos_kontrole/Tikrinimas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_kontrole/Tikrinimas"
tags: [gov, vat, tikrinimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/fitosanitarijos_kontrole.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/fitosanitarijos_kontrole.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1892/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarijos_kontrole"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Tikrinimas — Pasienio kontrolės punktų fitosanitarijos postų (skyrių) tikrinimų duomenys

- **Model:** `datasets/gov/vat/fitosanitarijos_kontrole/Tikrinimas`[^manifest]
- **Dataset:** [Pateikiama informacija apie iš viso atliktų patikrinimų skaičių pagal kontroliuojamas sritis...](../fitosanitarijos_kontrole.md) (`datasets/gov/vat/fitosanitarijos_kontrole`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/fitosanitarijos_kontrole.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/fitosanitarijos_kontrole.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_kontrole/Tikrinimas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/fitosanitarijos_kontrole.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/fitosanitarijos_kontrole.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarijos_kontrole (https://data.gov.lt/datasets/1892/)
