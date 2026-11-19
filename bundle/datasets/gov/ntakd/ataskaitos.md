---
type: Dataset
title: "Alkoholio ir tabako ataskaitų duomenys"
description: "Narkotikų, tabako ir alkoholio kontrolės departamento (NTAKD) naudojamoje alkoholio produktų ir tabako gaminių ataskaitų teikimo sistemoje kaupiamos juridinių bei fizinių asmenų pateiktos alkoholio ir tabako gaminių ataskaitos."
resource: "https://get.data.gov.lt/datasets/gov/ntakd/ataskaitos"
tags: [gov, ntakd, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/alkoholis_tabakas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ntakd/alkoholis_tabakas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2824/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ntakd/ataskaitos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Alkoholio ir tabako ataskaitų duomenys

- **Namespace:** `datasets/gov/ntakd/ataskaitos`[^manifest]
- **Manifest CSV:** [datasets/gov/ntakd/alkoholis_tabakas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/alkoholis_tabakas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntakd/ataskaitos` (`deployed`)[^manifest]
- **Provider:** `ntakd` — Narkotikų, tabako ir alkoholio kontrolės departamentas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2824/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ntakd/ataskaitos`[^dcat]
- **Portal Title (`@lt`):** Alkoholio ir tabako ataskaitų duomenys[^dcat]
- **Portal Title (`@en`):** Alcohol and Tobacco Reporting Data[^dcat]
- **Issued (`dct:issued`):** `2024-11-07`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2024-11-07` .. `2025-12-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Narkotikų, tabako ir alkoholio kontrolės departamento (NTAKD) naudojamoje alkoholio produktų ir tabako gaminių ataskaitų teikimo sistemoje kaupiamos juridinių bei fizinių asmenų pateiktos alkoholio ir tabako gaminių ataskaitos. Duomenys sistemoje kaupiami nuo 2020 m. ir atnaujinami iki šiol. Duomenų rinkinys sudarytas iš: ataskaitą pateikusio fizinio arba juridinio asmens pseudonimizuoto kodo, ataskaitos teikėjo asmens rūšies, alkoholio arba tabako gaminio pavadinimo, gaminio KN kodo, licencijos, skaičiaus, kiek atitinkamo gaminio pagaminta arba nupirkta bei parduota arba panaudota atitinkamu ataskaitos periodu, mato vieneto bei ataskaitos periodo metų, numerio ir dažnio. Vienas įrašas atitinka vieną ataskaitos teikėjo, gaminio, ataskaitos metų ir periodo numerio kombinaciją. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Reports on alcohol and tobacco products submitted by legal and natural persons shall be compiled in the reporting system for alcohol products and tobacco products used by the Department of Drugs, Tobacco and Alcohol Control (NTAKD). Data has been stored in the system since 2020 and has been updated so far. The dataset shall consist of: the pseudonymised code of the natural or legal person submitting the report, the type of person of the reporting provider, the name of the alcohol or tobacco product, the CN code of the product, the licence, the number of products produced or purchased and sold or used during the relevant reporting period, the year, number and frequency of the unit and reporting period. One entry corresponds to one combination of the report provider, product, report year, and period number. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Ataskaita](ataskaitos/Ataskaita.md) | Alkoholio ir tabako ataskaitų duomenys | `4` | `medziagos_id` | — | `12` | Narkotikų, tabako ir alkoholio kontrolės departamento (NTAKD) naudojamoje alkoholio produktų ir tabako gaminių ataskaitų teikimo sistemoje kaupiamos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntakd/alkoholis_tabakas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/alkoholis_tabakas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ntakd/ataskaitos (https://data.gov.lt/datasets/2824/)
