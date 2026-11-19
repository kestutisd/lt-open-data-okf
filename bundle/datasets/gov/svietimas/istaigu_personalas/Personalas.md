---
type: Table
title: "Personalas"
description: "Lietuvos savivaldybių švietimo įstaigų personalo duomenys"
resource: "https://get.data.gov.lt/datasets/gov/svietimas/istaigu_personalas/Personalas"
tags: [gov, svietimas, personalas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/svietimas/istaigu_personalas.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/svietimas/istaigu_personalas.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3815/"
    title: "data.gov.lt DCAT-AP — datasets/gov/svietimas/istaigu_personalas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Personalas

Lietuvos savivaldybių švietimo įstaigų personalo duomenys[^manifest]

- **Model:** `datasets/gov/svietimas/istaigu_personalas/Personalas`[^manifest]
- **Dataset:** [Lietuvos savivaldybių švietimo įstaigų personalas](../istaigu_personalas.md) (`datasets/gov/svietimas/istaigu_personalas`)[^manifest]
- **Manifest CSV:** [datasets/gov/svietimas/istaigu_personalas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/svietimas/istaigu_personalas.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/svietimas/istaigu_personalas/Personalas` (`deployed`)[^manifest]
- **Provider:** `svietimas`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `tabelio_numeris` | `string` | — | `4` | `open` | — | Tabelio numeris | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `ak_validacija` | `string` | — | `4` | `open` | — | Požymis ar asmens kodas validus | — |
| `gimimo_desimtmetis` | `date` | `10Y` | `4` | `open` | — | Gimimo datos dešimtmetis iš asmens kodo | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | — |
| `dirba_nuo` | `date` | `M` | `4` | `open` | — | Dirba nuo | — |
| `dirba_iki` | `date` | `M` | `4` | `open` | — | Dirba iki | — |
| `pareigos` | `string` | — | `4` | `open` | — | Asmens pareigos | — |
| `etatu_skaicius` | `number` | — | `4` | `open` | — | Etato dydis | — |
| `projektas_mokykla` | `string` | — | `4` | `open` | — | Projektinė ar ugdomoji veikla | — |
| `institucija` | `string` | — | `4` | `open` | — | Švietimo įstaigos pavadinimas | — |
| `institucijos_kodas` | `string` | — | `4` | `open` | — | Švietimo įstaigos JAR kodas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_ak` | `"Moteris"` | — | — | Moteris | — |
| `lytis_ak` | `"Vyras"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/svietimas/istaigu_personalas.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/svietimas/istaigu_personalas.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/svietimas/istaigu_personalas (https://data.gov.lt/datasets/3815/)
