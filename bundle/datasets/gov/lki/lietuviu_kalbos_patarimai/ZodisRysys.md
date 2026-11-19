---
type: Table
title: "ZodisRysys — Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinis bankas. Esminių žodžių ryšiai su kitais žodžiais."
description: "Lentelėje pateikti Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinio banko (https://kkb.lki.lt/) esminių žodžių ryšiai su kitais žodžiais."
resource: "https://get.data.gov.lt/datasets/gov/lki/lietuviu_kalbos_patarimai/ZodisRysys"
tags: [gov, lki, zodisrysys, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L16"
    title: "atviriduomenys/manifest — datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L16"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2765/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lki/lietuviu_kalbos_patarimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ZodisRysys — Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinis bankas. Esminių žodžių ryšiai su kitais žodžiais.

Lentelėje pateikti Lietuvių kalbos instituto Kalbos konsultacijų kompiuterinio banko (https://kkb.lki.lt/) esminių žodžių ryšiai su kitais žodžiais. Duomenys rinkti nuo 1997 iki 2005 metų. Šiuo metu bankas nebepildomas ir 2005 metų perduotas VLKK.[^manifest]

- **Model:** `datasets/gov/lki/lietuviu_kalbos_patarimai/ZodisRysys`[^manifest]
- **Dataset:** [Lietuvių kalbos vartosenos patarimai](../lietuviu_kalbos_patarimai.md) (`datasets/gov/lki/lietuviu_kalbos_patarimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L16)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/lietuviu_kalbos_patarimai/ZodisRysys` (`deployed`)[^manifest]
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
| `klausimo_esminis_zodis` | `string` | — | `4` | `open` | — | Klausimo esminis žodis | — |
| `rysys` | `string` | — | `4` | `open` | — | Esminio klausimo žodžio ryšys su kitu (-ais) žodžiu (-iais) | — |
| `susije_zodziai` | `string` | — | `4` | `open` | — | Su raktiniu klausimo žodžiu susijęs (-ę) žodis (-iai) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L16 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/lietuviu_kalbos_patarimai.csv#L16)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lki/lietuviu_kalbos_patarimai (https://data.gov.lt/datasets/2765/)
