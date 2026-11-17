---
type: Table
title: "MetinisVeiklosPlanas — Valstybės kontrolės metinio veiklos plano duomenys"
description: "Valstybės kontrolės metinio veiklos plano, kuriame pateikiama informacija apie planuojamus, atliekamus auditus ir vertinimus, duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/mvp/MetinisVeiklosPlanas"
tags: [gov, vk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vk/mvp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/mvp.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# MetinisVeiklosPlanas — Valstybės kontrolės metinio veiklos plano duomenys

Valstybės kontrolės metinio veiklos plano, kuriame pateikiama informacija apie planuojamus, atliekamus auditus ir vertinimus, duomenys

- **Model:** `datasets/gov/vk/mvp/MetinisVeiklosPlanas`[^manifest]
- **Dataset:** [datasets/gov/vk/mvp](../mvp.md) (`datasets/gov/vk/mvp`)
- **Manifest CSV:** [datasets/gov/vk/mvp.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/mvp.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/mvp/MetinisVeiklosPlanas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `audit_cardid` | `integer` | — | `3` | `open` | — | Produkto ID | Produkto (audito, vertinimo, išvados, ataskaitos, projekcijos) identifikacijos numeris |
| `plano_metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `veiklos_rusis` | `string` | — | `4` | `open` | — | Veiklos rūšis | Kokio pobūdžio produktas suplanuotas: veiklos auditas, finansinis auditas, atitikties auditas, Europos Sąjungos investicijų auditas, išvada atliekant biudžeto politikos kontrolės institucijos funkcijas, vertinimas |
| `srities_pavadinimas` | `string` | — | `3` | `open` | — | Srities pavadinimas | Srities, kurioje suplanuota atlikti auditą, vertinimą, teikti išvadą, pavadinimas |
| `pavadinimas` | `string` | — | `3` | `open` | — | Pavadinimas | Suplanuoto audito, vertinimo, išvados pavadinimas |
| `aprasymas` | `string` | — | `3` | `open` | — | Aprašymas | Suplanuoto audito, vertinimo, išvados detalesnis aprašymas |
| `busena` | `string` | — | `3` | `open` | — | Būsena | Audito, vertinimo, išvados vykdymo būsenos statusas |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiklos_rusis` | `"Veiklos auditai"` | — | — | Veiklos auditai | Veiklos auditai – kai vertinama audituojamo subjekto veikla ekonomiškumo, efektyvumo ir rezultatyvumo požiūriu. |
| `veiklos_rusis` | `"Finansiniai auditai"` | — | — | Finansiniai auditai | Finansiniai auditai – kai vertinami audituojamo subjekto metinių (konsoliduotųjų) finansinių ir biudžeto vykdymo ataskaitų rinkinių duomenis ir pareiškiama nepriklausoma auditoriaus nuomonė. |
| `veiklos_rusis` | `"Atitikties auditai"` | — | — | Atitikties auditai | Atitikties auditai – kai vertinama audituojamo subjekto veiklos atitiktis teisės aktų ir (ar) kitiems reikalavimams ir gali būti pareiškiama nepriklausoma auditoriaus nuomonė. |
| `veiklos_rusis` | `"Auditai atliekant Europos Sąjungos fondų investicijų audito institucijos funkcijas"` | — | — | Auditai atliekant Europos Sąjungos fondų investicijų audito institucijos funkcijas | Europos Sąjungos investicijų auditai – kai vertinama 2014–2020 m. ES fondų investicijų veiksmų programai įgyvendinti sukurta valdymo ir kontrolės sistema ir Europos Komisijos deklaruojamų lėšų tinkamumas. |
| `veiklos_rusis` | `"Išvados atliekant biudžeto politikos kontrolės institucijos funkcijas"` | — | — | Išvados atliekant biudžeto politikos kontrolės institucijos funkcijas | Išvados (ataskaitos, vertinimai) dėl makroekonominių prognozių, fiskalinės drausmės taisyklių laikymosi, struktūrinio postūmio užduoties nustatymo pagrįstumo, metinių biudžeto projektų, kt. |
| `veiklos_rusis` | `"Vertinimai"` | — | — | Vertinimai | Vertinimai – tai AAI vykdoma veikla, kai susisteminama ir apibendrinama tam tikroje viešojo sektoriaus srityje atliktų valstybinių auditų informacija ir atskleidžiama viešojo sektoriaus srities esama būklė. |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `plano_metai` | `update(type: "date", ref: "Y")` | `type, ref` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/mvp.csv
