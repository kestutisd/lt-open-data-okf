---
type: Table
title: "LovosProfilis — Lovų profiliai"
description: "Pagal asmens sveikatos priežiūros įstaigą, lovų specialybės grupes, savivaldybes"
resource: "https://get.data.gov.lt/datasets/gov/hi/lovos/LovosProfilis"
tags: [gov, hi, lovosprofilis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L13"
    title: "atviriduomenys/manifest — datasets/gov/hi/lovos.csv#L13"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1230/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/lovos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# LovosProfilis — Lovų profiliai

**Dataset Context:** Pagal asmens sveikatos priežiūros įstaigą, lovų specialybės grupes, savivaldybes[^manifest]

- **Model:** `datasets/gov/hi/lovos/LovosProfilis`[^manifest]
- **Dataset:** [Stacionaro lovų skaičius ir jų veiklos rodikliai](../lovos.md) (`datasets/gov/hi/lovos`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/lovos.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L13)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/lovos/LovosProfilis` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `prof_kod`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prof_kod` | `string` | — | `4` | `open` | — | Lovos profillo kodas | — |
| `grupes_kodas` | `string` | — | `4` | `open` | — | Lovos profilio grupės kodas | — |
| `prof_pavadinimas` | `string` | — | `4` | `open` | — | Lovos profilio pavadinimas | — |
| `grupes_pavadinimas` | `string` | — | `4` | `open` | — | Lovos profilio grupės pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/lovos.csv#L13 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L13)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/lovos (https://data.gov.lt/datasets/1230/)
