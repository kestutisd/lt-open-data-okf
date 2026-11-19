---
type: Table
title: "ChemMisiniai — Cheminių medžiagų / mišinių klasifikatoriai"
description: "Spinta table datasets/gov/aaa/cheminiai_misiniai/ChemMisiniai (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/cheminiai_misiniai/ChemMisiniai"
tags: [gov, aaa, chemmisiniai, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/cheminiai_misiniai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/aaa/cheminiai_misiniai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1561/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/cheminiai_misiniai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# ChemMisiniai — Cheminių medžiagų / mišinių klasifikatoriai

- **Model:** `datasets/gov/aaa/cheminiai_misiniai/ChemMisiniai`[^manifest]
- **Dataset:** [Lietuvos rinkoje esantys pavojingi cheminiai mišiniai](../cheminiai_misiniai.md) (`datasets/gov/aaa/cheminiai_misiniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/cheminiai_misiniai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/cheminiai_misiniai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/cheminiai_misiniai/ChemMisiniai` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiksmas` | `"EK"` | — | — | Eksportuota | — |
| `veiksmas` | `"SU"` | — | — | Sunaudota | — |
| `veiksmas` | `"IS"` | — | — | Išplatinta (parduota) | — |
| `veiksmas` | `"PA"` | — | — | Pagaminta | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/cheminiai_misiniai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/cheminiai_misiniai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/cheminiai_misiniai (https://data.gov.lt/datasets/1561/)
