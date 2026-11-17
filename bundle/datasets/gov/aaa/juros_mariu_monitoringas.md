---
type: Dataset
title: "datasets/gov/aaa/juros_mariu_monitoringas"
description: "Spinta dataset datasets/gov/aaa/juros_mariu_monitoringas (9 tables)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas"
tags: [gov, aaa, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/aaa/juros_mariu_monitoringas

- **Namespace:** `datasets/gov/aaa/juros_mariu_monitoringas`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/juros_mariu_monitoringas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Hidrochemija](juros_mariu_monitoringas/Hidrochemija.md) | Kuršių marių ir Baltijos jūros hidrocheminių parametrų tyrimai vandenyje | `2` | `reg_nr` | — | 14 | — |
| [Hidrometeorologija](juros_mariu_monitoringas/Hidrometeorologija.md) | Kuršių marių ir Baltijos jūros hidrologinių matavimų vandenyje ir meteorologinių stebėjimų duomenys | `2` | `reg_nr` | — | 13 | — |
| [ChlorofilasA](juros_mariu_monitoringas/ChlorofilasA.md) | Kuršių marių ir Baltijos jūros chlorofilo a tyrimų duomenys | `4` | `reg_nr` | — | 14 | — |
| [Fitoplanktonas](juros_mariu_monitoringas/Fitoplanktonas.md) | Kuršių marių ir Baltijos jūros fitoplanktono tyrimų duomenys | `2` | `reg_nr` | — | 22 | — |
| [Zoobentosas](juros_mariu_monitoringas/Zoobentosas.md) | Kuršių marių ir Baltijos jūros zoobentoso tyrimų duomenys | `2` | `reg_nr` | — | 18 | — |
| [Zooplanktonas](juros_mariu_monitoringas/Zooplanktonas.md) | Kuršių marių ir Baltijos jūros zooplanktono tyrimų duomenys | `2` | `reg_nr` | — | 18 | — |
| [SpTersalaiV](juros_mariu_monitoringas/SpTersalaiV.md) | Specifinių teršalų tyrimai Kuršių marių ir Baltijos jūros vandenyje | `2` | `reg_nr` | — | 14 | — |
| [SpTersalaiDN](juros_mariu_monitoringas/SpTersalaiDN.md) | Specifinių teršalų tyrimai Kuršių marių ir Baltijos jūros dugno nuosėdose | `2` | `reg_nr` | — | 15 | — |
| [SpTersalaiB](juros_mariu_monitoringas/SpTersalaiB.md) | Specifinių teršalų tyrimai Kuršių marių ir Baltijos jūros biotoje | `2` | `reg_nr` | — | 18 | — |

# Enumerations

| Enum (`ref`) | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `nustatymo_zyme` | `'SP'` | — | — | Nėra galimybės arba nereikia nurodyti konkretaus rūšies pavadinimo | — |
| `nustatymo_zyme` | `'SPP'` | — | — | Kelios nenustatytos tos pačios genties rūšys | — |
| `nustatymo_zyme` | `'CF'` | — | — | Žymėjimas dedamas tarp genties ir rūšies pavadinimo, reiškiantis, kad individas kaip įmanoma (su tam tikra abejone) atpažintas iki rūšies | — |
| `nustatymo_zyme` | `'CPX'` | — | — | Žymėjimas reiškia, kad yra labai panašių viena į kitą rūšių grupė pavadinta pagal labiausiai paplitusią rūšį regione | — |
| `nustatymo_zyme` | `'VARIA'` | — | — | Žymima, kai individai identifikuojami iki klasės | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv
