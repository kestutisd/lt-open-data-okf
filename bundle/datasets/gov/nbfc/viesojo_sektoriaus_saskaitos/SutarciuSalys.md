---
type: Table
title: "SutarciuSalys — Sutarčių šalys"
description: "Viešųjų pirkimų sutarčių šalys"
resource: "https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/SutarciuSalys"
tags: [gov, nbfc, sutarciusalys, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L56"
    title: "atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv#L56"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3924/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nbfc/viesojo_sektoriaus_saskaitos"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# SutarciuSalys — Sutarčių šalys

Viešųjų pirkimų sutarčių šalys[^manifest]

- **Model:** `datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/SutarciuSalys`[^manifest]
- **Dataset:** [Viešojo sektoriaus sąskaitų administravimo bendroji informacinė sistema](../viesojo_sektoriaus_saskaitos.md) (`datasets/gov/nbfc/viesojo_sektoriaus_saskaitos`)[^manifest]
- **Manifest CSV:** [datasets/gov/nbfc/sabis.csv#L56](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L56)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/SutarciuSalys` (`deployed`)[^manifest]
- **Provider:** `nbfc` — Nacionalinis bendrųjų funkcijų centras *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Tiekėjas"` | — | — | Sutarties tiekėjas | — |
| `tipas` | `"Pirkėjas"` | — | — | Sutarties pirkėjas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv#L56 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L56)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nbfc/viesojo_sektoriaus_saskaitos (https://data.gov.lt/datasets/3924/)
