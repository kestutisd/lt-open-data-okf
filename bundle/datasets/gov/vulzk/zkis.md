---
type: Dataset
title: "Pacientų gydymo operacijomis duomenys"
description: "Vilniaus universiteto ligoninės Žalgirio klinikos ŽKIS sistema kaupia pacientų odontologinių sutrikimų gydymo operacijomis duomenis."
resource: "https://get.data.gov.lt/datasets/gov/vulzk/zkis"
tags: [gov, vulzk, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/zkis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vulzk/zkis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2660/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vulzk/zkis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pacientų gydymo operacijomis duomenys

- **Namespace:** `datasets/gov/vulzk/zkis`[^manifest]
- **Manifest CSV:** [datasets/gov/vulzk/zkis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/zkis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vulzk/zkis` (`deployed`)[^manifest]
- **Provider:** `vulzk` — VšĮ Vilniaus universiteto ligoninės Žalgirio klinika *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2660/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vulzk/zkis`[^dcat]
- **Portal Title (`@lt`):** Pacientų gydymo operacijomis duomenys[^dcat]
- **Portal Title (`@en`):** Data on the treatment of patients with surgery[^dcat]
- **Issued (`dct:issued`):** `2024-05-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-05-17` .. `2024-05-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Vilniaus universiteto ligoninės Žalgirio klinikos ŽKIS sistema kaupia pacientų odontologinių sutrikimų gydymo operacijomis duomenis. Duomenų laikotarpis yra nuo 2015 m. iki 2024 m. Duomenų rinkinys apima vykdytos operacijos protokolo identifikatorių, šifruotą paciento asmens kodą, gimimo metus, ligos TLK-10-AM kodą bei žodinį pavadinimą, operacijos pradžios, pabaigos laikus, taikytos anestezės rūšies, rizikos kodus bei jos pradžios ir pabaigos laikus. Papildomai pateikiamas paciento draudiko pavadinimas, JAR kodas ir draudimo rūšis, duomenys imami iš Sveidra. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

THE Žalgiris Clinic in Vilnius University Hospital collects data on patients' dental disorders through surgery. The data period shall be from 2015 to 2024. The data set shall include the protocol identifier of the operation carried out, the patient's code encrypted, the year of birth, the TLK-10-AM disease code and the verbal name, the start, end times of the operation, the type of anaesthesia used, the risk codes and the start and end times of the operation. In addition, the name of the patient insurer, the Jaris code and the type of insurance shall be provided and the data shall be taken from Smirra.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Operacija](zkis/Operacija.md) | Pacientų gydymo operacijomis duomenys | `4` | `operacijos_id` | — | `16` | Vilniaus universiteto ligoninės Žalgirio klinikos ŽKIS sistema kaupia pacientų odontologinių sutrikimų gydymo operacijomis duomenis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vulzk/zkis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/zkis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vulzk/zkis (https://data.gov.lt/datasets/2660/)
