---
type: Table
title: "Sutartys — Sutartys"
description: "Viešųjų pirkimų sutarčių informacija"
resource: "https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/Sutartys"
tags: [gov, nbfc, sutartys, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L43"
    title: "atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv#L43"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3924/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nbfc/viesojo_sektoriaus_saskaitos"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Sutartys — Sutartys

Viešųjų pirkimų sutarčių informacija[^manifest]

- **Model:** `datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/Sutartys`[^manifest]
- **Dataset:** [Viešojo sektoriaus sąskaitų administravimo bendroji informacinė sistema](../viesojo_sektoriaus_saskaitos.md) (`datasets/gov/nbfc/viesojo_sektoriaus_saskaitos`)[^manifest]
- **Manifest CSV:** [datasets/gov/nbfc/sabis.csv#L43](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L43)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/Sutartys` (`deployed`)[^manifest]
- **Provider:** `nbfc` — Nacionalinis bendrųjų funkcijų centras *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikatorius | — |
| `sutarties_uid` | `string` | — | `4` | `open` | — | Unikalus sutarties identifikatorius | — |
| `vp_id` | `string` | — | `4` | `open` | — | Viešųjų pirkimų sutarties identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Sutarties tipas | — |
| `sutarties_numeris` | `string` | — | `4` | `open` | — | Viešųjų pirkimų sutarties numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Sutarties pavadinimas | — |
| `cpv_kodas` | `string` | — | `4` | `open` | — | Sutarties Bendrąjį Viešųjų Pirkimų Žodyno kodas | — |
| `cpv_pav` | `string` | — | `4` | `open` | — | Sutarties Bendrąjį Viešųjų Pirkimų Žodyno kodo pavadinimas | — |
| `sutarties_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Sutarties įsigaliojimo data | — |
| `sutarties_galiojimo_data` | `date` | `D` | `4` | `open` | — | Sutarties galiojima data | — |
| `suma` | `number` | — | `4` | `open` | — | Sutarties suma eurais | — |

# Related References

- [BVPŽ / CPV Procurement Vocabulary (Reg. (EC) No 213/2008)](../../../../references/cpv-bvpz-kodai.md) — 45 2-digit CPV divisions (`03`–`98`) and 272 3-digit groups.

[^manifest]: atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv#L43 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L43)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nbfc/viesojo_sektoriaus_saskaitos (https://data.gov.lt/datasets/3924/)
