---
type: Dataset
title: "VšĮ Centrinės projektų valdymo agentūros administruojamos ES fondų ir tarptautinių programų projektų sutartys"
description: "Duomenys pateikiami iš Informacinių projektų administravimo sistemų (EEENORIS, SPIS, LŠBP, CPVAIS), skirtų kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros..."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_dr"
tags: [gov, cpva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_drugeliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# VšĮ Centrinės projektų valdymo agentūros administruojamos ES fondų ir tarptautinių programų projektų sutartys

Duomenys pateikiami iš Informacinių projektų administravimo sistemų (EEENORIS, SPIS, LŠBP, CPVAIS), skirtų kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2007–2017 m. fondų programų projektų įgyvendinimu. Rinkinyje pateikiamos dvi lentelės, kuriose galima rasti tokią informaciją: pateiktas paraiškas ir pasirašytas finansuoti sutartis (viena eilutė atitinka atitinkamą paraišką, pasirašytos sutarties statusų pasikeitimų eigą); pažeidimų tyrimų informaciją įtariant pažeidimą (viena eilutė atitinka vieną įtariamą pažeidimą ir statusą, nurodantį, ar pažeidimas nustatytas).

Projektai, kurie buvo vykdomi naudojantis šia sistema jau pasibaigę, todėl duomenys nebebus atnaujinami.

- **Namespace:** `datasets/gov/cpva/paramu_duomenys_dr`[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_dr`
- **Parent Namespace (`ns`):** VšĮ Centrinė projektų valdymo agentūra (`datasets/gov/cpva`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PazeidimoTyrimas](paramu_duomenys_dr/PazeidimoTyrimas.md) | Pažeidimų tyrimų informacija įtariant pažeidimą | `4` | `pazeidimo_tyr_id` | — | 9 | Duomenys pateikiami iš Informacinių projektų administravimo sistemų (EEENORIS, SPIS, LŠBP, CPVAIS), skirtų kaupti, apdoroti ir saugoti statistinius ir... |
| [Sutartis](paramu_duomenys_dr/Sutartis.md) | Pateiktos paraiškos bei pasirašytos finansuoti sutartys | `4` | `vda_prime_key` | — | 21 | Duomenys pateikiami iš Informacinių projektų administravimo sistemų (EEENORIS, SPIS, LŠBP, CPVAIS), skirtų kaupti, apdoroti ir saugoti statistinius ir... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_drugeliai.csv
