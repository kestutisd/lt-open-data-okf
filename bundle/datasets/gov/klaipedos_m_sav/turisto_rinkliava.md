---
type: Dataset
title: "Turisto rinkliavos deklaravimo duomenų rinkinys"
description: "Informacija apie pateiktas turisto rinkliavos deklaracijas"
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/turisto_rinkliava"
tags: [gov, klaipedos_m_sav, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3972/"
    title: "data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/turisto_rinkliava"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Turisto rinkliavos deklaravimo duomenų rinkinys

Informacija apie pateiktas turisto rinkliavos deklaracijas[^manifest]

- **Namespace:** `datasets/gov/klaipedos_m_sav/turisto_rinkliava`[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/turisto_rinkliava` (`deployed`)[^manifest]
- **Provider:** `klaipedos_m_sav` — Klaipėdos miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3972/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/turisto_rinkliava`[^dcat]
- **Portal Title (`@lt`):** Turisto rinkliavos deklaravimo duomenų rinkinys[^dcat]
- **Portal Title (`@en`):** TRIS[^dcat]
- **Issued (`dct:issued`):** `2025-11-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-11-25` .. `2025-11-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Klaipėdos miesto savivaldybės vietinės rinkliavos už suteiktą nakvynę (vadinamąjį turisto rinkliavos mokestį) deklaracijų duomenys. Vietinė rinkliava Klaipėdoje yra 1 euras už vienam asmeniui suteiktą nakvynę. Deklaracijas teikia fiziniai ir juridiniai asmenys, teikiantys apgyvendinimo paslaugas Klaipėdos mieste – nepriklausomai nuo to, ar veikla vykdoma pagal verslo liudijimą, individualios veiklos pažymą ar kitą apgyvendinimo paslaugų teikimo formą. Rinkinio objektas – viena turisto rinkliavos deklaracija, pateikta konkretaus apgyvendinimo paslaugų teikėjo už atitinkamus atskaitinius metus ir mėnesį ar ketvirtį. Rinkinyje pateikiami duomenys nurodo deklaraciją pateikusio subjekto tipą (fizinis ar juridinis asmuo), jo veiklą pagal Ekonominės veiklos rūšių klasifikatorių (EVRK 2.1), bei deklaracijos pateikimo laikotarpį. Šiame rinkinyje pateikiami duomenys neapima konkrečių nakvynių skaičiaus ar mokėtinų rinkliavos sumų, o atspindi faktą, jog deklaracija už tam tikrą laikotarpį buvo pateikta. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

TRIS[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TuristoRinkliava](turisto_rinkliava/TuristoRinkliava.md) | Turisto rinkliavos deklaravimo duomenys | `4` | `vda_prime_key` | — | `8` | Rinkinyje pateikiami Klaipėdos miesto savivaldybės vietinės rinkliavos už suteiktą nakvynę (vadinamąjį turisto rinkliavos mokestį) deklaracijų duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/turisto_rinkliava (https://data.gov.lt/datasets/3972/)
