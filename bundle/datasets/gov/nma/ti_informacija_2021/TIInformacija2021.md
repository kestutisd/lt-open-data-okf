---
type: Table
title: "TIInformacija2021 — Tiesioginės ir kompensacinės išmokos už deklaruotos plotus ir (arba) gyvulius. Bendra informacija. 2021 m."
description: "Spinta table datasets/gov/nma/ti_informacija_2021/TIInformacija2021 (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/ti_informacija_2021/TIInformacija2021"
tags: [gov, nma, tiinformacija2021, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/ti_informacija_2021.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/nma/ti_informacija_2021.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2322/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nma/ti_informacija_2021"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TIInformacija2021 — Tiesioginės ir kompensacinės išmokos už deklaruotos plotus ir (arba) gyvulius. Bendra informacija. 2021 m.

- **Model:** `datasets/gov/nma/ti_informacija_2021/TIInformacija2021`[^manifest]
- **Dataset:** [Tiesioginės ir kompensacinės išmokos už deklaruotos plotus ir (arba) gyvulius. Bendra...](../ti_informacija_2021.md) (`datasets/gov/nma/ti_informacija_2021`)[^manifest]
- **Manifest CSV:** [datasets/gov/nma/ti_informacija_2021.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/ti_informacija_2021.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/ti_informacija_2021/TIInformacija2021` (`deployed`)[^manifest]
- **Provider:** `nma` — Nacionalinė mokėjimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė | — |
| `programa` | `string` | — | `3` | `open` | — | Programa | — |
| `deklaruoti_hektarai` | `number` | `ha` | `4` | `open` | — | Deklaruoti hektarai pagal programą | — |
| `patvirtinti_hektarai` | `number` | `ha` | `4` | `open` | — | Patvirtinti hektarai pagal programą | — |
| `prasoma_suma` | `number` | — | `2` | `open` | — | Prašoma paramos suma | — |
| `ismoketa_suma` | `number` | — | `2` | `open` | — | Išmokėta paramos suma | — |
| `valda` | `string` | — | `4` | `open` | — | Valda | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `pareiskejo_tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `pareiskejo_lytis` | `"V"` | — | — | Vyras | — |
| `pareiskejo_lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `prasoma_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `ismoketa_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/ti_informacija_2021.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/ti_informacija_2021.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nma/ti_informacija_2021 (https://data.gov.lt/datasets/2322/)
