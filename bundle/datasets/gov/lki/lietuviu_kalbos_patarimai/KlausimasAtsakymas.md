---
type: Table
title: "KlausimasAtsakymas — Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinis bankas. Klausimai ir atsakymai."
description: "Lentelėje pateikti klausimai ir atsakymai iš Lietuvių kalbos instituto kurto Kalbos konsultacijų kompiuterinio banko (https://kkb.lki.lt/)."
resource: "https://get.data.gov.lt/datasets/gov/lki/lietuviu_kalbos_patarimai/KlausimasAtsakymas"
tags: [gov, lki, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lki/lietuviu_kalbos_patarimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# KlausimasAtsakymas — Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinis bankas. Klausimai ir atsakymai.

Lentelėje pateikti klausimai ir atsakymai iš Lietuvių kalbos instituto kurto Kalbos konsultacijų kompiuterinio banko (https://kkb.lki.lt/). Duomenys rinkti nuo 1997 iki 2005 metų. Šiuo metu bankas nebepildomas ir nuo 2005 metų perduotas VLKK.

- **Model:** `datasets/gov/lki/lietuviu_kalbos_patarimai/KlausimasAtsakymas`[^manifest]
- **Dataset:** [Lietuvių kalbos vartosenos patarimai](../lietuviu_kalbos_patarimai.md) (`datasets/gov/lki/lietuviu_kalbos_patarimai`)
- **Manifest CSV:** [datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/lietuviu_kalbos_patarimai/KlausimasAtsakymas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `klausimo_id` | `string` | — | `4` | `open` | — | Klausimo identifikacinis numeris | — |
| `klausimas` | `string` | — | `4` | `open` | — | Klausimas | — |
| `atsakymas` | `string` | — | `4` | `open` | — | Atsakymas | — |
| `klausimo_esminis_zodis` | `string` | — | `4` | `open` | — | Klausimo esminis žodis | — |
| `rysys` | `string` | — | `4` | `open` | — | Esminio klausimo žodžio ryšys su taikoma taisykle | — |
| `taisykle` | `string` | — | `4` | `open` | — | Taikoma taisyklė | — |
| `paaiskinimas` | `string` | — | `4` | `open` | — | Paaiškinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/lietuviu_kalbos_patarimai.csv
