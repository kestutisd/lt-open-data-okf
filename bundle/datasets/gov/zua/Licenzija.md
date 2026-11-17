---
type: Table
title: "Licenzija — Paraiškų ir licencijų duomenys"
description: "Rinkinyje pateikiama informacija apie paraiškas gauti licencijas, teikiamas Žemės ūkio agentūrai."
resource: "https://get.data.gov.lt/datasets/gov/zua/Licenzija"
tags: [gov, zua, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zua/licenzijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zua/licenzijos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Licenzija — Paraiškų ir licencijų duomenys

Rinkinyje pateikiama informacija apie paraiškas gauti licencijas, teikiamas Žemės ūkio agentūrai. Duomenys apima paraiškų identifikatorius, pateikimo ir patvirtinimo datas, produktų aprašymus ir kiekius, eksporto tipus, garantijos sumas, įmonių pavadinimus ir adresus bei geografines koordinates (LKS-94).

- **Model:** `datasets/gov/zua/Licenzija`[^manifest]
- **Dataset:** [Žemės ūkio agentūra prie Lietuvos Respublikos žemės ūkio ministerijos](../zua.md) (`datasets/gov/zua`)
- **Manifest CSV:** [datasets/gov/zua/licenzijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zua/licenzijos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/zua/Licenzija`
- **Primary Key (`ref`):** `paraiskos_identifikatorius`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paraiskos_identifikatorius` | `string` | — | `4` | `open` | — | Unikalus paraiškos identifikatorius | — |
| `pateikimo_data` | `datetime` | `L` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `patvirtinimo_data` | `datetime` | `L` | `4` | `open` | — | Paraiškos patvirtinimo data | — |
| `produkto_aprasymas` | `string` | — | `4` | `open` | — | Produkto aprašymas | — |
| `produkto_kiekis` | `number` | — | `4` | `open` | — | Produkto kiekis | — |
| `produkto_kiekis_tekstu` | `string` | — | `4` | `open` | — | Produkto kiekis tekstu | — |
| `specifiniai_parametrai` | `string` | — | `4` | `open` | — | Specifiniai parametrai | — |
| `eksporto_tipas` | `string` | — | `4` | `open` | — | Eksporto tipas | — |
| `garantijos_suma` | `number` | — | `4` | `open` | — | Garantijos suma | — |
| `imones_pavadinimas` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `adresas` | `string` | — | `4` | `open` | — | Įmonės adresas (gatvė) | — |
| `miestas` | `string` | — | `4` | `open` | — | Įmonės adresas (miestas) | — |
| `x_koord_lks` | `number` | — | `4` | `open` | — | Stačiakampės plokštuminės LKS-94 koordinatės | — |
| `y_koord_lks` | `number` | — | `4` | `open` | — | Stačiakampės plokštuminės LKS-94 koordinatės | — |
| `iraso_ikelimo_data` | `datetime` | `L` | `4` | `open` | — | Įrašo įkėlimo data | — |
| `iraso_modifikavimo_data` | `datetime` | `L` | `4` | `open` | — | Įrašo modifikavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zua/licenzijos.csv
