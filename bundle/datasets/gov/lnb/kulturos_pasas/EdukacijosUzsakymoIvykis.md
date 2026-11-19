---
type: Table
title: "EdukacijosUzsakymoIvykis"
description: "Spinta table datasets/gov/lnb/kulturos_pasas/EdukacijosUzsakymoIvykis (22 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas/EdukacijosUzsakymoIvykis"
tags: [gov, lnb, edukacijosuzsakymoivykis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L43"
    title: "atviriduomenys/manifest — datasets/gov/lnb/kulturos_pasas.csv#L43"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2659/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/kulturos_pasas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# EdukacijosUzsakymoIvykis

- **Model:** `datasets/gov/lnb/kulturos_pasas/EdukacijosUzsakymoIvykis`[^manifest]
- **Dataset:** [KEIS Kultūros paso edukacijos](../kulturos_pasas.md) (`datasets/gov/lnb/kulturos_pasas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/kulturos_pasas.csv#L43](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L43)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas/EdukacijosUzsakymoIvykis` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `uzsakymo_id` | `string` | — | `4` | `open` | — | Užsakymo unikalus identitfikatorius | — |
| `edukacijos_id` | `string` | — | `4` | `open` | — | Edukacijos unikalus identifikatorius | — |
| `ivykio_id` | `string` | — | `4` | `open` | — | Įvykio unikalus identitfikatorius | — |
| `statusas` | `string` | — | `4` | `open` | — | Užsakymo statusas | — |
| `ivykio_data` | `datetime` | `H` | `4` | `open` | — | Įvykio data ir laikas | — |
| `uzsakymo_vykdymo_vieta` | `string` | — | `4` | `open` | — | Vykdymo vieta | — |
| `dalyviu_skaicius` | `integer` | — | `4` | `open` | — | Dalyvių skaičius | — |
| `dalyviai_judejimo_negalia` | `integer` | — | `4` | `open` | — | Skaičius dalyvių su judėjimo negalia | — |
| `dalyviai_kurtieji` | `integer` | — | `4` | `open` | — | Skaičius dalyvių su klausos negalia | — |
| `dalyviai_intelektualiu_sutrikimu` | `integer` | — | `4` | `open` | — | Skaičius dalyvių su intelektualiu sutrikimu | — |
| `dalyviai_regejimo_negalia` | `integer` | — | `4` | `open` | — | Skaičius dalyvių su regėjimo negalia | — |
| `lydintys_asmenys` | `integer` | — | `4` | `open` | — | Lydinčių asmenų skaičius | — |
| `dalyviai_uzsienieciai` | `boolean` | — | `4` | `open` | — | Požymis ar dalyvauja užsieniečiai | — |
| `atsaukimo_prasymas` | `boolean` | — | `4` | `open` | — | Atšaukimo prašymas | — |
| `atsaukimo_laikas` | `datetime` | `U` | `4` | `open` | — | Atšaukimo laikas | — |
| `tiekejo_atsaukimo_prasymas` | `boolean` | — | `4` | `open` | — | Atšaukimas iš tiekėjo pusės | — |
| `saskaitos_suma` | `integer` | — | `4` | `open` | — | Sąskaitos suma, dalyvių skaičius * edukacijos įkainis | — |
| `uzsakymo_institucija` | `string` | — | `4` | `open` | — | Užsakymo institucija | — |
| `uzsakymo_institucijos_kodas` | `string` | — | `4` | `open` | — | Institucijos unikalus identofikatorius | — |
| `uzsakymo_savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `uzsakancio_asmens_tipas` | `string` | — | `4` | `open` | — | Užsakančio asmens tipas | — |
| `mokytojo_id` | `string` | — | `4` | `open` | — | Mokytojo ar koordinatoriaus unikalus identitfikatorius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/kulturos_pasas.csv#L43 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L43)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/kulturos_pasas (https://data.gov.lt/datasets/2659/)
