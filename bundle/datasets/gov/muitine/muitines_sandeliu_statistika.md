---
type: Dataset
title: "Muitinės sandėlių, laikinojo saugojimo sandėlių bei garantų, pateikusių muitinei garantijas už šiuose sandėliuose saugomas prekes, statistika"
description: "Šiame rinkinyje pateikiama informacija apie Lietuvos Respublikos teritorijoje veikiančius muitinės sandėlius ir laikinojo saugojimo sandėlius, garantų ir sandėlių veiklai taikomų garantijų statistiką."
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika"
tags: [gov, muitine, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_statistika.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4117/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_sandeliu_statistika"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Muitinės sandėlių, laikinojo saugojimo sandėlių bei garantų, pateikusių muitinei garantijas už šiuose sandėliuose saugomas prekes...

Šiame rinkinyje pateikiama informacija apie Lietuvos Respublikos teritorijoje veikiančius muitinės sandėlius ir laikinojo saugojimo sandėlius, garantų ir sandėlių veiklai taikomų garantijų statistiką. Informacija gaunama iš Muitinės sandėlių ir terminalų veiklos apskaitos ir kontrolės informacinės sistemos (MSAS). Rinkinys apima: 1)	Lietuvos Respublikos teritorijoje veikiančių muitinės sandėlių ir laikinojo saugojimo sandėlių ir muitinės sandėliams leistų įprastinių prekių tvarkymo operacijų sąrašus (duomenys nuo 2006 m., atnaujinami kas mėnesį); 2) garantų, pateikusių muitinei garantijas už prekes, saugomas muitinės sandėliuose ir laikinojo saugojimo sandėliuose, ir jų pateiktų garantijų apibendrintą statistiką, įskaitant sandėlių ir garantijų skaičių bei vidutinę garantijos vertę (duomenys nuo 2005 m., atnaujinami kas metus).[^manifest]

- **Namespace:** `datasets/gov/muitine/muitines_sandeliu_statistika`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/muitines_sandeliu_statistika.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4117/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika`[^dcat]
- **Portal Title (`@lt`):** Muitinės sandėlių, laikinojo saugojimo sandėlių bei garantų, pateikusių muitinei garantijas už šiuose sandėliuose saugomas prekes, statistika[^dcat]
- **Portal Title (`@en`):** Statistics on customs warehouses, temporary storage warehouses and guarantors providing customs guarantees for goods stored in these warehouses[^dcat]
- **Issued (`dct:issued`):** `2026-02-04`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-02-02` .. `2026-10-01`[^dcat]

### Portal Description (`@lt`)

Šiame rinkinyje pateikiama informacija apie Lietuvos Respublikos teritorijoje veikiančius muitinės sandėlius ir laikinojo saugojimo sandėlius, garantų ir sandėlių veiklai taikomų garantijų statistiką. Informacija gaunama iš Muitinės sandėlių ir terminalų veiklos apskaitos ir kontrolės informacinės sistemos (MSAS). Rinkinys apima: 1)	Lietuvos Respublikos teritorijoje veikiančių muitinės sandėlių ir laikinojo saugojimo sandėlių ir muitinės sandėliams leistų įprastinių prekių tvarkymo operacijų sąrašus (duomenys nuo 2006 m., atnaujinami kas mėnesį). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt. 2) Lentelėje pateikiama informacija apima garantų, pateikusių muitinei garantijas už prekes, saugomas muitinės sandėliuose ir laikinojo saugojimo sandėliuose, ir jų pateiktų garantijų apibendrintą statistiką, įskaitant sandėlių ir garantijų skaičių bei vidutinę garantijos vertę (duomenys nuo 2005 m., atnaujinami kas metus). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SandelioOperacija](muitines_sandeliu_statistika/SandelioOperacija.md) | Muitinės sandėliuose prekėms atliekamų operacijų sąrašai | `4` | `vda_id` | — | `7` | Lentelėje pateikiami Lietuvos Respublikos teritorijoje veikiančių muitinės sandėlių ir laikinojo saugojimo sandėlių ir muitinės sandėliams leistų įprastinių... |
| [GarantoStatistika](muitines_sandeliu_statistika/GarantoStatistika.md) | Muitinės sandėliams suteiktų garantijų statistika | `4` | `vda_id` | — | `7` | Lentelėje pateikiama informacija apima garantų, pateikusių muitinei garantijas už prekes, saugomas muitinės sandėliuose ir laikinojo saugojimo sandėliuose... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_statistika.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_sandeliu_statistika (https://data.gov.lt/datasets/4117/)
