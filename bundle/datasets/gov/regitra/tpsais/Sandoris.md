---
type: Table
title: "Sandoris — Transporto priemonių sandorių duomenys"
description: "AB „Regitra“ Transporto priemonių savininkų apskaitos informacinė sistema kaupia transporto priemonių (toliau TP) savininkų bei jų vykdytų sandorių duomenis."
resource: "https://get.data.gov.lt/datasets/gov/regitra/tpsais/Sandoris"
tags: [gov, regitra, sandoris, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/tpsais.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/regitra/tpsais.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2812/"
    title: "data.gov.lt DCAT-AP — datasets/gov/regitra/tpsais"
    author: "team:vda"
    last_modified: "2026-08-27T00:00:00Z"
---

# Sandoris — Transporto priemonių sandorių duomenys

AB „Regitra“ Transporto priemonių savininkų apskaitos informacinė sistema kaupia transporto priemonių (toliau TP) savininkų bei jų vykdytų sandorių duomenis. Duomenys kaupiami nuo 2021-05-01 ir yra atnaujinami. Duomenų rinkinys sudarytas iš pseudonimizuotų dokumento identifikatoriaus bei išorinio rakto į sisteminę veiklą, iš dokumento rūšies, nurodančios santorio pobūdį, dokumento išdavimo datos, sandorio šalies, sumos, valiutos, atsiskaitymo būdo bei įrašo modifikavimo laiko. Vienas įrašas rinkinyje atitinka vieną sandorio dokumentą. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/regitra/tpsais/Sandoris`[^manifest]
- **Dataset:** [Transporto priemonių sandorių duomenys](../tpsais.md) (`datasets/gov/regitra/tpsais`)[^manifest]
- **Manifest CSV:** [datasets/gov/regitra/tpsais.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/tpsais.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/regitra/tpsais/Sandoris` (`deployed`)[^manifest]
- **Provider:** `regitra` — AB „Regitra“ *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `dok_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-08-27`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_id` | `string` | — | `4` | `open` | — | Pseudonimizuotas sandorio dokumento identifikatorius | — |
| `veiklos_id` | `string` | — | `4` | `open` | — | Pseudonimizuotas išorinis raktas į sisteminę veiklą | — |
| `dok_rusis` | `string` | — | `4` | `open` | — | Sandorio dokumento rūšis | — |
| `isd_data` | `datetime` | `D` | `4` | `open` | — | Dokumento išdavimo data | — |
| `salis` | `string` | — | `4` | `open` | — | Sandorio šalis | — |
| `suma` | `number` | — | `4` | `open` | — | Sandorio suma | — |
| `valiuta` | `string` | — | `4` | `open` | — | Sandorio valiuta | — |
| `mokejimo_budas` | `string` | — | `4` | `open` | — | Atsiskaitymo būdas sandoryje | — |
| `iraso_mod_data` | `datetime` | `S` | `4` | `open` | — | Įrašo modifikavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/regitra/tpsais.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/tpsais.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/regitra/tpsais (https://data.gov.lt/datasets/2812/)
