---
type: Table
title: "Paraiska — Mokslinių tyrimų ir eksperimentinės plėtros (MTEP) finansavimo priemonėse finansuotų projektų duomenys"
description: "Spinta table datasets/gov/mita/paraiskos/Paraiska (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/mita/paraiskos/Paraiska"
tags: [gov, mita, paraiska, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/paraiskos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/mita/paraiskos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1444/"
    title: "data.gov.lt DCAT-AP — datasets/gov/mita/paraiskos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Paraiska — Mokslinių tyrimų ir eksperimentinės plėtros (MTEP) finansavimo priemonėse finansuotų projektų duomenys

- **Model:** `datasets/gov/mita/paraiskos/Paraiska`[^manifest]
- **Dataset:** [Mokslo, inovacijų ir technologijų agentūros administruojamose mokslinių tyrimų ir...](../paraiskos.md) (`datasets/gov/mita/paraiskos`)[^manifest]
- **Manifest CSV:** [datasets/gov/mita/paraiskos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/paraiskos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/mita/paraiskos/Paraiska` (`deployed`)[^manifest]
- **Provider:** `mita` — Mokslo, inovacijų ir technologijų agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Paraiškos kodas | Teiktos paraiškos finansavimui gauti kodas |
| `pavadinimas` | `string` | — | `4` | `open` | — | Paraiškos pavadinimas | Teiktos paraiškos pavadinimas |
| `mokslo_sritis` | `string` | — | `2` | `open` | — | Mokslo sritis | Atitinka Mokslo ir meno sričių klasifikatorių (patvirtinta LR Vyriausybės 2018 m. gruodžio 19 d. nutarimu Nr. 1317) |
| `mokslo_kryptis` | `string` | — | `2` | `open` | — | Mokslo kryptis | Atitinka Mokslo ir meno krypčių klasifikatorių (patvirtinta LR švietimo, mokslo ir sporto ministro 2019 m. vasario 6 d. įsakymu Nr. V-93 (2019 m. vasario 20 d. įsakymo Nr. V-156 redakcija) |
| `organizacija` | `string` | — | `2` | `open` | — | Organizacija | Paraiškos teikėjas |
| `finansavimas` | `number` | — | `2` | `open` | — | Skirtas finansavimas | — |
| `kvietimo_pavadinimas` | `string` | — | `3` | `open` | — | Kvietimo pavadinimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `finansavimas` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/mita/paraiskos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/paraiskos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/mita/paraiskos (https://data.gov.lt/datasets/1444/)
