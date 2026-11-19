---
type: Table
title: "CovidPoveikisAkvakultura — Lietuvos žuvininkystės sektoriaus 2014–2020 metų veiksmų programos priemonės „Visuomenės sveikatai skirtos priemonės“ veiklos sritis „COVID-19 protrūkio neigiamo poveikio akvakultūrai mažinimas“"
description: "Spinta table datasets/gov/nma/covid_poveikis_akvakulturai/CovidPoveikisAkvakultura (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/covid_poveikis_akvakulturai/CovidPoveikisAkvakultura"
tags: [gov, nma, covidpoveikisakvakultura, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/covid_poveikis_akvakulturai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/nma/covid_poveikis_akvakulturai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2302/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nma/covid_poveikis_akvakulturai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# CovidPoveikisAkvakultura — Lietuvos žuvininkystės sektoriaus 2014–2020 metų veiksmų programos priemonės „Visuomenės sveikatai skirtos...

- **Model:** `datasets/gov/nma/covid_poveikis_akvakulturai/CovidPoveikisAkvakultura`[^manifest]
- **Dataset:** [Lietuvos žuvininkystės sektoriaus 2014–2020 metų veiksmų programos priemonės „Visuomenės...](../covid_poveikis_akvakulturai.md) (`datasets/gov/nma/covid_poveikis_akvakulturai`)[^manifest]
- **Manifest CSV:** [datasets/gov/nma/covid_poveikis_akvakulturai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/covid_poveikis_akvakulturai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/covid_poveikis_akvakulturai/CovidPoveikisAkvakultura` (`deployed`)[^manifest]
- **Provider:** `nma` — Nacionalinė mokėjimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `3` | `open` | — | Priemonės pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `rajonas` | `string` | — | `3` | `open` | — | Rajonas | — |
| `suma_eur` | `number` | — | `2` | `open` | — | Išmokėta suma | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma_eur` | `update(type: "money, ref: "EUR")"` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/covid_poveikis_akvakulturai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/covid_poveikis_akvakulturai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nma/covid_poveikis_akvakulturai (https://data.gov.lt/datasets/2302/)
