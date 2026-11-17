---
type: Table
title: "JuridinisSkolininkas"
description: "Spinta table datasets/gov/rc/taar/juridiniai_skolininkai/JuridinisSkolininkas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/juridiniai_skolininkai/JuridinisSkolininkas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/juridiniai_skolininkai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/juridiniai_skolininkai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# JuridinisSkolininkas

- **Model:** `datasets/gov/rc/taar/juridiniai_skolininkai/JuridinisSkolininkas`[^manifest]
- **Dataset:** [TAAR pirminiai duomenys (raw data) apie skolininkus (skolininkai juridiniai asmenys)](../juridiniai_skolininkai.md) (`datasets/gov/rc/taar/juridiniai_skolininkai`)
- **Manifest CSV:** [datasets/gov/rc/taar/juridiniai_skolininkai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/juridiniai_skolininkai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/juridiniai_skolininkai/JuridinisSkolininkas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Turto arešto akto dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `dokumento_statusas` | `ref` | [/datasets/gov/rc/taar/klasifikatoriai/DokumentoStatusas](../klasifikatoriai/DokumentoStatusas.md) | `4` | `open` | — | Turto arešto akto statusas iš TAAR dokumentų statusų klasifikatoriaus | — |
| `ai_tipas` | `ref` | [/datasets/gov/rc/taar/klasifikatoriai/AI](../klasifikatoriai/AI.md) | `4` | `open` | — | Areštuojančios institucijos tipas iš TAAR areštuojančių institucijų klasifikatoriaus | — |
| `skolininkoid` | `integer` | — | `4` | `open` | — | Juridinio asmens dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `jar_teisine_forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../../jar/formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens teisinė forma iš JAR teisinių formų klasifikatoriaus | — |
| `ar_uzsienietis` | `integer` | — | `4` | `open` | — | Požymis, ar Juridinis asmuo įregistruotas Juridinių asmenų registre | — |
| `taa_iregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo metai | — |
| `taa_iregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo mėnuo | — |
| `taa_isregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo metai | — |
| `taa_isregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo mėnuo | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ar_uzsienietis` | `1` | — | — | Taip | — |
| `ar_uzsienietis` | `0` | — | — | Ne | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/juridiniai_skolininkai.csv
