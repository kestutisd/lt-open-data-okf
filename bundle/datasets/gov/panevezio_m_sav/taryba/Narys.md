---
type: Table
title: "Narys — Rinkinyje pateikiamas buvusių ir esamų Panevėžio miesto tarybos narių sąrašas. Duomenys apima laikotarpį nuo 2007m. iki šių dienų."
description: "Rinkinyje pateikiamas buvusių ir esamų Panevėžio miesto tarybos narių sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/taryba/Narys"
tags: [gov, panevezio_m_sav, narys, deployed, level-4, cadence-annual_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/tarybos_nariai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/tarybos_nariai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2716/"
    title: "data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/taryba"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Narys — Rinkinyje pateikiamas buvusių ir esamų Panevėžio miesto tarybos narių sąrašas. Duomenys apima laikotarpį nuo 2007m. iki šių dienų.

**Dataset Context:** Rinkinyje pateikiamas buvusių ir esamų Panevėžio miesto tarybos narių sąrašas. Duomenys apima laikotarpį nuo 2007m. iki šių dienų.[^manifest]

- **Model:** `datasets/gov/panevezio_m_sav/taryba/Narys`[^manifest]
- **Dataset:** [Panevėžio miesto tarybos narių sąrašas](../taryba.md) (`datasets/gov/panevezio_m_sav/taryba`)[^manifest]
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/tarybos_nariai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/tarybos_nariai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/taryba/Narys` (`deployed`)[^manifest]
- **Provider:** `panevezio_m_sav` — Panevėžio miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `delegato_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_3`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `delegato_id` | `string` | — | `4` | `open` | — | Tarybos nario identifikacinis numeris | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Tarybos nario vardas ir pavardė | — |
| `pareigos` | `string` | — | `4` | `open` | — | Tarybos nario pareigos | — |
| `ar_aktyvus` | `boolean` | — | `4` | `open` | — | Požymis, ar Tarybos narys eina pareigas einamosios kadencijos metu | — |
| `duomenu_sviezumas` | `date` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/tarybos_nariai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/tarybos_nariai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/taryba (https://data.gov.lt/datasets/2716/)
