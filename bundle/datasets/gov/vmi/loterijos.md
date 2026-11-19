---
type: Dataset
title: "Loterijų verslo loterijų ir lošimų mokesčio deklaracijų (forma FR0583) duomenys"
description: "Deklaraciją pildo juridiniai asmenys, organizuojantys loterijas pagal LR Loterijų įstatymą."
resource: "https://get.data.gov.lt/datasets/gov/vmi/loterijos"
tags: [gov, vmi, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/loterijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/loterijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1922/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/loterijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Loterijų verslo loterijų ir lošimų mokesčio deklaracijų (forma FR0583) duomenys

Deklaraciją pildo juridiniai asmenys, organizuojantys loterijas pagal LR Loterijų įstatymą. Daugiau informacijos apie mokestį galite rasti Lietuvos Respublikos loterijų ir lošimų mokesčio įstatyme[^manifest]

- **Namespace:** `datasets/gov/vmi/loterijos`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/loterijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/loterijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/loterijos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1922/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/loterijos`[^dcat]
- **Portal Title (`@lt`):** Loterijų verslo loterijų ir lošimų mokesčio duomenys[^dcat]
- **Portal Title (`@en`):** Lottery business lotteries and gambling tax data[^dcat]
- **Issued (`dct:issued`):** `2023-03-09`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-03-09` .. `2026-06-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Didžiųjų ir mažųjų loterijų organizatorių šios veiklos deklaruotų mokesčių (forma FR0583) duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on the operating income and tax to the budget of organizers of large and small lotteries (form FR0583)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Didzioji](loterijos/Didzioji.md) | Didžiųjų verslo loterijų ir lošimų mokesčio deklaracijų duomenys | `3` | — | — | `4` | Loterija, kurios bilietai platinami visoje Lietuvos Respublikos teritorijoje ir nominalioji numatomų išplatinti bilietų vertė neribojama. |
| [Mazoji](loterijos/Mazoji.md) | Mažųjų verslo loterijų ir lošimų mokesčio deklaracijų duomenys | `3` | — | — | `4` | Iki 2020-04-30: loterija, kurios organizatorius turi savivaldybės, kurios teritorijoje organizuojama loterija, vykdomosios institucijos licenciją, išduotą... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/loterijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/loterijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/loterijos (https://data.gov.lt/datasets/1922/)
