---
type: Table
title: "PirkimuZurnalas — Varėnos globos namų 2023 metų viešųjų pirkimų žurnalas"
description: "2023 m. biudžetiniais metais atliktų pirkimų registracijos žurnalas"
resource: "https://get.data.gov.lt/datasets/gov/vgn/viesieji_pirkimai/PirkimuZurnalas"
tags: [gov, vgn, pirkimuzurnalas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgn/viesieji_pirkimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vgn/viesieji_pirkimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2750/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vgn/viesieji_pirkimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PirkimuZurnalas — Varėnos globos namų 2023 metų viešųjų pirkimų žurnalas

2023 m. biudžetiniais metais atliktų pirkimų registracijos žurnalas[^manifest]

- **Model:** `datasets/gov/vgn/viesieji_pirkimai/PirkimuZurnalas`[^manifest]
- **Dataset:** [Varėnos globos namų 2023 metų viešųjų pirkimų žurnalas](../viesieji_pirkimai.md) (`datasets/gov/vgn/viesieji_pirkimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vgn/viesieji_pirkimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgn/viesieji_pirkimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgn/viesieji_pirkimai/PirkimuZurnalas` (`deployed`)[^manifest]
- **Provider:** `vgn` — Varėnos globos namai *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `data` | `date` | `D` | `4` | `open` | — | Data | — |
| `numatoma_sutarties_verte_eur` | `number` | — | `4` | `open` | — | Sutarties vertė arba paslaugos kaina, Eur | — |
| `pirkimo_budas` | `string` | — | `4` | `open` | — | Apklausa žodžiu ar raštu | — |
| `ar_paslauga` | `string` | — | `4` | `open` | — | Požymis, ar paslauga | — |
| `objekto_kodas` | `string` | — | `4` | `open` | — | Objekto kodas, nurodytas BVPŽ (Bendrasis Viešųjų Pirkimų Žodynas) sąraše | — |
| `pirkimo_objektas` | `string` | — | `4` | `open` | — | Viešojo pirkimo objektas ir sudarytos sutarties numeris | — |
| `sutarties_trukme` | `string` | — | `4` | `open` | — | Vienkartinė sutartis ar terminuota sutartis | — |
| `tiekejas` | `string` | — | `4` | `open` | — | Tiekėjo pavadinimas, įmonės kodas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ar_paslauga` | `"paslauga"` | — | — | paslauga | — |
| `ar_paslauga` | `"pratęsimas"` | — | — | pratęsimas | — |

# Related References

- [BVPŽ / CPV Procurement Vocabulary (Reg. (EC) No 213/2008)](../../../../references/cpv-bvpz-kodai.md) — 45 2-digit CPV divisions (`03`–`98`) and 272 3-digit groups.

[^manifest]: atviriduomenys/manifest — datasets/gov/vgn/viesieji_pirkimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgn/viesieji_pirkimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vgn/viesieji_pirkimai (https://data.gov.lt/datasets/2750/)
