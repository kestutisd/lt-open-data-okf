---
type: Dataset
title: "Duomenys apie valstybinės reikšmės kelių projektus"
description: "\"Duomenų rinkinyje pateikiami AB „Via Lietuva“ duomenys apie užsakomus valstybinės reikšmės kelių projektavimo, tiesimo, statybos, rekonstravimo, taisymo (remonto) ir priežiūros darbų projektus, finansuojamus iš Lietuvos Respublikos kelių priežiūros ir plėtros programos bei..."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/keliu_projektai"
tags: [gov, via_lietuva, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/keliu_projektai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/keliu_projektai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3844/"
    title: "data.gov.lt DCAT-AP — datasets/gov/via_lietuva/keliu_projektai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Duomenys apie valstybinės reikšmės kelių projektus

"Duomenų rinkinyje pateikiami AB „Via Lietuva“ duomenys apie užsakomus valstybinės reikšmės kelių projektavimo, tiesimo, statybos, rekonstravimo, taisymo (remonto) ir priežiūros darbų projektus, finansuojamus iš Lietuvos Respublikos kelių priežiūros ir plėtros programos bei Europos Sąjungos paramos lėšų. Duomenų rinkinį sudaro dvi lentelės: 1. „Kelių projektų darbai“ – informacija apie kelių atkarpose vykdomus darbus, 2. „Kelio darbų atkarpos“ – informacija apie kelio atkarpas. Duomenų teikėjas – AB „Via Lietuva“. Duomenys kaupiami nuo 2004 m. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. "[^manifest]

- **Namespace:** `datasets/gov/via_lietuva/keliu_projektai`[^manifest]
- **Manifest CSV:** [datasets/gov/via_lietuva/keliu_projektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/keliu_projektai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/keliu_projektai` (`deployed`)[^manifest]
- **Provider:** `via_lietuva` — AB „Via Lietuva“ (buv. LAKD) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3844/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/via_lietuva/keliu_projektai`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie valstybinės reikšmės kelių projektus[^dcat]
- **Portal Title (`@en`):** Data on road projects of national significance[^dcat]
- **Issued (`dct:issued`):** `2025-06-12`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-07-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami AB „Via Lietuva“ duomenys apie užsakomus valstybinės reikšmės kelių projektavimo, tiesimo, statybos, rekonstravimo, taisymo (remonto) ir priežiūros darbų projektus, finansuojamus iš Lietuvos Respublikos kelių priežiūros ir plėtros programos bei Europos Sąjungos paramos lėšų. Duomenų rinkinį sudaro dvi lentelės: 1. „Kelių projektų darbai“ – informacija apie kelių atkarpose vykdomus darbus, 2. „Kelio darbų atkarpos“ – informacija apie kelio atkarpas. Duomenų teikėjas – AB „Via Lietuva“. Duomenys kaupiami nuo 2004 m. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set shall contain data of AB Via Lietuva on the commissioned projects of state significance road design, construction, construction, reconstruction, repair (repair) and maintenance works financed from the Programme of Road Maintenance and Development of the Republic of Lithuania and EU support funds. The dataset consists of two tables: 1. '“Road project works” means information on works carried out on road sections, 2.' Road sections shall mean information on sections of the road. Data provider – AB Via Lietuva. Data has been collected since 2004. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KelioDarbuProjektas](keliu_projektai/KelioDarbuProjektas.md) | „Kelių projektų darbai“ | `4` | `vda_prime_key` | — | `19` | "Duomenys apie valstybinės reikšmės keliuose vykstančius kelio darbų projektus. |
| [KelioAtkarpa](keliu_projektai/KelioAtkarpa.md) | „Kelio darbų atkarpos“ | `4` | `atkarpos_id` | — | `5` | "Duomenys apie kelių atkarpas, kuriose vykdomi kelių darbų projektai. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/keliu_projektai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/keliu_projektai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/via_lietuva/keliu_projektai (https://data.gov.lt/datasets/3844/)
