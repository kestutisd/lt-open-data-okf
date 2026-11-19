---
type: Dataset
title: "Vilniaus miesto savivaldybės teisės aktų registras"
description: "Rinkinyje skelbiami Vilniaus miesto savivaldybės mero, tarybos, administracijos ir seniūnų paskelbti teisės aktų objektai: įsakymai, sprendimai, potvarkiai, projektai ir įsakai."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai"
tags: [gov, vilniaus_m_sav, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3857/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/aktai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vilniaus miesto savivaldybės teisės aktų registras

Rinkinyje skelbiami Vilniaus miesto savivaldybės mero, tarybos, administracijos ir seniūnų paskelbti teisės aktų objektai: įsakymai, sprendimai, potvarkiai, projektai ir įsakai. Duomenys apima laikotarpį nuo 1990 m. Rinkinio objektas – vienas dokumentas. Rinkinyje kaupiami istoriniai duomenys, todėl įtraukti ir nustoję galioti teisės aktai. Skelbiami šie teisės aktų požymiai: pavadinimas, paskelbimo data, potvarkio numeris, aktą paskelbęs savivaldybės subjektas ir akto statusas. Vartotojai taip pat gali analizuoti paskelbtų teisės aktų tarpusavio ryšius – kurie dokumentai susiję, keičia ar yra priedai kitiems teisės aktams (žr. modelį Jungimas). Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vilniaus_m_sav/aktai`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/aktai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3857/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai`[^dcat]
- **Portal Title (`@lt`):** Vilniaus miesto savivaldybės teisės aktų registras[^dcat]
- **Portal Title (`@en`):** Vilnius City Municipality Register of Legal Acts[^dcat]
- **Issued (`dct:issued`):** `2025-11-19`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2025-07-01` .. `2026-09-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

The package publishes legal objects published by the mayor, council, administration and elders of Vilnius City Municipality: orders, decisions, ordinances, drafts and orders. The data shall cover the period from 1990. The object of the sample shall be one document. The collection collects historical data and therefore includes legislation that has expired. The following features of legal acts shall be published: the name, the date of publication, the number of the ordinance, the municipal entity which issued the act and the status of the act. Consumers can also analyse the relationship between published legislation – which documents are related, whether or not there are annexes to other legislation (see the Merger model). Data provider – Vilnius City Municipality Administration. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dokumentas](aktai/Dokumentas.md) | Vilniaus miesto savivaldybės teisės aktai | `4` | `dokumento_id` | — | `8` | — |
| [Jungimas](aktai/Jungimas.md) | Vilniaus miesto savivaldybės teisės aktų tarpusavio sąryšiai | `4` | `rysio_id` | — | `4` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/aktai (https://data.gov.lt/datasets/3857/)
