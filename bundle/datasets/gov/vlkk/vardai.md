---
type: Dataset
title: "Vardų lingvistiniai duomenys"
description: "Valstybinė lietuvių kalbos komisijos (VLKK) Lietuvos Respublikos piliečių vardų sąvadas, kaip duomenų rinkinio šaltinis, yra sukurtas Gyventojų registro 2006 m. pilietybę turėjusių asmenų vardų duomenimis ir toliau yra pildomas naujagimių vardais."
resource: "https://get.data.gov.lt/datasets/gov/vlkk/vardai"
tags: [gov, vlkk, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/vardai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlkk/vardai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2664/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlkk/vardai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vardų lingvistiniai duomenys

- **Namespace:** `datasets/gov/vlkk/vardai`[^manifest]
- **Manifest CSV:** [datasets/gov/vlkk/vardai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/vardai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlkk/vardai` (`deployed`)[^manifest]
- **Provider:** `vlkk` — Valstybinė lietuvių kalbos komisija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2664/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlkk/vardai`[^dcat]
- **Portal Title (`@lt`):** Vardų lingvistiniai duomenys[^dcat]
- **Portal Title (`@en`):** Name linguistic data[^dcat]
- **Issued (`dct:issued`):** `2024-05-20`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2024-05-20` .. `2026-09-18`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybinė lietuvių kalbos komisijos (VLKK) Lietuvos Respublikos piliečių vardų sąvadas, kaip duomenų rinkinio šaltinis, yra sukurtas Gyventojų registro 2006 m. pilietybę turėjusių asmenų vardų duomenimis ir toliau yra pildomas naujagimių vardais. Rinkinyje duomenys kaupiami nuo 2010 m. ir yra atnaujinami kas 3 mėnesius. Duomenys apima pilną vardą, sudarančių vardų skaičių (komponentiškumą), vardo lytį, normiškumą, ar tai yra šventojo vardas, vardo įvedimo datą, vėliausias atnaujinimo bei paieškos datas, paieškų skaičių ir iki po 5 vardų kilmės grupes, pogrupius ir poskyrius. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The State List of Citizens' NAMES of the Republic of Lithuania of the Lithuanian Language Commission (VLKK), as a source of the data set, is created according to the names of persons who held citizenship in 2006 of the Population Register and continues to be filled in with the names of newborns. The collection has been compiled since 2010 and is updated every 3 months. Data include full name, number of names (comity), gender of name, normality, whether it is the name of the saint, date of name input, latest renewal and search dates, number of searches, and groups of origin, subgroups, and subdivisions of up to 5 names each.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Vardas](vardai/Vardas.md) | Vardų lingvistiniai duomenys | `4` | `id` | `open` | `25` | Valstybinė lietuvių kalbos komisijos (VLKK) Lietuvos Respublikos piliečių vardų sąvadas, kaip duomenų rinkinio šaltinis, yra sukurtas Gyventojų registro... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlkk/vardai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/vardai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlkk/vardai (https://data.gov.lt/datasets/2664/)
