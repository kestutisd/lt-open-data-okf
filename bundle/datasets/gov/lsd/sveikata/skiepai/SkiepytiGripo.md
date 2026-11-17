---
type: Table
title: "SkiepytiGripo — Asmenys, paskiepyti šaltojo sezono ligų (gripo) skiepais, pagal ligą (gripas), įstaigą lytį ir amžiaus grupę"
description: "Kol kas pateikti tik gripo duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiGripo"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# SkiepytiGripo — Asmenys, paskiepyti šaltojo sezono ligų (gripo) skiepais, pagal ligą (gripas), įstaigą lytį ir amžiaus grupę

Kol kas pateikti tik gripo duomenys

- **Model:** `datasets/gov/lsd/sveikata/skiepai/SkiepytiGripo`[^manifest]
- **Dataset:** [Asmenys, paskiepyti įvairių ligų skiepais](../skiepai.md) (`datasets/gov/lsd/sveikata/skiepai`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/skiepai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiGripo`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `sezonas` | `integer` | — | `4` | `open` | — | Sezono pradžios metai | Sezonas prasideda nuo rugsėjo mėn. Pvz., "2023" sezonas apima periodą nuo 2023 rugsėjo 1 d. iki 2024 rugpjūčio 31 d. |
| `liga` | `string` | — | `2` | `open` | — | Liga, nuo kurios skiepijama | — |
| `laikotarpis` | `string` | — | `2` | `open` | — | Laikotarpis | Mėnuo, kai buvo paskiepyta, arba "Visas sezonas" |
| `osp_sav_pav` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje registruota skiepijanti įstaiga | Nurodyta "pan-LT" įstaigoms, kurios turi filialų įvairiose šalies vietose |
| `espbi_ist_pav` | `string` | — | `3` | `open` | — | Skiepijančios įstaigos pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Skiepijančios įstaigos JAR kodas | — |
| `ist_type` | `string` | — | `4` | `open` | — | Skiepijančios įstaigos tipas | — |
| `lytis` | `string` | — | `4` | `open` | — | Skiepyto žmogaus lytis | — |
| `age_gr` | `string` | — | `4` | `open` | — | Skiepyto žmogaus apytikslė amžiaus grupė | Konfidencialumo tikslais pridėta triukšmo (<2 m.) ir sugrupuota |
| `n` | `integer` | — | `4` | `open` | — | Asmenų skaičius | Skaičius nurodyto amžiaus ir lyties asmenų, paskiepytų toje įstaigoje nurodytu laikotarpiu, nuo nurodytos ligos. Skaičiuojami unikalūs asmenys įstaigos ir laikotarpio lygiu, taigi asmuo gali būti įtrauktas į šią lentelę kelis kartus, jei skiepijosi skirtingose įstaigose, o taip pat viso sezono skaičius gali būti mažesnis nei visų mėnesių skaičių suma |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ist_type` | `"vieša"` | — | — | Vieša | — |
| `ist_type` | `"privati"` | — | — | Privati | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv
