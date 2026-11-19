---
type: Table
title: "KelioAtkarpa — Valstybinių kelių atkarpos"
description: "\"Duomenys apie valstybinių kelių atkarpas."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/KelioAtkarpa"
tags: [gov, via_lietuva, kelioatkarpa, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L78"
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv#L78"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1250/"
    title: "data.gov.lt DCAT-AP — datasets/gov/via_lietuva/eismo_ribojimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KelioAtkarpa — Valstybinių kelių atkarpos

"Duomenys apie valstybinių kelių atkarpas. Viena lentelės eilutė atitinka vieną kelio atkarpos identifikatorių su jo ilgio parametrais. Lentelę sudaro: unikalus kelio identifikacinis numeris, kelio numeris ir pavadinimas, kelio atkarpos pradžios ir pabaigos kilometras. Du paskutiniai techniniai stulpeliai nurodo įrašo sukūrimo ir atnaujinimo datas duomenų bazėje."[^manifest]

- **Model:** `datasets/gov/via_lietuva/eismo_ribojimai/KelioAtkarpa`[^manifest]
- **Dataset:** ["Eismo ribojimai valstybinės reikšmės keliuose"](../eismo_ribojimai.md) (`datasets/gov/via_lietuva/eismo_ribojimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/via_lietuva/eismo_ribojimai.csv#L78](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L78)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/KelioAtkarpa` (`deployed`)[^manifest]
- **Provider:** `via_lietuva` — AB „Via Lietuva“ (buv. LAKD) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kelio_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kelio_id` | `string` | — | `4` | `open` | — | Kelio atkarpos identifikacinis numeris | — |
| `numeris` | `string` | — | `4` | `open` | — | Kelio atkarpos numeris | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Kelio atkarpos pavadinimas | — |
| `km_nuo` | `number` | — | `4` | `open` | — | Kelio atkarpos pradžios kilometras | — |
| `km_iki` | `number` | — | `4` | `open` | — | Kelio atkarpos pabaigos kilometras | — |
| `irasas_sukurtas` | `datetime` | `U` | `4` | `open` | — | Įrašo sukūrimo duomenų bazėje data ir laikas | — |
| `irasas_atnaujintas` | `datetime` | `U` | `4` | `open` | — | Įrašo atnaujinimo duomenų bazėje data ir laikas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv#L78 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L78)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/via_lietuva/eismo_ribojimai (https://data.gov.lt/datasets/1250/)
