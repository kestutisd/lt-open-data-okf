---
type: Table
title: "UkioSubjektas — Ataskaitą teikiantys subjektai"
description: "Spinta table datasets/gov/aaa/nuotekos/UkioSubjektas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/nuotekos/UkioSubjektas"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# UkioSubjektas — Ataskaitą teikiantys subjektai

- **Model:** `datasets/gov/aaa/nuotekos/UkioSubjektas`[^manifest]
- **Dataset:** [datasets/gov/aaa/nuotekos](../nuotekos.md) (`datasets/gov/aaa/nuotekos`)
- **Manifest CSV:** [datasets/gov/aaa/nuotekos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/nuotekos/UkioSubjektas`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_atsisk_data_nuo` | `integer` | — | `2` | `open` | — | Data, už kurią yra teikiamas dokumentas. | — |
| `usb_aob_id` | `string` | — | `4` | `open` | — | Ūkio subjekto id | — |
| `usb_aob_pavad` | `string` | — | `2` | `open` | — | Ūkio subjekto (USB) pavadinimas | — |
| `usb_aob_kodas` | `string` | — | `3` | `open` | — | Ūkio subjekto (USB) kodas | — |
| `usb_ja_kodas` | `string` | — | `2` | `open` | — | Ūkio subjekto juridinio asmens kodas | — |
| `aob_gis_taskas` | `geometry(point, 3346)` | — | `2` | `open` | — | Ūkio subjekto (USB) koordinatės | — |
| `adr_sav_pavad` | `string` | — | `2` | `open` | — | Ūkio subjekto (USB) adreso savivaldybės pavadinimas | — |
| `aob_aob_id_prikl` | `string` | — | `4` | `open` | — | Priklausomumo objektui id | — |
| `uvo_aob_pavad` | `string` | — | `2` | `open` | — | Ūkinės veiklos objekto (UVO) pavadinimas | — |
| `uvo_aob_kodas` | `string` | — | `3` | `open` | — | Ūkinės veiklos objekto (UVO) kodas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_atsisk_data_nuo` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv
