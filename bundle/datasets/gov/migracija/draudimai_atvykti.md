---
type: Dataset
title: "Duomenys apie uždraudimą atvykti"
description: "Duomenys apie asmenis, kuriems uždrausta atvykti į Lietuvos Respubliką"
resource: "https://get.data.gov.lt/datasets/gov/migracija/draudimai_atvykti"
tags: [gov, migracija, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/draudimai_atvykti.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/migracija/draudimai_atvykti.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1945/"
    title: "data.gov.lt DCAT-AP — datasets/gov/migracija/draudimai_atvykti"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Duomenys apie uždraudimą atvykti

Duomenys apie asmenis, kuriems uždrausta atvykti į Lietuvos Respubliką[^manifest]

- **Namespace:** `datasets/gov/migracija/draudimai_atvykti`[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/draudimai_atvykti.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/draudimai_atvykti.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/draudimai_atvykti` (`deployed`)[^manifest]
- **Provider:** `migracija` — Migracijos departamentas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1945/`[^dcat]
- **Publisher (`dct:publisher`):** Migracijos departamentas prie Lietuvos Respublikos vidaus reikalų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/migracija/draudimai_atvykti`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie uždraudimą atvykti[^dcat]
- **Portal Title (`@en`):** Entry ban details[^dcat]
- **Issued (`dct:issued`):** `2023-06-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-03` .. `2026-06-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie užsieniečius, kuriems buvo uždrausta atvykti į Lietuvos Respubliką, kuriems buvo atsisakyta išduoti vizą ar ji buvo panaikinta, ar atšaukta Šengeno viza arba kuriems buvo atsisakyta išduoti leidimą gyventi ar jis buvo panaikintas, užsieniečius, kurie buvo neįleisti į Lietuvos Respubliką, įpareigoti išvykti iš Lietuvos Respublikos, grąžinti į užsienio valstybę, perduoti užsienio valstybei pagal Lietuvos Respublikos sudarytą tarptautinę sutartį dėl neteisėtai esančių asmenų grąžinimo (readmisijos) arba bandė neteisėtai išvykti iš Lietuvos Respublikos ar išvyko iš jos, arba užsieniečius, kurie neturi teisės gyventi Lietuvos Respublikoje ir nevykdo įsipareigojimų muitinei ar nesumokėjo Lietuvos Respublikos įstatymų nustatyta tvarka skirtos (skirtų) baudos (baudų). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on aliens who have been refused entry to the Republic of Lithuania, whose visa has been refused or annulled, or whose Schengen visa has been refused or revoked, aliens who have not been admitted to the Republic of Lithuania are obliged to leave Republic of Lithuania, returned to a foreign state, transferred to a foreign state in accordance with an international agreement concluded by the Republic of Lithuania on the return of illegally staying persons or attempted to leave the Republic of Lithuania illegally or aliens who do not have the right to reside in the Republic of Lithuania whether he has not paid the fine (s) imposed in accordance with the procedure established by the laws of the Republic of Lithuania.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Draudimas](draudimai_atvykti/Draudimas.md) | Duomenys apie užsieniečius, kuriems buvo uždrausta atvykti į Lietuvos Respubliką, kuriems buvo atsisakyta išduoti vizą ar ji buvo panaikinta, ar atšaukta Šengeno viza arba kuriems buvo atsisakyta išduoti leidimą gyventi ar jis buvo panaikintas, užsieniečius, kurie buvo neįleisti į Lietuvos Respubliką, įpareigoti išvykti iš Lietuvos Respublikos, grąžinti į užsienio valstybę, perduoti užsienio valstybei pagal Lietuvos Respublikos sudarytą tarptautinę sutartį dėl neteisėtai esančių asmenų grąžinimo (readmisijos) arba bandė neteisėtai išvykti iš Lietuvos Respublikos ar išvyko iš jos, arba užsieniečius, kurie neturi teisės gyventi Lietuvos Respublikoje ir nevykdo įsipareigojimų muitinei ar nesumokėjo Lietuvos Respublikos įstatymų nustatyta tvarka skirtos (skirtų) baudos (baudų). | `4` | `id` | `open` | `8` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/draudimai_atvykti.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/draudimai_atvykti.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/migracija/draudimai_atvykti (https://data.gov.lt/datasets/1945/)
