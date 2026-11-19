---
type: Table
title: "Sesija — Panevėžio miesto tarybos posėdžių balsavimų rezultatai"
description: "Lentelėje pateikiami agreguoti Panevėžio miesto tarybos narių balsavimų rezultatai dėl posėdžių metu iškeltų klausimų nuo 2023m."
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai/Sesija"
tags: [gov, panevezio_m_sav, sesija, deployed, level-4, cadence-annual_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L17"
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv#L17"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2715/"
    title: "data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/balsavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sesija — Panevėžio miesto tarybos posėdžių balsavimų rezultatai

Lentelėje pateikiami agreguoti Panevėžio miesto tarybos narių balsavimų rezultatai dėl posėdžių metu iškeltų klausimų nuo 2023m. iki šių dienų. Lentelės objektas - klausimas, dėl kurio posėdžio metu įvyko balsavimas. Pateikiami agreguoti balsavimų rezultatai: tarybos narių, balsavusių už, prieš ir susilaikiusių, skaičius; taip pat nurodoma, ar balsavimo metu susidarė kvorumas ir ar pasiūlymas buvo priimtas.[^manifest]

- **Model:** `datasets/gov/panevezio_m_sav/balsavimai/Sesija`[^manifest]
- **Dataset:** [Panevėžio miesto tarybos posėdžių balsavimų rezultatai](../balsavimai.md) (`datasets/gov/panevezio_m_sav/balsavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/balsavimai.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L17)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai/Sesija` (`deployed`)[^manifest]
- **Provider:** `panevezio_m_sav` — Panevėžio miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_3`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `sesijos_id` | `string` | — | `4` | `open` | — | Balsavimo sesijos identifikacinis numeris | — |
| `agenda_id` | `string` | — | `4` | `open` | — | Klausimo identifikacinis numeris | — |
| `klausimas_lt` | `string` | — | `4` | `open` | — | Balsavimo klausimas | — |
| `aprasymas_lt` | `string` | — | — | — | — | Aprašymas | — |
| `laikas` | `datetime` | `L` | `4` | `open` | — | Balsavimo laiko žyma | — |
| `tarybos_sk` | `number` | `U` | `4` | `open` | — | Tarybos narių skaičius | — |
| `viso_dalyvavo` | `number` | `U` | `4` | `open` | — | Iš viso dalyvavusių tarybos narių posėdyje skaičius | — |
| `viso_uz` | `number` | `U` | `4` | `open` | — | Viso balsavusių už skaičius | — |
| `viso_susilaike` | `number` | `U` | `4` | `open` | — | Viso susilaikiusių balsavime skaičius | — |
| `viso_pries` | `number` | `U` | `4` | `open` | — | Viso balsavusių prieš skaičius | — |
| `viso_balsu` | `number` | `U` | `4` | `open` | — | Viso balsavusių skaičius | — |
| `ar_kvorumas` | `boolean` | — | `4` | `open` | — | Požymis, ar balsavime dėl iškelto klausimas pasiektas kvorumas | — |
| `ar_priimtas` | `boolean` | — | `4` | `open` | — | Požymis, ar pasiūlymui pritarta. | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `klausimas_lt` | `"update(property: ""klausimas[]"", type: ""array"", source: ""Klausimas"")"` | `property` | `4` | — | — | — | — |
| `aprasymas_lt` | `"update(property: ""aprasymas[]"", type: ""array"", source: ""Aprasymas"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv#L17 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L17)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/balsavimai (https://data.gov.lt/datasets/2715/)
