---
type: Table
title: "TurtoTipas — Turto arešto aktų registro turto tipų klasifikatorius"
description: "Turto arešto aktų registro klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.): TAAR turto tipų klasifikatorius; TAAR tipų potipių klasifikatorius; TAAR dokumentų statusų klasifikatorius; TAAR areštuojančių institucijų klasifikatorius."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/klasifikatoriai/TurtoTipas"
tags: [gov, rc, turtotipas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/klasifikatoriai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/klasifikatoriai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2240/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/taar/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TurtoTipas — Turto arešto aktų registro turto tipų klasifikatorius

**Dataset Context:** Turto arešto aktų registro klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.): TAAR turto tipų klasifikatorius; TAAR tipų potipių klasifikatorius; TAAR dokumentų statusų klasifikatorius; TAAR areštuojančių institucijų klasifikatorius.[^manifest]

- **Model:** `datasets/gov/rc/taar/klasifikatoriai/TurtoTipas`[^manifest]
- **Dataset:** [TAAR klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/rc/taar/klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/taar/klasifikatoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/klasifikatoriai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/klasifikatoriai/TurtoTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Turto tipo kodas iš TAAR turto tipų klasifikatoriaus | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Turto tipo pavadinimas iš TAAR turto tipų klasifikatoriaus | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/klasifikatoriai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/klasifikatoriai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/taar/klasifikatoriai (https://data.gov.lt/datasets/2240/)
