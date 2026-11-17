---
type: Dataset
title: "Viešųjų pirkimų duomenys"
description: "Viešųjų pirkimų tarnybos Centrinė viešųjų pirkimų sistemos sutarčių posistemė kaupia viešųjų pirkimų sutarčių bei juose dalyvaujančių šalių duomenis."
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/cvpp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Viešųjų pirkimų duomenys

Viešųjų pirkimų tarnybos Centrinė viešųjų pirkimų sistemos sutarčių posistemė kaupia viešųjų pirkimų sutarčių bei juose dalyvaujančių šalių duomenis. Rinkinys sudarytas iš dviejų atskirų lentelių apie viešųjų pirkimų sutatis ir jose dalyvaujančias šalis. Abi lentelės yra apjungiamos dokumentų identifikatoriaus stulpelių. Nors sutarčių lentelės stulpeliai palikti kuo panašesni į pradinius įstaigos prašymu, šalių lentelės stulpeliai pervadinti vartotojui draugiškesne kalba siekiant išvengti painiavos naudojant pradinius pavadinimus.

- **Namespace:** `datasets/gov/lsd/vpt/cvpp`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/vpt/cvpp.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sutartis](cvpp/Sutartis.md) | Viešųjų pirkimų sutartys | — | `dok_id` | — | 26 | Viešųjų pirkimų sutarčių lentelė. |
| [Salis](cvpp/Salis.md) | Viešųjų pirkimų šalys | — | `vda_prime_key` | — | 7 | Viešųjų pirkimų šalių lentelė. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/cvpp.csv
