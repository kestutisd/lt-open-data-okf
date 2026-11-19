---
type: Table
title: "NTArestas"
description: "Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie areštuojamą nekilnojamąjį turtą, nekilnojamojo turto tipą ir potipį, turto arešto aktų jų statusus, įregistravimo / išregistravimo datas, areštuojančią instituciją."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/nt_arestai/NTArestas"
tags: [gov, rc, ntarestas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/nt_arestai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/nt_arestai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2236/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/taar/nt_arestai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NTArestas

**Dataset Context:** Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie areštuojamą nekilnojamąjį turtą, nekilnojamojo turto tipą ir potipį, turto arešto aktų jų statusus, įregistravimo / išregistravimo datas, areštuojančią instituciją.[^manifest]

- **Model:** `datasets/gov/rc/taar/nt_arestai/NTArestas`[^manifest]
- **Dataset:** [TAAR pirminiai duomenys (raw data) apie areštuotą nekilnojamąjį turtą](../nt_arestai.md) (`datasets/gov/rc/taar/nt_arestai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/taar/nt_arestai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/nt_arestai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/nt_arestai/NTArestas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Turto arešto akto dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `ntid` | `integer` | — | `4` | `open` | — | Nekilnojamojo turto dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `turto_tipas` | `ref` | [TurtoTipas](../klasifikatoriai/TurtoTipas.md) (`level=4 UUID`: `turto_tipas._id`) | `4` | `open` | — | Turto tipas iš TAAR turto tipų klasifikatoriaus | — |
| `turto_potipis` | `ref` | [TurtoPotipis](../klasifikatoriai/TurtoPotipis.md) (`level=4 UUID`: `turto_potipis._id`) | `4` | `open` | — | Turto potipis iš TAAR turto tipų klasifikatoriaus | — |
| `dokumento_statusas` | `ref` | [DokumentoStatusas](../klasifikatoriai/DokumentoStatusas.md) (`level=4 UUID`: `dokumento_statusas._id`) | `4` | `open` | — | Turto arešto akto statusas iš TAAR dokumentų statusų klasifikatoriaus | — |
| `iregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo metai | — |
| `iregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo mėnuo | — |
| `isregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo metai | — |
| `isregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo mėnuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/nt_arestai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/nt_arestai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/taar/nt_arestai (https://data.gov.lt/datasets/2236/)
