---
type: Dataset
title: "Šiukšliavežių maršrutai"
description: "Duomenų rinkinyje pateikiami šiukšliavežių maršrutų duomenys: šifruotas automobilio valstybinis numeris, automobilio markė, laikas ir koordinatės, nurodančios vietą, kurioje tuo metu buvo automobilis."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/marsrutai"
tags: [gov, asmlis, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/marsrutai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/marsrutai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2918/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/marsrutai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Šiukšliavežių maršrutai

Duomenų rinkinyje pateikiami šiukšliavežių maršrutų duomenys: šifruotas automobilio valstybinis numeris, automobilio markė, laikas ir koordinatės, nurodančios vietą, kurioje tuo metu buvo automobilis.[^manifest]

- **Namespace:** `datasets/gov/asmlis/marsrutai`[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/marsrutai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/marsrutai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/marsrutai` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2918/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/asmlis/marsrutai`[^dcat]
- **Portal Title (`@lt`):** Šiukšliavežių maršrutų duomenys[^dcat]
- **Portal Title (`@en`):** Trash routes data[^dcat]
- **Issued (`dct:issued`):** `2025-01-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-01-15` .. `2026-10-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, šiukšliavežių maršrutų duomenys. Duomenų rinkinyje pateikiami šiukšliavežių maršrutų duomenys: šifruotas automobilio valstybinis numeris, automobilio markė, laikas ir koordinatės, nurodančios vietą, kurioje tuo metu buvo automobilis. Duomenų teikėjai: Šalčininkų rajono savivaldybės administracija; Kėdainių rajono savivaldybės administracija; UAB „Kauno švara“; Vilniaus rajono savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The information system OF the municipal administration of Šalčininkai district shall accumulate data on waste management charges and other data. The data set provides data on the trash routes: the encrypted vehicle's state number, car brand, time and coordinates indicating the location where the vehicle was located at the time. Data provider – Salcininku District Municipality administration. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SalcininkuSiuksliavezioMarsrutas](marsrutai/SalcininkuSiuksliavezioMarsrutas.md) | Šalčininkų rajono šiukšliavežių maršrutai | `4` | `vda_prime_key` | — | `12` | Šalčininkų rajono savivaldybės administracijos informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis. |
| [KedainiuSiuksliavezioMarsrutas](marsrutai/KedainiuSiuksliavezioMarsrutas.md) | Kėdainių rajono šiukšliavežių maršrutai | `4` | `vda_prime_key` | — | `10` | Kėdainių rajono savivaldybės administracijos informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis. |
| [KaunoSvaraSiuksliavezioMarsrutas](marsrutai/KaunoSvaraSiuksliavezioMarsrutas.md) | UAB Kauno švara šiukšliavežių maršrutai | `4` | `vda_prime_key` | — | `10` | UAB Kauno švara informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis. |
| [VilniausRajSiuksliavezioMarsrutas](marsrutai/VilniausRajSiuksliavezioMarsrutas.md) | Vilniaus rajono savivaldybės šiukšliavežių maršrutai | `4` | `vda_prime_key` | — | `10` | Vilniaus rajono savivaldybės informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/marsrutai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/marsrutai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/marsrutai (https://data.gov.lt/datasets/2918/)
