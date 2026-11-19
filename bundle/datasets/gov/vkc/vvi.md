---
type: Dataset
title: "Valstybės valdomų įmonių finansiniai duomenys"
description: "Valdymo koordinavimo centro (VKC) sistemoje „Valstybės valdomų įmonių finansiniai ir nefinansiniai duomenys“ informacija kaupiama nuo 2019 m. ir yra atnaujinama iki šiol."
resource: "https://get.data.gov.lt/datasets/gov/vkc/vvi"
tags: [gov, vkc, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/vvi.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vkc/vvi.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2839/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vkc/vvi"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Valstybės valdomų įmonių finansiniai duomenys

- **Namespace:** `datasets/gov/vkc/vvi`[^manifest]
- **Manifest CSV:** [datasets/gov/vkc/vvi.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/vvi.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vkc/vvi` (`deployed`)[^manifest]
- **Provider:** `vkc` — Valdymo koordinavimo centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2839/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vkc/vvi`[^dcat]
- **Portal Title (`@lt`):** Valstybės valdomų įmonių finansiniai duomenys[^dcat]
- **Portal Title (`@en`):** Financial data of state-owned enterprises[^dcat]
- **Issued (`dct:issued`):** `2024-10-30`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-10-30` .. `2024-10-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valdymo koordinavimo centro (VKC) sistemoje „Valstybės valdomų įmonių finansiniai ir nefinansiniai duomenys“ informacija kaupiama nuo 2019 m. ir yra atnaujinama iki šiol. Duomenų rinkinį sudaro: duomenų aktualumo data, įmonės JAR kodas, pavadinimas, sektorius, nurodoma, ar yra valstybės valdomų įmonių (VVĮ) portfelyje, teisinė forma, atstovaujanti įstaiga, valstybei priklausanti dalis, bendras pelnas, veiklos pelnas, pelno mokestis, grynasis pelnas, ilgalaikis ir trumpalaikis turtas, laikotarpiai po einamųjų metų pajamų su sąnaudomis, bendrasis turtas, įstatinis pasirašytasis kapitalas, įprasti ir perkainojimo rezervai, nepaskirstytasis pelnas, įsipareigojimai einamaisiais metais, metais po einamųjų metų, ir bendri įsipareigojimai. Vienas įrašas atitinka vieną įmonę konkrečiais metais. Valstybei priklausanti dalis matuojama procentais šimtųjų tikslumu, visi kiti skaičiai matuojami tūkst. eurų. Jeigu skaičius yra neigiamas, jis reiškia matuojamo požymio priešingybę (pvz., neigiamas pelnas reiškia nuostolius). Atvertas duomenų rinkinys nebus atnaujinamas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The system of the Centre for Governance Co-ordination (VCC) “Financial and Non-Financial Data of State-owned Enterprises” collects financial data of state-owned Enterprises. Data shall be collected from 2019 and updated. The dataset consists of the date of relevance of the data, the company's Jaris code, name, sector, whether it is in the portfolio of state-owned enterprises (SOEs), legal form representing the institution, state-owned interest, gross profit, operating profit, corporate tax, net profit, fixed assets, short-term assets, post-current year income with costs, gross assets, authorised subscribed capital, ordinary and revaluation reserves, retained profits, liabilities in the current year, the year following the current year and total liabilities. One entry corresponds to one company in a given year. The state-owned share is measured in percentages with the accuracy of hundreds, and all other figures are measured at thousands of euros. If the number is negative, it represents the opposite of the measurable attribute, for example, negative profit represents loss. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Imone](vvi/Imone.md) | Valstybės valdomų įmonių finansiniai duomenys | `4` | `vda_prime_key` | — | `24` | Valdymo koordinavimo centro (VKC) sistema „Valstybės valdomų įmonių finansiniai ir nefinansiniai duomenys“ kaupia valstybės valdomų įmonių finansinius duomenis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vkc/vvi.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/vvi.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vkc/vvi (https://data.gov.lt/datasets/2839/)
