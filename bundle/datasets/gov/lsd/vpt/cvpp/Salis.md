---
type: Table
title: "Salis — Viešųjų pirkimų šalys"
description: "Viešųjų pirkimų šalių lentelė."
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp/Salis"
tags: [gov, lsd, salis, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L42"
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/cvpp.csv#L42"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2867/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/vpt/cvpp"
    author: "team:vda"
    last_modified: "2026-06-12T00:00:00Z"
---

# Salis — Viešųjų pirkimų šalys

Viešųjų pirkimų šalių lentelė. Duomenų rinkinys sudarytas iš pirkimo dokumento identifikatoriaus, šalies asmens kodo, asmens rūšies, pavadinimo, eilės numerio viešojo pirkimio sutartyje, požymio, ar ši šalis yra tiekėjas, bei tiekėjo subjekto patikslinimo. Vienas įrašas atitinka vieną dokumento ir šalies kombinaciją.[^manifest]

- **Model:** `datasets/gov/lsd/vpt/cvpp/Salis`[^manifest]
- **Dataset:** [Viešųjų pirkimų duomenys](../cvpp.md) (`datasets/gov/lsd/vpt/cvpp`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/vpt/cvpp.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L42)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp/Salis` (`deployed`)[^manifest]
- **Provider:** `lsd` — Viešųjų pirkimų tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-06-12`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `salies_asmens_rusis` | — | `"Juridinis"` | — | Juridinis | — |
| `salies_asmens_rusis` | — | `"Fizinis"` | — | Fizinis | — |
| `salies_asmens_rusis` | — | `"Nežinomas"` | — | Nežinomas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/cvpp.csv#L42 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L42)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/vpt/cvpp (https://data.gov.lt/datasets/2867/)
