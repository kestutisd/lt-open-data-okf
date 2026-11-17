---
type: Table
title: "DantuIvertinimas — Dantų ir žandikaulių būklės įvertinimas"
description: "E027-1 formos antros dalies duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/mokiniu_sveikata/DantuIvertinimas"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/mokiniu_sveikata.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L52"
    last_modified: "2026-11-11T14:39:20Z"
---

# DantuIvertinimas — Dantų ir žandikaulių būklės įvertinimas

E027-1 formos antros dalies duomenys.

- **Model:** `datasets/gov/lsd/sveikata/mokiniu_sveikata/DantuIvertinimas`[^manifest]
- **Dataset:** [Kasmetinės vaikų sveikatos patikros duomenys](../mokiniu_sveikata.md) (`datasets/gov/lsd/sveikata/mokiniu_sveikata`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L52](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L52)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/mokiniu_sveikata/DantuIvertinimas`
- **Primary Key (`ref`):** `tikrinimo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tikrinimo_id` | `string` | — | `4` | `open` | — | Dantų tikrinimo vizito identifikatorius | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Mokinio asmens identifikatorius | — |
| `gimimo_metai` | `date` | `D` | `4` | `open` | — | Mokinio gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Mokinio lytis | — |
| `mokinio_savivaldybe` | `string` | — | `4` | `open` | — | Mokinio gyvenamoji savivaldybė pagal deklaraciją iš gyventojų registro | — |
| `mokinio_gyvenviete` | `string` | — | `4` | `open` | — | Gyvenvietė pagal deklaraciją iš gyventojų registro | Esant mažiau nei 10 mokinių, deklaravusių gyvenamąją vietą toje pačioje gyvenvietėje, gimusių tais pačiais metais, ir tais metais atlikusių sveikatos tikrinimą, gyvenvietė nurodoma "kita" |
| `gyvenvietes_tipas` | `string` | — | `4` | `open` | — | Gyvenvietės tipas | — |
| `iraso_laikas` | `datetime` | `S` | `4` | `open` | — | Įrašo įvedimo laiko žyma, suapvalinta iki artimiausios valandos | — |
| `duomenu_atnaujinimas` | `datetime` | `S` | `4` | `open` | — | Įrašo duomenų atnaujinimo laiko žyma, suapvalinta iki artimiausios valandos | — |
| `netaisyklingas_sakandis` | `string` | — | `4` | `open` | — | Netaisyklingo sąkandžio požymis | — |
| `pieniniai_isgede` | `integer` | — | `4` | `open` | — | Pieninių išgedusių dantų skaičius | — |
| `pieniniai_uzplombuoti` | `integer` | — | `4` | `open` | — | Pieninių užplombuotų dantų skaičius | — |
| `pieniniai_prarasti` | `integer` | — | `4` | `open` | — | Pieninių prarastų dantų skaičius | — |
| `nuolatiniai_isgede` | `integer` | — | `4` | `open` | — | Nuolatinių išgedusių dantų skaičius | — |
| `nuolatiniai_uzplombuoti` | `integer` | — | `4` | `open` | — | Nuolatininių užplombuotų dantų skaičius | — |
| `nuolatiniai_prarasti` | `integer` | — | `4` | `open` | — | Nuolatininių prarastų dantų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `gyvenvietes_tipas` | `"miestas"` | — | — | — | — |
| `gyvenvietes_tipas` | `"kaimas"` | — | — | — | — |
| `gyvenvietes_tipas` | `"miestelis"` | — | — | — | — |
| `gyvenvietes_tipas` | `"viensėdis"` | — | — | — | — |
| `gyvenvietes_tipas` | `"geležinkelio stotis"` | — | — | — | — |
| `netaisyklingas_sakandis` | `"Nėra"` | — | — | — | — |
| `netaisyklingas_sakandis` | `"Pavienių dantų"` | — | — | — | — |
| `netaisyklingas_sakandis` | `"Žandikaulių"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/mokiniu_sveikata.csv
