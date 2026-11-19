---
type: Dataset
title: "Juridinių asmenų ekonominės veiklos rūšys ir instituciniai sektoriai"
description: "Rinkinyje pateikiama informacija apie visus juridinių asmenų registre (VĮ Registrų centras) įregistruotus juridinius asmenis, jų vykdomą pagrindinę ekonominę veiklą, jiems priskirtą institucinių sektorių ir subsektorių, jų nuosavybės formą."
resource: "https://get.data.gov.lt/datasets/gov/lsd/cl/ja_asmenys"
tags: [gov, lsd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/ja_asmenys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/cl/ja_asmenys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2088/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/cl/ja_asmenys"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# Juridinių asmenų ekonominės veiklos rūšys ir instituciniai sektoriai

- **Namespace:** `datasets/gov/lsd/cl/ja_asmenys`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/cl/ja_asmenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/ja_asmenys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/cl/ja_asmenys` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2088/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/cl/ja_asmenys`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų ekonominės veiklos rūšys ir instituciniai sektoriai[^dcat]
- **Portal Title (`@en`):** Types of economic activity of legal entities and institutional sectors[^dcat]
- **Issued (`dct:issued`):** `2023-02-20`[^dcat]
- **Last Modified (`dct:modified`):** `2026-02-25`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2022-12-13` .. `2026-10-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiama informacija apie visus juridinių asmenų registre (VĮ Registrų centras) įregistruotus juridinius asmenis, jų vykdomą pagrindinę ekonominę veiklą, jiems priskirtą institucinių sektorių ir subsektorių, jų nuosavybės formą. Taip pat ir apie išregistruotus juridinius asmenis su jiems jų išregistravimo metu nustatyta informacija Statistinio ūkio subjektų registre (SŪSR). Taip pat yra galimybė iš duomenų rinkinio išskirti tik veikiančius juridinius asmenis. Veikiančių juridinių asmenų sąrašas - tai yra tam tikros datos SŪSR išrašas, kuris sudaromas naudojant papildomus statistinius duomenis apie jų vykdomą veiklą, pajamas, darbuotojus ir kt. Sąrašas sudaromas kartą metuose ir nekeičiamas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Open data on all legal entities registered in the Register of Legal Entities (VĮ Registruu centras), performing economic activity and not performing it, with and without employees and/or income, including information of deregistered legal entities from the Register of Statistical Economic Entities.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [JuridinisAsmuo](ja_asmenys/JuridinisAsmuo.md) | Juridinis Asmuo | `4` | — | — | `14` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/cl/ja_asmenys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/ja_asmenys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/cl/ja_asmenys (https://data.gov.lt/datasets/2088/)
