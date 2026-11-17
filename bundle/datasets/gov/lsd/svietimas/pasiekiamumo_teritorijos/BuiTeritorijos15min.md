---
type: Table
title: "BuiTeritorijos15min — Švietimo institucijų 15 minučių pasiekiamumo pėsčiomis ir automobiliu teritorijos."
description: "Duomenų aprėptį sudaro švietimo institucijos, kuriose, tikslinių metų rugsėjo 1 dienos duomenimis, yra ugdomi mokiniai pagal bendrojo ugdymo programas."
resource: "https://get.data.gov.lt/datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos/BuiTeritorijos15min"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/pasiekiamumo_teritorijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# BuiTeritorijos15min — Švietimo institucijų 15 minučių pasiekiamumo pėsčiomis ir automobiliu teritorijos.

Duomenų aprėptį sudaro švietimo institucijos, kuriose, tikslinių metų rugsėjo 1 dienos duomenimis, yra ugdomi mokiniai pagal bendrojo ugdymo programas. Priskiriant mokinį prie teritorijos Laikoma, kad jo gyvenamoji vieta sutampa su Gyventojų registre deklaruota gyvenamąja vieta tikslinių metų rugsėjo 1 dieną. Tais atvejais, kai šią datą asmuo nebuvo deklaravęs gyvenamosios vietos, mokinio gyvenamąja vieta buvo laikoma paskutinė ankstesnė deklaruota jo gyvenamoji vieta.

Sudarant 15 min pasiekiamumo automobiliu teritorijas, neatsižvelgta į piko valandas ir savaitės dienas. Duomenų rinkinys atnaujinamas du kartus per metus (spalio ir sausio mėnesį).

- **Model:** `datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos/BuiTeritorijos15min`[^manifest]
- **Dataset:** [Švietimo institucijų pasiekiamumo pėsčiomis ir automobiliu teritorijos](../pasiekiamumo_teritorijos.md) (`datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos`)
- **Manifest CSV:** [datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos/BuiTeritorijos15min`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ins_pagr_tipas` | `"Gimnazija"` | — | — | — | — |
| `ins_pagr_tipas` | `"Pagrindinė mokykla"` | — | — | — | — |
| `ins_pagr_tipas` | `"Progimnazija"` | — | — | — | — |
| `ins_pagr_tipas` | `"Pradinė mokykla"` | — | — | — | — |
| `ins_pagr_tipas` | `"Profesinio mokymo įstaiga"` | — | — | — | — |
| `ins_pagr_tipas` | `"Kitas švietimo teikėjas"` | — | — | — | — |
| `keliavimo_budas` | `"pėsčiomis"` | — | — | — | — |
| `keliavimo_budas` | `"automobiliu"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/pasiekiamumo_teritorijos.csv
