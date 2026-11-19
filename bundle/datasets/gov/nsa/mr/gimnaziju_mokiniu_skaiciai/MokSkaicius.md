---
type: Table
title: "MokSkaicius — Gimnazijų mokinių skaičiai pamečiui"
description: "Lentelėje pateikiami gimnazijų ir jų padalinių mokinių skaičiai pamečiui nuo 2018 metų iš Nacionalinės švietimo agentūros (NŠA) Mokinių registro (MR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai/MokSkaicius"
tags: [gov, nsa, mokskaicius, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4056/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MokSkaicius — Gimnazijų mokinių skaičiai pamečiui

Lentelėje pateikiami gimnazijų ir jų padalinių mokinių skaičiai pamečiui nuo 2018 metų iš Nacionalinės švietimo agentūros (NŠA) Mokinių registro (MR). Duomenys atnaujinami kas mėnesį.[^manifest]

- **Model:** `datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai/MokSkaicius`[^manifest]
- **Dataset:** [Gimnazijų ir jų padalinių mokinių skaičiai pamečiui](../gimnaziju_mokiniu_skaiciai.md) (`datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai`)[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai/MokSkaicius` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Duomenų eilutės identifikatorius (sugeneruotas Valstybės duomenų agentūros) | — |
| `mokslo_metai_pavadinimas` | `string` | — | `4` | `open` | — | Mokslo metai | — |
| `mokslo_metai_pradzios_data` | `date` | `D` | `4` | `open` | — | Mokslo metų pradžios data | — |
| `mokslo_metai_pabaigos_data` | `date` | `D` | `4` | `open` | — | Mokslo metų pabaigos data | — |
| `ins_pagr_tipas` | `string` | — | `4` | `open` | — | Pagrindinis institucijos tipas | — |
| `institucijos_kodas` | `string` | — | `4` | `open` | — | Institucijos juridinio asmens kodas | — |
| `institucijos_pavadinimas` | `string` | — | `4` | `open` | — | Institucijos pavadinimas | — |
| `padalinys_kodas` | `string` | — | `4` | `open` | — | Institucijos padalinio kodas | — |
| `padalinys_pavadinimas` | `string` | — | `4` | `open` | — | Institucijos padalinio pavadinimas | — |
| `jungtinis_kodas` | `string` | — | `4` | `open` | — | Institucijos juridinio asmens kodas arba padalinio kodas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Institucijos savivaldybė | — |
| `aob_kodas` | `string` | — | `4` | `open` | — | Institucijos adreso identifikacinis kodas | — |
| `e_koord` | `number` | — | `4` | `open` | — | Objekto rytų ilgumos koordinatė (WGS84) | — |
| `n_koord` | `number` | — | `4` | `open` | — | Objekto šiaurės platumos koordinatė (WGS84) | — |
| `koord_x` | `number` | — | `4` | `open` | — | X koordinatė LKS sistemoje | — |
| `koord_y` | `number` | — | `4` | `open` | — | Y koordinatė LKS sistemoje | — |
| `mokiniu_sk_viso` | `integer` | — | `4` | `open` | — | Visų institucijos mokinių skaičius | — |
| `m_mokiniu_sk` | `integer` | — | `4` | `open` | — | Mergaičių skaičius institucijoje | — |
| `v_mokiniu_sk` | `integer` | — | `4` | `open` | — | Berniukų skaičius institucijoje | — |
| `nuo_11_iki_12_klases_mokiniu_sk` | `integer` | — | `4` | `open` | — | Mokinių nuo 11 iki 12 klasės arba III-IV gimnazijos klasės skaičius | — |
| `nuo_9_iki_10_klases_mokiniu_sk` | `integer` | — | `4` | `open` | — | Mokinių nuo 9 iki 10 klasės arba I-II gimnazijos klasės skaičius | — |
| `nuo_5_iki_8_klases_mokiniu_sk` | `integer` | — | `4` | `open` | — | Mokinių nuo 5 iki 8 klasės skaičius | — |
| `nuo_1_iki_4_klases_mokiniu_sk` | `integer` | — | `4` | `open` | — | Mokinių nuo 1 iki 4 klasės skaičius | — |
| `profesinio_ugdymo_klases_mokiniu_sk` | `integer` | — | `4` | `open` | — | Mokinių darbinėse ir profesinio ugdymo klasėse skaičius | — |
| `pvaiku_ugdymo_grupes_mokiniu_sk` | `integer` | — | `4` | `open` | — | Mokinių pasirenkamojo vaikų ugdymo grupėse skaičius | — |
| `ikimokyklines_grupes_mokiniu_sk` | `integer` | — | `4` | `open` | — | Asmenų ikimokyklinėse grupėse skaičius | — |
| `priesmokyklines_grupes_mokiniu_sk` | `integer` | — | `4` | `open` | — | Asmenų priešmokyklinės grupėse skaičius | — |
| `paskutinis_atnaujinimas` | `date` | `D` | `4` | `open` | — | Paskutinis duomenų atnaujinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/mr/gimnaziju_mokiniu_skaiciai (https://data.gov.lt/datasets/4056/)
