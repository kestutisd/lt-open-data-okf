---
type: Table
title: "Prasymas — Nekilnojamojo turto (nesuformuotų plotų) prašymų duomenys"
description: "Duomenų rinkinys apima informaciją apie fizinių ar juridinių asmenų prašymus, susijusius su nesuformuotais žemės plotais."
resource: "https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme/Prasymas"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/nesuformuota_zeme.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L21"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Nekilnojamojo turto (nesuformuotų plotų) prašymų duomenys

Duomenų rinkinys apima informaciją apie fizinių ar juridinių asmenų prašymus, susijusius su nesuformuotais žemės plotais. Kiekvienas įrašas žymi konkretų prašymą su unikaliu identifikatoriumi, paslaugos tipu, nagrinėjimo etapu ir būsena. Taip pat pateikiama ploto geometrija – perimetras, plotas bei įvairūs erdviniai formatai (WKT, GeoJSON LKS/WGS).

- **Model:** `datasets/gov/ssva/nesuformuota_zeme/Prasymas`[^manifest]
- **Dataset:** [Nesuformuoti žemės plotai](../nesuformuota_zeme.md) (`datasets/gov/ssva/nesuformuota_zeme`)
- **Manifest CSV:** [datasets/gov/ssva/nesuformuota_zeme.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L21)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme/Prasymas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikatorius | — |
| `nt_registro_kodas` | `string` | — | `4` | `open` | — | Nekilnojamo turto kadastro objektas, su kuriuo susijęs prašymas | — |
| `paslauga` | `string` | — | `4` | `open` | — | Paslaugos kodas | — |
| `etapas` | `string` | — | `4` | `open` | — | Pršymo nagrinėjimo etapas | — |
| `busena` | `string` | — | `4` | `open` | — | Prašymo nagrinėjimo etapo būsena | — |
| `perimetras_m` | `number` | — | `4` | `open` | — | Nesuformuoto ploto perimetras metrais | — |
| `plotas_m2` | `number` | — | `4` | `open` | — | Nesuformuotas plotas kvadratiniais metrais | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Nesuformuoto ploto taškinė geometrija WKT (Well-Known Text) formatu | — |
| `geom_wkt` | `string` | — | `4` | `open` | — | Nesuformuoto ploto geometrija WKT (Well-Known Text) formatu (LKS94) | — |
| `geojson_wgs` | `string` | — | `4` | `open` | — | Nesuformuoto ploto geometrija GeoJSON formatu (koordinatės WGS84 sistemoje) | — |
| `geojson_lks` | `string` | — | `4` | `open` | — | Nesuformuoto ploto geometrija GeoJSON formatu (koordinatės LKS94 sistemoje) | — |
| `paskutinio_atnaujinimo_data` | `datetime` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/nesuformuota_zeme.csv
