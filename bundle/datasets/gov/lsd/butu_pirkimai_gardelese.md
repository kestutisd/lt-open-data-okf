---
type: Dataset
title: "Nekilnojamojo turto registro butų pirkimų sandorių informacija gardelėse"
description: "Lentelėje pateikiami agreguoti VĮ Registrų centro Nekilnojamojo turto registro (NTR) gyvenamosios paskirties objektų (butų) pirkimų sandorių duomenys 1 km stačiakampėse gardelėse."
resource: "https://get.data.gov.lt/datasets/gov/lsd/butu_pirkimai_gardelese"
tags: [gov, lsd, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/butu_pirkimai_gardelese.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/butu_pirkimai_gardelese.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2559/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/butu_pirkimai_gardelese"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Nekilnojamojo turto registro butų pirkimų sandorių informacija gardelėse

- **Namespace:** `datasets/gov/lsd/butu_pirkimai_gardelese`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/butu_pirkimai_gardelese.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/butu_pirkimai_gardelese.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/butu_pirkimai_gardelese` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2559/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/butu_pirkimai_gardelese/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Nekilnojamojo turto registro butų pirkimų sandorių informacija gardelėse[^dcat]
- **Portal Title (`@en`):** Real estate registry (NTR) apartment purchase transactions[^dcat]
- **Issued (`dct:issued`):** `2024-04-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2024-04-12` .. `2026-06-10`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikiami agreguoti VĮ Registrų centro Nekilnojamojo turto registro (NTR) gyvenamosios paskirties objektų (butų) pirkimų sandorių duomenys 1 km stačiakampėse gardelėse. Lentelės stulpeliuose - kiekvienai gardelei apskaičiuoti sandorių verčių, įsigytų butų plotų, butų verčių, masinio (visuotinio) vertinimo verčių vidurkiai, mažiausios ir didžiausios vertės, 10 - 90 procentiliai. Laiko aprėptis - nuo 1998 m. Duomenys šiame rinkinyje apima ne visus gyvenamosios paskirties objektų (butų) pirkimų aibės sandorius, bet tik tuos sandorius, kurių metu įsigytas tik vienas objektas. Informacija apie sandorius, kurių metu buvo perkami keli objektai (pvz.: butas ir sandėliukas arba butas ir žemės sklypas) šioje lentelėje nepateikiami. Geografinė informacija (gardelės) gauta iš VĮ Registrų centro Adresų registro. Duomenys jungiami su stačiakampių 1x1 km dydžio gardelių tinklų sudarytu Lietuvos valstybinėje koordinačių sistemoje LKS-94. Stačiakampės gardelės 1 km (LKS-94) https://data.gov.lt/datasets/2047/data/Grid1KmSq/?select(_id,grid_id,x_centroid,y_centroid,sav_pav,sav_kodas,geometrija). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table contains information on purchases of residential (apartments) objects of the Real Property Register (NTR) of the Centre of Registers of the SE since 1998. Geographic coverage: information is provided at the level of the Lithuanian municipalities and rectangles (1 km) and hexagonal (1 km) cells. Geographical information (cells) was obtained by connecting data from the Register of Adres of the Centre of Registers of the SE.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ButuPirkimas](butu_pirkimai_gardelese/ButuPirkimas.md) | Agreguoti VĮ Registrų centro Nekilnojamojo turto registro (NTR) gyvenamosios paskirties (butų) objektų pirkimų sandorių duomenys 1 km stačiakampėse gardelėse. | `4` | `iraso_id` | — | `54` | Lentelėje pateikiami agreguoti VĮ Registrų centro Nekilnojamojo turto registro (NTR) gyvenamosios paskirties (butų) objektų pirkimų sandorių duomenys 1 km... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/butu_pirkimai_gardelese.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/butu_pirkimai_gardelese.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/butu_pirkimai_gardelese (https://data.gov.lt/datasets/2559/)
