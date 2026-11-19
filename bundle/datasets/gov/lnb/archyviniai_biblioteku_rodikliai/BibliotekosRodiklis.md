---
type: Table
title: "BibliotekosRodiklis — Archyviniai bibliotekų statistikos rodikliai"
description: "Rinkinyje pateikiami pagrindiniai šalies bibliotekų veiklos rezultatai ir rodikliai nuo 2007 iki 2023 metų pagal savivaldybę, rajoną, biblioteką."
resource: "https://get.data.gov.lt/datasets/gov/lnb/archyviniai_biblioteku_rodikliai/BibliotekosRodiklis"
tags: [gov, lnb, bibliotekosrodiklis, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2738/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/archyviniai_biblioteku_rodikliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# BibliotekosRodiklis — Archyviniai bibliotekų statistikos rodikliai

Rinkinyje pateikiami pagrindiniai šalies bibliotekų veiklos rezultatai ir rodikliai nuo 2007 iki 2023 metų pagal savivaldybę, rajoną, biblioteką.[^manifest]

- **Model:** `datasets/gov/lnb/archyviniai_biblioteku_rodikliai/BibliotekosRodiklis`[^manifest]
- **Dataset:** [Archyviniai bibliotekų statistikos rodikliai](../archyviniai_biblioteku_rodikliai.md) (`datasets/gov/lnb/archyviniai_biblioteku_rodikliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/archyviniai_biblioteku_rodikliai/BibliotekosRodiklis` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `4` | `open` | — | Rodiklio statistikos metai | — |
| `biblioteka` | `string` | — | `4` | `open` | — | Bibliotekos pavadinimas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Teritorijos pavadinimas | — |
| `apskritis` | `string` | — | `2` | `open` | — | Apskrities pavadinimas | — |
| `rodiklio_grupe` | `string` | — | `4` | `open` | — | Rodiklio grupė, jungianti kelis rodiklius | — |
| `rodiklio_kodas` | `string` | — | `4` | `open` | — | Rodiklio sutrumpintas kodas | — |
| `rodiklio_aprasymas` | `string` | — | `4` | `open` | — | Rodiklio aprašymas | — |
| `reiksme` | `integer` | — | `4` | `open` | — | Rodiklio reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/archyviniai_biblioteku_rodikliai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/archyviniai_biblioteku_rodikliai (https://data.gov.lt/datasets/2738/)
