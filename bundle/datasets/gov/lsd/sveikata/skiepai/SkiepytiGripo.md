---
type: Table
title: "SkiepytiGripo — Asmenys, paskiepyti šaltojo sezono ligų (gripo) skiepais, pagal ligą (gripas), įstaigą lytį ir amžiaus grupę"
description: "Kol kas pateikti tik gripo duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiGripo"
tags: [gov, lsd, skiepytigripo, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2777/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/skiepai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SkiepytiGripo — Asmenys, paskiepyti šaltojo sezono ligų (gripo) skiepais, pagal ligą (gripas), įstaigą lytį ir amžiaus grupę

Kol kas pateikti tik gripo duomenys[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/skiepai/SkiepytiGripo`[^manifest]
- **Dataset:** [Asmenys, paskiepyti įvairių ligų skiepais](../skiepai.md) (`datasets/gov/lsd/sveikata/skiepai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/skiepai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai/SkiepytiGripo` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ist_type` | `"vieša"` | — | — | Vieša | — |
| `ist_type` | `"privati"` | — | — | Privati | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/skiepai (https://data.gov.lt/datasets/2777/)
