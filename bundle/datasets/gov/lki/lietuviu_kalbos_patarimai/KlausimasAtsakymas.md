---
type: Table
title: "KlausimasAtsakymas — Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinis bankas. Klausimai ir atsakymai."
description: "Lentelėje pateikti klausimai ir atsakymai iš Lietuvių kalbos instituto kurto Kalbos konsultacijų kompiuterinio banko (https://kkb.lki.lt/)."
resource: "https://get.data.gov.lt/datasets/gov/lki/lietuviu_kalbos_patarimai/KlausimasAtsakymas"
tags: [gov, lki, klausimasatsakymas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2765/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lki/lietuviu_kalbos_patarimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KlausimasAtsakymas — Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinis bankas. Klausimai ir atsakymai.

Lentelėje pateikti klausimai ir atsakymai iš Lietuvių kalbos instituto kurto Kalbos konsultacijų kompiuterinio banko (https://kkb.lki.lt/). Duomenys rinkti nuo 1997 iki 2005 metų. Šiuo metu bankas nebepildomas ir nuo 2005 metų perduotas VLKK.[^manifest]

- **Model:** `datasets/gov/lki/lietuviu_kalbos_patarimai/KlausimasAtsakymas`[^manifest]
- **Dataset:** [Lietuvių kalbos vartosenos patarimai](../lietuviu_kalbos_patarimai.md) (`datasets/gov/lki/lietuviu_kalbos_patarimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/lietuviu_kalbos_patarimai/KlausimasAtsakymas` (`deployed`)[^manifest]
- **Provider:** `lki` — Lietuvių kalbos institutas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lki/lietuviu_kalbos_patarimai (https://data.gov.lt/datasets/2765/)
