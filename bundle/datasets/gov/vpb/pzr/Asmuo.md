---
type: Table
title: "Asmuo — Prekių ženklams priskirti asmenys"
description: "Lentelė „Prekių ženklams priskirti asmenys“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/pzr/Asmuo"
tags: [gov, vpb, asmuo, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/vpb/pzr.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3809/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/pzr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Asmuo — Prekių ženklams priskirti asmenys

Lentelė „Prekių ženklams priskirti asmenys“. Lentelę sudaro: prekės ir paraiškos numeriai, priskirto juridinio asmens pavadinimas arba fizinio asmens vardas ir pavardė, asmens tipas, vaidmuo prekės ženkle, pateiktas adresas ir šalis. Vienas įrašas atitinka vieną unikalią prekės ženklo registracijos, paraiškos numerių, asmens, jo adreso ir vaidmens prekės ženkle kombinaciją.[^manifest]

- **Model:** `datasets/gov/vpb/pzr/Asmuo`[^manifest]
- **Dataset:** [Lietuvos Respublikos prekių ženklai](../pzr.md) (`datasets/gov/vpb/pzr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/pzr.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/pzr/Asmuo` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Prekės ženklo bylos registracijos numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Prekės ženklo bylos paraiškos numeris | — |
| `asmuo` | `string` | — | `4` | `open` | — | Prekės ženklui priskirto fizinio asmens vardas su pavarde arba juridinio asmens pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Prekės ženklui priskirto asmens tipas | — |
| `vaidmuo` | `string` | — | `4` | `open` | — | Prekės ženklui priskirto asmens vaidmuo | — |
| `salis` | `string` | — | `4` | `open` | — | Prekės ženkui priskirto asmens šalis | — |
| `adresas` | `string` | — | `4` | `open` | — | Prekės ženkui priskirto asmens adresas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Fizinis"` | — | `open` | Fizinis asmuo | — |
| `tipas` | `"Juridinis"` | — | `open` | Juridinis asmuo | — |
| `vaidmuo` | `"Pareiškėjas"` | — | — | Pareiškėjas | — |
| `vaidmuo` | `"Atstovas"` | — | — | Atstovas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/pzr.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L27)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/pzr (https://data.gov.lt/datasets/3809/)
