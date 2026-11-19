---
type: Table
title: "VaistoDoze — Vaistinių preparatų vartojimo parametrai"
description: "\"Lentelėje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo parametrus."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai/VaistoDoze"
tags: [gov, vvkt, vaistodoze, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L13"
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistu_parametrai.csv#L13"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3802/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkt/vaistu_parametrai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VaistoDoze — Vaistinių preparatų vartojimo parametrai

"Lentelėje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo parametrus. Kiekviena eilutė nurodo vaistinio preparato vidutinę paros dozę pagal vartojimo būdą ir ATC kodą. Vieną eilutę sudaro: vaistinio preparato identifikacinis numeris, ATC kodas, vaistinio preparato vartojimo būdas, DDD (angl. Defined daily dose, vidutinė paros dozė) įvertis, DDD įverčio matavimo vienetai ir papildomas stulpelis su DDD įverčio pastabomis. "[^manifest]

- **Model:** `datasets/gov/vvkt/vaistu_parametrai/VaistoDoze`[^manifest]
- **Dataset:** [Vaistinių preparatų vartojimo ir sudėties parametrai](../vaistu_parametrai.md) (`datasets/gov/vvkt/vaistu_parametrai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvkt/vaistu_parametrai.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L13)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai/VaistoDoze` (`deployed`)[^manifest]
- **Provider:** `vvkt` — Valstybinė vaistų kontrolės tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | "Unikalus Valstybės duomenų agentūros sugeneruotas eilutės identifikatorius. Eilutės unikalumą sudaro vid, atc_kodas, vartojimo_budas, ddd_pastabos" |
| `vid` | `string` | — | `4` | `open` | — | Vaistinio preparato identifikacinis numeris | — |
| `atc_kodas` | `string` | — | `4` | `open` | — | ATC kodas | "ATC (Anatomical Therapeutic Chemical) kodas – tarptautinė vaistų klasifikacijos sistema, kuri priskiria vaistus pagal jų terapinę ir cheminę klasifikaciją" |
| `vartojimo_budas` | `string` | — | `4` | `open` | — | Vartojimo būdas | Vaistinio preparato vartojimo būdas |
| `ddd` | `number` | — | `4` | `open` | — | Vidutinė paros dozė | Numanoma vidutinė paros dozė vaistui. DDD – Defined daily dose |
| `ddd_matav_vnt` | `string` | — | `4` | `open` | — | Vidutinės paros dozės matavimo vienetai | — |
| `ddd_pastabos` | `string` | — | `2` | `open` | — | DDD pastabos | Papildoma informacija apie vidutinės paros dozės įvertį |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistu_parametrai.csv#L13 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L13)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkt/vaistu_parametrai (https://data.gov.lt/datasets/3802/)
