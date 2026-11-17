---
type: Dataset
title: "Muitinės leidimų sistemos leidimų ir prašymų duomenys"
description: "Leidimų sistemos duomenys aprašo kelią nuo prašymo pateikimo iki leidimo išdavimo ir galiojimo."
resource: "https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys"
tags: [gov, muitine, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Muitinės leidimų sistemos leidimų ir prašymų duomenys

Leidimų sistemos duomenys aprašo kelią nuo prašymo pateikimo iki leidimo išdavimo ir galiojimo. Jie parodo, kas kreipėsi, kokio leidimo prašoma, kokia yra nagrinėjimo būsena ir kada leidimas galioja. Prie kiekvieno prašymo ir leidimo gali būti pridėtos papildomos detalės (lankstūs laukeliai), nes skirtingiems leidimų tipams reikia skirtingos informacijos. Šis rinkinys padeda aiškiai matyti, kiek ir kokių leidimų išduota bei kokioje stadijoje yra prašymai.

- **Namespace:** `datasets/gov/muitine/leidimu_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/leidimu_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys`
- **Parent Namespace (`ns`):** Muitinės departamentas prie LR FM (`datasets/gov/muitine`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Leidimas](leidimu_duomenys/Leidimas.md) | Leidimai | `4` | `vda_prime_key` | — | 13 | Duomenys apie suteiktą teisę atlikti tam tikrą veiklą ar naudotis lengvata. |
| [LeidimoDuomuo](leidimu_duomenys/LeidimoDuomuo.md) | Leidimų duomenys | — | `vda_prime_key` | — | 9 | Papildomos leidimo detalės eilutėmis (po vieną detalę per eilutę). |
| [Prasymas](leidimu_duomenys/Prasymas.md) | Prašymai | — | `vda_prime_key` | — | 12 | Pateiktas prašymas gauti leidimą. |
| [PrasymoDuomuo](leidimu_duomenys/PrasymoDuomuo.md) | Prašymų duomenys | — | `vda_prime_key` | — | 10 | Papildomos prašymo detalės eilutėmis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv
