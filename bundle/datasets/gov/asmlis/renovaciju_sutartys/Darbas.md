---
type: Table
title: "Darbas — Renovacijos darbų klasifikatorius"
description: "Viena renovacijos darbų klasifikatoriaus eilutė atitinka vieno renovacijos darbo pavadinimą"
resource: "https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys/Darbas"
tags: [gov, asmlis, darbas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L41"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv#L41"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3880/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/renovaciju_sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Darbas — Renovacijos darbų klasifikatorius

Viena renovacijos darbų klasifikatoriaus eilutė atitinka vieno renovacijos darbo pavadinimą[^manifest]

- **Model:** `datasets/gov/asmlis/renovaciju_sutartys/Darbas`[^manifest]
- **Dataset:** [Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”...](../renovaciju_sutartys.md) (`datasets/gov/asmlis/renovaciju_sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/renovaciju_sutartys.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L41)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys/Darbas` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `darbo_tipo_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `darbo_tipo_kodas` | `string` | — | `4` | `open` | — | Renovacijos darbo tipo kodas | — |
| `darbo_pavadinimas` | `string` | — | `4` | `open` | — | Renovacijos darbo pavadinimas | — |
| `paskut_redagav_data` | `datetime` | `L` | `4` | `open` | — | Renovacijos darbų paskutinio redagavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv#L41 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L41)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/renovaciju_sutartys (https://data.gov.lt/datasets/3880/)
