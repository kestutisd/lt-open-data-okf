---
type: Dataset
title: "Olimpiadų nugalėtojų duomenys"
description: "Lietuvos neformaliojo švietimo agentūros (LINEŠA) Olimpiadų nugalėtojų duomenų bazėje kaupiami vietinėse bei tarptautinėse olimpiadose nugalėjusių moksleivių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/linesa/ondb"
tags: [gov, linesa, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/linesa/ondb.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/linesa/ondb.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2775/"
    title: "data.gov.lt DCAT-AP — datasets/gov/linesa/ondb"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Olimpiadų nugalėtojų duomenys

- **Namespace:** `datasets/gov/linesa/ondb`[^manifest]
- **Manifest CSV:** [datasets/gov/linesa/ondb.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/linesa/ondb.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/linesa/ondb` (`deployed`)[^manifest]
- **Provider:** `linesa` — Lietuvos neformaliojo švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2775/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/linesa/ondb`[^dcat]
- **Portal Title (`@lt`):** Olimpiadų nugalėtojų duomenys[^dcat]
- **Portal Title (`@en`):** Olimpiada winners' data[^dcat]
- **Issued (`dct:issued`):** `2024-09-12`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-09-05` .. `2024-09-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos neformaliojo švietimo agentūros (LINEŠA) Olimpiadų nugalėtojų duomenų bazėje kaupiami vietinėse bei tarptautinėse olimpiadose nugalėjusių moksleivių duomenys. Duomenys kaupiami nuo 2008 m. ir yra atnaujinami kasmet. Viena duomenų lentelės eilutė priskirta vienam moksleiviui, tam tikru metu dalyvavusiam kurioje nors iš olimpiadų. Duomenis sudaro: olimpiados pavadinimas, olimpiados tipas (vietinė arba tarptautinė), dalyvavusio moksleivio pelnytas prizas arba užimta vieta, šifruoti nugalėtojo vardas ir pavardė, moksleivio švietimo įstaiga, klasė bei olimpiadai ruošęs mokytojas, tarptautinėse olimpiadose paskirti komandų vadovai, olimpiados vieta ir data. *Lietuvos neformaliojo švietimo agentūros nuomone, olimpiadų nugalėtojai negali būti skelbiami. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The database of the winners of the Olympics of the Lithuanian Non-formal Education Agency (LINESA) collects data of the students who have won at local and international Olympics. Data have been collected since 2008 and are updated annually. One line in the data table is assigned to one student who attended any of the Olympics at a certain time. The data include: the name of the Olympics, the type of the Olympics (local or international), the prize or place earned by the student involved, the name of the winner in encryption, the educational institution of the student, the class and the teacher preparing the Olympics, team leaders appointed at the international Olympics, the location and date of the Olympics. * According to the Lithuanian Non-formal Education Agency, the winners of the Olympics cannot be announced. If you have any questions about the dataset, please contact the State Data Control Opening Team by e-mail atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dalyvis](ondb/Dalyvis.md) | Olimpiadų nugalėtojų duomenys | `4` | `vda_prime_key` | — | `13` | Lietuvos neformaliojo švietimo agentūros (LINEŠA) Olimpiadų nugalėtojų duomenų bazėje kaupiami vietinėse bei tarptautinėse olimpiadose nugalėjusių... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/linesa/ondb.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/linesa/ondb.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/linesa/ondb (https://data.gov.lt/datasets/2775/)
