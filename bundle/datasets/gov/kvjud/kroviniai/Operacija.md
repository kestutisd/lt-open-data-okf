---
type: Table
title: "Operacija — Krovininių laivų operacijos Klaipėdos valstybinio jūrų uoste"
description: "Spinta table datasets/gov/kvjud/kroviniai/Operacija (19 columns)."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/kroviniai/Operacija"
tags: [gov, kvjud, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kvjud/kroviniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/kroviniai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Operacija — Krovininių laivų operacijos Klaipėdos valstybinio jūrų uoste

- **Model:** `datasets/gov/kvjud/kroviniai/Operacija`[^manifest]
- **Dataset:** [Krovininių laivų operacijos Klaipėdos valstybiniame jūrų uoste](../kroviniai.md) (`datasets/gov/kvjud/kroviniai`)
- **Manifest CSV:** [datasets/gov/kvjud/kroviniai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/kroviniai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/kroviniai/Operacija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agenūros įrašo unikalus identifikatorius | — |
| `operacijos_id` | `string` | — | `4` | `open` | — | Operacijos identifikatorius | — |
| `op_tipas` | `string` | — | `4` | `open` | — | Operacijos tipas | — |
| `op_rusis` | `string` | — | `4` | `open` | — | Operacijos rūšis | — |
| `data` | `datetime` | `S` | `4` | `open` | — | Operacijos data | — |
| `agentas` | `string` | — | `4` | `open` | — | Laivo savininko atstovas uoste | — |
| `imo_kodas` | `string` | — | `4` | `open` | — | Laivo IMO numeris | — |
| `laivas` | `string` | — | `4` | `open` | — | Laivo pavadinimas | — |
| `dedveitas_t` | `number` | `t` | `4` | `open` | — | Laivo dedveitas, išreikštas tonomis. | Dedveitas - tai dydis, nurodantis, kokios masės krovinį laivas gali saugiai gabenti. |
| `bendroji_talpa` | `number` | — | `4` | `open` | — | Laivo bendroji talpa | — |
| `laivo_tipas` | `string` | — | `4` | `open` | — | Laivo tipas | — |
| `veliava` | `string` | — | `4` | `open` | — | Laivo registravimo valstybė | — |
| `atvykimo_reg_nr` | `string` | — | `4` | `open` | — | Atvykimo registracijos numeris | — |
| `atvykimo_uostas` | `string` | — | `4` | `open` | — | Laivo atvykimo uostas | — |
| `faktinis_atvykimas` | `datetime` | `S` | `4` | `open` | — | Laivo faktinis atvykimo laikas | — |
| `isvykimo_loc` | `string` | — | `4` | `open` | — | Laivo išvykimo uosto LOC kodas | LOC kodas - tai penkiaženklis raidinis kodas |
| `isvykimo_mca` | `string` | — | `4` | `open` | — | Laivo išvykimo uosto MCA kodas | MCA - tai keturženklis jūrų pakrančių zonos kodas. |
| `isvykimo_uostas` | `string` | — | `4` | `open` | — | Laivo išvykimo uostas | — |
| `faktinis_isvykimas` | `datetime` | `S` | `4` | `open` | — | Laivo faktinis išvykimo laikas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `op_tipas` | `"ATV"` | — | — | Atvykimas | — |
| `op_tipas` | `"ISV"` | — | — | Išvykimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/kroviniai.csv
