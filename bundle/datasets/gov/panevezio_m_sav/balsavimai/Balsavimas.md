---
type: Table
title: "Balsavimas — Panevėžio miesto tarybos narių asmeniniai balsavimų rezultatai"
description: "Lentelėje pateikiami Panevėžio miesto tarybos narių asmeniniai balsavimai dėl Tarybos posėdžiuose teikiamų klausimų."
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai/Balsavimas"
tags: [gov, panevezio_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Balsavimas — Panevėžio miesto tarybos narių asmeniniai balsavimų rezultatai

Lentelėje pateikiami Panevėžio miesto tarybos narių asmeniniai balsavimai dėl Tarybos posėdžiuose teikiamų klausimų. Lentelės objektas - Tarybos nario balsavimo duomenys individualiam klausimui. Duomenys apima laikotarpį nuo 2023m. balandžio iki šių dienų.

- **Model:** `datasets/gov/panevezio_m_sav/balsavimai/Balsavimas`[^manifest]
- **Dataset:** [Panevėžio miesto tarybos posėdžių balsavimų rezultatai](../balsavimai.md) (`datasets/gov/panevezio_m_sav/balsavimai`)
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/balsavimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai/Balsavimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `sesijos_id` | `ref` | [Sesija[sesijos_id]](Sesija.md) | `4` | `open` | — | Balsavimo sesijos identifikacinis numeris | — |
| `balsavimo_laikas` | `datetime` | `L` | `4` | `open` | — | Balsavimo laiko žyma | — |
| `delegato_id` | `string` | — | `4` | `open` | — | Delegato identifikacinis numeris | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Tarybos nario vardas ir pavardė | — |
| `ar_dalyvavo` | `boolean` | — | `4` | `open` | — | Požymis, ar Tarybos narys dalyvavo balsavime | — |
| `uz` | `number` | `U` | `4` | `open` | — | Požymis, ar balsavo už (1 - taip, 0 - ne) | — |
| `pries` | `number` | `U` | `4` | `open` | — | Požymis, ar balsavo prieš (1 - taip, 0 - ne) | — |
| `susilaike` | `number` | `U` | `4` | `open` | — | Požymis, ar balsavimo metu susilaikė (1 - taip, 0 - ne) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv
