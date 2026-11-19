---
type: Table
title: "KitiVeiklosRezultatai — Valstybės kontrolės vertinimų rezultatai"
description: "Valstybės kontrolės vertinimų (ne auditų) rezultatai"
resource: "https://get.data.gov.lt/datasets/gov/vk/kiti_rezultatai/KitiVeiklosRezultatai"
tags: [gov, vk, kitiveiklosrezultatai, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/kitirezultatai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vk/kitirezultatai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1692/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/kiti_rezultatai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# KitiVeiklosRezultatai — Valstybės kontrolės vertinimų rezultatai

Valstybės kontrolės vertinimų (ne auditų) rezultatai[^manifest]

- **Model:** `datasets/gov/vk/kiti_rezultatai/KitiVeiklosRezultatai`[^manifest]
- **Dataset:** [Valstybės kontrolės vertinimų rezultatai](../kiti_rezultatai.md) (`datasets/gov/vk/kiti_rezultatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vk/kitirezultatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/kitirezultatai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/kiti_rezultatai/KitiVeiklosRezultatai` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `audit_cardid` | `integer` | — | `3` | `open` | — | Produkto ID | Vertinimo (ne audito) identifikacijos numeris |
| `vertinimo_pavadinimas` | `string` | — | `3` | `open` | — | Produkto pavadinimas | Vertinimo (ne audito) pavadinimas |
| `registravimo_data` | `date` | `D` | `4` | `open` | — | Registracijos data | Dokumento registracijos dokumentų valdymo posistemyje data |
| `failo_url` | `url` | — | `4` | `open` | — | Nuoroda į produkto dokumentą | Vertinimo (ne audito) dokumentas |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/kitirezultatai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/kitirezultatai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/kiti_rezultatai (https://data.gov.lt/datasets/1692/)
