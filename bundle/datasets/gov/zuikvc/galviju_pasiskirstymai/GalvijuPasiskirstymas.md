---
type: Table
title: "GalvijuPasiskirstymas — Galvijų pasiskirstymas pagal savivaldybes"
description: "Spinta table datasets/gov/zuikvc/galviju_pasiskirstymai/GalvijuPasiskirstymas (7 columns)."
tags: [gov, zuikvc, galvijupasiskirstymas, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_pasiskirstymai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/galviju_pasiskirstymai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# GalvijuPasiskirstymas — Galvijų pasiskirstymas pagal savivaldybes

- **Model:** `datasets/gov/zuikvc/galviju_pasiskirstymai/GalvijuPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/galviju_pasiskirstymai](../galviju_pasiskirstymai.md) (`datasets/gov/zuikvc/galviju_pasiskirstymai`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/galviju_pasiskirstymai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_pasiskirstymai.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `savivaldybe`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `asmenys_laikantys_galvijus` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko galvijus savivaldybėje, skaičius | — |
| `galviju_sk` | `integer` | `U` | `4` | `open` | — | Galvijų skaičius | — |
| `asmenys_laikantys_pienines_karves` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko pieninių veislių karves savivaldybėje, skaičius | — |
| `pieniniu_karviu_sk` | `integer` | `U` | `4` | `open` | — | Pieninių veislių karvių skaičius | — |
| `asmenys_laikantys_mesinius_galvijus` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko mėsinius arba mišrūnus galvijus savivaldybėje, skaičius | — |
| `mesiniu_galviju_sk` | `integer` | `U` | `4` | `open` | — | Mėsinių ir mišrūnų galvijų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/galviju_pasiskirstymai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_pasiskirstymai.csv#L8)
