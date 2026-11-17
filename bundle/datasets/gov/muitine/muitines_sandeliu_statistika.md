---
type: Dataset
title: "Muitinės sandėlių, laikinojo saugojimo sandėlių bei garantų, pateikusių muitinei garantijas už šiuose sandėliuose saugomas prekes, statistika"
description: "Šiame rinkinyje pateikiama informacija apie Lietuvos Respublikos teritorijoje veikiančius muitinės sandėlius ir laikinojo saugojimo sandėlius, garantų ir sandėlių veiklai taikomų garantijų statistiką."
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika"
tags: [gov, muitine, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_statistika.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Muitinės sandėlių, laikinojo saugojimo sandėlių bei garantų, pateikusių muitinei garantijas už šiuose sandėliuose saugomas prekes, statistika

Šiame rinkinyje pateikiama informacija apie Lietuvos Respublikos teritorijoje veikiančius muitinės sandėlius ir laikinojo saugojimo sandėlius, garantų ir sandėlių veiklai taikomų garantijų statistiką. Informacija gaunama iš Muitinės sandėlių ir terminalų veiklos apskaitos ir kontrolės informacinės sistemos (MSAS). Rinkinys apima:

1) Lietuvos Respublikos teritorijoje veikiančių muitinės sandėlių ir laikinojo saugojimo sandėlių ir muitinės sandėliams leistų įprastinių prekių tvarkymo operacijų sąrašus (duomenys nuo 2006 m., atnaujinami kas mėnesį);

2) garantų, pateikusių muitinei garantijas už prekes, saugomas muitinės sandėliuose ir laikinojo saugojimo sandėliuose, ir jų pateiktų garantijų apibendrintą statistiką, įskaitant sandėlių ir garantijų skaičių bei vidutinę garantijos vertę (duomenys nuo 2005 m., atnaujinami kas metus).

- **Namespace:** `datasets/gov/muitine/muitines_sandeliu_statistika`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/muitines_sandeliu_statistika.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika`
- **Parent Namespace (`ns`):** Muitinės departamentas prie LR FM (`datasets/gov/muitine`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SandelioOperacija](muitines_sandeliu_statistika/SandelioOperacija.md) | Muitinės sandėliuose prekėms atliekamų operacijų sąrašai | `4` | `vda_id` | — | 7 | Lentelėje pateikiami Lietuvos Respublikos teritorijoje veikiančių muitinės sandėlių ir laikinojo saugojimo sandėlių ir muitinės sandėliams leistų įprastinių... |
| [GarantoStatistika](muitines_sandeliu_statistika/GarantoStatistika.md) | Muitinės sandėliams suteiktų garantijų statistika | `4` | `vda_id` | — | 7 | Lentelėje pateikiama informacija apima garantų, pateikusių muitinei garantijas už prekes, saugomas muitinės sandėliuose ir laikinojo saugojimo sandėliuose... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_statistika.csv
