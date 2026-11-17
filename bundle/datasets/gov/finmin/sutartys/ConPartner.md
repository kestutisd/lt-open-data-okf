---
type: Table
title: "ConPartner — Sutarties partneriai"
description: "Spinta table datasets/gov/finmin/sutartys/ConPartner (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConPartner"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L58"
    last_modified: "2026-11-11T14:39:20Z"
---

# ConPartner — Sutarties partneriai

- **Model:** `datasets/gov/finmin/sutartys/ConPartner`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L58](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L58)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConPartner`
- **Primary Key (`ref`):** `con_partner_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_partner_id` | `string` | — | `4` | `open` | — | Sutarties partnerio identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `partner` | `string` | — | `2` | `open` | — | Partnerio pavadinimas | Fiziniams asmenims vertės pašalintos |
| `code` | `string` | — | `2` | `open` | — | Partnerio JAR kodas | Užsienio pareiškėjams nurodyti analogiški kodai. Fiziniams asmenims vertės pašalintos |
| `city_district` | `string` | — | `2` | `open` | — | Partnerio miestas / rajonas | — |
| `legal_form` | `string` | — | `3` | `open` | — | Partnerio teisinė forma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv
