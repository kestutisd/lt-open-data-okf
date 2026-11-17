---
type: Table
title: "SutarciuSalys — Sutarčių šalys"
description: "Viešųjų pirkimų sutarčių šalys"
resource: "https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/SutarciuSalys"
tags: [gov, nbfc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L56"
    last_modified: "2026-11-11T14:39:20Z"
---

# SutarciuSalys — Sutarčių šalys

Viešųjų pirkimų sutarčių šalys

- **Model:** `datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/SutarciuSalys`[^manifest]
- **Dataset:** [Viešojo sektoriaus sąskaitų administravimo bendroji informacinė sistema](../viesojo_sektoriaus_saskaitos.md) (`datasets/gov/nbfc/viesojo_sektoriaus_saskaitos`)
- **Manifest CSV:** [datasets/gov/nbfc/sabis.csv#L56](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L56)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/SutarciuSalys`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus sutarties šalies identifikatorius | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Sutarties šalies tipas | — |
| `validus_asmens_kodas` | `string` | — | `4` | `open` | — | Sutaties šalies validus šifruotas fizinio asmens kodas | — |
| `validus_jar_kodas` | `string` | — | `4` | `open` | — | Sutaties šalies validus juridinio asmens kodas | — |
| `kitas_kodas` | `string` | — | `4` | `open` | — | Kitas sutaties šalies kodas (ne validus fizinio ar juridinis asmens kodas) | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Sutarties šalies pavadinimas | — |
| `ne_pvm_moketojas` | `boolean` | — | `4` | `open` | — | Požymis ar sutarties šalis PVM mokėtojas | — |
| `veiklos_vieta` | `string` | — | `4` | `open` | — | Suarties šalies veiklos vieta | — |
| `data` | `datetime` | `S` | `4` | `open` | — | Sutarties šalies atnaujinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Tiekėjas"` | — | — | Sutarties tiekėjas | — |
| `tipas` | `"Pirkėjas"` | — | — | Sutarties pirkėjas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv
