---
type: Table
title: "Vertinimas — Objektų vertinimai"
description: "\"Objektų pritaikomumo negaliai įverčiai iš Asmens su negalia teisių apsaugos agentūros, statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio."
resource: "https://get.data.gov.lt/datasets/gov/anta/stasis/Vertinimas"
tags: [gov, anta, vertinimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L23"
    title: "atviriduomenys/manifest — datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L23"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3870/"
    title: "data.gov.lt DCAT-AP — datasets/gov/anta/stasis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vertinimas — Objektų vertinimai

"Objektų pritaikomumo negaliai įverčiai iš Asmens su negalia teisių apsaugos agentūros, statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio. Viena eilutė yra vieno unikalaus objekto įvertis atitinkamam negalios tipui pagal tam tikrą kriterijų. Eilutėje nurodomi unikalios eilutės ir objekto identifikaciniai numeriai, negalios tipas, vertinimo kriterijus ir rezultatas."[^manifest]

- **Model:** `datasets/gov/anta/stasis/Vertinimas`[^manifest]
- **Dataset:** [Objektų pritaikomumo negalią turintiems asmenims vertinimai](../stasis.md) (`datasets/gov/anta/stasis`)[^manifest]
- **Manifest CSV:** [datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L23)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/anta/stasis/Vertinimas` (`deployed`)[^manifest]
- **Provider:** `anta` — Asmens su negalia teisių apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA unikalus ID | "Unikalios eilutės identifikatorius sudarytas iš stulpelių - objekto_id, negalios_tipas, kriterijus" |
| `objekto_id` | `string` | — | `4` | `open` | — | Objekto ID | Objekto identifikacinis numeris |
| `negalios_tipas` | `string` | — | `4` | `open` | — | Negalio tipas | Vertinamos negalios tipas |
| `kriterijus` | `string` | — | `4` | `open` | — | Kriterijus | Kriterijaus tipas |
| `rezultatas` | `integer` | — | `4` | `open` | — | Rezultatas | "Įvertis nuo 0 iki 100. 0 - visai nepritaikyta, 100 - pritaikyta" |

[^manifest]: atviriduomenys/manifest — datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L23 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L23)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/anta/stasis (https://data.gov.lt/datasets/3870/)
