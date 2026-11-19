---
type: Table
title: "VeiklosVieta — Socialinės globos licencijų paslaugų teikimo vietos"
description: "Spinta table datasets/gov/sppd/vietos/VeiklosVieta (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sppd/vietos/VeiklosVieta"
tags: [gov, sppd, veiklosvieta, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/soc_globos_licencijos.csv#L28"
    title: "atviriduomenys/manifest — datasets/gov/sppd/soc_globos_licencijos.csv#L28"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2869/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sppd/vietos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VeiklosVieta — Socialinės globos licencijų paslaugų teikimo vietos

- **Model:** `datasets/gov/sppd/vietos/VeiklosVieta`[^manifest]
- **Dataset:** [Socialinės globos licencijų paslaugų teikimo vietos](../vietos.md) (`datasets/gov/sppd/vietos`)[^manifest]
- **Manifest CSV:** [datasets/gov/sppd/soc_globos_licencijos.csv#L28](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/soc_globos_licencijos.csv#L28)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sppd/vietos/VeiklosVieta` (`deployed`)[^manifest]
- **Provider:** `sppd` — Socialinių paslaugų priežiūros departamentas prie SADM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `vietos_id` | `string` | — | `4` | `open` | — | Vietos unikalus identifikatorius | — |
| `licencijos_id` | `string` | — | `4` | `open` | — | Licencijos unikalus identifikatorius | — |
| `vietos_statusas` | `string` | — | `4` | `open` | — | Vietos statusas | — |
| `vietos_statusas_nuo` | `date` | `D` | `4` | `open` | — | Vietos būsenos data nuo | — |
| `vietos_statusas_iki` | `date` | `D` | `4` | `open` | — | Vietos būsenos data iki | — |
| `vietos_statuso_busena` | `string` | — | `4` | `open` | — | Vietos statuso būsena | — |
| `paskirtys` | `string` | — | `4` | `open` | — | Vietos paslaugų teikimo paskirtys | — |
| `adresas` | `string` | — | `4` | `open` | — | "Vietos adresas: jei veikla vykdoma asmenų namuose - adreso nebus, arba nenurodyta, kad asmens namuose. Jei Šeimyna - adresas ir koordinatės nerodomos" | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS sistemoje | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sppd/soc_globos_licencijos.csv#L28 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/soc_globos_licencijos.csv#L28)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sppd/vietos (https://data.gov.lt/datasets/2869/)
