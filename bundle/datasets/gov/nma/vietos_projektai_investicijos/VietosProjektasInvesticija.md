---
type: Table
title: "VietosProjektasInvesticija — Lietuvos kaimo plėtros programos 2014 - 2020 metų priemonė \"Parama vietos projektams įgyvendinti pagal VPS (2014-2020)\""
description: "Spinta table datasets/gov/nma/vietos_projektai_investicijos/VietosProjektasInvesticija (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/vietos_projektai_investicijos/VietosProjektasInvesticija"
tags: [gov, nma, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/vietos_projektai_investicijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/vietos_projektai_investicijos.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# VietosProjektasInvesticija — Lietuvos kaimo plėtros programos 2014 - 2020 metų priemonė "Parama vietos projektams įgyvendinti pagal VPS (2014-2020)"

- **Model:** `datasets/gov/nma/vietos_projektai_investicijos/VietosProjektasInvesticija`[^manifest]
- **Dataset:** [datasets/gov/nma/vietos_projektai_investicijos](../vietos_projektai_investicijos.md) (`datasets/gov/nma/vietos_projektai_investicijos`)
- **Manifest CSV:** [datasets/gov/nma/vietos_projektai_investicijos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/vietos_projektai_investicijos.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/vietos_projektai_investicijos/VietosProjektasInvesticija`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priemone` | `string` | — | `4` | `open` | — | Priemonių grupės pavadinimas | — |
| `veiklos_sritis` | `string` | — | `4` | `open` | — | Administravimo proceso pavadinimas | — |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `bylos_etapas` | `string` | — | `4` | `open` | — | Bylos etapas | — |
| `islaidu_kategorija` | `string` | — | `4` | `open` | — | Išlaidų kategorija | — |
| `islaidu_rusis` | `string` | — | `4` | `open` | — | Išlaidų rūšis | — |
| `islaidos_paramos_suma` | `number` | — | `2` | `open` | — | Išlaidos paramos suma | — |
| `intensyvumas` | `number` | `%` | `4` | `open` | — | Intensyvumas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `"Fizinis"` | — | — | Fizinis | — |
| `pareiskejo_tipas` | `"Juridinis"` | — | — | Juridinis | — |
| `pareiskejo_lytis` | `"V"` | — | — | Vyras | — |
| `pareiskejo_lytis` | `"M"` | — | — | Moteris | — |
| `bylos_etapas` | `"Išregistravimas"` | — | — | Išregistravimas | — |
| `bylos_etapas` | `"Paramos administravimas"` | — | — | Paramos administravimas | — |
| `bylos_etapas` | `"Atmetimas"` | — | — | Atmetimas | — |
| `bylos_etapas` | `"Vertinimas"` | — | — | Vertinimas | — |
| `bylos_etapas` | `"Sutarties rengimas"` | — | — | Sutarties rengimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `islaidos_paramos_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/vietos_projektai_investicijos.csv
