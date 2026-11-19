---
type: Table
title: "Skundas — VVTAT ištirtų skundų rezultatai"
description: "Rinkinyje pateikiami duomenys apie VVTAT ištirtus skundus: jų registracijos ir tyrimo pabaigos datas, skunduose minimas įmones ir tyrimo rezultatus."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/skundu_rezultatai/Skundas"
tags: [gov, vvtat, skundas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/skundu_rezultatai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vvtat/skundu_rezultatai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2684/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvtat/skundu_rezultatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Skundas — VVTAT ištirtų skundų rezultatai

Rinkinyje pateikiami duomenys apie VVTAT ištirtus skundus: jų registracijos ir tyrimo pabaigos datas, skunduose minimas įmones ir tyrimo rezultatus.[^manifest]

- **Model:** `datasets/gov/vvtat/skundu_rezultatai/Skundas`[^manifest]
- **Dataset:** [VVTAT ištirtų skundų rezultatai](../skundu_rezultatai.md) (`datasets/gov/vvtat/skundu_rezultatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvtat/skundu_rezultatai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/skundu_rezultatai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/skundu_rezultatai/Skundas` (`deployed`)[^manifest]
- **Provider:** `vvtat` — Valstybinė vartotojų teisių apsaugos tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `registracija` | `date` | `D` | `4` | `open` | — | Skundo registracijos VVTAT data | — |
| `issprendimas` | `date` | `D` | `4` | `open` | — | Skundo išsprendimo data | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įmonės juridinio asmens kodas | — |
| `imone` | `string` | — | `2` | `open` | — | Įmonės pavadinimas | — |
| `skundo_priezastis` | `string` | — | `4` | `open` | — | Skundo teikimo priežastis | — |
| `ar_pagristas` | `boolean` | — | `4` | `open` | — | Žyma, ar skundas yra pagrįstas | — |
| `nenustatymo_priezastis` | `string` | — | `4` | `open` | — | Priežastis, dėl kurios VVTAT nenustatė skundo | — |
| `nepagristumo_priezastis` | `string` | — | `4` | `open` | — | Priežastis, dėl kurios VVTAT skundo nelaiko pagrįstu | — |
| `rezultatas` | `string` | — | `4` | `open` | — | Ištirto skundo rezultatas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `skundo_priezastis` | `"update(property: ""skundo_priezastis[]"", type: ""array"", source: ""Skundo_priezastis"")"` | `property` | `4` | — | — | — | — |
| `nepagristumo_priezastis` | `"update(property: ""nepagristumo_priezastis[]"", type: ""array"", source: ""Nepagristumo_priezastis"")"` | `property` | `4` | — | — | — | — |
| `rezultatas` | `"update(property: ""rezultatas[]"", type: ""array"", source: ""Rezultatas"")"` | `property` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/skundu_rezultatai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/skundu_rezultatai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvtat/skundu_rezultatai (https://data.gov.lt/datasets/2684/)
