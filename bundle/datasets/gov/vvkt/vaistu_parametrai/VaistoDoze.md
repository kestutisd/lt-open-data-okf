---
type: Table
title: "VaistoDoze — Vaistinių preparatų vartojimo parametrai"
description: "Lentelėje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo parametrus."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai/VaistoDoze"
tags: [gov, vvkt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistu_parametrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# VaistoDoze — Vaistinių preparatų vartojimo parametrai

Lentelėje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo parametrus. Kiekviena eilutė nurodo vaistinio preparato vidutinę paros dozę pagal vartojimo būdą ir ATC kodą. Vieną eilutę sudaro: vaistinio preparato identifikacinis numeris, ATC kodas, vaistinio preparato vartojimo būdas, DDD (angl. Defined daily dose, vidutinė paros dozė) įvertis, DDD įverčio matavimo vienetai ir papildomas stulpelis su DDD įverčio pastabomis.

- **Model:** `datasets/gov/vvkt/vaistu_parametrai/VaistoDoze`[^manifest]
- **Dataset:** [Vaistinių preparatų vartojimo ir sudėties parametrai](../vaistu_parametrai.md) (`datasets/gov/vvkt/vaistu_parametrai`)
- **Manifest CSV:** [datasets/gov/vvkt/vaistu_parametrai.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai/VaistoDoze`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | Unikalus Valstybės duomenų agentūros sugeneruotas eilutės identifikatorius. Eilutės unikalumą sudaro vid, atc_kodas, vartojimo_budas, ddd_pastabos |
| `vid` | `string` | — | `4` | `open` | — | Vaistinio preparato identifikacinis numeris | — |
| `atc_kodas` | `string` | — | `4` | `open` | — | ATC kodas | ATC (Anatomical Therapeutic Chemical) kodas – tarptautinė vaistų klasifikacijos sistema, kuri priskiria vaistus pagal jų terapinę ir cheminę klasifikaciją |
| `vartojimo_budas` | `string` | — | `4` | `open` | — | Vartojimo būdas | Vaistinio preparato vartojimo būdas |
| `ddd` | `number` | — | `4` | `open` | — | Vidutinė paros dozė | Numanoma vidutinė paros dozė vaistui. DDD – Defined daily dose |
| `ddd_matav_vnt` | `string` | — | `4` | `open` | — | Vidutinės paros dozės matavimo vienetai | — |
| `ddd_pastabos` | `string` | — | `2` | `open` | — | DDD pastabos | Papildoma informacija apie vidutinės paros dozės įvertį |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistu_parametrai.csv
