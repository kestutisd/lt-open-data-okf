---
type: Dataset
title: "Apgyvendinimo įstaigų skaičius"
description: "Ketvirtiniai, metiniai apgyvendinimo paslaugų tiekėjų kiekiai pagal administracinę teritoriją, apgyvendinimo tipą ir viešbučio kategoriją."
resource: "https://get.data.gov.lt/datasets/gov/lsd/statistika/apgyv_ist"
tags: [gov, lsd, deployed, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/apgyv_ist.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/statistika/apgyv_ist.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2443/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/apgyv_ist"
    author: "team:vda"
    last_modified: "2026-10-09T00:00:00Z"
---

# Apgyvendinimo įstaigų skaičius

- **Namespace:** `datasets/gov/lsd/statistika/apgyv_ist`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/statistika/apgyv_ist.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/apgyv_ist.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/statistika/apgyv_ist` (`deployed`)[^manifest]
- **Provider:** `lsd` — Oficialiosios statistikos portalo rodiklių duomenų bazės rinkiniai *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2443/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/statistika/apgyv_ist/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Apgyvendinimo įstaigų skaičius[^dcat]
- **Portal Title (`@en`):** Number of accommodation establishments[^dcat]
- **Issued (`dct:issued`):** `2023-12-19`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-09`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `OTHER` (`http://publications.europa.eu/resource/authority/frequency/OTHER`)[^dcat]
- **Distribution Date Span:** `2026-07-03` .. `2026-10-09`[^dcat]

### Portal Description (`@lt`)

Ketvirtiniai, metiniai apgyvendinimo paslaugų tiekėjų kiekiai pagal administracinę teritoriją, apgyvendinimo tipą ir viešbučio kategoriją. Naudojami klasifikatoriai: Lietuvos Respublikos administracinių vienetų ir gyvenamųjų vietovių klasifikatorius (LR AVGVK 2018); Apibrėžtys: Apgyvendinimo įstaiga – vietos veiklos rūšies vienetas, teikiantis mokamas trumpalaikio apgyvendinimo paslaugas turistui. Statistinė tiriamoji visuma juridiniai asmenys, teikiantys apgyvendinimo paslaugas, nepriklausomai nuo pagrindinės ekonominės veiklos rūšies pagal tokias EVRK 2 red. I sekcijos grupes: 55.1 – viešbučių ir panašių laikinų buveinių veikla, 55.2 – poilsiautojų ir kita trumpalaikio apgyvendinimo veikla, 55.3 – poilsinių transporto priemonių, priekabų aikštelių ir stovyklaviečių veikla (toliau – EVRK 2 red. I sekcija, grupės 55.1, 55.2, 55.3). Fiziniai asmenys, dirbantys pagal verslo liudijimą (010, 043 kodai pagal „Verslo liudijimų klasifikatorių“) ar (ir) individualios veiklos pažymą ir teikiantys apgyvendinimo veiklos (EVRK 2 red. I sekcija, grupės 55.1, 55.2, 55.3) paslaugas turistams. Geografinė aprėptis: statistinė informacija rengiama šalies, regionų, apskričių ir savivaldybių lygmeniu. Laiko aprėptis: nuo 2012 m. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Quarterly, annual quantities of accommodation providers by administrative territory, type of accommodation and hotel category. Used classifications: classification of administrative units and residential areas of the Republic of Lithuania (LR AVGVK 2018); Definitions: Accommodation is a local activity unit providing paid short-term accommodation to a tourist. “Statistical survey population” means legal persons providing accommodation services irrespective of the main economic activity according to the following groups of Chapter I of Rev. 2 of the ECEC: 55.1 – activities of hotels and similar temporary establishments, 55.2 – activities of holidaymakers and other short-term accommodation, 55.3 – activities of recreational vehicles, trailer grounds and camping sites (hereinafter referred to as “Section I of Rev. 2 of the ECEC”, groups 55.1, 55.2, 55.3). Natural persons working under a business certificate (codes 010, 043 according to the “Classification of Business Certificates”) or/or an individual activity certificate and providing accommodation activities (section I of Rev. 2 ECEC, group 55.1, 55.2, 55.3) to tourists. Geographical coverage: statistical information is produced at national, regional, county and municipal level. Time coverage: from 2012[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [S8R862M40902034](apgyv_ist/S8R862M40902034.md) | Apgyvendinimo įstaigų skaičius (pagal apgyvendinimo tipą ir administracinę teritoriją, ketvirtiniai) | `4` | `vda_id` | — | `12` | Kas ketvirtiniai apgyvendinimo paslaugų tiekėjų kiekiai pagal administracinę teritoriją ir apgyvendinimo tipą. |
| [S8R862M40903034](apgyv_ist/S8R862M40903034.md) | Apgyvendinimo įstaigų skaičius (pagal apgyvendinimo tipą ir administracinę teritoriją, metiniai) | `4` | `vda_id` | — | `12` | Metiniai apgyvendinimo paslaugų tiekėjų kiekiai pagal administracinę teritoriją ir apgyvendinimo tipą. |
| [S8R862M40903085](apgyv_ist/S8R862M40903085.md) | Apgyvendinimo įstaigų skaičius (pagal viešbučio kategorija, metiniai) | — | — | — | `9` | Metiniai apgyvendinimo įstaigų kiekiai pagal viešbučio kategorija 3.3 Sektorinė aprėptis EVRK 2 red. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/statistika/apgyv_ist.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/apgyv_ist.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/apgyv_ist (https://data.gov.lt/datasets/2443/)
