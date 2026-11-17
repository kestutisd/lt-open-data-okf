---
type: Table
title: "Gabenimas — Atliekų priėmimas / perdavimas Klaipėdos regione"
description: "Klaipėdos regiono atliekų tvarkymo centro naudojama Atliekų surinkimo, monitoringo ir logistikos informacinė sistema (ASMLIS) kaupia gabenamų atliekų duomenis."
resource: "https://get.data.gov.lt/datasets/gov/kratc/asmlis/Gabenimas"
tags: [gov, kratc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kratc/asmlis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kratc/asmlis.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gabenimas — Atliekų priėmimas / perdavimas Klaipėdos regione

Klaipėdos regiono atliekų tvarkymo centro naudojama Atliekų surinkimo, monitoringo ir logistikos informacinė sistema (ASMLIS) kaupia gabenamų atliekų duomenis. Duomenys kaupiami nuo 2008-07-01 ir atnaujinami iki šiol. Duomenų rinkinys sudarytas iš atliekų gabenimo datos ir laiko, atliekų svorio, atliekų gabenimo kliento sistemoje identifikatoriaus, kliento pseudonimizuoto vardo su pavarde arba pavadinimo, kliento tipo, gabenamų atliekų kodo, apibūdinimo, priėmimo vietos, kurioje svertos atliekos, pavadinimo, adreso ir atliekų tvarkymo veiklos. Vienas įrašas atitinka vieną atliekų gabenimo įvykį. Klientų nurodyti kaip „galimai juridiniai“, kadangi jų asmenų kodai neatitinka JAR kodo taisyklių, tačiau pavadinimai sufleruoja, jog tai juridiniai asmenys.

- **Model:** `datasets/gov/kratc/asmlis/Gabenimas`[^manifest]
- **Dataset:** [Atliekų priėmimas / perdavimas Klaipėdos regione](../asmlis.md) (`datasets/gov/kratc/asmlis`)
- **Manifest CSV:** [datasets/gov/kratc/asmlis.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kratc/asmlis.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kratc/asmlis/Gabenimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `atlieku_priemimo_data_laikas` | `datetime` | `S` | `4` | `open` | — | Atliekų priėmimo data ir laikas | — |
| `atlieku_svoris_t` | `number` | `t` | `4` | `open` | — | Gabenamų atliekų svoris | — |
| `kliento_id` | `string` | — | `4` | `open` | — | Atliekų gabenimo kliento identifikatorius | — |
| `kliento_pavadinimas` | `string` | — | `4` | `open` | — | Rinkliavos mokėtojo pseudonimizuoti pavadinimas arba vardas su pavarde | — |
| `kliento_tipas` | `string` | — | `4` | `open` | — | Rinkliavos mokėtojo asmens rūšis | — |
| `atlieku_kodas` | `string` | — | `4` | `open` | — | Gabenamų atliekų kodas | — |
| `atlieku_pavadinimas` | `string` | — | `4` | `open` | — | Gabenamų atliekų apibūdinimas | — |
| `atlieku_priemimo_vieta` | `string` | — | `4` | `open` | — | Atliekų priėmimo vieta | — |
| `atlieku_priemimo_vietos_adresas` | `string` | — | `4` | `open` | — | Atliekų priėmimo vietos adresas | — |
| `atlieku_tvarkymo_veiklos_pavadinimas` | `string` | — | `4` | `open` | — | Atliekų gabenimo tikslas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kliento_tipas` | `"Juridinis"` | — | — | Lietuvos Respublikos juridinis asmuo | — |
| `kliento_tipas` | `"Nežinoma"` | — | — | Nežinoma asmens rūšis | — |
| `kliento_tipas` | `"Galimai juridinis"` | — | — | Galimai Lietuvos Respublikos juridinis asmuo | — |
| `kliento_tipas` | `"Fizinis"` | — | — | Lietuvos Respublikos fizinis asmuo | — |
| `atlieku_tvarkymo_veiklos_pavadinimas` | `"Priėmimas"` | — | — | Atliekų priėmimas | — |
| `atlieku_tvarkymo_veiklos_pavadinimas` | `"Pervežimas"` | — | — | Atliekų pervežimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kratc/asmlis.csv
