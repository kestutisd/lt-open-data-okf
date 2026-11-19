---
type: Dataset
title: "Vilniaus miesto tarybos balsavimai"
description: "Rinkinyje pateikiama informacija apie Vilniaus miesto tarybos posėdžiuose svarstytus klausimus ir balsavimus."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai"
tags: [gov, vilniaus_m_sav, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3849/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/balsavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vilniaus miesto tarybos balsavimai

Rinkinyje pateikiama informacija apie Vilniaus miesto tarybos posėdžiuose svarstytus klausimus ir balsavimus. Rinkinį sudaro dvi pagrindinės lentelės: viena reprezentuoja posėdžių ir klausimų informaciją su apibendrintais balsavimo duomenimis, kita – detalius kiekvieno tarybos nario balsus dėl individualaus klausimo. Rinkinyje pateikiami duomenys apie įvykusį posėdį (laiko žyma, posėdžio pirmininkas ir sekretorius), balsavimus (iškeltas klausimas, svarstymo tvarka, balsavimo rezultatai) ir priimtus sprendimus. Pažymėtina, jog abi rinkinio lentelės siejasi tarpusavyje per lauką "balsavimo_id".[^manifest]

- **Namespace:** `datasets/gov/vilniaus_m_sav/balsavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/balsavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3849/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai`[^dcat]
- **Portal Title (`@lt`):** Vilniaus miesto tarybos balsavimai[^dcat]
- **Portal Title (`@en`):** Votes of Vilnius City Council[^dcat]
- **Issued (`dct:issued`):** `2025-06-06`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2025-06-06` .. `2026-09-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiama informacija apie Vilniaus miesto tarybos posėdžiuose svarstytus klausimus ir balsavimus. Rinkinį sudaro dvi pagrindinės lentelės: viena reprezentuoja posėdžių ir klausimų informaciją su apibendrintais balsavimo duomenimis, kita – detalius kiekvieno tarybos nario balsus dėl individualaus klausimo. Rinkinyje pateikiami duomenys apie įvykusį posėdį (laiko žyma, posėdžio pirmininkas ir sekretorius), balsavimus (iškeltas klausimas, svarstymo tvarka, balsavimo rezultatai) ir priimtus sprendimus. Pažymėtina, kad abi rinkinio lentelės tarpusavyje siejasi per lauką „balsavimo_id“. Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains information on issues and votes discussed at Vilnius City Council meetings. The package consists of two main tables, one representing meeting and question information with aggregated voting data and the other representing detailed votes of each councillor on an individual issue. The package shall include data on the meeting held (time stamp, chairman and secretary of the meeting), votes (raised issue, procedure of consideration, results of votes) and decisions taken. It should be noted that the two tables in the set relate to each other through the “voting _id” field. Data provider: Vilnius City Municipality Administration. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Klausimas](balsavimai/Klausimas.md) | Vilniaus miesto tarybos posėdžių duomenys ir apibendrinti rezultatai | `4` | `vda_id` | — | `17` | — |
| [Balsas](balsavimai/Balsas.md) | Vilniaus miesto tarybos narių individualūs balsavimų duomenys | `4` | `vda_id` | — | `5` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/balsavimai (https://data.gov.lt/datasets/3849/)
