---
type: Table
title: "TurtoArestoAktas"
description: "Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie turto arešto aktus, jų statusus, įregistravimo / išregistravimo datas, areštuojančią instituciją, turto arešto mastą (rėžius), jeigu nustatomas."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/turto_aresto_aktai/TurtoArestoAktas"
tags: [gov, rc, turtoarestoaktas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/turto_aresto_aktai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/turto_aresto_aktai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2231/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/taar/turto_aresto_aktai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TurtoArestoAktas

**Dataset Context:** Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie turto arešto aktus, jų statusus, įregistravimo / išregistravimo datas, areštuojančią instituciją, turto arešto mastą (rėžius), jeigu nustatomas.[^manifest]

- **Model:** `datasets/gov/rc/taar/turto_aresto_aktai/TurtoArestoAktas`[^manifest]
- **Dataset:** [TAAR pirminiai duomenys (raw data) apie turto arešto aktus](../turto_aresto_aktai.md) (`datasets/gov/rc/taar/turto_aresto_aktai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/taar/turto_aresto_aktai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/turto_aresto_aktai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/turto_aresto_aktai/TurtoArestoAktas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Turto arešto akto dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `dokumento_statusas` | `ref` | [DokumentoStatusas](../klasifikatoriai/DokumentoStatusas.md) (`level=4 UUID`: `dokumento_statusas._id`) | `4` | `open` | — | Turto arešto akto statusas iš TAAR dokumentų statusų klasifikatoriaus | — |
| `ai_tipas` | `ref` | [AI](../klasifikatoriai/AI.md) (`level=4 UUID`: `ai_tipas._id`) | `4` | `open` | — | Areštuojančios institucijos tipas iš TAAR areštuojančių institucijų klasifikatoriaus | — |
| `mastas_rez` | `string` | — | `3` | `open` | — | Turto arešto mastas (rėžiai), jeigu nustatomas | — |
| `taa_iregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo metai | — |
| `taa_iregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo mėnuo | — |
| `taa_isregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo metai | — |
| `taa_isregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto išegistravimo mėnuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/turto_aresto_aktai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/turto_aresto_aktai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/taar/turto_aresto_aktai (https://data.gov.lt/datasets/2231/)
