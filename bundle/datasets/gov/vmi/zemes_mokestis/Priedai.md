---
type: Table
title: "Priedai — Žemės mokesčio deklaracijų priedų duomenys"
description: "Spinta table datasets/gov/vmi/zemes_mokestis/Priedai (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/zemes_mokestis/Priedai"
tags: [gov, vmi, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/zemes_mokestis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/zemes_mokestis.csv#L33"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priedai — Žemės mokesčio deklaracijų priedų duomenys

- **Model:** `datasets/gov/vmi/zemes_mokestis/Priedai`[^manifest]
- **Dataset:** [Žemės mokesčio deklaracijų duomenys](../zemes_mokestis.md) (`datasets/gov/vmi/zemes_mokestis`)
- **Manifest CSV:** [datasets/gov/vmi/zemes_mokestis.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/zemes_mokestis.csv#L33)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/zemes_mokestis/Priedai`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Deklaracijos ID (atitinka -ID lentelėje KIT703) | — |
| `metai_id` | `integer` | — | `2` | `open` | — | Įrašo identifikacinis numeris informacinėje sistemoje (Mokestinis laikotarpis) | — |
| `sklypo_sav_kodas` | `integer` | — | `2` | `open` | — | Sklypo savivaldybės kodas | — |
| `plotas_be_misko` | `number` | `ha` | `4` | `open` | — | Bendras sklypo plotas be miško | — |
| `apmokest_plotas` | `number` | `ha` | `4` | `open` | — | Sklypo apmokestinamas plotas | — |
| `dalies_verte_prad` | `number` | — | `2` | `open` | — | Apmokestinamo sklypo mokestinė vertė | — |
| `km_koef` | `number` | — | `2` | `open` | — | Žemės ūkio paskirties (įskaitant sodų) žemei taikomas koeficientas | — |
| `dalies_verte` | `number` | — | `2` | `open` | — | Apmokestinamo sklypo (dalies) mokestinė vertė, įvertinus žemės ūkio paskirties žemei taikomą 0,35 koeficientą | — |
| `tarifas` | `number` | — | `2` | `open` | — | Žemės mokesčio tarifas | — |
| `lengvatos_verte` | `number` | — | `2` | `open` | — | Taikomos lengvatos vertė | — |
| `mokescio_suma` | `number` | — | `2` | `open` | — | Apskaičiuota žemės mokesčio suma | — |
| `az_saltinis` | `string` | — | `4` | `open` | — | Apleistos žemės požymis: S - savivaldybė, V - valstybės žemės fondas | — |
| `az_eiluteje_pozymis` | `string` | — | `4` | `open` | — | Požymis: 1-neapleista žemė, 2-apleista žemė. | — |
| `tvirtinimo_data` | `datetime` | `D` | `4` | `open` | — | Deklaracijos tvirtinimo data (Perskaičiavimo data deklaracijoje) | — |
| `sst_kodas` | `string` | — | `4` | `open` | — | Žemės mokesčio mokėtojo tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `az_saltinis` | `"savivaldybė"` | `S` | — | savivaldybė | — |
| `az_saltinis` | `"valstybės žemės fondas"` | `V` | — | valstybės žemės fondas | — |
| `az_eiluteje_pozymis` | `"neapleista žemė"` | `1` | — | neapleista žemė | — |
| `az_eiluteje_pozymis` | `"apleista žemė"` | `2` | — | apleista žemė | — |
| `sst_kodas` | `"Fizinis asmuo"` | `1` | — | Fizinis asmuo | — |
| `sst_kodas` | `"Juridinis asmuo"` | `2` | — | Juridinis asmuo | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "eil_nr")` | `ref` | `4` | `open` | — | — | — |
| `metai_id` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `metai_id` | `update(property: "metai")` | `property` | `4` | `open` | — | — | — |
| `sklypo_sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `sklypo_sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `dalies_verte_prad` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `dalies_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `tarifas` | `update(ref: "%")` | `ref` | `4` | `open` | — | — | — |
| `lengvatos_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `mokescio_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/zemes_mokestis.csv
