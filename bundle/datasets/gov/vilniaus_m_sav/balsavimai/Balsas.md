---
type: Table
title: "Balsas — Vilniaus miesto tarybos narių individualūs balsavimų duomenys"
description: "Rinkinyje pateikiama informacija apie Vilniaus miesto tarybos posėdžiuose svarstytus klausimus ir balsavimus."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai/Balsas"
tags: [gov, vilniaus_m_sav, balsas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L36"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv#L36"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3849/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/balsavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Balsas — Vilniaus miesto tarybos narių individualūs balsavimų duomenys

**Dataset Context:** Rinkinyje pateikiama informacija apie Vilniaus miesto tarybos posėdžiuose svarstytus klausimus ir balsavimus. Rinkinį sudaro dvi pagrindinės lentelės: viena reprezentuoja posėdžių ir klausimų informaciją su apibendrintais balsavimo duomenimis, kita – detalius kiekvieno tarybos nario balsus dėl individualaus klausimo. Rinkinyje pateikiami duomenys apie įvykusį posėdį (laiko žyma, posėdžio pirmininkas ir sekretorius), balsavimus (iškeltas klausimas, svarstymo tvarka, balsavimo rezultatai) ir priimtus sprendimus. Pažymėtina, jog abi rinkinio lentelės siejasi tarpusavyje per lauką "balsavimo_id".[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/balsavimai/Balsas`[^manifest]
- **Dataset:** [Vilniaus miesto tarybos balsavimai](../balsavimai.md) (`datasets/gov/vilniaus_m_sav/balsavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/balsavimai.csv#L36](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L36)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai/Balsas` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `balsavimo_id` | `string` | — | `4` | `open` | — | Balsavimo identifikacinis numeris | — |
| `balsavimo_laikas` | `datetime` | `S` | `4` | `open` | — | Balsavimo laiko žyma | — |
| `narys` | `string` | — | `4` | `open` | — | Tarybos narys, dalyvavęs balsavime | — |
| `balsas` | `string` | — | `4` | `open` | — | Tarybos nario atiduotas balsavimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv#L36 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L36)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/balsavimai (https://data.gov.lt/datasets/3849/)
