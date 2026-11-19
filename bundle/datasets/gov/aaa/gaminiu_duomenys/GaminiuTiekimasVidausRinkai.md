---
type: Table
title: "GaminiuTiekimasVidausRinkai — Gaminių tiekimo vidaus rinkai apskaitos duomenys"
description: "Spinta table datasets/gov/aaa/gaminiu_duomenys/GaminiuTiekimasVidausRinkai (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/gaminiu_duomenys/GaminiuTiekimasVidausRinkai"
tags: [gov, aaa, gaminiutiekimasvidausrinkai, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/gaminiu_duomenys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/aaa/gaminiu_duomenys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1786/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/gaminiu_duomenys"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# GaminiuTiekimasVidausRinkai — Gaminių tiekimo vidaus rinkai apskaitos duomenys

- **Model:** `datasets/gov/aaa/gaminiu_duomenys/GaminiuTiekimasVidausRinkai`[^manifest]
- **Dataset:** [Gaminių tiekimo vidaus rinkai apskaitos duomenys](../gaminiu_duomenys.md) (`datasets/gov/aaa/gaminiu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/gaminiu_duomenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/gaminiu_duomenys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/gaminiu_duomenys/GaminiuTiekimasVidausRinkai` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės nr. | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Metai | — |
| `srautas` | `string` | — | `2` | `open` | — | Gaminių srautas | Pagal Gamintojų ir importuotojų registravimo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 2009-05-27 Nr. D1-291, priedą. Apibrėžta gaminių srautų klasifikacija naudojama ir Vieningos gaminių, pakuočių ir atliekų apskaitos informacinėje sistemoje (GPAIS). |
| `rusis` | `string` | — | `2` | `open` | — | Gaminio rūšis | Pagal Gamintojų ir importuotojų registravimo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 2009-05-27 Nr. D1-291, priedą. Apibrėžta gaminių rūšių klasifikacija naudojama ir Vieningos gaminių, pakuočių ir atliekų apskaitos informacinėje sistemoje (GPAIS). |
| `imoniu_sk` | `integer` | `U` | `4` | `open` | — | Įmonių, pateikusių ataskaitas, skaičius, vnt. | Skaičiuojamos įmonės, kurios GPAIS patvirtino ketvirčių suvestines, kurių metinės ataskaitos yra suformuotos ar vertinamos bei įmonės, pateikusios VMI deklaracijas FR0523 |
| `kiekis` | `integer` | `t` | `4` | `open` | — | Patiekta vidaus rinkai, t | Kiekis tonomis |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/gaminiu_duomenys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/gaminiu_duomenys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/gaminiu_duomenys (https://data.gov.lt/datasets/1786/)
