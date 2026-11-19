---
type: Table
title: "BuiTeritorijos15min — Švietimo institucijų 15 minučių pasiekiamumo pėsčiomis ir automobiliu teritorijos."
description: "Duomenų aprėptį sudaro švietimo institucijos, kuriose, tikslinių metų rugsėjo 1 dienos duomenimis, yra ugdomi mokiniai pagal bendrojo ugdymo programas."
resource: "https://get.data.gov.lt/datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos/BuiTeritorijos15min"
tags: [gov, lsd, buiteritorijos15min, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2048/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# BuiTeritorijos15min — Švietimo institucijų 15 minučių pasiekiamumo pėsčiomis ir automobiliu teritorijos.

Duomenų aprėptį sudaro švietimo institucijos, kuriose, tikslinių metų rugsėjo 1 dienos duomenimis, yra ugdomi mokiniai pagal bendrojo ugdymo programas. Priskiriant mokinį prie teritorijos Laikoma, kad jo gyvenamoji vieta sutampa su Gyventojų registre deklaruota gyvenamąja vieta tikslinių metų rugsėjo 1 dieną. Tais atvejais, kai šią datą asmuo nebuvo deklaravęs gyvenamosios vietos, mokinio gyvenamąja vieta buvo laikoma paskutinė ankstesnė deklaruota jo gyvenamoji vieta. Sudarant 15 min pasiekiamumo automobiliu teritorijas, neatsižvelgta į piko valandas ir savaitės dienas. Duomenų rinkinys atnaujinamas du kartus per metus (spalio ir sausio mėnesį).[^manifest]

- **Model:** `datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos/BuiTeritorijos15min`[^manifest]
- **Dataset:** [Švietimo institucijų pasiekiamumo pėsčiomis ir automobiliu teritorijos](../pasiekiamumo_teritorijos.md) (`datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos/BuiTeritorijos15min` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Rinkinio unikalus identifikatorius | — |
| `laikas_min` | `integer` | — | `2` | `open` | — | Maksimalus laikas minutėmis, per kurį įmanoma pasiekti švietimo instituciją | — |
| `ins_kodas` | `string` | — | `2` | `open` | — | Institucijos kodas | Švietimo ir mokslo institucijų registre (JAR kodas, jei neegzistuoja - Švietimo ir mokslo institucijų registro (ŠMIR) kodas) |
| `ins_pagr_tipas` | `string` | — | `2` | `open` | — | Švietimo institucijos pagrindinis tipas | — |
| `ins_pavad_lt` | `string` | — | `2` | `open` | — | Švietimo institucijos pavadinimas | — |
| `is_viso_mokiniu` | `integer` | — | `4` | `open` | — | Bendras mokinių skaičius priskirtas prie institucijos tikslinių metų rugsėjo 1-ai dienai | — |
| `is_viso_mokosi_kontakt_budu` | `integer` | — | `4` | `open` | — | Besimokančių kontaktiniu būdu (kasdieniu mokymosi organizavimo būdu) bendras mokinių skaičius priskirtas prie institucijos tikslinių metų rugsėjo 1-ai dienai | — |
| `teritorijoje_mokiniu` | `integer` | — | `4` | `open` | — | Bendras mokinių skaičius, patenkantys į 15 min. teritoriją, priskirtas prie institucijos tikslinių metų rugsėjo 1-ai dienai. | — |
| `teritorijoje_kontakt_budu` | `integer` | — | `2` | `open` | — | Besimokančių kontaktiniu būdu (kasdieniu mokymosi organizavimo būdu) bendras mokinių skaičius, patenkantys į 15 min. teritoriją, priskirtas prie institucijos tikslinių metų rugsėjo 1-ai dienai | — |
| `keliavimo_budas` | `string` | — | `2` | `open` | — | Keliavimo būdas, kuriuo galima pasiekti švietimo instituciją per 15 minučių | — |
| `naujinimo_data` | `date` | `D` | `4` | `open` | — | Duomenų naujinimo data | — |
| `geometrija` | `geometry(geometry, 3346)` | `m` | `4` | `open` | — | Objekto geometrija WKT formatu (LKS94) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ins_pagr_tipas` | `"Gimnazija"` | — | — | — | — |
| `ins_pagr_tipas` | `"Pagrindinė mokykla"` | — | — | — | — |
| `ins_pagr_tipas` | `"Progimnazija"` | — | — | — | — |
| `ins_pagr_tipas` | `"Pradinė mokykla"` | — | — | — | — |
| `ins_pagr_tipas` | `"Profesinio mokymo įstaiga"` | — | — | — | — |
| `ins_pagr_tipas` | `"Kitas švietimo teikėjas"` | — | — | — | — |
| `keliavimo_budas` | `"pėsčiomis"` | — | — | — | — |
| `keliavimo_budas` | `"automobiliu"` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos (https://data.gov.lt/datasets/2048/)
