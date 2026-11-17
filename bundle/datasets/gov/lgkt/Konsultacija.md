---
type: Table
title: "Konsultacija — Lygių galimybių kontrolierių tarnybos konsultacijos telefonu ar gyvai"
description: "Lygių galimybių tarnybos gyvų ir konsultacijų telefonu registras."
resource: "https://get.data.gov.lt/datasets/gov/lgkt/Konsultacija"
tags: [gov, lgkt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgkt/lgkt_konsultacijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/lgkt_konsultacijos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Konsultacija — Lygių galimybių kontrolierių tarnybos konsultacijos telefonu ar gyvai

Lygių galimybių tarnybos gyvų ir konsultacijų telefonu registras. Gyvų ir konsultacijų telefonu registras dėl lygių galimybių pažeidimų.

- **Model:** `datasets/gov/lgkt/Konsultacija`[^manifest]
- **Dataset:** [Lygių galimybių kontrolierių tarnyba](../lgkt.md) (`datasets/gov/lgkt`)
- **Manifest CSV:** [datasets/gov/lgkt/lgkt_konsultacijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/lgkt_konsultacijos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgkt/Konsultacija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `data` | `date` | `D` | `4` | `open` | — | Konsultacijos data | — |
| `datos_pozymis` | `string` | — | `4` | `open` | — | Tiksli - data nurodyta šaltinyje; Nustatyta - šaltinio metų pirma diena, kai šaltinyje nekorektiška data, arba ji nenurodyta | — |
| `tipas` | `string` | — | `4` | `open` | — | Konsultuoto asmens lytis | — |
| `sritis` | `string` | — | `4` | `open` | — | Lygių galimybių įstatyme nurodyta viena iš penkių sričių | — |
| `pagrindas` | `string` | — | `4` | `open` | — | Lygių galimybių įstatymo numatytas vienas iš keturiolikos pagrindų | — |
| `konsultacijos_budas` | `string` | — | `4` | `open` | — | Konsultacijos būdas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje asmuo gyvena arba įvyko pažeidimo veiksmas. Pildoma nuo 2023 metų | — |
| `saltinis` | `integer` | — | `4` | `open` | — | Duomenų šaltinio metai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgkt/lgkt_konsultacijos.csv
