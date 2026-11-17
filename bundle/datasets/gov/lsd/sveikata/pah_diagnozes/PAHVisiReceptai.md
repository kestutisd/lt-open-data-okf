---
type: Table
title: "PAHVisiReceptai — Visi galiojantys receptai, išrašyti nurodant PAH diagnozę"
description: "Visi galiojantys receptai, išrašyti nurodant PAH diagnozę (I27.0, I27.2, I27.8 TLK-10-AM) ir nesaistomi konfidencialumo apribojimų."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes/PAHVisiReceptai"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L39"
    last_modified: "2026-11-11T14:39:20Z"
---

# PAHVisiReceptai — Visi galiojantys receptai, išrašyti nurodant PAH diagnozę

Visi galiojantys receptai, išrašyti nurodant PAH diagnozę (I27.0, I27.2, I27.8 TLK-10-AM) ir nesaistomi konfidencialumo apribojimų. Pateikiama recepto išrašymo data (su triukšmu iki 5 dienų), vaisto ATC kodas, bendrinis pavadinimas, požymis, ar vaistas išduotas, savivaldybė, kurioje veikiančioje įstaigoje išduotas vaistas (nustatoma pagal įstaigos filialą, kuriame dirba išdavęs specialistas tuo metu).

- **Model:** `datasets/gov/lsd/sveikata/pah_diagnozes/PAHVisiReceptai`[^manifest]
- **Dataset:** [Pacientų, sergančių plaučių arterine hipertenzija, gydymo duomenys](../pah_diagnozes.md) (`datasets/gov/lsd/sveikata/pah_diagnozes`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/pah_diagnozes.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L39)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes/PAHVisiReceptai`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `diagnoz_kodas` | `string` | — | `4` | `open` | — | Diagnozės TLK-10-AM kodas | — |
| `diagnoz_pav` | `string` | — | `4` | `open` | — | Diagnozės pavadinimas | — |
| `israsymo_data` | `date` | `D` | `4` | `open` | — | Recepto išrašymo data | Recepto išrašymo data, su triukšmu iki 5 d. |
| `vaisto_atc_kodas` | `string` | — | `4` | `open` | — | Vaisto ATC kodas | — |
| `vaisto_bendr_pav` | `string` | — | `4` | `open` | — | Vaisto bendrinis pavadinimas | — |
| `ar_isduotas` | `boolean` | — | `4` | `open` | — | Ar vaistas išduotas | Požymis, ar vaistas buvo išduotas |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv
