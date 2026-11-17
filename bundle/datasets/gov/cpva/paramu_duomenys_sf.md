---
type: Dataset
title: "VšĮ Centrinės projektų valdymo agentūros Vidaus saugumo fondo ir Integruoto sienų valdymo fondo informacinių sistemų sutarčių duomenys."
description: "Duomenų rinkį sudaro VšĮ Centrinės projektų valdymo agentūros administruojamų projektų sutarčių duomenys, susiję su Vidaus saugumo fondu ir Integruoto sienų valdymo fondu."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_sf"
tags: [gov, cpva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_vorai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_vorai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# VšĮ Centrinės projektų valdymo agentūros Vidaus saugumo fondo ir Integruoto sienų valdymo fondo informacinių sistemų sutarčių duomenys.

Duomenų rinkį sudaro VšĮ Centrinės projektų valdymo agentūros administruojamų projektų sutarčių duomenys, susiję su Vidaus saugumo fondu ir Integruoto sienų valdymo fondu. Rinkinyje pateikiama informacija apie projektą įgyvendinančią instituciją, nurodomas jos identifikatorius (JAR), sutarties numeris ir pavadinimas. Lentelėje fiksuojamos svarbiausios projekto datos – paraiškos pateikimo, veiklų pradžios ir pabaigos, sutarties įsigaliojimo bei projekto pabaigos datos.

Taip pat pateikiami finansiniai rodikliai: finansavimo procentas, prašoma suma, finansuojama suma ir faktiškai išmokėta suma bei paskutinio mokėjimo data. Duomenys leidžia įvertinti projektų finansavimo apimtį ir mokėjimų eigą. Lentelėje nurodomas partnerių skaičius, leidžiantis analizuoti projektų bendradarbiavimo mastą. Be to, pateikiamas nustatytų pažeidimų skaičius, kuris svarbus priežiūros ir rizikų vertinimui. Papildomi laukai – regionas ir priemonės pavadinimas – sudaro galimybę analizuoti projektų pasiskirstymą teritoriniu ir programiniu pjūviu.

Duomenų teikėjas – VšĮ Centrinė projektų valdymo agentūra.

- **Namespace:** `datasets/gov/cpva/paramu_duomenys_sf`[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys_vorai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_vorai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_sf`
- **Parent Namespace (`ns`):** VšĮ Centrinė projektų valdymo agentūra (`datasets/gov/cpva`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sutartis](paramu_duomenys_sf/Sutartis.md) | VšĮ Centrinės projektų valdymo agentūros Vidaus saugumo fondo ir Integruoto sienų valdymo fondo informacinių sistemų sutarčių duomenys. | `4` | `sutarties_nr` | — | 18 | Duomenų rinkį sudaro VšĮ Centrinės projektų valdymo agentūros administruojamų projektų sutarčių duomenys, susiję su Vidaus saugumo fondu ir Integruoto sienų... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_vorai.csv
