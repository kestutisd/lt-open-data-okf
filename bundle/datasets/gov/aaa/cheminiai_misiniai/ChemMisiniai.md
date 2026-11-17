---
type: Table
title: "ChemMisiniai — Cheminių medžiagų / mišinių klasifikatoriai"
description: "Spinta table datasets/gov/aaa/cheminiai_misiniai/ChemMisiniai (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/cheminiai_misiniai/ChemMisiniai"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/cheminiai_misiniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/cheminiai_misiniai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# ChemMisiniai — Cheminių medžiagų / mišinių klasifikatoriai

- **Model:** `datasets/gov/aaa/cheminiai_misiniai/ChemMisiniai`[^manifest]
- **Dataset:** [datasets/gov/aaa/cheminiai_misiniai](../cheminiai_misiniai.md) (`datasets/gov/aaa/cheminiai_misiniai`)
- **Manifest CSV:** [datasets/gov/aaa/cheminiai_misiniai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/cheminiai_misiniai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/cheminiai_misiniai/ChemMisiniai`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės nr. | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Cheminio mišinio pavadinimas | — |
| `kn_kodas` | `string` | — | `2` | `open` | — | Kombinuotosios nomenklatūros (KN) kodas. KN kodų aprašymai: https://osp.stat.gov.lt/documents/10180/8410423/KN_2022.zip | — |
| `ufi_kodas` | `string` | — | `2` | `open` | — | UFI kodas | Unikalus mišinio identifikatorius, nurodomas ant produktų, kurie pagal ES klasifikavimo, ženklinimo ir pakavimo reglamentą klasifikuojami kaip keliantys pavojų sveikatai arba fizinį pavojų. Produktų, kurie parduodami ES iki 2021 m., etiketėse privaloma pradėti nurodyti šį kodą ne vėliau kaip iki 2025 m. Plačiau: https://aaa.lrv.lt/uploads/aaa/documents/files/Pranesimas%20del%20UFI%20_final.pdf |
| `kiekis` | `number` | `t` | `4` | `open` | — | Kiekis | — |
| `veiksmas` | `string` | — | `4` | `open` | — | Veiksmas | — |
| `pav_frazes` | `string` | — | `2` | `open` | — | Pavojingumo frazės | Pavojingumo frazės su paaiškinimais: https://ec.europa.eu/taxation_customs/dds2/SAMANCTA/LT/Safety/HP_LT.htm |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiksmas` | `"EK"` | — | — | Eksportuota | — |
| `veiksmas` | `"SU"` | — | — | Sunaudota | — |
| `veiksmas` | `"IS"` | — | — | Išplatinta (parduota) | — |
| `veiksmas` | `"PA"` | — | — | Pagaminta | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/cheminiai_misiniai.csv
