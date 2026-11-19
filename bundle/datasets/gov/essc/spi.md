---
type: Dataset
title: "ASPĮ ekstremalių situacijų valdymo planų vertinimas"
description: "Sveikatos apsaugos ministerijos Ekstremalių sveikatai situacijų centras (ESSC) koordinuoja Lietuvos nacionalinės sveikatos sistemos įstaigų pasirengimą ir veiklą ekstremaliųjų situacijų atvejais, vykdydamas asmens ir visuomenės sveikatos priežiūros įstaigų (toliau – SPĮ)..."
resource: "https://get.data.gov.lt/datasets/gov/essc/spi"
tags: [gov, essc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/spi.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/essc/spi.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2618/"
    title: "data.gov.lt DCAT-AP — datasets/gov/essc/spi"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ASPĮ ekstremalių situacijų valdymo planų vertinimas

- **Namespace:** `datasets/gov/essc/spi`[^manifest]
- **Manifest CSV:** [datasets/gov/essc/spi.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/spi.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/essc/spi` (`deployed`)[^manifest]
- **Provider:** `essc` — Ekstremalių sveikatai situacijų centras *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2618/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/essc/spi`[^dcat]
- **Portal Title (`@lt`):** Sveikatos priežiūros įstaigų parengties ekstremaliosioms situacijoms stebėsenos duomenų bazė[^dcat]
- **Portal Title (`@en`):** Database for monitoring emergency preparedness of health care institutions[^dcat]
- **Issued (`dct:issued`):** `2024-04-18`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-04-22` .. `2026-03-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Sveikatos apsaugos ministerijos Ekstremalių sveikatai situacijų centras (ESSC) koordinuoja Lietuvos nacionalinės sveikatos sistemos įstaigų pasirengimą ir veiklą ekstremaliųjų situacijų atvejais, vykdydamas asmens ir visuomenės sveikatos priežiūros įstaigų (toliau – SPĮ) pasirengimo veiklai ekstremaliųjų situacijų atvejais stebėseną ir kaupia sveikatos priežiūros įstaigų ekstremalių situacijų valdymo planų įvertinimus duomenų bazėje. Duomenys atnaujinami atnaujinami 1 kartą per metus (metų pradžioje už praėjusius metus). Duomenys apima SPĮ pavadinimą, geografinį ir cenzūruotą el. pašto adresus, apskritį, pavaldumą, vertinimų datą, tipą ir artimiausio vertinimo metus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Health Emergency Centre (ESSC) of the Ministry of Health shall coordinate the preparation and activities of institutions of the National Health System of Lithuania in the event of emergencies by carrying out monitoring of the preparedness of individual and public health care institutions (hereinafter referred to as the “SPE”) for activities in the event of emergencies and accumulate assessments of emergency management plans of health care institutions in the database. The data shall be updated 1 time per year (at the beginning of the year for the previous year). The data shall include the name of the SPE, the geographic and censored e-mail addresses, the county, subordination, the date, type of evaluations and the year of the nearest evaluation.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SPI](spi/SPI.md) | ASPĮ ekstremalių situacijų valdymo planų vertinimas | `4` | `vda_id` | — | `9` | Ekstremalių sveikatai situacijų centras (ESSC) kaupia sveikatos priežiūros įstaigų ekstremalių situacijų valdymo planų vertinimus, gautus iš Sveikatos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/essc/spi.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/spi.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/essc/spi (https://data.gov.lt/datasets/2618/)
