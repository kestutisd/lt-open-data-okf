---
type: Table
title: "Salis — Viešųjų pirkimų šalys"
description: "Viešųjų pirkimų šalių lentelė."
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp/Salis"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/cvpp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L42"
    last_modified: "2026-11-11T14:39:20Z"
---

# Salis — Viešųjų pirkimų šalys

Viešųjų pirkimų šalių lentelė. Duomenų rinkinys sudarytas iš pirkimo dokumento identifikatoriaus, šalies asmens kodo, asmens rūšies, pavadinimo, eilės numerio viešojo pirkimio sutartyje, požymio, ar ši šalis yra tiekėjas, bei tiekėjo subjekto patikslinimo. Vienas įrašas atitinka vieną dokumento ir šalies kombinaciją.

- **Model:** `datasets/gov/lsd/vpt/cvpp/Salis`[^manifest]
- **Dataset:** [Viešųjų pirkimų duomenys](../cvpp.md) (`datasets/gov/lsd/vpt/cvpp`)
- **Manifest CSV:** [datasets/gov/lsd/vpt/cvpp.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L42)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp/Salis`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `dok_id` | `string` | — | `4` | `open` | — | Išorinis raktas į viešojo pirkimo sutartį | — |
| `salies_kodas` | `string` | — | `4` | `open` | — | Šalies asmens kodas | — |
| `salies_asmens_rusis` | `string` | — | `4` | `open` | — | Šalies asmens rūšis | — |
| `salies_pavadinimas` | `string` | — | `4` | `open` | — | Šalies pavadinimas | — |
| `salies_eil_nr` | `integer` | — | `4` | `open` | — | Šalies eilės numeris atitinkamoje viešojo pirkimo sutartyje | — |
| `ar_salis_tiekejas` | `boolean` | — | `4` | `open` | — | Ar šalis yra tiekėjas atitinkamoje viešojo pirkimo sutartyje | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `salies_asmens_rusis` | — | `"Juridinis"` | — | Juridinis | — |
| `salies_asmens_rusis` | — | `"Fizinis"` | — | Fizinis | — |
| `salies_asmens_rusis` | — | `"Nežinomas"` | — | Nežinomas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/cvpp.csv
