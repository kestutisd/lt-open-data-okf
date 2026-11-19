---
type: Table
title: "Seniunaitija — Klaipėdos miesto savivaldybės seniūnaitijos"
description: "Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys/Seniunaitija"
tags: [gov, klaipedos_m_sav, seniunaitija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L25"
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L25"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2856/"
    title: "data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/geografiniai_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Seniunaitija — Klaipėdos miesto savivaldybės seniūnaitijos

Klaipėdos miesto savivaldybės ARGIS informacinėje sistemoje kaupiami geografiniai miesto duomenys. Šioje lentelėje pateikiamos Klaipėdos miesto savivaldybėje esančios seniūnaitojos bei jų teritorijų koordinatės. Duomenys pateikiami aktualūs šiai dienai. Duomenų teikėjas: Klaipėdos miesto savivaldybė Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/klaipedos_m_sav/geografiniai_duomenys/Seniunaitija`[^manifest]
- **Dataset:** [Klaipėdos miesto savivaldybės objektų geografiniai duomenys](../geografiniai_duomenys.md) (`datasets/gov/klaipedos_m_sav/geografiniai_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L25](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L25)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/geografiniai_duomenys/Seniunaitija` (`deployed`)[^manifest]
- **Provider:** `klaipedos_m_sav` — Klaipėdos miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `object_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `object_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Seniūnaitijos pavadinimas | — |
| `apygarda` | `string` | — | `4` | `open` | — | Agygarda kuriai priklauso seniūnaitija | — |
| `geometrija` | `geometry(3346)` | — | `3` | `open` | — | Geometrija (teritorija) | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L25 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/geografiniai_duomenys.csv#L25)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/geografiniai_duomenys (https://data.gov.lt/datasets/2856/)
