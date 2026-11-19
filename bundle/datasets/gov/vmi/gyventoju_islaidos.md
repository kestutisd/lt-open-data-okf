---
type: Dataset
title: "Gyventojų patirtos išlaidos"
description: "Agreguoti duomenys iš juridinių asmenų pateiktos informacijos apie gyventojų patirtas įmokas ir gyventojų deklaruotas išlaidas, kuriomis gali būti mažinamos gyventojų apmokestinamosios pajamos."
resource: "https://get.data.gov.lt/datasets/gov/vmi/gyventoju_islaidos"
tags: [gov, vmi, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_islaidos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/gyventoju_islaidos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1183/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/gyventoju_islaidos"
    author: "team:vda"
    last_modified: "2026-03-09T00:00:00Z"
---

# Gyventojų patirtos išlaidos

- **Namespace:** `datasets/gov/vmi/gyventoju_islaidos`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/gyventoju_islaidos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_islaidos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/gyventoju_islaidos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1183/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/gyventoju_islaidos`[^dcat]
- **Portal Title (`@lt`):** Gyventojų patirtos išlaidos[^dcat]
- **Portal Title (`@en`):** Expenditure incurred by the population[^dcat]
- **Issued (`dct:issued`):** `2022-03-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-03-09`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-02-09` .. `2026-03-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Agreguoti duomenys iš juridinių asmenų pateiktos informacijos apie gyventojų patirtas įmokas ir gyventojų deklaruotas išlaidas, kuriomis gali būti mažinamos gyventojų apmokestinamosios pajamos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Aggregate data from information provided by legal entities on contributions received by residents and expenditure declared by residents, which may reduce the taxable income of residents[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [GyventojuIslaidos](gyventoju_islaidos/GyventojuIslaidos.md) | Duomenys apie mokėtojo deklaruotas išlaidas, kuriomis pagal GPMĮ 21 str. gali būti mažinamos apmokestinamosios pajamos | `4` | — | — | `7` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/gyventoju_islaidos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_islaidos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/gyventoju_islaidos (https://data.gov.lt/datasets/1183/)
