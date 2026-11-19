---
type: Dataset
title: "Metinių nuotekų tvarkymo apskaitos ataskaitų duomenys"
description: "Metinių nuotekų tvarkymo apskaitos ataskaitų duomenų rinkinyje pateikiami ūkio subjektų nuotekų tvarkymo apskaitos metinių ataskaitų duomenys apie ūkio subjektų su nuotekomis į aplinką išleistus teršalus, nuotekų kokybę, nuotekų valymo įrenginius, išleistuvus ir priimtuvus."
resource: "https://get.data.gov.lt/datasets/gov/aaa/nuotekos"
tags: [gov, aaa, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1784/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/nuotekos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Metinių nuotekų tvarkymo apskaitos ataskaitų duomenys

- **Namespace:** `datasets/gov/aaa/nuotekos`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/nuotekos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/nuotekos` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1784/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/aaa/nuotekos`[^dcat]
- **Portal Title (`@lt`):** Metinių nuotekų tvarkymo apskaitos ataskaitų duomenys[^dcat]
- **Portal Title (`@en`):** Data from annual wastewater treatment accounting reports[^dcat]
- **Issued (`dct:issued`):** `2023-06-30`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-06-30` .. `2025-08-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Metinių nuotekų tvarkymo apskaitos ataskaitų duomenų rinkinyje pateikiami ūkio subjektų nuotekų tvarkymo apskaitos metinių ataskaitų duomenys apie ūkio subjektų su nuotekomis į aplinką išleistus teršalus, nuotekų kokybę, nuotekų valymo įrenginius, išleistuvus ir priimtuvus. Nuotekų tvarkymo apskaitos metines ataskaitas ūkio subjektai teikia Aplinkos apsaugos agentūrai per informacinę sistemą „Aplinkos informacijos valdymo integruota kompiuterinė sistema“ (AIVIKS), vadovaujantis Vandens naudojimo ir nuotekų tvarkymo apskaitos tvarkos aprašo reikalavimais. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Annual Wastewater Treatment Accounting Reports Dataset contains data from annual wastewater management accounting reports of economic operators about pollutants discharged to the environment, wastewater quality, wastewater treatment plants, discharge points and receiving water bodies, are given. Economic operators submit their annual reports on wastewater treatment accounting to the Environmental Protection Agency through information system "Integrated Computer System for Environmental Information Management" (AIVIKS), in accordance with the requirements of the Description of Procedures for Water Use and Wastewater Management Accounting.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [UkioSubjektas](nuotekos/UkioSubjektas.md) | Ataskaitą teikiantys subjektai | `2` | — | — | `10` | — |
| [NuotekuValymas](nuotekos/NuotekuValymas.md) | Nuotekų valymo įrenginio nuotekų valymo būdai (įskaitant papildomą valymą), nurodyti metinėje nuotekų ataskaitoje, su nuotekų valymo įrenginio paskirtimi | `2` | — | — | `24` | — |
| [IsleistuvasTarsa](nuotekos/IsleistuvasTarsa.md) | Metinę nuotekų ataskaitą teikiančio subjekto duomenys dėl išleidžiamų nuotekų (įskaitant kiekius pagal išleistuvą) | `2` | — | — | `36` | — |
| [IsleistuvasPriimtuvas](nuotekos/IsleistuvasPriimtuvas.md) | Išleistuvai į gamt. aplinką, į nuotakyną ir kt. įrenginiai pagal aob_uvo.aob_rusis su priimtuvo (įskaitant vandens telkinius) informacija | `2` | — | — | `20` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/nuotekos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/nuotekos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/nuotekos (https://data.gov.lt/datasets/1784/)
