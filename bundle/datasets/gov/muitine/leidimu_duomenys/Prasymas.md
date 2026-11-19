---
type: Table
title: "Prasymas — Prašymai"
description: "Pateiktas prašymas gauti leidimą."
resource: "https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys/Prasymas"
tags: [gov, muitine, prasymas, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L32"
    title: "atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv#L32"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3915/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/leidimu_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Prasymas — Prašymai

Pateiktas prašymas gauti leidimą. Matosi, kas kreipėsi, ko prašo, kokia prašymo būsena (pateiktas, nagrinėjamas, patvirtintas ar atmestas) ir kada jis sukurtas.[^manifest]

- **Model:** `datasets/gov/muitine/leidimu_duomenys/Prasymas`[^manifest]
- **Dataset:** [Muitinės leidimų sistemos leidimų ir prašymų duomenys](../leidimu_duomenys.md) (`datasets/gov/muitine/leidimu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/leidimu_duomenys.csv#L32](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L32)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys/Prasymas` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `pras_lrn` | `string` | — | `4` | `open` | — | Pareiškėjo prašymui suteiktas unikalus numeris (LRN) | — |
| `pras_arn` | `string` | — | `4` | `open` | — | Prašymo registracijos numeris (ARN) | — |
| `pras_aun_ref` | `string` | — | `4` | `open` | — | Leidimo registracijos numeris (AUN) | — |
| `pras_asm_ident_nr` | `string` | — | `4` | `open` | — | Pareiškėjo kodas | — |
| `pras_asm_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo kodo rūšis | — |
| `pras_nagr_ist` | `string` | — | `4` | `open` | — | Prašymą nagrinėjančios muitinės įstaigos kodas | — |
| `pras_tipo_kod` | `string` | — | `4` | `open` | — | Prašymo rūšies kodas | — |
| `pras_pavadinimas` | `string` | — | `4` | `open` | — | Prašymo rūšies pavadinimas | — |
| `pras_busenos_kod` | `string` | — | `4` | `open` | — | Prašymo būsenos kodas | — |
| `pras_busena` | `string` | — | `4` | `open` | — | Prašymo būsena | — |
| `pras_sukurimo_data` | `date` | `D` | `4` | `open` | — | Prašymo sukūrimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv#L32 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L32)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/leidimu_duomenys (https://data.gov.lt/datasets/3915/)
