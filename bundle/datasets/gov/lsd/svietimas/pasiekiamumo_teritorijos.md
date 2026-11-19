---
type: Dataset
title: "Švietimo institucijų pasiekiamumo pėsčiomis ir automobiliu teritorijos"
description: "Duomenų objektas yra švietimo institucijos, kuriose, tikslinių metų rugsėjo 1 dienos duomenimis, yra ugdomi mokiniai pagal bendrojo ugdymo programas."
resource: "https://get.data.gov.lt/datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos"
tags: [gov, lsd, deployed, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2048/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Švietimo institucijų pasiekiamumo pėsčiomis ir automobiliu teritorijos

- **Namespace:** `datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2048/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos`[^dcat]
- **Portal Title (`@lt`):** Švietimo institucijų 15 ir 30 minučių pasiekiamumo pėsčiomis ir automobiliu teritorijos[^dcat]
- **Portal Title (`@en`):** Territories of educational institutions within 15 and 30 minutes on foot and by car[^dcat]
- **Issued (`dct:issued`):** `2022-10-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_2` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_2`)[^dcat]
- **Distribution Date Span:** `2022-10-21` .. `2025-11-20`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų objektas yra švietimo institucijos, kuriose, tikslinių metų rugsėjo 1 dienos duomenimis, yra ugdomi mokiniai pagal bendrojo ugdymo programas. Priskiriant mokinį prie teritorijos laikoma, kad jo gyvenamoji vieta sutampa su Gyventojų registre deklaruota gyvenamąja vieta tikslinių metų rugsėjo 1-ą dieną. Tais atvejais, kai šia data asmuo nebuvo deklaravęs gyvenamosios vietos, mokinio gyvenamoji vieta buvo laikoma paskutinė/ankstesnė deklaruota jo gyvenamoji vieta. Sudarant pasiekiamumo automobiliu teritorijas, neatsižvelgta į piko valandas ir savaitės dienas. Duomenų rinkinys atnaujinamas du kartus per metus (spalio ir sausio mėnesį). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The object of the data is educational institutions where, according to the data of September 1 of the target year, students are educated according to general education programs. When assigning a student to the territory, it is considered that his place of residence coincides with the place of residence declared in the Population Register on September 1 of the target year. In cases where the person had not declared a place of residence on this date, the student&#39;s place of residence was considered his last/previously declared place of residence. Peak hours and days of the week are not taken into account when creating car accessibility areas. The dataset is updated twice a year (in October and January).[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BuiTeritorijos15min](pasiekiamumo_teritorijos/BuiTeritorijos15min.md) | Švietimo institucijų 15 minučių pasiekiamumo pėsčiomis ir automobiliu teritorijos. | `4` | `vda_prime_key` | — | `12` | Duomenų aprėptį sudaro švietimo institucijos, kuriose, tikslinių metų rugsėjo 1 dienos duomenimis, yra ugdomi mokiniai pagal bendrojo ugdymo programas. |
| [BuiTeritorijos30min](pasiekiamumo_teritorijos/BuiTeritorijos30min.md) | Švietimo institucijų 30 minučių pasiekiamumo pėsčiomis ir automobiliu teritorijos. | `4` | `vda_prime_key` | — | `12` | Duomenų aprėptį sudaro švietimo institucijos, kuriose, tikslinių metų rugsėjo 1 dienos duomenimis, yra ugdomi mokiniai pagal bendrojo ugdymo programas. |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pasiekiamumo_teritorijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/pasiekiamumo_teritorijos (https://data.gov.lt/datasets/2048/)
