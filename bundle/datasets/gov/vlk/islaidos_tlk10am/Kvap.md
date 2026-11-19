---
type: Table
title: "Kvap — PSDF biudžeto išlaidos vaistams ir MPP pagal TLK-10-AM kodus"
description: "Informacija apie PSDF biudžeto išlaidas vaistams ir MPP pagal TLK-10-AM kodus"
resource: "https://get.data.gov.lt/datasets/gov/vlk/islaidos_tlk10am/Kvap"
tags: [gov, vlk, kvap, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/islaidos_tlk10am.csv#L44"
    title: "atviriduomenys/manifest — datasets/gov/vlk/islaidos_tlk10am.csv#L44"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1585/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/islaidos_tlk10am"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Kvap — PSDF biudžeto išlaidos vaistams ir MPP pagal TLK-10-AM kodus

Informacija apie PSDF biudžeto išlaidas vaistams ir MPP pagal TLK-10-AM kodus[^manifest]

- **Model:** `datasets/gov/vlk/islaidos_tlk10am/Kvap`[^manifest]
- **Dataset:** [PSDF biudžeto išlaidos asmens sveikatos priežiūros paslaugoms, vaistams ir MPP pagal TLK-10-AM kodus](../islaidos_tlk10am.md) (`datasets/gov/vlk/islaidos_tlk10am`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/islaidos_tlk10am.csv#L44](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/islaidos_tlk10am.csv#L44)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/islaidos_tlk10am/Kvap` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `data` | `date` | `M` | `4` | `open` | — | Data | Ataskaitinio laikotarpio data mėnesio tikslumu |
| `tlk10am` | `ref` | [Tlk10am](../tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[code]`: `tlk10am._id`) | `4` | `open` | — | Diagnozės kodas | Diagnozės kodas pagal tarptautinę statistinę ligų ir sveikatos sutrikimų klasifikaciją, dešimtąjį leidimą, Australijos modifikaciją (TLK-10-AM) |
| `islaidos` | `number` | — | `2` | `open` | — | PSDF biudžeto išlaidos eurais | — |
| `priemokos` | `number` | — | `2` | `open` | — | Priemokų suma eurais | — |
| `padeng_priemoka` | `number` | — | `2` | `open` | — | Padengiama priemokų suma eurais | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `islaidos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `priemokos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `padeng_priemoka` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/islaidos_tlk10am.csv#L44 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/islaidos_tlk10am.csv#L44)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/islaidos_tlk10am (https://data.gov.lt/datasets/1585/)
