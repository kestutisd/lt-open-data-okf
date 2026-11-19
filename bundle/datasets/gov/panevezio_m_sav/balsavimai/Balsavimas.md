---
type: Table
title: "Balsavimas — Panevėžio miesto tarybos narių asmeniniai balsavimų rezultatai"
description: "Lentelėje pateikiami Panevėžio miesto tarybos narių asmeniniai balsavimai dėl Tarybos posėdžiuose teikiamų klausimų."
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai/Balsavimas"
tags: [gov, panevezio_m_sav, balsavimas, deployed, level-4, cadence-annual_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2715/"
    title: "data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/balsavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Balsavimas — Panevėžio miesto tarybos narių asmeniniai balsavimų rezultatai

Lentelėje pateikiami Panevėžio miesto tarybos narių asmeniniai balsavimai dėl Tarybos posėdžiuose teikiamų klausimų. Lentelės objektas - Tarybos nario balsavimo duomenys individualiam klausimui. Duomenys apima laikotarpį nuo 2023m. balandžio iki šių dienų.[^manifest]

- **Model:** `datasets/gov/panevezio_m_sav/balsavimai/Balsavimas`[^manifest]
- **Dataset:** [Panevėžio miesto tarybos posėdžių balsavimų rezultatai](../balsavimai.md) (`datasets/gov/panevezio_m_sav/balsavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/balsavimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai/Balsavimas` (`deployed`)[^manifest]
- **Provider:** `panevezio_m_sav` — Panevėžio miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_3`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `sesijos_id` | `ref` | [Sesija](Sesija.md) (`level=4 UUID` via `Sesija[sesijos_id]`: `sesijos_id._id`) | `4` | `open` | — | Balsavimo sesijos identifikacinis numeris | — |
| `balsavimo_laikas` | `datetime` | `L` | `4` | `open` | — | Balsavimo laiko žyma | — |
| `delegato_id` | `string` | — | `4` | `open` | — | Delegato identifikacinis numeris | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Tarybos nario vardas ir pavardė | — |
| `ar_dalyvavo` | `boolean` | — | `4` | `open` | — | Požymis, ar Tarybos narys dalyvavo balsavime | — |
| `uz` | `number` | `U` | `4` | `open` | — | Požymis, ar balsavo už (1 - taip, 0 - ne) | — |
| `pries` | `number` | `U` | `4` | `open` | — | Požymis, ar balsavo prieš (1 - taip, 0 - ne) | — |
| `susilaike` | `number` | `U` | `4` | `open` | — | Požymis, ar balsavimo metu susilaikė (1 - taip, 0 - ne) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/balsavimai (https://data.gov.lt/datasets/2715/)
