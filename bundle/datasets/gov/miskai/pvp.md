---
type: Dataset
title: "Privačių vidinės miškotvarkos projektų rengėjų sąrašas"
description: "Pateikiamas sąrašas, kuriame matomi asmenys, galintys rengti vidinės miškotvarkos projektus."
resource: "https://get.data.gov.lt/datasets/gov/miskai/pvp"
tags: [gov, miskai, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/miskai/pvp.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/916/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/pvp"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Privačių vidinės miškotvarkos projektų rengėjų sąrašas

- **Namespace:** `datasets/gov/miskai/pvp`[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/pvp.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/pvp` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `9` (9 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/916/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė miškų tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/miskai/pvp/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Privačių vidinės miškotvarkos projektų rengėjų sąrašas[^dcat]
- **Portal Title (`@en`):** List of private internal forest management project developers[^dcat]
- **Issued (`dct:issued`):** `2023-06-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-06-13` .. `2025-12-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiamas sąrašas, kuriame matomi asmenys, galintys rengti vidinės miškotvarkos projektus.[^dcat]

### Portal Description (`@en`)

There is a list of people who can prepare internal forest management projects.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PVPBukle](pvp/PVPBukle.md) | Projekto būklė | `4` | — | — | `1` | — |
| [PrivacValduProjektas](pvp/PrivacValduProjektas.md) | Privačių miškų vidinės miškotvarkos projektas | `4` | — | — | `9` | — |
| [PVPAutorius](pvp/PVPAutorius.md) | Projekto autorius | `4` | — | — | `1` | — |
| [Rajonas](pvp/Rajonas.md) | Savivaldybė | `4` | — | — | `1` | — |
| [PVPBuklesKaita](pvp/PVPBuklesKaita.md) | Projekto būklės data | `4` | — | — | `3` | — |
| [Vietove](pvp/Vietove.md) | Vietovė | `4` | — | — | `2` | Vietovė / Blokas : Sklypas = kadastro numeris |
| [BlokuSklypas](pvp/BlokuSklypas.md) | Sklypas | `4` | — | — | `3` | Vietovė / Blokas : Sklypas = kadastro numeris |
| [PVPKadSklypas](pvp/PVPKadSklypas.md) | PVP sklypai | `4` | — | — | `2` | — |
| [VietovesBlokas](pvp/VietovesBlokas.md) | Blokas | `4` | — | — | `3` | Vietovė / Blokas : Sklypas = kadastro numeris |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/pvp.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/pvp (https://data.gov.lt/datasets/916/)
