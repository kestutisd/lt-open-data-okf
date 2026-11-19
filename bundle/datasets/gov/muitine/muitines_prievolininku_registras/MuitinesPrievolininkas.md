---
type: Table
title: "MuitinesPrievolininkas — Ekonominės veiklos vykdytojai įtraukti į MPR"
description: "Ekonominės veiklos vykdytojai ir kiti asmenys įtraukti į muitinės prievolininkų registrą"
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_prievolininku_registras/MuitinesPrievolininkas"
tags: [gov, muitine, muitinesprievolininkas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_prievolininkai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_prievolininkai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2705/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_prievolininku_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MuitinesPrievolininkas — Ekonominės veiklos vykdytojai įtraukti į MPR

**Dataset Context:** Ekonominės veiklos vykdytojai ir kiti asmenys įtraukti į muitinės prievolininkų registrą[^manifest]

- **Model:** `datasets/gov/muitine/muitines_prievolininku_registras/MuitinesPrievolininkas`[^manifest]
- **Dataset:** [Muitinės prievolininkų registras](../muitines_prievolininku_registras.md) (`datasets/gov/muitine/muitines_prievolininku_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/muitines_prievolininkai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_prievolininkai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_prievolininku_registras/MuitinesPrievolininkas` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `muitines_prievolininko_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `muitines_prievolininko_id` | `string` | — | `4` | `open` | — | Šifruotas įrašo ID | — |
| `salies_suteikusios_evv_id_kodas` | `string` | — | `4` | `open` | — | Šalies, kuri suteikė unikalų ekonominės veiklos vykdytojo identifikatorių, kodas | — |
| `id_nacionaliniame_domene` | `string` | — | `4` | `open` | — | Šifruotas unikalus ekonominės veiklos vykdytojo identifikatorius nacionaliniame domene | — |
| `evv_asmens_tipas` | `string` | — | `4` | `open` | — | Ekonominės veiklos vykdytojo asmens tipas | — |
| `evv_pavadinimas` | `string` | — | `4` | `open` | — | Šifruotas ekonominės veiklos vykdytojo pavadinimas (vardas, pavardė) | — |
| `iregistravimo_data` | `date` | `D` | `4` | `open` | — | Ekonominės veiklos vykdytojo įregistravimo MPR data | — |
| `isregistravimo_data` | `date` | `D` | `4` | `open` | — | Ekonominės veiklos vykdytojo išregistravimo iš MPR data | — |
| `buveines_salies_kodas` | `string` | — | `4` | `open` | — | Buveinės/gyvenamosios vietos adresas (šalies kodas) | — |
| `buveines_miesto_kodas` | `string` | — | `4` | `open` | — | Šifruotas buveinės/gyvenamosios vietos adresas (miestas) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_prievolininkai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_prievolininkai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_prievolininku_registras (https://data.gov.lt/datasets/2705/)
