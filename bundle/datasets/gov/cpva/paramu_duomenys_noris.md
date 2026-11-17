---
type: Dataset
title: "VšĮ Centrinės projektų valdymo agentūros 2014–2021 m. Europos ekonominės erdvės ir Norvegijos finansinių mechanizmų administravimo ir procesų automatizavimo informacinės sistemos duomenys"
description: "Duomenys pateikiami iš Informacinių projektų administravimo sistemos NORIS, skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų 2014–2021 m...."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_noris"
tags: [gov, cpva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_noris.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_noris.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# VšĮ Centrinės projektų valdymo agentūros 2014–2021 m. Europos ekonominės erdvės ir Norvegijos finansinių mechanizmų administravimo ir procesų automatizavimo informacinės sistemos duomenys

Duomenys pateikiami iš Informacinių projektų administravimo sistemos NORIS, skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų 2014–2021 m. Europos ekonominės erdvės ir Norvegijos finansinių programų projektų įgyvendinimu. Rinkinyje pateikiamos dvi lentelės, kuriose galima rasti informaciją apie projektus, jų finansavimą (viena eilutė atitinka vieną projektą) ir pažeidimus, nustatytus projektų vykdymo metu (viena eilutė – vienas fiksuotas pažeidimas). Lenteles galima sujungti per projekto kodą.

- **Namespace:** `datasets/gov/cpva/paramu_duomenys_noris`[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys_noris.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_noris.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_noris`
- **Parent Namespace (`ns`):** VšĮ Centrinė projektų valdymo agentūra (`datasets/gov/cpva`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pazeidimas](paramu_duomenys_noris/Pazeidimas.md) | Pažeidimų informacija įtariant pažeidimą | `4` | `pazeidimo_id` | — | 11 | Ši lentelė pateikia informaciją apie nustatytus pažeidimus, susijusius su 2014–2021 m. Europos ekonominės erdvės ir Norvegijos finansinių mechanizmų... |
| [Sutartis](paramu_duomenys_noris/Sutartis.md) | Pateiktos paraiškos bei pasirašytos finansuoti sutartys | `4` | — | — | 22 | Ši lentelė aprašo projektus, įgyvendinamus pagal 2014–2021 m. Europos ekonominės erdvės ir Norvegijos finansinius mechanizmus, kuriuos administruoja... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_noris.csv
