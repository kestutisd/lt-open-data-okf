---
type: Table
title: "Produktas — VVTAT tikrintų produktų duomenys"
description: "Pateikiami Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) ne maisto produktų tikrinimų metu tikrinti produktai."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/planiniai_patikrinimai/Produktas"
tags: [gov, vvtat, produktas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/vvtat/planiniai_patikrinimai.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2683/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvtat/planiniai_patikrinimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Produktas — VVTAT tikrintų produktų duomenys

Pateikiami Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) ne maisto produktų tikrinimų metu tikrinti produktai. Informacija pateikiama nuo 2004m. iki šių dienų ir nurodo tikrintą produktą, jo kilmės šalį ir vertintojo išvadą.[^manifest]

- **Model:** `datasets/gov/vvtat/planiniai_patikrinimai/Produktas`[^manifest]
- **Dataset:** [Nemaisto produktų planinių tikrinimų duomenys](../planiniai_patikrinimai.md) (`datasets/gov/vvtat/planiniai_patikrinimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvtat/planiniai_patikrinimai.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/planiniai_patikrinimai/Produktas` (`deployed`)[^manifest]
- **Provider:** `vvtat` — Valstybinė vartotojų teisių apsaugos tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `patikrinimo_id` | `ref` | [Patikrinimas](Patikrinimas.md) (`level=4 UUID` via `Patikrinimas[patikrinimo_id]`: `patikrinimo_id._id`) | `4` | `open` | — | Patikrinimo identifikacinis numeris | — |
| `produktas_lt` | `string` | — | `1` | `open` | — | Tikrinamas produktas | — |
| `kilmes_salis` | `string` | — | `4` | `open` | — | Tikrinamo produkto kilmės šalis | — |
| `isvada` | `string` | — | `4` | `open` | — | Patikrinimo išvada | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `produktas_lt` | `update(property: "produktas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `isvada` | `"update(property: ""isvada[]"", type: ""array"", source: ""Isvada"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/planiniai_patikrinimai.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L27)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvtat/planiniai_patikrinimai (https://data.gov.lt/datasets/2683/)
