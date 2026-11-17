---
type: Table
title: "Dalyvis — Olimpiadų nugalėtojų duomenys"
description: "Lietuvos neformaliojo švietimo agentūros (LINEŠA) Olimpiadų nugalėtojų duomenų bazėje kaupiami vietinėse bei tarptautinėse olimpiadose nugalėjusių moksleivių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/linesa/ondb/Dalyvis"
tags: [gov, linesa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/linesa/ondb.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/linesa/ondb.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dalyvis — Olimpiadų nugalėtojų duomenys

Lietuvos neformaliojo švietimo agentūros (LINEŠA) Olimpiadų nugalėtojų duomenų bazėje kaupiami vietinėse bei tarptautinėse olimpiadose nugalėjusių moksleivių duomenys. Duomenys kaupiami nuo 2008 m. ir yra atnaujinami kasmet. Viena duomenų lentelės eilutė priskirta vienam moksleiviui, tam tikru metu dalyvavusiam kurioje nors iš olimpiadų. Duomenis sudaro: olimpiados pavadinimas, olimpiados tipas (vietinė arba tarptautinė), dalyvavusio moksleivio pelnytas prizas arba užimta vieta, šifruoti nugalėtojo vardas ir pavardė, moksleivio švietimo įstaiga, klasė bei olimpiadai ruošęs mokytojas, tarptautinėse olimpiadose paskirti komandų vadovai, olimpiados vieta ir data. *Lietuvos neformaliojo švietimo agentūros nuomone, olimpiadų nugalėtojai negali būti skelbiami.

- **Model:** `datasets/gov/linesa/ondb/Dalyvis`[^manifest]
- **Dataset:** [Olimpiadų nugalėtojų duomenys](../ondb.md) (`datasets/gov/linesa/ondb`)
- **Manifest CSV:** [datasets/gov/linesa/ondb.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/linesa/ondb.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/linesa/ondb/Dalyvis`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `renginys` | `string` | — | `4` | `open` | — | Olimpiados renginio pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Olimpiados renginio tipas | — |
| `laimejimas` | `string` | — | `4` | `open` | — | Dalyvio pelnytas laimėjimas | — |
| `vardas` | `string` | — | `4` | `open` | — | Dalyvio užšifruotas vardas | — |
| `pavarde` | `string` | — | `4` | `open` | — | Dalyvio užšifruota pavardė | — |
| `mokytojai` | `string` | — | `4` | `open` | — | Dalyvį parengę mokytojai | — |
| `komandos_vadovai` | `string` | — | `4` | `open` | — | Tarptautinėse olimpiadose paskirti komandų vadovai | — |
| `svietimo_istaiga` | `string` | — | `4` | `open` | — | Dalyvio švietimo įstaiga, kurioje mokėsi | — |
| `klase` | `string` | — | `4` | `open` | — | Dalyvio mokyklinė klasė | — |
| `vieta` | `string` | — | `4` | `open` | — | Olimpiados renginio vieta | — |
| `metai` | `integer` | — | `4` | `open` | — | Olimpiados renginio tikslūs metai | — |
| `pilna_data` | `string` | — | `4` | `open` | — | Olimpiados renginio žodinė data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Lietuvos"` | `Lietuvos` | — | Lietuvoje vykusi olimpiada | — |
| `tipas` | `"Tarptautinis"` | `Tarptautinis` | — | Užsienyje vykusi olimpiada | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/linesa/ondb.csv
