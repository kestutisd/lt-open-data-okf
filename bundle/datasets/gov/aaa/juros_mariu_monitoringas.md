---
type: Dataset
title: "Kuršių marių ir Baltijos jūros valstybinio monitoringo duomenys"
description: "Rinkinyje pateikiami valstybinio Kuršių marių ir Baltijos jūros aplinkos monitoringo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas"
tags: [gov, aaa, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1790/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/juros_mariu_monitoringas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Kuršių marių ir Baltijos jūros valstybinio monitoringo duomenys

- **Namespace:** `datasets/gov/aaa/juros_mariu_monitoringas`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/juros_mariu_monitoringas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `9` (9 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1790/`[^dcat]
- **Publisher (`dct:publisher`):** Aplinkos apsaugos agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas`[^dcat]
- **Portal Title (`@lt`):** Kuršių marių ir Baltijos jūros valstybinio monitoringo duomenys[^dcat]
- **Portal Title (`@en`):** Data from the state monitoring of the Curonian Lagoon and the Baltic Sea[^dcat]
- **Issued (`dct:issued`):** `2022-10-11`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-10-11` .. `2025-12-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami valstybinio Kuršių marių ir Baltijos jūros aplinkos monitoringo duomenys. Duomenų rinkinį sudaro Baltijos jūros ir Kuršių marių monitoringo vietose atliktų hidrologinių, hidrocheminių, biologinių ir specifinių teršalų (vandenyje, dugno nuosėdose, biotoje) matavimų ir tyrimų rezultatai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The collection contains data from national environmental monitoring of the Curonian Lagoon and the Baltic Sea. The dataset consists of measurements and analyses of hydrological, hydrochemical, biological and specific pollutants (in water, bottom sediments, biota) at monitoring sites in the Baltic Sea and the Curonian Lagoon.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Hidrochemija](juros_mariu_monitoringas/Hidrochemija.md) | Kuršių marių ir Baltijos jūros hidrocheminių parametrų tyrimai vandenyje | `2` | `reg_nr` | — | `14` | — |
| [Hidrometeorologija](juros_mariu_monitoringas/Hidrometeorologija.md) | Kuršių marių ir Baltijos jūros hidrologinių matavimų vandenyje ir meteorologinių stebėjimų duomenys | `2` | `reg_nr` | — | `13` | — |
| [ChlorofilasA](juros_mariu_monitoringas/ChlorofilasA.md) | Kuršių marių ir Baltijos jūros chlorofilo a tyrimų duomenys | `4` | `reg_nr` | — | `14` | — |
| [Fitoplanktonas](juros_mariu_monitoringas/Fitoplanktonas.md) | Kuršių marių ir Baltijos jūros fitoplanktono tyrimų duomenys | `2` | `reg_nr` | — | `22` | — |
| [Zoobentosas](juros_mariu_monitoringas/Zoobentosas.md) | Kuršių marių ir Baltijos jūros zoobentoso tyrimų duomenys | `2` | `reg_nr` | — | `18` | — |
| [Zooplanktonas](juros_mariu_monitoringas/Zooplanktonas.md) | Kuršių marių ir Baltijos jūros zooplanktono tyrimų duomenys | `2` | `reg_nr` | — | `18` | — |
| [SpTersalaiV](juros_mariu_monitoringas/SpTersalaiV.md) | Specifinių teršalų tyrimai Kuršių marių ir Baltijos jūros vandenyje | `2` | `reg_nr` | — | `14` | — |
| [SpTersalaiDN](juros_mariu_monitoringas/SpTersalaiDN.md) | Specifinių teršalų tyrimai Kuršių marių ir Baltijos jūros dugno nuosėdose | `2` | `reg_nr` | — | `15` | — |
| [SpTersalaiB](juros_mariu_monitoringas/SpTersalaiB.md) | Specifinių teršalų tyrimai Kuršių marių ir Baltijos jūros biotoje | `2` | `reg_nr` | — | `18` | — |

# Enumerations

| Enum (ref) | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `nustatymo_zyme` | `'SP'` | — | — | Nėra galimybės arba nereikia nurodyti konkretaus rūšies pavadinimo | — |
| `nustatymo_zyme` | `'SPP'` | — | — | Kelios nenustatytos tos pačios genties rūšys | — |
| `nustatymo_zyme` | `'CF'` | — | — | Žymėjimas dedamas tarp genties ir rūšies pavadinimo, reiškiantis, kad individas kaip įmanoma (su tam tikra abejone) atpažintas iki rūšies | — |
| `nustatymo_zyme` | `'CPX'` | — | — | Žymėjimas reiškia, kad yra labai panašių viena į kitą rūšių grupė pavadinta pagal labiausiai paplitusią rūšį regione | — |
| `nustatymo_zyme` | `'VARIA'` | — | — | Žymima, kai individai identifikuojami iki klasės | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/juros_mariu_monitoringas (https://data.gov.lt/datasets/1790/)
