---
type: Table
title: "VtsFr0564Mainai — FR0564_DUOMENYS"
description: "Spinta table datasets/gov/vmi/prekiu_paslaugu_es_pvm/VtsFr0564Mainai (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/prekiu_paslaugu_es_pvm/VtsFr0564Mainai"
tags: [gov, vmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# VtsFr0564Mainai — FR0564_DUOMENYS

- **Model:** `datasets/gov/vmi/prekiu_paslaugu_es_pvm/VtsFr0564Mainai`[^manifest]
- **Dataset:** [Prekių tiekimo ir paslaugų teikimo kitų ES šalių PVM mokėtojams vertės](../prekiu_paslaugu_es_pvm.md) (`datasets/gov/vmi/prekiu_paslaugu_es_pvm`)
- **Manifest CSV:** [datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/prekiu_paslaugu_es_pvm/VtsFr0564Mainai`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `4` | `open` | — | Ataskaitinio laikotarpio metai | — |
| `ketvirtis` | `integer` | — | `4` | `open` | — | Ataskaitinio laikotarpio ketvirtis | — |
| `menuo` | `integer` | — | `4` | `open` | — | Ataskaitinio laikotarpio mėnuo | — |
| `evrk_sekcija` | `string` | — | `4` | `open` | — | Deklaracijoje nurodyta pagrindinė vykdomos veiklos rūšis pagal Ekonominės veiklos rūšių klasifikatorių, patvirtintą Statistikos departamento generalinio direktoriaus 2007 m. spalio 31 d. įsakymu Nr.DĮ-226 (Žin., 2007, Nr.119-4877, toliau - EVRK) | Užsiimančių ta pačia veikla mokesčių mokėtojų dominavimo atveju taip pat nėra nustatyta EVRK sekcija, EVRK skyrius ir apskritis |
| `evrk_skyrius` | `string` | — | `4` | `open` | — | Pagrindinė vykdomos veiklos rūšis pagal EVRK. Imama iš klasifikatoriaus, jei pavyko identifikuoti pagal deklaracijoje įrašytą kodą | Užsiimančių ta pačia veikla mokesčių mokėtojų dominavimo atveju taip pat nėra nustatyta EVRK sekcija, EVRK skyrius ir apskritis |
| `apskrities_kodas` | `string` | — | `4` | `open` | — | Deklaracijai priskirtos apskrities kodas | Užsiimančių ta pačia veikla mokesčių mokėtojų dominavimo atveju taip pat nėra nustatyta EVRK sekcija, EVRK skyrius ir apskritis |
| `apskritis` | `string` | — | `4` | `open` | — | Deklaracijai priskirtos apskrities pavadinimas | Užsiimančių ta pačia veikla mokesčių mokėtojų dominavimo atveju taip pat nėra nustatyta EVRK sekcija, EVRK skyrius ir apskritis |
| `mm_skaicius` | `integer` | — | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |
| `valstybes_kodas` | `string` | — | `4` | `open` | — | ES valstybės narės, kurioje PVM mokėtoju registruotas pirkėjas arba PVM mokėtoju registruotas disponuojamas prekes verslo tikslais pervežantis Lietuvos PVM mokėtojas | — |
| `prekiu_verte` | `number` | — | `4` | `open` | — | Patiektų prekių apmokestinamoji vertė | — |
| `trikampe_prekyba` | `number` | — | `4` | `open` | — | Trikampės prekybos prekių vertė | — |
| `paslaugu_verte` | `number` | — | `4` | `open` | — | Paslaugų vertė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `ketvirtis` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |
| `apskrities_kodas` | `create(property: "apskritis", type: "ref", ref: "/datasets/gov/rc/ar/apskritis/Apskritis")` | `type` | `4` | `open` | — | — | — |
| `apskrities_kodas` | `update(property: "apskritis.adm_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `apskritis` | `update(property: "apskritis.pavadinimas", type: "")` | `type` | `4` | — | — | — | — |
| `prekiu_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `trikampe_prekyba` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `paslaugu_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv
