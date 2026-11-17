---
type: Dataset
title: "VšĮ Centrinės projektų valdymo agentūros teikiamų paramų sutartys ir finansavimas"
description: "Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos..."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys"
tags: [gov, cpva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# VšĮ Centrinės projektų valdymo agentūros teikiamų paramų sutartys ir finansavimas

Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2014–2020 m. struktūrinių fondų programos projektų įgyvendinimu. Rinkinyje pateikiamos 3 lentelės, kuriose galima rasti tokią informaciją:

pateiktos paraiškos bei pasirašytos finansuoti sutartys (viena eilutė atitinka atitinkamą paraišką, pasirašytos sutarties statusų pasikeitimų eigą);

projekto įgyvendinimui prašomos finansuoti, finansuotos bei grąžintos sumos (viena eilutė atitinka vienos paraiškos prašomą finansuoti sumą. Esant grąžinamų pinigu faktui, tuo pačiu nurodoma pati grąžintina suma bei priežasties tipas);

pažeidimų tyrimų informacija įtariant pažeidimą (viena eilutė atitinka vieną įtariamą pažeidimą ir statusą, nurodantį, ar pažeidimas nustatytas).

Projektai, kurie buvo vykdomi naudojantis šia sistema jau pasibaigę, bet sistemos duomenys retais atvejais vis dar atnaujinami. Tokiu atveju, duomenų atnaujinimas numatomas kas 6 mėn.

- **Namespace:** `datasets/gov/cpva/paramu_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys`
- **Parent Namespace (`ns`):** VšĮ Centrinė projektų valdymo agentūra (`datasets/gov/cpva`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [FinansuojamaSuma](paramu_duomenys/FinansuojamaSuma.md) | Projekto įgyvendinimui prašomos finansuoti, finansuotos bei grąžintos sumos | `4` | `vda_prime_key` | — | 9 | Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis... |
| [PazeidimoTyrimas](paramu_duomenys/PazeidimoTyrimas.md) | Pažeidimų tyrimų informacija įtariant pažeidimą | `4` | `pazeidimo_tyr_id` | — | 7 | Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis... |
| [Sutartis](paramu_duomenys/Sutartis.md) | Pateiktos paraiškos bei pasirašytos finansuoti sutartys | `4` | `vda_prime_key` | — | 20 | Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys.csv
