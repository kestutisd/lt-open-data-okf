---
type: Dataset
title: "Pacientams atliktų operacijų duomenys"
description: "Respublikinės Vilniaus universitetinės ligoninės Operacijų planavimo ir valdymo sistemoje (HOPS) kaupiami pacientams atliktų operacijų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/rvul/hops"
tags: [gov, rvul, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rvul/hops.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pacientams atliktų operacijų duomenys

Respublikinės Vilniaus universitetinės ligoninės Operacijų planavimo ir valdymo sistemoje (HOPS) kaupiami pacientams atliktų operacijų duomenys. Rinkinyje pateikiami nuo 2023 metų rugpjūčio mėnesio sukaupti ir iki šiol atnaujinami duomenys. Bendras duomenų rinkinys sudarytas iš penkių lentelių: „Operacijos“, „Medikai“, „Anestezijos“, „Vaidmenys“ ir „Pacientai“. Rinkinyje visi laikai nurodyti Centrinės Europos (CET) laiko zona. Duomenų teikėjai – VšĮ Respublikinė Vilniaus universitetinė ligoninė ir Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba prie Sveikatos Apsaugos Ministerijos (VASPVT).

- **Namespace:** `datasets/gov/rvul/hops`[^manifest]
- **Manifest CSV:** [datasets/gov/rvul/hops.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rvul/hops`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Operacija](hops/Operacija.md) | Operacijos | `4` | `vda_prime_key` | — | 12 | Lentelė „Operacijos“. |
| [Medikas](hops/Medikas.md) | Medikai | `4` | `vda_prime_key` | — | 16 | Lentelė „Medikai“. |
| [Pacientas](hops/Pacientas.md) | Pacientai | `4` | `vda_prime_key` | — | 6 | Lentelė „Pacientai“. |
| [Anestezija](hops/Anestezija.md) | Anestezijos | `4` | `vda_prime_key` | — | 8 | Lentelė „Anestezijos“. |
| [Vaidmuo](hops/Vaidmuo.md) | Vaidmenys | `4` | `vda_prime_key` | — | 5 | Lentelė „Vaidmenys“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rvul/hops.csv
