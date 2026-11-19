---
type: Table
title: "TelyciosKarvesAmzius — Mėsinių ir mišrūnų veislių telyčių ir karvių pasiskirstymas pagal amžiaus grupes"
description: "Spinta table datasets/gov/zuikvc/telyciu_karviu_amzius/TelyciosKarvesAmzius (12 columns)."
tags: [gov, zuikvc, telycioskarvesamzius, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/telyciu_karviu_amzius.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/telyciu_karviu_amzius.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# TelyciosKarvesAmzius — Mėsinių ir mišrūnų veislių telyčių ir karvių pasiskirstymas pagal amžiaus grupes

- **Model:** `datasets/gov/zuikvc/telyciu_karviu_amzius/TelyciosKarvesAmzius`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/telyciu_karviu_amzius](../telyciu_karviu_amzius.md) (`datasets/gov/zuikvc/telyciu_karviu_amzius`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/telyciu_karviu_amzius.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/telyciu_karviu_amzius.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `savivaldybe`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `laik` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko mėsinių arba mišrūnų veislių telyčias arba karves | — |
| `tel_0_8_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių telyčių iki 8 mėnesių amžiaus skaičius | — |
| `tel_0_8_mis` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių telyčių iki 8 mėnesių amžiaus skaičius | — |
| `tel_8_12_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių telyčių nuo 8 iki 12 mėnesių amžiaus skaičius | — |
| `tel_8_12_mis` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių telyčių nuo 8 iki 12 mėnesių amžiaus skaičius | — |
| `tel_12_24_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių telyčių nuo 12 iki 24 mėnesių amžiaus skaičius | — |
| `tel_12_24_mis` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių telyčių nuo 12 iki 24 mėnesių amžiaus skaičius | — |
| `tel_24_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių telyčių nuo 24 mėnesių amžiaus skaičius | — |
| `tel_24_mis` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių telyčių nuo 24 mėnesių amžiaus skaičius | — |
| `karv_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių karvių skaičius | — |
| `karv_mis` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių karvių skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/telyciu_karviu_amzius.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/telyciu_karviu_amzius.csv#L8)
