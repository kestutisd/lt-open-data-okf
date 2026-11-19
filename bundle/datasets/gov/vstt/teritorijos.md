---
type: Dataset
title: "Saugomų teritorijų valstybės kadastro duomenys"
description: "Saugomų teritorijų valstybės kadastro duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vstt/teritorijos"
tags: [gov, vstt, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/789/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/teritorijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Saugomų teritorijų valstybės kadastro duomenys

Saugomų teritorijų valstybės kadastro duomenys[^manifest]

- **Namespace:** `datasets/gov/vstt/teritorijos`[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/saugomu_ter_kadastras.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `18` (18 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/789/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė saugomų teritorijų tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vstt/teritorijos`[^dcat]
- **Portal Title (`@lt`):** Saugomų teritorijų valstybės kadastro duomenys[^dcat]
- **Portal Title (`@en`):** State Cadastre of Protected Areas of the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2023-03-02`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2020-06-10` .. `2026-07-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

LR saugomų teritorijų valstybės kadastre kaupiama ir teikiama informacija apie Lietuvos Respublikos teritorijoje įsteigtas saugomas teritorijas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The State Cadastre of Protected Areas of the Republic of Lithuania collects and provides information on protected areas established in the territory of the Republic of Lithuania.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BuveiniuApsaugaiSvarbiTeritorija](teritorijos/BuveiniuApsaugaiSvarbiTeritorija.md) | Buveinių apsaugai svarbios teritorijos | `4` | `bast_kodas` | — | `16` | — |
| [BiosferosPoligonas](teritorijos/BiosferosPoligonas.md) | Biosferos poligonai | `4` | `id` | — | `25` | — |
| [BiosferosRezervatas](teritorijos/BiosferosRezervatas.md) | Biosferos rezervatai | `4` | `id` | — | `31` | — |
| [BotaninisGpoPlotas](teritorijos/BotaninisGpoPlotas.md) | Botaniniai GPO Plotai | `4` | `id` | — | `55` | — |
| [BotaninisGpoTaskas](teritorijos/BotaninisGpoTaskas.md) | Botaniniai GPO Taškai | `4` | `id` | — | `49` | — |
| [BuferineApsaugosZona](teritorijos/BuferineApsaugosZona.md) | Buferinės apsaugos zonos | `4` | `id` | — | `19` | — |
| [Draustinis](teritorijos/Draustinis.md) | Draustiniai | `4` | `id` | — | `30` | — |
| [FunkcinioPrioritetoZona](teritorijos/FunkcinioPrioritetoZona.md) | Funkcinio prioriteto zonos | `4` | `id` | — | `25` | — |
| [GeologinisGpoPlotas](teritorijos/GeologinisGpoPlotas.md) | Geologiniai GPO Plot | `4` | `id` | — | `47` | — |
| [GeologinisGpoTaskas](teritorijos/GeologinisGpoTaskas.md) | Geologiniai GPO Taškai | `4` | `id` | — | `48` | — |
| [GeomorfologinisGpoPlotas](teritorijos/GeomorfologinisGpoPlotas.md) | Geomorfologiniai GPO Plotai | `4` | `id` | — | `47` | — |
| [HidrogeologinisGpoPlotas](teritorijos/HidrogeologinisGpoPlotas.md) | Hidrogeologiniai GPO Plotai | `4` | `id` | — | `54` | — |
| [HidrografinisGpoPlotas](teritorijos/HidrografinisGpoPlotas.md) | Hidrografiniai GPO Plotai | `4` | `id` | — | `48` | — |
| [Parkas](teritorijos/Parkas.md) | Parkai | `4` | `id` | — | `31` | — |
| [PauksciuApsaugaiSvarbiTeritorija](teritorijos/PauksciuApsaugaiSvarbiTeritorija.md) | Paukščių apsaugai svarbios teritorijos | `4` | `id` | — | `17` | — |
| [Rezervatas](teritorijos/Rezervatas.md) | Rezervatai | `4` | `id` | — | `30` | — |
| [Sklypas](teritorijos/Sklypas.md) | Atkuriamieji sklypai ir genetiniai sklypai | `4` | `id` | — | `26` | — |
| [ZoologinisGpoPlotas](teritorijos/ZoologinisGpoPlotas.md) | Zoologiniai GPO Plotai | `4` | `id` | — | `48` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/saugomu_ter_kadastras.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/saugomu_ter_kadastras.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/teritorijos (https://data.gov.lt/datasets/789/)
