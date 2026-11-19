---
type: Table
title: "Anestezija — Anestezijos"
description: "Lentelė „Anestezijos“. Lentelę sudaro: operacijos, jos procedūros bei anestezijos identifikatoriai, anestezijos pavadinimas, rūšis, paskyrimo pradžios ir pabaigos laikai."
resource: "https://get.data.gov.lt/datasets/gov/rvul/hops/Anestezija"
tags: [gov, rvul, anestezija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L74"
    title: "atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L74"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3865/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rvul/hops"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Anestezija — Anestezijos

Lentelė „Anestezijos“. Lentelę sudaro: operacijos, jos procedūros bei anestezijos identifikatoriai, anestezijos pavadinimas, rūšis, paskyrimo pradžios ir pabaigos laikai. Vienas lentelės įrašas atitinka vieną operacijos, procedūros ir anestezijos kombinaciją. Dalis operacijų šioje lentelėje neturi paskirtos anestezijos, kadangi techninė galimybė tai padaryti atsirado sistemos vystymo eigoje, jau susidarius daliai įrašų.[^manifest]

- **Model:** `datasets/gov/rvul/hops/Anestezija`[^manifest]
- **Dataset:** [Pacientams atliktų operacijų duomenys](../hops.md) (`datasets/gov/rvul/hops`)[^manifest]
- **Manifest CSV:** [datasets/gov/rvul/hops.csv#L74](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L74)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rvul/hops/Anestezija` (`deployed`)[^manifest]
- **Provider:** `rvul` — VšĮ Respublikinė Vilniaus universitetinė ligoninė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L74 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L74)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rvul/hops (https://data.gov.lt/datasets/3865/)
