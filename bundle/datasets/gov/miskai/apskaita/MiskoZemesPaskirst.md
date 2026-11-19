---
type: Table
title: "MiskoZemesPaskirst — Miško žemės pasiskirstymas pagal žemės naudmenas (ha)"
description: "Spinta table datasets/gov/miskai/apskaita/MiskoZemesPaskirst (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/apskaita/MiskoZemesPaskirst"
tags: [gov, miskai, miskozemespaskirst, deployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/miskai/apskaita.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# MiskoZemesPaskirst — Miško žemės pasiskirstymas pagal žemės naudmenas (ha)

- **Model:** `datasets/gov/miskai/apskaita/MiskoZemesPaskirst`[^manifest]
- **Dataset:** [datasets/gov/miskai/apskaita](../apskaita.md) (`datasets/gov/miskai/apskaita`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/apskaita.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/apskaita/MiskoZemesPaskirst` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `misku_gr_kateg`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `misku_gr_kateg` | `string` | — | `3` | `open` | — | Miškų grupės ir kategorijos | — |
| `bendras_misko_zem_plotas` | `number` | `ha` | `4` | `open` | — | Bendras miško žemės plotas | — |
| `viso_apaugusi_misku` | `number` | `ha` | `4` | `open` | — | Apaugusi mišku. Iš viso | — |
| `zeldiniai` | `number` | `ha` | `4` | `open` | — | Apaugusi mišku. Iš jos želdiniai | — |
| `viso_neapaugusi_misku` | `number` | `ha` | `4` | `open` | — | Neapaugusi mišku. Iš viso | — |
| `kirtavietes` | `number` | `ha` | `4` | `open` | — | Neapaugusi mišku. Iš jos - kirtavietės | — |
| `zeme_miskui_iveisti` | `number` | `ha` | `4` | `open` | — | Neapaugusi mišku. Iš jos - žemė miškui įveisti | — |
| `dauginamosios_medziagos_zeme` | `number` | `ha` | `4` | `open` | — | Miško dauginamosios medžiagos išauginimo žemė | — |
| `tech_pask_misko_zeme` | `number` | `ha` | `4` | `open` | — | Technologinės paskirties miško žemė | — |
| `kitos_pask_misko_zeme` | `number` | `ha` | `4` | `open` | — | Kitos paskirties miško žemė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/apskaita.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L27)
