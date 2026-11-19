---
type: Table
title: "SPI — ASPĮ ekstremalių situacijų valdymo planų vertinimas"
description: "Ekstremalių sveikatai situacijų centras (ESSC) kaupia sveikatos priežiūros įstaigų ekstremalių situacijų valdymo planų vertinimus, gautus iš Sveikatos apsaugos ministerijos."
resource: "https://get.data.gov.lt/datasets/gov/essc/spi/SPI"
tags: [gov, essc, spi, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/spi.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/essc/spi.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2618/"
    title: "data.gov.lt DCAT-AP — datasets/gov/essc/spi"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# SPI — ASPĮ ekstremalių situacijų valdymo planų vertinimas

Ekstremalių sveikatai situacijų centras (ESSC) kaupia sveikatos priežiūros įstaigų ekstremalių situacijų valdymo planų vertinimus, gautus iš Sveikatos apsaugos ministerijos. Duomenys kaupiami nuo 2012 m. ir atnaujinami balandžio ir spalio mėnesiais. Duomenys apima įstaigos pavadinimą, geografinį ir cenzūruotą el. pašto adresus, apskritį, kam yra pavaldi. Iš vertinimų yra duomenų apie jo datą, tipą ir artimiausio vertinimo metus.[^manifest]

- **Model:** `datasets/gov/essc/spi/SPI`[^manifest]
- **Dataset:** [ASPĮ ekstremalių situacijų valdymo planų vertinimas](../spi.md) (`datasets/gov/essc/spi`)[^manifest]
- **Manifest CSV:** [datasets/gov/essc/spi.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/spi.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/essc/spi/SPI` (`deployed`)[^manifest]
- **Provider:** `essc` — Ekstremalių sveikatai situacijų centras *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `istaigos_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `istaigos_adresas` | `string` | — | `3` | `open` | — | Įstaigos adresas | — |
| `el_pastas` | `string` | — | `3` | `open` | — | Cenzūruotas įstaigos el. Pašto adresas | — |
| `apskritis` | `string` | — | `2` | `open` | — | Įstaigos apskritis | — |
| `pavaldumas` | `string` | — | `4` | `open` | — | Kam įstaiga yra pavaldi | — |
| `istaigos_vertinimo_data` | `date` | `D` | `4` | `open` | — | Įstaigos vertinimo data | — |
| `vertinimo_tipas` | `string` | — | `4` | `open` | — | Vertinimo tipas | — |
| `sekancio_vertinimo_metai` | `integer` | — | `4` | `open` | — | Sekančio vertinimo metai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/essc/spi.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/spi.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/essc/spi (https://data.gov.lt/datasets/2618/)
