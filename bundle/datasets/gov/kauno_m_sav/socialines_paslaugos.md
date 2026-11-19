---
type: Dataset
title: "Kauno miesto savivaldybės suteiktos socialinės paslaugos"
description: "Šiame rinkinyje pateikiami Kauno miesto savivaldybės Socialinių paslaugų informacinėje sistemoje nuo 2000 m. fiksuojamų suteiktų paslaugų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/socialines_paslaugos"
tags: [gov, kauno_m_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2773/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/socialines_paslaugos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kauno miesto savivaldybės suteiktos socialinės paslaugos

- **Namespace:** `datasets/gov/kauno_m_sav/socialines_paslaugos`[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/socialines_paslaugos` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2773/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/socialines_paslaugos`[^dcat]
- **Portal Title (`@lt`):** Kauno miesto savivaldybės suteiktos socialinės paslaugos[^dcat]
- **Portal Title (`@en`):** Social services provided by Kaunas City Municipality[^dcat]
- **Issued (`dct:issued`):** `2024-09-04`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-10-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šiame rinkinyje pateikiami Kauno miesto savivaldybės Socialinių paslaugų informacinėje sistemoje nuo 2000 m. fiksuojamų suteiktų paslaugų duomenys. Vienoje duomenų lentelės eilutėje nurodyta viena atitinkamam asmeniui suteikta paslauga. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

This package provides data on the services provided in the Social Services Information System of Kaunas City Municipality since 2000. One row in the data table shows one service provided to the person concerned. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Paslauga](socialines_paslaugos/Paslauga.md) | Kauno miesto savivaldybės suteiktos socialinės paslaugos | `4` | `vda_prime_key` | — | `11` | Šiame rinkinyje pateikiamos Kauno miesto savivaldybės Socialinių paslaugų informacinėje sistemoje fiksuojamos suteiktos paslaugos. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/socialines_paslaugos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/socialines_paslaugos (https://data.gov.lt/datasets/2773/)
