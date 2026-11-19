---
type: Dataset
title: "Kontroliuojamų medžiagų deklaracijų duomenys"
description: "Narkotikų, tabako ir alkoholio kontrolės departamento naudojamoje Pirmtakų teisėtos apyvartos kontrolės informacinė sistemoje (PTAKIS) kaupiamos juridinių bei fizinių asmenų narkotinių pirmtakų (prekursorių) deklaracijos."
resource: "https://get.data.gov.lt/datasets/gov/ntakd/ptakis"
tags: [gov, ntakd, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/prekursoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ntakd/prekursoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2822/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ntakd/ptakis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kontroliuojamų medžiagų deklaracijų duomenys

- **Namespace:** `datasets/gov/ntakd/ptakis`[^manifest]
- **Manifest CSV:** [datasets/gov/ntakd/prekursoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/prekursoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntakd/ptakis` (`deployed`)[^manifest]
- **Provider:** `ntakd` — Narkotikų, tabako ir alkoholio kontrolės departamentas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2822/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ntakd/ptakis`[^dcat]
- **Portal Title (`@lt`):** Kontroliuojamų medžiagų deklaracijų duomenys[^dcat]
- **Portal Title (`@en`):** Data on declarations of controlled substances[^dcat]
- **Issued (`dct:issued`):** `2024-10-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2024-10-11` .. `2026-07-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Narkotikų, tabako ir alkoholio kontrolės departamento naudojamoje Pirmtakų teisėtos apyvartos kontrolės informacinė sistemoje (PTAKIS) kaupiamos juridinių bei fizinių asmenų narkotinių pirmtakų (prekursorių) deklaracijos. Duomenys kaupiami nuo 2021-04-01 ir atnaujinami iki šiol. Duomenų rinkinį sudaro: pseudonimizuotas deklaravusio fizinio arba juridinio asmens (deklaranto) kodas, deklaranto asmens rūšis, ataskaitos forma, deklaruotos medžiagos pavadinimas, paskirtis ir kiekis deklaracijos periodo pradžioje ir pabaigoje, deklaracijos periodo metai ir tų metų deklaracijos numeris. Vienas įrašas atitinka vieną deklaranto, medžiagos, deklaracijos metų ir periodo numerio kombinaciją. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Information System for the Control of Legal Traffic (PTAKIS) used by the Department of Drugs, Tobacco and Alcohol Control shall compile the declarations of narcotic precursors of legal and natural persons. Data are collected from 2021-04-01 and updated to date. The data set shall comprise: the pseudonymised code of the natural or legal person (declarant) who declared, the type of declarant, the form of the report, the name, purpose and quantity of the declared material at the beginning and end of the declaration period, the year of the declaration period and the number of the declaration for that year. One entry corresponds to one combination of declarant, material, year of declaration and period number. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Deklaracija](ptakis/Deklaracija.md) | Kontroliuojamų medžiagų deklaracijų duomenys | `4` | `vda_prime_key` | — | `11` | Narkotikų, tabako ir alkoholio kontrolės departamento (NTAKD) naudojama Pirmtakų teisėtos apyvartos kontrolės informacinė sistema (PTAKIS) kaupia juridinių... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntakd/prekursoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/prekursoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ntakd/ptakis (https://data.gov.lt/datasets/2822/)
