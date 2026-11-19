---
type: Dataset
title: "Viešųjų pirkimų duomenys"
description: "Viešųjų pirkimų tarnybos Centrinė viešųjų pirkimų sistemos sutarčių posistemė kaupia viešųjų pirkimų sutarčių bei juose dalyvaujančių šalių duomenis."
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp"
tags: [gov, lsd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/cvpp.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2867/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/vpt/cvpp"
    author: "team:vda"
    last_modified: "2026-06-12T00:00:00Z"
---

# Viešųjų pirkimų duomenys

Viešųjų pirkimų tarnybos Centrinė viešųjų pirkimų sistemos sutarčių posistemė kaupia viešųjų pirkimų sutarčių bei juose dalyvaujančių šalių duomenis. Rinkinys sudarytas iš dviejų atskirų lentelių apie viešųjų pirkimų sutatis ir jose dalyvaujančias šalis. Abi lentelės yra apjungiamos dokumentų identifikatoriaus stulpelių. Nors sutarčių lentelės stulpeliai palikti kuo panašesni į pradinius įstaigos prašymu, šalių lentelės stulpeliai pervadinti vartotojui draugiškesne kalba siekiant išvengti painiavos naudojant pradinius pavadinimus. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/lsd/vpt/cvpp`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/vpt/cvpp.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp` (`deployed`)[^manifest]
- **Provider:** `lsd` — Viešųjų pirkimų tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2867/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp`[^dcat]
- **Portal Title (`@lt`):** Viešųjų pirkimų duomenys[^dcat]
- **Portal Title (`@en`):** Procurement data of the Public Procurement Office[^dcat]
- **Issued (`dct:issued`):** `2024-11-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-06-12`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-22` .. `2026-10-20`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Viešųjų pirkimų tarnybos Centrinė viešųjų pirkimų sistemos sutarčių posistemė kaupia viešųjų pirkimų sutarčių bei jose dalyvaujančių šalių duomenis. Rinkinys sudarytas iš dviejų atskirų lentelių apie viešųjų pirkimų sutartis ir jose dalyvaujančias šalis. Abi lentelės yra apjungiamos dokumentų identifikatoriaus stulpeliais. Nors sutarčių lentelės stulpeliai palikti kuo panašesni į pradinius įstaigos prašymu, šalių lentelės stulpeliai pervadinti vartotojui draugiškesne kalba, siekiant išvengti painiavos naudojant pradinius pavadinimus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Central Subsystem of Contracts of the Public Procurement Office shall collect data on public procurement contracts and the countries participating therein. The package consists of two separate tables on the nature of public procurement and the countries involved. Both tables are combined by document identifier columns. Although the columns in the contract table have been kept as close as possible to the original ones at the institution's request, the columns in the country table have been renamed a more user friendly language in order to avoid confusion in the use of the original names. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sutartis](cvpp/Sutartis.md) | Viešųjų pirkimų sutartys | — | `dok_id` | — | `26` | Viešųjų pirkimų sutarčių lentelė. |
| [Salis](cvpp/Salis.md) | Viešųjų pirkimų šalys | — | `vda_prime_key` | — | `7` | Viešųjų pirkimų šalių lentelė. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/cvpp.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/vpt/cvpp (https://data.gov.lt/datasets/2867/)
