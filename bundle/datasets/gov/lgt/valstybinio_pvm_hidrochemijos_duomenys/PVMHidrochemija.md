---
type: Table
title: "PVMHidrochemija — Valstybinio požeminio vandens monitoringo požeminio vandens hidrochemijos duomenys"
description: "Spinta table datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys/PVMHidrochemija (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys/PVMHidrochemija"
tags: [gov, lgt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# PVMHidrochemija — Valstybinio požeminio vandens monitoringo požeminio vandens hidrochemijos duomenys

- **Model:** `datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys/PVMHidrochemija`[^manifest]
- **Dataset:** [Valstybinio požeminio vandens monitoringo požeminio vandens hidrochemijos duomenys](../valstybinio_pvm_hidrochemijos_duomenys.md) (`datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys`)
- **Manifest CSV:** [datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/valstybinio_pvm_hidrochemijos_duomenys/PVMHidrochemija`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/pozeminio_vandens_hidrochemija.csv
