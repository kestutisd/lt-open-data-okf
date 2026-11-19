---
type: Table
title: "IvykiuSavivaldybes — BPC įvykių savivaldybės"
description: "Bendrojo pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, teritorinė statistika pagal savivaldybę."
resource: "https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/IvykiuSavivaldybes"
tags: [gov, bpc, ivykiusavivaldybes, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L31"
    title: "atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv#L31"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1763/"
    title: "data.gov.lt DCAT-AP — datasets/gov/bpc/pagalbos_skambuciai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IvykiuSavivaldybes — BPC įvykių savivaldybės

Bendrojo pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, teritorinė statistika pagal savivaldybę. Tai yra agreguota lentelė, kuri į vieną eilutę sujungia unikalią šių požymių kombinaciją: įvykio tipas, savivaldybė, metai, mėnuo. Lentelės tikslas yra geografinio pasiskirstymo palengvintam stebėjimui. Dėl konfidencialumo nepateikiama tiksli įvykio data. Praneštų įvykių skaičiai nebūtinai turi sutapti su Administracinių nusižengimų registro duomenimis (pranešimai gali būti melagingi arba nepasiekti administracinių nusižengimų bylos stadijos).[^manifest]

- **Model:** `datasets/gov/bpc/pagalbos_skambuciai/IvykiuSavivaldybes`[^manifest]
- **Dataset:** [Bendrojo pagalbos centro 112 skambučių duomenų rinkinys](../pagalbos_skambuciai.md) (`datasets/gov/bpc/pagalbos_skambuciai`)[^manifest]
- **Manifest CSV:** [datasets/gov/bpc/pagalbos_skambuciai.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L31)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/IvykiuSavivaldybes` (`deployed`)[^manifest]
- **Provider:** `bpc` — Bendrasis pagalbos centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ivykio_tipo_kodas` | `ref` | [IvykiuKlasifikatorius](IvykiuKlasifikatorius.md) (`level=4 UUID`: `ivykio_tipo_kodas._id`) | `4` | `open` | — | Įvykio tipo kodas | Šio požymio kodų prasmės yra pagalbinėje lentelėje BPC įvykių klasifikatorius |
| `savivaldybes_kodas` | `integer` | — | `2` | `open` | — | Savivaldybės, kurioje įvyko įvykiai, standartinis kodas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės, kurioje įvyko įvykiai, pavadinimas | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai, kuomet įvyko įvykiai | — |
| `menuo` | `integer` | — | `2` | `open` | — | mėnuo, kuomet įvyko įvykiai | — |
| `ivykiu_skaicius` | `integer` | — | `4` | `open` | — | įvykių, apie kuriuos gauti pranešimai, skaičius šioje agregacijos grupėje | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `menuo` | `1` | — | — | Sausis | — |
| `menuo` | `2` | — | — | Vasaris | — |
| `menuo` | `3` | — | — | Kovas | — |
| `menuo` | `4` | — | — | Balandis | — |
| `menuo` | `5` | — | — | Gegužė | — |
| `menuo` | `6` | — | — | Birželis | — |
| `menuo` | `7` | — | — | Liepa | — |
| `menuo` | `8` | — | — | Rugpjūtis | — |
| `menuo` | `9` | — | — | Rugsėjis | — |
| `menuo` | `10` | — | — | Spalis | — |
| `menuo` | `11` | — | — | Lapkritis | — |
| `menuo` | `12` | — | — | Gruodis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybes_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `savivaldybes_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv#L31 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L31)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/bpc/pagalbos_skambuciai (https://data.gov.lt/datasets/1763/)
