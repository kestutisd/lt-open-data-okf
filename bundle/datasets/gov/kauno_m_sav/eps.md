---
type: Dataset
title: "Kauno m. sav. Elektronine paslaugų sistema besinaudojančios įmonės"
description: "Kauno miesto savivaldybės valdoma Elektroninių paslaugų sistema (EPS) saugo Kauno m. sav."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/eps"
tags: [gov, kauno_m_sav, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/eps.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/eps.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2741/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/eps"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kauno m. sav. Elektronine paslaugų sistema besinaudojančios įmonės

- **Namespace:** `datasets/gov/kauno_m_sav/eps`[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/eps.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/eps.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/eps` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2741/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/eps`[^dcat]
- **Portal Title (`@lt`):** Kauno miesto savivaldybėje elektronine paslaugų sistema besinaudojančios įmonės[^dcat]
- **Portal Title (`@en`):** Enterprises using electronic services system in Kaunas City Municipality[^dcat]
- **Issued (`dct:issued`):** `2024-08-12`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-03-05` .. `2026-04-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Kauno miesto savivaldybės valdoma Elektroninių paslaugų sistema (EPS) saugo Kauno m. sav. administracijos teikiamų elektroninių paslaugų duomenis. Duomenys renkami nuo 2017 m., ir yra atnaujinami kasdien. Duomenų rinkinyje saugomi EPS besinaudojančių įmonių duomenys: JAR kodas, pavadinimas, buveinės adresas ir teisinė forma. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Electronic Services System (EPS) managed by Kaunas City Municipality shall store data on electronic services provided by Kaunas Municipality. Data have been collected since 2017 and are updated on a daily basis. The data set shall contain the data of the undertakings benefiting from the EPA: the JAR code, the name, the address of the registered office and the legal form. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Imone](eps/Imone.md) | Kauno m. sav. Elektronine paslaugų sistema besinaudojančios įmonės | `4` | `jar_kodas` | — | `4` | Kauno miesto savivaldybės valdoma Elektroninių paslaugų sistema (EPS) saugo Kauno m. sav. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/eps.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/eps.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/eps (https://data.gov.lt/datasets/2741/)
