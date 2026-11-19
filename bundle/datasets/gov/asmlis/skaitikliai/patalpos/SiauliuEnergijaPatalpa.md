---
type: Table
title: "SiauliuEnergijaPatalpa — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” AB „Šiaulių energija“ patalpų įrašai."
description: "Savivaldybių MOKESTA ir ASMLIS sistemų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/patalpos/SiauliuEnergijaPatalpa"
tags: [gov, asmlis, siauliuenergijapatalpa, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L60"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv#L60"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2944/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/skaitikliai/patalpos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SiauliuEnergijaPatalpa — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” AB „Šiaulių energija“...

**Dataset Context:** Savivaldybių MOKESTA ir ASMLIS sistemų duomenys[^manifest]

- **Model:** `datasets/gov/asmlis/skaitikliai/patalpos/SiauliuEnergijaPatalpa`[^manifest]
- **Dataset:** [Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”...](../patalpos.md) (`datasets/gov/asmlis/skaitikliai/patalpos`)[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/skaitikliu_parodymai.csv#L60](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L60)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/patalpos/SiauliuEnergijaPatalpa` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `patalpos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patalpos_id` | `string` | — | `4` | `open` | — | Patalpos identifikatorius | — |
| `patalpos_plotas` | `number` | — | `4` | `open` | — | Patalpos plotas | — |
| `patalpos_turis` | `number` | — | `4` | `open` | — | Patalpos tūris | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Paslaugos teikimo vietos platumos koordinatė wgs | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Paslaugos teikimo vietos ilgumos koordinatė wgs | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Paslaugos teikimo vietos koordinatės wgs | — |
| `koord_adreso_tipas` | `string` | — | `4` | `open` | — | Paslaugos teikimo vietos koordinačių tipas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv#L60 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L60)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/skaitikliai/patalpos (https://data.gov.lt/datasets/2944/)
