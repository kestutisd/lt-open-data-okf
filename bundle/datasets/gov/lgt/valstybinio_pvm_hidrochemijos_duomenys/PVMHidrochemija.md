---
type: Table
title: "PVMHidrochemija — Valstybinio požeminio vandens monitoringo požeminio vandens hidrochemijos duomenys"
description: "Spinta table datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys/PVMHidrochemija (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys/PVMHidrochemija"
tags: [gov, lgt, pvmhidrochemija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1332/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PVMHidrochemija — Valstybinio požeminio vandens monitoringo požeminio vandens hidrochemijos duomenys

- **Model:** `datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys/PVMHidrochemija`[^manifest]
- **Dataset:** [Valstybinio požeminio vandens monitoringo požeminio vandens hidrochemijos duomenys](../valstybinio_pvm_hidrochemijos_duomenys.md) (`datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys/PVMHidrochemija` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `posto_nr` | `integer` | — | `4` | `open` | — | Stebimojo posto numeris | — |
| `posto_pavadinimas` | `string` | — | `4` | `open` | — | Stebimojo posto pavadinimas | — |
| `grezinio_nr` | `string` | — | `4` | `open` | — | Gręžinio numeris | — |
| `koord` | `geometry(point,3346)` | `m` | `4` | `open` | — | Koordinatės | — |
| `abs_aukstis` | `number` | `m` | `4` | `open` | — | Taško absoliutinis aukštis | — |
| `gylis_nuo` | `number` | `m` | `4` | `open` | — | Bandinio paėmimo intervalo gylis nuo | — |
| `gylis_iki` | `number` | `m` | `4` | `open` | — | Bandinio paėmimo intervalo gylis iki | — |
| `ban_paemimo_data` | `date` | `D` | `4` | `open` | — | Bandinio paėmimo data | — |
| `chemijos_pavadinimas` | `string` | — | `3` | `open` | — | Cheminio elemento arba tiriamo parametro pavadinimas | — |
| `cas_nr` | `string` | — | `4` | `open` | — | Cheminių medžiagų santrumpų tarnybos (angl. Chemical Abstracts Service) suteiktas medžiagos registracijos numeris | — |
| `kiekio_charakteristika` | `string` | — | `3` | `open` | — | Kiekio charakteristika | — |
| `kiekis` | `number` | — | `4` | `open` | — | Kiekis | — |
| `mato_vienetas` | `string` | — | `4` | `open` | — | Matavimo vienetas | — |
| `standartas` | `string` | — | `3` | `open` | — | Standartas | — |
| `metodas` | `string` | — | `3` | `open` | — | Metodas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys (https://data.gov.lt/datasets/1332/)
