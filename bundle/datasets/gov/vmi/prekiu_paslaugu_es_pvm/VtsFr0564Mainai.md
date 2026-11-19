---
type: Table
title: "VtsFr0564Mainai — FR0564_DUOMENYS"
description: "Spinta table datasets/gov/vmi/prekiu_paslaugu_es_pvm/VtsFr0564Mainai (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/prekiu_paslaugu_es_pvm/VtsFr0564Mainai"
tags: [gov, vmi, vtsfr0564mainai, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1175/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/prekiu_paslaugu_es_pvm"
    author: "team:vda"
    last_modified: "2026-03-09T00:00:00Z"
---

# VtsFr0564Mainai — FR0564_DUOMENYS

- **Model:** `datasets/gov/vmi/prekiu_paslaugu_es_pvm/VtsFr0564Mainai`[^manifest]
- **Dataset:** [Prekių tiekimo ir paslaugų teikimo kitų ES šalių PVM mokėtojams vertės](../prekiu_paslaugu_es_pvm.md) (`datasets/gov/vmi/prekiu_paslaugu_es_pvm`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/prekiu_paslaugu_es_pvm/VtsFr0564Mainai` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-03-09`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/prekiu_paslaugu_es_pvm.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/prekiu_paslaugu_es_pvm (https://data.gov.lt/datasets/1175/)
