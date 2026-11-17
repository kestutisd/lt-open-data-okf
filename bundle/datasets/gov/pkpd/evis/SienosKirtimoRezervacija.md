---
type: Table
title: "SienosKirtimoRezervacija — Transporto priemonių rezervacijos kirsti pasienį"
description: "Pasienio kontrolės punktų direkcijos (PKPD) ir VĮ „Regitra“ duomenų bendras rinkinys, sudarytas Valstybės duomenų agentūros."
resource: "https://get.data.gov.lt/datasets/gov/pkpd/evis/SienosKirtimoRezervacija"
tags: [gov, pkpd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pkpd/evis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/evis.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# SienosKirtimoRezervacija — Transporto priemonių rezervacijos kirsti pasienį

Pasienio kontrolės punktų direkcijos (PKPD) ir VĮ „Regitra“ duomenų bendras rinkinys, sudarytas Valstybės duomenų agentūros. Duomenys kaupiami nuo 2013 m. ir atnaujinami kasdien. Duomenų rinkinyje saugomas paslaugos kirsti pasienį registracijos identifikatorius, registracijos kaina, mokestis ir kaina su mokesčiu. Taip pat yra nurodyti atvykimo į laukimo aikštelę, į pasienio kontrolės punktą laikai, punkto pavadinimas bei kaimyninė valstybė. Saugomas eilės tipas, transporto priemonės šifruotas valstybinis numeris, VIN šalis, rūšis, kategorija, ar transporto priemonė registruota Lietuvoje, šifruotas fizinio savininko arba atviras juridinio asmens kodas ir savininko pavadinimas, jei tai juridinis asmuo.

- **Model:** `datasets/gov/pkpd/evis/SienosKirtimoRezervacija`[^manifest]
- **Dataset:** [Transporto priemonių rezervacijos kirsti pasienį](../evis.md) (`datasets/gov/pkpd/evis`)
- **Manifest CSV:** [datasets/gov/pkpd/evis.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/evis.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pkpd/evis/SienosKirtimoRezervacija`
- **Primary Key (`ref`):** `reg_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_id` | `string` | — | `4` | `open` | — | Registracijos kirsti sieną paslaugos identifikatorius | — |
| `reg_kaina` | `number` | — | `4` | `open` | — | Registracijos kirsti sieną kaina eurais | — |
| `reg_mok` | `number` | — | `4` | `open` | — | Registracijos kirsti sieną mokestis eurais | — |
| `reg_kaina_su_mok` | `number` | — | `4` | `open` | — | Registracijos kirsti sieną kaina su mokesčiu eurais | — |
| `rezervacijos_sukurimo_laikas` | `datetime` | `S` | `4` | `open` | — | Rezervacijos įrašo sukūrimo data ir laikas | — |
| `atvykimo_i_aikstele_laikas` | `datetime` | `S` | `4` | `open` | — | Atvykimo į aikštelę data ir laikas | — |
| `atvykimo_i_pkp_laikas` | `datetime` | `S` | `4` | `open` | — | Atvykimo į pasienio kontrolės punktą data ir laikas | — |
| `punkto_pav` | `string` | — | `4` | `open` | — | Punkto pavadinimas | — |
| `kaimynine_valstybe` | `string` | — | `4` | `open` | — | Punkto kaimyninė valstybė | — |
| `eiles_tipas` | `string` | — | `4` | `open` | — | Eilės tipas: gyvoji, rezervinė arba prioritetinė | — |
| `tp_valst_nr` | `string` | — | `4` | `open` | — | Transporto priemonės valstybinis numeris | — |
| `tp_vin_salis` | `string` | — | `4` | `open` | — | Transporto priemonės šalis iš VIN | — |
| `tp_rusis` | `string` | — | `4` | `open` | — | Transporto priemonės rūšis | — |
| `tp_kategorija` | `string` | — | `4` | `open` | — | Transporto priemonės kategorija | — |
| `ar_tp_registruota_lr` | `string` | — | `4` | `open` | — | Ar transporto priemonė registruota Lietuvos Respublikoje | — |
| `tp_sav_kodas` | `string` | — | `4` | `open` | — | Transporto priemonės savininko fizinio arba juridinio asmens kodas | — |
| `tp_sav_jur_asm_pav` | `string` | — | `4` | `open` | — | Transporto priemonės juridinio asmens kaip savininko pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `eiles_tipas` | `"Gyvoji"` | `Gyvoji` | — | Gyvoji eilė | — |
| `eiles_tipas` | `"Išankstinė rezervacija"` | `Išankstinė rezervacija` | — | Išankstinės rezervacijos eilė | — |
| `eiles_tipas` | `"Prioritetinė"` | `Prioritetinė` | — | Prioritetinė eilė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_kaina` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `reg_mok` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `reg_kaina_su_mok` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pkpd/evis.csv
