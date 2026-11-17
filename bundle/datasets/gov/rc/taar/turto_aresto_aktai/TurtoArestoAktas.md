---
type: Table
title: "TurtoArestoAktas"
description: "Spinta table datasets/gov/rc/taar/turto_aresto_aktai/TurtoArestoAktas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/turto_aresto_aktai/TurtoArestoAktas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/turto_aresto_aktai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/turto_aresto_aktai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# TurtoArestoAktas

- **Model:** `datasets/gov/rc/taar/turto_aresto_aktai/TurtoArestoAktas`[^manifest]
- **Dataset:** [TAAR pirminiai duomenys (raw data) apie turto arešto aktus](../turto_aresto_aktai.md) (`datasets/gov/rc/taar/turto_aresto_aktai`)
- **Manifest CSV:** [datasets/gov/rc/taar/turto_aresto_aktai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/turto_aresto_aktai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/turto_aresto_aktai/TurtoArestoAktas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Turto arešto akto dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `dokumento_statusas` | `ref` | [/datasets/gov/rc/taar/klasifikatoriai/DokumentoStatusas](../klasifikatoriai/DokumentoStatusas.md) | `4` | `open` | — | Turto arešto akto statusas iš TAAR dokumentų statusų klasifikatoriaus | — |
| `ai_tipas` | `ref` | [/datasets/gov/rc/taar/klasifikatoriai/AI](../klasifikatoriai/AI.md) | `4` | `open` | — | Areštuojančios institucijos tipas iš TAAR areštuojančių institucijų klasifikatoriaus | — |
| `mastas_rez` | `string` | — | `3` | `open` | — | Turto arešto mastas (rėžiai), jeigu nustatomas | — |
| `taa_iregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo metai | — |
| `taa_iregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo mėnuo | — |
| `taa_isregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo metai | — |
| `taa_isregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto išegistravimo mėnuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/turto_aresto_aktai.csv
