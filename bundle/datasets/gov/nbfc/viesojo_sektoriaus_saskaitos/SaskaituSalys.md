---
type: Table
title: "SaskaituSalys — Sąskaitų šalys"
description: "Viešojo sektoriaus sąskaitų šalys"
resource: "https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/SaskaituSalys"
tags: [gov, nbfc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L26"
    last_modified: "2026-11-11T14:39:20Z"
---

# SaskaituSalys — Sąskaitų šalys

Viešojo sektoriaus sąskaitų šalys

- **Model:** `datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/SaskaituSalys`[^manifest]
- **Dataset:** [Viešojo sektoriaus sąskaitų administravimo bendroji informacinė sistema](../viesojo_sektoriaus_saskaitos.md) (`datasets/gov/nbfc/viesojo_sektoriaus_saskaitos`)
- **Manifest CSV:** [datasets/gov/nbfc/sabis.csv#L26](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L26)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/SaskaituSalys`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus sąskaitos šalies identifikatorius | — |
| `sf_id` | `string` | — | `4` | `open` | — | Sąskaitos identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Sąskaitos šalies tipas | — |
| `validus_asmens_kodas` | `string` | — | `4` | `open` | — | Sutaties šalies validus šifruotas fizinio asmens kodas | — |
| `validus_jar_kodas` | `string` | — | `4` | `open` | — | Sutaties šalies validus juridinio asmens kodas | — |
| `kitas_kodas` | `string` | — | `4` | `open` | — | Sutaties šalies šifruotas kitas kodas (ne validus fizinio ar juridinis asmens kodas) | — |
| `kitas_kodas_paaiskinimas` | `string` | — | `4` | `open` | — | šifruoto kito kodo paaiškinimas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Pirkėjo/Tiekėjo pavadinimas | — |
| `ne_pvm_moketojas` | `boolean` | — | `4` | `open` | — | Požymis nurodantis ar šalis yra mokesčių mokėtojas | — |
| `veiklos_vieta` | `string` | — | `4` | `open` | — | Sąskaitos šalies veiklos vieta | — |
| `data` | `datetime` | `S` | `4` | `open` | — | Sutarties šalies atnaujinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Tiekėjas"` | — | — | Sąskaitos tiekėjas | — |
| `tipas` | `"Pirkėjas"` | — | — | Sąskaitos pirkėjas | — |
| `tipas` | `"Pristatymo gavėjas"` | — | — | Sąskaitos naudos gavėjas | — |
| `tipas` | `"Mokėjimo gavėjas"` | — | — | Sąskaitos mokėjimo gavėjas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv
