---
type: Table
title: "Produktas — VVTAT tikrintų produktų duomenys"
description: "Pateikiami Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) ne maisto produktų tikrinimų metu tikrinti produktai."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/planiniai_patikrinimai/Produktas"
tags: [gov, vvtat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvtat/planiniai_patikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L27"
    last_modified: "2026-11-11T14:39:20Z"
---

# Produktas — VVTAT tikrintų produktų duomenys

Pateikiami Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) ne maisto produktų tikrinimų metu tikrinti produktai. Informacija pateikiama nuo 2004m. iki šių dienų ir nurodo tikrintą produktą, jo kilmės šalį ir vertintojo išvadą.

- **Model:** `datasets/gov/vvtat/planiniai_patikrinimai/Produktas`[^manifest]
- **Dataset:** [Nemaisto produktų planinių tikrinimų duomenys](../planiniai_patikrinimai.md) (`datasets/gov/vvtat/planiniai_patikrinimai`)
- **Manifest CSV:** [datasets/gov/vvtat/planiniai_patikrinimai.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L27)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/planiniai_patikrinimai/Produktas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `patikrinimo_id` | `ref` | [/datasets/gov/vvtat/planiniai_patikrinimai/Patikrinimas[patikrinimo_id]](Patikrinimas.md) | `4` | `open` | — | Patikrinimo identifikacinis numeris | — |
| `produktas_lt` | `string` | — | `1` | `open` | — | Tikrinamas produktas | — |
| `kilmes_salis` | `string` | — | `4` | `open` | — | Tikrinamo produkto kilmės šalis | — |
| `isvada` | `string` | — | `4` | `open` | — | Patikrinimo išvada | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `produktas_lt` | `update(property: "produktas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `isvada` | `"update(property: ""isvada[]"", type: ""array"", source: ""Isvada"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/planiniai_patikrinimai.csv
