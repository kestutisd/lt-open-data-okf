---
type: Dataset
title: "Juridinių asmenų elektros energijos suvartojimo duomenys"
description: "Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) juridinių asmenų elektros suvartojimo duomenys, apjungti su ekonominės veiklos rūšies klasifikatoriumi (2 red.)."
resource: "https://get.data.gov.lt/datasets/gov/eso/jur_asm_elektros_suvartojimas"
tags: [gov, eso, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2742/"
    title: "data.gov.lt DCAT-AP — datasets/gov/eso/jur_asm_elektros_suvartojimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Juridinių asmenų elektros energijos suvartojimo duomenys

- **Namespace:** `datasets/gov/eso/jur_asm_elektros_suvartojimas`[^manifest]
- **Manifest CSV:** [datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/eso/jur_asm_elektros_suvartojimas` (`deployed`)[^manifest]
- **Provider:** `eso` — Energijos skirstymo operatorius *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2742/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/eso/jur_asm_elektros_suvartojimas`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų elektros energijos suvartojimo duomenys[^dcat]
- **Portal Title (`@en`):** Electricity consumption data of legal persons[^dcat]
- **Issued (`dct:issued`):** `2024-09-10`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-03-14` .. `2026-04-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) juridinių asmenų elektros suvartojimo duomenys, apjungti su ekonominės veiklos rūšies klasifikatoriumi (2 red.). Rinkinys sudarytas Valstybės duomenų agentūros. Adresai pateikiami 10 kilometrų dydžio stačiakampėmis gardelėmis Lietuvos koordinačių sistemoje (LKS-94). Elektros suvartojimo duomenys pateikiami mėnesio tikslumu. Vartotojo kodas, įmonės kodas ir objekto numeris yra užšifruoti. Realus suvartotas elektros kiekis gali skirtis nuo pateikiamų duomenų tokiu atveju, kai vartotojas neteisingai deklaruoja suvartotą elektros kiekį arba turi įsirengęs saulės elektrinę. Duomenų laiko aprėptis – nuo 2019 m. sausio 1 d. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table shows the electricity consumption data of the legal entities of the Energy Distribution Operator (ESO) combined with the economic activity classification (Rev. 2). The set is compiled by the State Data Agency. Addresses are provided in rectangular stalls of 10 kilometres in the Lithuanian coordinate system (LKS-94). Electricity consumption data shall be provided with the accuracy of the month. The user code, company code, and object number are encrypted. The actual amount of electricity consumed may differ from the data provided in case the consumer incorrectly declares the amount of electricity consumed or has installed a solar power plant. Data time coverage: from 1 January 2019. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [JurAsmElektraSuvartojimas](jur_asm_elektros_suvartojimas/JurAsmElektraSuvartojimas.md) | Juridinių asmenų elektros energijos suvartojimo duomenys | `4` | `iraso_id` | — | `25` | Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) juridinių asmenų elektros suvartojimo duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/eso/jur_asm_elektros_suvartojimas (https://data.gov.lt/datasets/2742/)
