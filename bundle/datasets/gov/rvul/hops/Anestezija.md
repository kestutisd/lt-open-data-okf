---
type: Table
title: "Anestezija — Anestezijos"
description: "Lentelė „Anestezijos“."
resource: "https://get.data.gov.lt/datasets/gov/rvul/hops/Anestezija"
tags: [gov, rvul, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rvul/hops.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L74"
    last_modified: "2026-11-11T14:39:20Z"
---

# Anestezija — Anestezijos

Lentelė „Anestezijos“. Lentelę sudaro: operacijos, jos procedūros bei anestezijos identifikatoriai, anestezijos pavadinimas, rūšis, paskyrimo pradžios ir pabaigos laikai. Vienas lentelės įrašas atitinka vieną operacijos, procedūros ir anestezijos kombinaciją. Dalis operacijų šioje lentelėje neturi paskirtos anestezijos, kadangi techninė galimybė tai padaryti atsirado sistemos vystymo eigoje, jau susidarius daliai įrašų.

- **Model:** `datasets/gov/rvul/hops/Anestezija`[^manifest]
- **Dataset:** [Pacientams atliktų operacijų duomenys](../hops.md) (`datasets/gov/rvul/hops`)
- **Manifest CSV:** [datasets/gov/rvul/hops.csv#L74](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L74)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rvul/hops/Anestezija`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `operacijos_id` | `string` | — | `4` | `open` | — | Išorinis raktas į operaciją | — |
| `proceduros_id` | `string` | — | `4` | `open` | — | Išorinis raktas į procedūrą | — |
| `anestezijos_id` | `string` | — | `4` | `open` | — | Anestezijos identifikatorius | — |
| `anestezijos_pavadinimas` | `string` | — | `4` | `open` | — | Anestezijos pavadinimas | — |
| `anestezijos_rusis` | `string` | — | `4` | `open` | — | Anestezijos rūšis | — |
| `anestezijos_pradzia` | `datetime` | `S` | `4` | `open` | — | Anestezijos taikymo pradžios data ir laikas | — |
| `anestezijos_pabaiga` | `datetime` | `S` | `4` | `open` | — | Anestezijos taikymo pabaigos data ir laikas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `anestezijos_pavadinimas` | `"Intubacinė (BETA)"` | — | — | Intubacinė (BETA) | — |
| `anestezijos_pavadinimas` | `"Spinalinė"` | — | — | Spinalinė | — |
| `anestezijos_pavadinimas` | `"Nervų rezginių blokada"` | — | — | Nervų rezginių blokada | — |
| `anestezijos_pavadinimas` | `"Laringinė (LMA)"` | — | — | Laringinė (LMA) | — |
| `anestezijos_pavadinimas` | `"Intraveninė"` | — | — | Intraveninė | — |
| `anestezijos_pavadinimas` | `"Epidūrinė"` | — | — | Epidūrinė | — |
| `anestezijos_rusis` | `"Bendroji"` | — | — | Bendroji | — |
| `anestezijos_rusis` | `"Regioninė"` | — | — | Regioninė | — |
| `anestezijos_rusis` | `"Vietinė"` | — | — | Vietinė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rvul/hops.csv
