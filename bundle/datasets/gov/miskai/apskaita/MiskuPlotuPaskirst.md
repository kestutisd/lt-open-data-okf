---
type: Table
title: "MiskuPlotuPaskirst — Visų miškų plotų pasiskirstymas pagal žemės naudmenas (ha)"
description: "Spinta table datasets/gov/miskai/apskaita/MiskuPlotuPaskirst (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/apskaita/MiskuPlotuPaskirst"
tags: [gov, miskai, miskuplotupaskirst, deployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L39"
    title: "atviriduomenys/manifest — datasets/gov/miskai/apskaita.csv#L39"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# MiskuPlotuPaskirst — Visų miškų plotų pasiskirstymas pagal žemės naudmenas (ha)

- **Model:** `datasets/gov/miskai/apskaita/MiskuPlotuPaskirst`[^manifest]
- **Dataset:** [datasets/gov/miskai/apskaita](../apskaita.md) (`datasets/gov/miskai/apskaita`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/apskaita.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L39)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/apskaita/MiskuPlotuPaskirst` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `zemes_naudmenu_grupe` | `string` | — | `3` | `open` | — | Žemės naudmenų grupė | — |
| `zemes_naudmena` | `string` | — | `3` | `open` | — | Žemės naudmena | — |
| `plotas` | `number` | `ha` | `4` | `open` | — | Plotas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/apskaita.csv#L39 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L39)
