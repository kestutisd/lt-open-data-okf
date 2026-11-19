---
type: Table
title: "SeiminePadetis — Gyventojų registro duomenys apie gyventojų šeiminę padėtį, vaikų skaičių savivaldybėse"
description: "Spinta table datasets/gov/rc/gr/seimines_padetys/SeiminePadetis (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/seimines_padetys/SeiminePadetis"
tags: [gov, rc, seiminepadetis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/seimines_padetys.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/seimines_padetys.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1748/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/gr/seimines_padetys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SeiminePadetis — Gyventojų registro duomenys apie gyventojų šeiminę padėtį, vaikų skaičių savivaldybėse

- **Model:** `datasets/gov/rc/gr/seimines_padetys/SeiminePadetis`[^manifest]
- **Dataset:** [Gyventojų registro duomenys apie gyventojų šeiminę padėtį, vaikų skaičių savivaldybėse](../seimines_padetys.md) (`datasets/gov/rc/gr/seimines_padetys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/gr/seimines_padetys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/seimines_padetys.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/seimines_padetys/SeiminePadetis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Gyventojo eilės numeris šiame duomenų rinkinyje | — |
| `lytis` | `string` | — | `4` | `open` | — | Gyventojo lytis (V - Vyras; M - Moteris) | — |
| `amzius` | `string` | — | `3` | `open` | — | Gyventojo amžius / amžiaus grupė | — |
| `seim_statusas` | `string` | — | `3` | `open` | — | Gyventojo šeiminė padėtis (nevedęs / netekėjusi, vedęs / ištekėjusi, našlys / našlė, išsiskyręs / išsiskyrusi) | — |
| `vaiku_sk` | `string` | — | `3` | `open` | — | Gyventojo turimų vaikų skaičius | — |
| `vaiku_sk_nuo_0_iki_6` | `integer` | `U` | `4` | `open` | — | Gyventojo turimų vaikų skaičius (nuo 0 iki 6 metų imtinai); | — |
| `vaiku_sk_nuo_7_iki_17` | `integer` | `U` | `4` | `open` | — | Gyventojo turimų vaikų skaičius (nuo 7 iki 17 metų imtinai); | — |
| `dek_metai` | `integer` | — | `2` | `open` | — | Gyventojo gyvenamosios vietos deklaravimo metai | — |
| `dek_ketvirtis` | `string` | — | `2` | `open` | — | Gyventojo gyvenamosios vietos deklaravimo metų ketvirtis | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybė, kurioje deklaruota gyventojo gyvenamoji vieta, iš Adresų registro | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/seimines_padetys.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/seimines_padetys.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/gr/seimines_padetys (https://data.gov.lt/datasets/1748/)
