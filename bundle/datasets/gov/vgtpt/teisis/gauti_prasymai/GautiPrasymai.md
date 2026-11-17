---
type: Table
title: "GautiPrasymai — Gautų prašymų suteikti antrinę teisinę pagalbą duomenys"
description: "Spinta table datasets/gov/vgtpt/teisis/gauti_prasymai/GautiPrasymai (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/gauti_prasymai/GautiPrasymai"
tags: [gov, vgtpt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/gauti_prasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/gauti_prasymai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# GautiPrasymai — Gautų prašymų suteikti antrinę teisinę pagalbą duomenys

- **Model:** `datasets/gov/vgtpt/teisis/gauti_prasymai/GautiPrasymai`[^manifest]
- **Dataset:** [Gautų prašymų suteikti antrinę teisinę pagalbą duomenys](../gauti_prasymai.md) (`datasets/gov/vgtpt/teisis/gauti_prasymai`)
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/gauti_prasymai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/gauti_prasymai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/gauti_prasymai/GautiPrasymai`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `gauta_metai` | `integer` | — | `2` | `open` | — | Metai, kada gautas prašymas suteikti antrinę teisinę pagalbą | — |
| `gauta_ketvirtis` | `integer` | — | `2` | `open` | — | Ketvirtis, kada gautas prašymas suteikti antrinę teisinę pagalbą | — |
| `priimta_metai` | `integer` | — | `2` | `open` | — | Metai, kada priimtas sprendimas suteikti antrinę teisinę pagalbą | — |
| `priimta_ketvirtis` | `integer` | — | `2` | `open` | — | Ketvirtis, kada priimtas sprendimas suteikti antrinę teisinę pagalbą | — |
| `teritorijos_kodas` | `ref` | [/datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija](../klasifikatoriai/Teritorija.md) | `4` | `open` | — | Pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | Iš TEISIS teritorijos klasifikatoriaus |
| `bylos_rusies_kodas` | `ref` | [/datasets/gov/vgtpt/teisis/klasifikatoriai/BylosRusis](../klasifikatoriai/BylosRusis.md) | `4` | `open` | — | Bylos, kurioje reikalinga antrinė teisinė pagalba | Rūšies kodas iš TEISIS bylų rūšių klasifikatoriaus |
| `kompensuojama` | `string` | — | `4` | `open` | — | Valstybės kompensuojamos teisinės pagalbos procentinė išraiška | — |
| `sprendimu_skaicius` | `integer` | `U` | `4` | `open` | — | Priimtų sprendimų suteikti antrinę teisinę pagalbą skaičius | — |
| `nesuteikta_pagalba` | `integer` | `U` | `4` | `open` | — | Sprendimų atsisakyti suteikti antrinę teisinę pagalbą skaičius | — |
| `neisnagrineti_prasymai` | `integer` | `U` | `4` | `open` | — | Prašymų suteikti antrinę teisinę pagalbą, kurie palikti nenagrinėti arba laukiama atsakymo, skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kompensuojama` | `"100"` | — | — | Kompensuojama 100 proc. teisinės pagalbos išlaidų | — |
| `kompensuojama` | `"50"` | — | — | Kompensuojama 50 proc. teisinės pagalbos išlaidų | — |
| `kompensuojama` | `"30"` | — | — | Kompensuojama 30 proc. teisinės pagalbos išlaidų | — |
| `kompensuojama` | `"15"` | — | — | Kompensuojama 15 proc. teisinės pagalbos išlaidų | — |
| `kompensuojama` | `"NOT_RELEVANT"` | — | — | Kompensavimo už teisinę pagalbą klausimą nagrinėjant turimo turto kiekis neaktualus | — |
| `kompensuojama` | `"NOT_IDENTIFIED"` | — | — | Kompensavimo už teisinę pagalbą klausimas neišspręstas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gauta_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |
| `priimta_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/gauti_prasymai.csv
