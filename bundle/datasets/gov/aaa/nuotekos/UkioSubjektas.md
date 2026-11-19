---
type: Table
title: "UkioSubjektas — Ataskaitą teikiantys subjektai"
description: "Spinta table datasets/gov/aaa/nuotekos/UkioSubjektas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/nuotekos/UkioSubjektas"
tags: [gov, aaa, ukiosubjektas, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1784/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/nuotekos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# UkioSubjektas — Ataskaitą teikiantys subjektai

- **Model:** `datasets/gov/aaa/nuotekos/UkioSubjektas`[^manifest]
- **Dataset:** [Metinių nuotekų tvarkymo apskaitos ataskaitų duomenys](../nuotekos.md) (`datasets/gov/aaa/nuotekos`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/nuotekos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/nuotekos/UkioSubjektas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/nuotekos (https://data.gov.lt/datasets/1784/)
