---
type: Table
title: "LeidimoDuomuo — Leidimų duomenys"
description: "Papildomos leidimo detalės eilutėmis (po vieną detalę per eilutę)."
resource: "https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys/LeidimoDuomuo"
tags: [gov, muitine, leidimoduomuo, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L21"
    title: "atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv#L21"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3915/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/leidimu_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# LeidimoDuomuo — Leidimų duomenys

Papildomos leidimo detalės eilutėmis (po vieną detalę per eilutę). Čia telpa įvairios sąlygos, pastabos ar kiti specifiniai laukeliai, kurių prireikia tik kai kuriems leidimų tipams.[^manifest]

- **Model:** `datasets/gov/muitine/leidimu_duomenys/LeidimoDuomuo`[^manifest]
- **Dataset:** [Muitinės leidimų sistemos leidimų ir prašymų duomenys](../leidimu_duomenys.md) (`datasets/gov/muitine/leidimu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/leidimu_duomenys.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L21)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys/LeidimoDuomuo` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `spec_aun` | `string` | — | `4` | `open` | — | Leidimo registracijos numeris (AUN) | — |
| `spec_tipo_kod` | `string` | — | `4` | `open` | — | Leidimo rūšies kodas | — |
| `leid_pavadinimas` | `string` | — | `4` | `open` | — | Leidimo rūšies pavadinimas | — |
| `spec_isdavimo_data` | `date` | `D` | `4` | `open` | — | Leidimo išdavimo data | — |
| `leid_busenos_kod` | `string` | — | `4` | `open` | — | Leidimo būsenos kodas | — |
| `leid_busena` | `string` | — | `4` | `open` | — | Leidimo būsena | — |
| `spec_elem_pav` | `string` | — | `4` | `open` | — | Specifinio duomenų elemento pavadinimas | — |
| `spec_elem_reiks` | `string` | — | `4` | `open` | — | Specifinio duomenų elemento reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv#L21 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L21)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/leidimu_duomenys (https://data.gov.lt/datasets/3915/)
