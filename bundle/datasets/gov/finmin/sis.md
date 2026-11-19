---
type: Dataset
title: "Stebėsenos informacinė sistemos dokumentai, elementų hierarchija, finansiniai ir rodiklių duomenys"
description: "Lietuvos respublikos finansų ministerijos Stebėsenos informacinės sistemos (SIS) duomenų rinkinyje pateikti nuo 2011 m. kaupiami dokumentų, elementų hierarchijos, finansiniai ir rodiklių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sis"
tags: [gov, finmin, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2862/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Stebėsenos informacinė sistemos dokumentai, elementų hierarchija, finansiniai ir rodiklių duomenys

- **Namespace:** `datasets/gov/finmin/sis`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sis/finmin.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sis` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2862/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/finmin/sis`[^dcat]
- **Portal Title (`@lt`):** Stebėsenos informacinė sistemos dokumentai, elementų hierarchija, finansiniai ir rodiklių duomenys[^dcat]
- **Portal Title (`@en`):** State Strategy Documents Data[^dcat]
- **Issued (`dct:issued`):** `2024-11-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2024-11-21` .. `2026-10-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos respublikos finansų ministerijos Stebėsenos informacinės sistemos (SIS) duomenų rinkinyje pateikti nuo 2011 m. kaupiami dokumentų, elementų hierarchijos, finansiniai ir rodiklių duomenys. Valstybės strategijų dokumentų duomenys Valstybės strategijų ir programų dokumentų duomenų lentelę sudaro: dokumento kodas, pavadinimas, dokumento tipas, paskutinės versijos numeris, proceso etapas, periodas, institucija ir jos kodas. Dokumento elementų hierarchija Valstybės strategijų ir programų elementų hierarchijos duomenų lentelę sudaro: dokumento ID, kuris referuoja į „Valstybės strategijų dokumentų duomenys“, elemento kodas, pavadinimas, klasė, tipas, aprašymas (rodikliams), pradžia ir pabaiga, periodiškumas, elemento matavimo vienetai, taip pat nurodyta, kokiu mastu įgyvendinamas elementas (šalies, organizacijos ar dokumento savininko). Valstybės strategijų rodiklių duomenys Valstybės strategijų ir programų rodiklių duomenų lentelę sudaro: dokumento ir objekto ID (referuoja į „Dokumento elementų hierarchija“ ir „Valstybės strategijų dokumentų duomenys“), rodiklio laikotarpis bei siektina ir faktinė reikšmės (kiekybinės ir kokybinės). Valstybės strategijų finansiniai duomenys Valstybės strategijų ir programų finansinių duomenų lentelę sudaro: dokumento ir objekto ID (referuoja į „Dokumento elementų hierarchija“ ir „Valstybės strategijų dokumentų duomenys“), elemento pradžios ir pabaigos datos, vertė eurais, išlaidų tipas, finansavimo šaltinis, lėšų tipas, valstybės funkcija, taip pat nurodyta, ar tai yra planas, patikslintas planas, poreikis ar faktas. Duomenų teikėjas – Lietuvos Respublikos finansų ministerija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data collection of the Monitoring Information System (SIS) of the Ministry of Finance of the Republic of Lithuania has compiled data on documents, hierarchy of elements, financial and indicators since 2011. State Strategy Documents Data The data table for State Strategy and Application Documents consists of: document code, title, document type, last version number, process stage, period, institution and its code. Document Item Hierarchy The data table of the hierarchy of state strategies and programme elements consists of: document ID, which referrals to “State Strategy Document Data”, item code, name, class, type, description (for indicators), beginning and end, periodicity, element units of measure, as well as the extent to which the element (country, organization or document owner) is implemented. Data on State Strategy Indicators The data table for indicators of state strategies and programmes consists of: document and object IDs (referenced to “Document item hierarchy” and “State strategy documents data”), indicator period and target and actual values (quantitative and qualitative). Financial data of state strategies The financial data table of state strategies and programmes consists of: document and object IDs (referenced to “Document item hierarchy” and “State strategy document data”), item start and end dates, value in euro, cost type, source of funding, type of funds, state function, as well as indication of whether this is a plan, revised plan, requirement or fact. Data provider means the Ministry of Finance of the Republic of Lithuania. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dokumentas](sis/Dokumentas.md) | "Lentelėje pateikti valstybės strategijų, programų dokumentų duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS)." | `4` | `doc_id` | — | `10` | — |
| [Elementas](sis/Elementas.md) | "Lentelėje pateikti valstybės strategijų, programų elementų hierarchijos duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS). " | `4` | `vda_id` | — | `16` | — |
| [Rodiklis](sis/Rodiklis.md) | "Lentelėje pateikti valstybės strategijų, programų rodiklių duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS). " | `4` | `id_planas` | — | `10` | — |
| [FinansinisDuomuo](sis/FinansinisDuomuo.md) | "Lentelėje pateikti valstybės strategijų, programų finansiniai duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS). " | `4` | `fnv_id` | — | `11` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sis (https://data.gov.lt/datasets/2862/)
