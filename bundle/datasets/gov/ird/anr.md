---
type: Dataset
title: "Administracinių nusižengimų registras"
description: "Registro objektai: LR administracinių nusižengimų kodekso nustatyta tvarka užfiksuoti administraciniai nusižengimai; LR įstatymų ir ES teisės aktų nustatyta tvarka užfiksuoti ūkio subjektų padaryti teisės pažeidimai, už kuriuos..."
resource: "https://get.data.gov.lt/datasets/gov/ird/anr"
tags: [gov, ird, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/anr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Administracinių nusižengimų registras

Registro objektai: LR administracinių nusižengimų kodekso nustatyta tvarka užfiksuoti administraciniai nusižengimai; LR įstatymų ir ES teisės aktų nustatyta tvarka užfiksuoti ūkio subjektų padaryti teisės pažeidimai, už kuriuos priežiūros institucijos skiria poveikio priemones. Registro valdytojas - LR Vidaus reikalų ministerija; tvarkytojas - Informatikos ir ryšių departamentas.

- **Namespace:** `datasets/gov/ird/anr`[^manifest]
- **Manifest CSV:** [datasets/gov/ird/anr.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/anr`
- **Parent Namespace (`ns`):** Informatikos ir ryšių departamentas (`datasets/gov/ird`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Bauda](anr/Bauda.md) | Administracinių nusižengimų bylose paskirtos baudos | `4` | `anr_id` | — | 9 | Administracinių nusižengimų registro (ANR) duomenų neagreguota lentelė (mikroduomenys), kurioje viena eilutė yra vienas administracinis nusižengimas už kurį... |
| [KetPazeidejas](anr/KetPazeidejas.md) | Kelių eismo taisyklių pažeidimai ir pažeidėjai | `4` | `vda_prime_key` | — | 10 | Administracinių nusižengimų registro (ANR) duomenų neagreguota lentelė (mikroduomenys), kurioje įtraukti tik tie nusižengimai kurių sudėtį nustatantys... |
| [Nusizengimas](anr/Nusizengimas.md) | Administracinių nusižengimų detali mėnesinė statistika | `3` | — | — | 7 | Administracinių nusižengimų registro (ANR) mėnesiniai statistiniai duomenys apie Administracinių nusižengimų kodekso nustatyta tvarka užfiksuotus... |
| [Str45Pazeidimas](anr/Str45Pazeidimas.md) | ANK 45 str. pažeidimai ir pažeidėjai | `4` | `vda_id` | — | 12 | Administracinių nusižengimų registro (ANR) bylos, kuriose minimas Administracinių nusižengimų kodekso (ANK) 45 straipsnis ("Visuomenės sveikatos srities... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/anr.csv
