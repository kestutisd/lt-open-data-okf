---
type: Table
title: "GynejoParinkimas — Gynėjo parinkimų duomenys baudžiamosiose bylose, kai gynėjo dalyvavimas pripažintas būtinu"
description: "Spinta table datasets/gov/vgtpt/teisis/gynejo_parinkimai/GynejoParinkimas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/gynejo_parinkimai/GynejoParinkimas"
tags: [gov, vgtpt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# GynejoParinkimas — Gynėjo parinkimų duomenys baudžiamosiose bylose, kai gynėjo dalyvavimas pripažintas būtinu

- **Model:** `datasets/gov/vgtpt/teisis/gynejo_parinkimai/GynejoParinkimas`[^manifest]
- **Dataset:** [Gynėjo parinkimų duomenys baudžiamosiose bylose, kai gynėjo dalyvavimas pripažintas būtinu](../gynejo_parinkimai.md) (`datasets/gov/vgtpt/teisis/gynejo_parinkimai`)
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/gynejo_parinkimai/GynejoParinkimas`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `parinkimo_metai` | `integer` | — | `2` | `open` | — | Metai, kada nustatytas gynėjo parinkimo pagrindas | — |
| `parinkimo_ketvirtis` | `integer` | — | `2` | `open` | — | Ketvirtis, kada nustatytas gynėjo parinkimo pagrindas | — |
| `teritorijos_kodas` | `ref` | [/datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija](../klasifikatoriai/Teritorija.md) | `4` | `open` | — | Antrinę teisinę pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | Iš TEISIS teritorijos klasifikatoriaus |
| `parinkimo_pagrindo_kodas` | `ref` | [/datasets/gov/vgtpt/teisis/klasifikatoriai/ParinkimoPagrindas](../klasifikatoriai/ParinkimoPagrindas.md) | `4` | `open` | — | Gynėjo parinkimų duomenys baudžiamosiose bylose | Kai gynėjo dalyvavimas pripažintas būtinu, teisinis pagrindas —Baudžiamojo proceso kodekso straipsnio kodas iš TEISIS pagalbos teikimo pagrindų klasifikatoriaus |
| `parinkimu_skaicius` | `integer` | `U` | `4` | `open` | — | Gynėjo parinkimų pagal gautus prašymus skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `parinkimo_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv
