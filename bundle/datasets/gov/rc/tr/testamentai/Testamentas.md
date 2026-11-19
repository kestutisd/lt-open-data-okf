---
type: Table
title: "Testamentas"
description: "Spinta table datasets/gov/rc/tr/testamentai/Testamentas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/tr/testamentai/Testamentas"
tags: [gov, rc, testamentas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/testamentai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/tr/testamentai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2141/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/tr/testamentai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Testamentas

- **Model:** `datasets/gov/rc/tr/testamentai/Testamentas`[^manifest]
- **Dataset:** [Testamentų registro (TR) duomenys apie testamentus](../testamentai.md) (`datasets/gov/rc/tr/testamentai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/tr/testamentai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/testamentai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/tr/testamentai/Testamentas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Registro objekto identifikavimo kodas šiame duomenų rinkinyje | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Registro objekto pavadinimas | — |
| `testamento_rusis` | `ref` | [TrRusis](../tr_klasifikatoriai/TrRusis.md) (`level=4 UUID`: `testamento_rusis._id`) | `4` | `open` | — | Testamento rūšis | — |
| `sudaryta_uzs` | `integer` | — | `4` | `open` | — | Ar sudarytas užsienyje | — |
| `reg_data` | `string` | — | `3` | `open` | — | Testamento įregistravimo laikotarpis (metai - ketvirtis) | — |
| `isreg_data` | `string` | — | `3` | `open` | — | Testamento išregistravimo laikotarpis (metai - ketvirtis) | — |
| `busena_id` | `integer` | — | `4` | `open` | — | Testamento būsenos identifikatorius | — |
| `bus_pavadinimas` | `string` | — | `3` | `open` | — | Testamento būsenos pavadinimas | — |
| `teikejas` | `string` | — | `3` | `open` | — | Duomenų teikėjas | — |
| `testatorius_lytis` | `string` | — | `4` | `open` | — | Testatoriaus Lytis | — |
| `uzsienietis` | `integer` | — | `4` | `open` | — | Požymis ar užsienietis | — |
| `testatorius_amzius` | `string` | — | `3` | `open` | — | Testatoriaus amžiaus grupė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sudaryta_uzs` | `1` | — | — | Testamentas sudarytas užsienyje | — |
| `sudaryta_uzs` | `0` | — | — | Testamentas sudarytas Lietuvoje | — |
| `testatorius_lytis` | `"V"` | — | — | Vyras | — |
| `testatorius_lytis` | `"M"` | — | — | Moteris | — |
| `testatorius_lytis` | `"ND"` | — | — | Nėra duomenų | — |
| `uzsienietis` | `1` | — | — | Užsienietis | — |
| `uzsienietis` | `0` | — | — | Lietuvos Respublikos pilietis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/tr/testamentai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/testamentai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/tr/testamentai (https://data.gov.lt/datasets/2141/)
