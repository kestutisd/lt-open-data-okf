---
type: Table
title: "Kvap — PSDF biudžeto išlaidos vaistams ir MPP pagal TLK-10-AM kodus"
description: "Informacija apie PSDF biudžeto išlaidas vaistams ir MPP pagal TLK-10-AM kodus"
resource: "https://get.data.gov.lt/datasets/gov/vlk/islaidos_tlk10am/Kvap"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/islaidos_tlk10am.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/islaidos_tlk10am.csv#L44"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kvap — PSDF biudžeto išlaidos vaistams ir MPP pagal TLK-10-AM kodus

Informacija apie PSDF biudžeto išlaidas vaistams ir MPP pagal TLK-10-AM kodus

- **Model:** `datasets/gov/vlk/islaidos_tlk10am/Kvap`[^manifest]
- **Dataset:** [datasets/gov/vlk/islaidos_tlk10am](../islaidos_tlk10am.md) (`datasets/gov/vlk/islaidos_tlk10am`)
- **Manifest CSV:** [datasets/gov/vlk/islaidos_tlk10am.csv#L44](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/islaidos_tlk10am.csv#L44)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/islaidos_tlk10am/Kvap`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `data` | `date` | `M` | `4` | `open` | — | Data | Ataskaitinio laikotarpio data mėnesio tikslumu |
| `tlk10am` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[code]](../tlk10am/Tlk10am.md) | `4` | `open` | — | Diagnozės kodas | Diagnozės kodas pagal tarptautinę statistinę ligų ir sveikatos sutrikimų klasifikaciją, dešimtąjį leidimą, Australijos modifikaciją (TLK-10-AM) |
| `islaidos` | `number` | — | `2` | `open` | — | PSDF biudžeto išlaidos eurais | — |
| `priemokos` | `number` | — | `2` | `open` | — | Priemokų suma eurais | — |
| `padeng_priemoka` | `number` | — | `2` | `open` | — | Padengiama priemokų suma eurais | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `islaidos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `priemokos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `padeng_priemoka` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/islaidos_tlk10am.csv
