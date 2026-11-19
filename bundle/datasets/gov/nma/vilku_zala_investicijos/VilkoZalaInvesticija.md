---
type: Table
title: "VilkoZalaInvesticija — Lietuvos kaimo plėtros programos 2014 - 2020 metų priemonė \"Prevencinių priemonių taikymas prieš vilkų ūkiniams gyvūnams daromą žalą\""
description: "Spinta table datasets/gov/nma/vilku_zala_investicijos/VilkoZalaInvesticija (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/vilku_zala_investicijos/VilkoZalaInvesticija"
tags: [gov, nma, vilkozalainvesticija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/vilku_zala_investicijos.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/nma/vilku_zala_investicijos.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2314/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nma/vilku_zala_investicijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VilkoZalaInvesticija — Lietuvos kaimo plėtros programos 2014 - 2020 metų priemonė "Prevencinių priemonių taikymas prieš vilkų ūkiniams...

- **Model:** `datasets/gov/nma/vilku_zala_investicijos/VilkoZalaInvesticija`[^manifest]
- **Dataset:** [Lietuvos kaimo plėtros programos 2014-2020 priemonės "Prevencinių priemonių taikymas prieš vilkų...](../vilku_zala_investicijos.md) (`datasets/gov/nma/vilku_zala_investicijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/nma/vilku_zala_investicijos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/vilku_zala_investicijos.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/vilku_zala_investicijos/VilkoZalaInvesticija` (`deployed`)[^manifest]
- **Provider:** `nma` — Nacionalinė mokėjimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/vilku_zala_investicijos.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/vilku_zala_investicijos.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nma/vilku_zala_investicijos (https://data.gov.lt/datasets/2314/)
