---
type: Table
title: "Sesija — Panevėžio miesto tarybos posėdžių balsavimų rezultatai"
description: "Lentelėje pateikiami agreguoti Panevėžio miesto tarybos narių balsavimų rezultatai dėl posėdžių metu iškeltų klausimų nuo 2023m. iki šių dienų."
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai/Sesija"
tags: [gov, panevezio_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L17"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sesija — Panevėžio miesto tarybos posėdžių balsavimų rezultatai

Lentelėje pateikiami agreguoti Panevėžio miesto tarybos narių balsavimų rezultatai dėl posėdžių metu iškeltų klausimų nuo 2023m. iki šių dienų. Lentelės objektas - klausimas, dėl kurio posėdžio metu įvyko balsavimas. Pateikiami agreguoti balsavimų rezultatai: tarybos narių, balsavusių už, prieš ir susilaikiusių, skaičius; taip pat nurodoma, ar balsavimo metu susidarė kvorumas ir ar pasiūlymas buvo priimtas.

- **Model:** `datasets/gov/panevezio_m_sav/balsavimai/Sesija`[^manifest]
- **Dataset:** [Panevėžio miesto tarybos posėdžių balsavimų rezultatai](../balsavimai.md) (`datasets/gov/panevezio_m_sav/balsavimai`)
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/balsavimai.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L17)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai/Sesija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv
