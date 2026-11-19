---
type: Table
title: "Kvietimas — Aplinkos projektams pateiktų kvietimų duomenys"
description: "Aplinkos projektų valdymo informacinėje sistemoje (APVIS) nuo 2019-04-18 kaupiami ir iki šiol atnaujinami Aplinkos projektų valdymo agentūros (APVA) paviešintų kvietimų įstaigos inicijuotiems projektams duomenys."
resource: "https://get.data.gov.lt/datasets/gov/apva/apvis/Kvietimas"
tags: [gov, apva, kvietimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/apvis.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/apva/apvis.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2854/"
    title: "data.gov.lt DCAT-AP — datasets/gov/apva/apvis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kvietimas — Aplinkos projektams pateiktų kvietimų duomenys

Aplinkos projektų valdymo informacinėje sistemoje (APVIS) nuo 2019-04-18 kaupiami ir iki šiol atnaujinami Aplinkos projektų valdymo agentūros (APVA) paviešintų kvietimų įstaigos inicijuotiems projektams duomenys. Duomenų rinkinį sudaro: kvietimo identifikatorius, kodas ir pavadinimas, nurodyta, ar kviečiami dalyviai yra fiziniai arba juridiniai asmenys, kvietimo projektą įgyvendinti parinktos priemonės kodas ir pavadinimas, įstaigos kodas, kvietime numatytas finansavimas, kompensacinė išmoka, paraiškų priėmimo laikotarpis bei kvietimo puslapio nuoroda. Vienas įrašas atitinka vieną kvietimą. Dalies kvietimų nuorodos nenukreipia į aktyvų kvietimo puslapį, nes yra nebeaktualūs. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/apva/apvis/Kvietimas`[^manifest]
- **Dataset:** [Aplinkos projektams pateiktų kvietimų duomenys](../apvis.md) (`datasets/gov/apva/apvis`)[^manifest]
- **Manifest CSV:** [datasets/gov/apva/apvis.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/apvis.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/apva/apvis/Kvietimas` (`deployed`)[^manifest]
- **Provider:** `apva` — Aplinkos projektų valdymo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | Kvietimo kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Kvietimo pavadinimas | — |
| `dalyvio_rusis` | `string` | — | `4` | `open` | — | Kvietime kviečiamų asmenų rūšis | — |
| `priemones_kodas` | `string` | — | `4` | `open` | — | Kvietimo priemonės kodas | — |
| `priemone` | `string` | — | `4` | `open` | — | Kvietimo primonės pavadinimas | — |
| `istaigos_kodas` | `string` | — | `4` | `open` | — | Kvietimo priemonės įstaigos kodas | — |
| `numatytas_finansavimas` | `number` | — | `4` | `open` | — | Kvietimo projektui numatytas finansavimas | — |
| `kompensacine_ismoka` | `number` | — | `4` | `open` | — | Kvietimo projekto kompensacinė išmoka | — |
| `paraiskos_priimamos_nuo` | `datetime` | `M` | `4` | `open` | — | Kvietimo projektui paraiškų priėmimo pradžia | — |
| `paraiskos_priimamos_iki` | `datetime` | `M` | `4` | `open` | — | Kvietimo projektui paraiškų priėmimo pabaiga | — |
| `puslapis` | `string` | — | `4` | `open` | — | Kvietimo internetinio puslapio nuoroda | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dalyvio_rusis` | `"Juridinis"` | — | — | Juridinis | — |
| `dalyvio_rusis` | `"Fizinis"` | — | — | Fizinis | — |
| `dalyvio_rusis` | `"Visi"` | — | — | Visi asmenys | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `numatytas_finansavimas` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `kompensacine_ismoka` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/apva/apvis.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/apvis.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/apva/apvis (https://data.gov.lt/datasets/2854/)
