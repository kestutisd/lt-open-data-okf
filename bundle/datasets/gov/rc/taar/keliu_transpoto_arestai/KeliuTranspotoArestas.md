---
type: Table
title: "KeliuTranspotoArestas"
description: "Spinta table datasets/gov/rc/taar/keliu_transpoto_arestai/KeliuTranspotoArestas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/keliu_transpoto_arestai/KeliuTranspotoArestas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/keliu_transpoto_arestai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/keliu_transpoto_arestai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# KeliuTranspotoArestas

- **Model:** `datasets/gov/rc/taar/keliu_transpoto_arestai/KeliuTranspotoArestas`[^manifest]
- **Dataset:** [TAAR pirminiai duomenys (raw data) apie areštuotas kelių transporto priemones](../keliu_transpoto_arestai.md) (`datasets/gov/rc/taar/keliu_transpoto_arestai`)
- **Manifest CSV:** [datasets/gov/rc/taar/keliu_transpoto_arestai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/keliu_transpoto_arestai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/keliu_transpoto_arestai/KeliuTranspotoArestas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Turto arešto akto dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `ktpid` | `integer` | — | `4` | `open` | — | Kelių transporto priemonės dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `turto_tipas` | `ref` | [/datasets/gov/rc/taar/klasifikatoriai/TurtoTipas](../klasifikatoriai/TurtoTipas.md) | `4` | `open` | — | Turto tipas iš TAAR turto tipų klasifikatoriaus | — |
| `dokumento_statusas` | `ref` | [/datasets/gov/rc/taar/klasifikatoriai/DokumentoStatusas](../klasifikatoriai/DokumentoStatusas.md) | `4` | `open` | — | Turto arešto akto statusas iš TAAR dokumentų statusų klasifikatoriaus | — |
| `iregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo metai | — |
| `iregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo mėnuo | — |
| `isregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo metai | — |
| `isregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo mėnuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/keliu_transpoto_arestai.csv
