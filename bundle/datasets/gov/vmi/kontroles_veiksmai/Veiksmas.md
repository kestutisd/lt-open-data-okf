---
type: Table
title: "Veiksmas — Atlikti kontrolės veiksmai"
description: "Spinta table datasets/gov/vmi/kontroles_veiksmai/Veiksmas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/kontroles_veiksmai/Veiksmas"
tags: [gov, vmi, veiksmas, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/kontroles_veiksmai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/kontroles_veiksmai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1300/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/kontroles_veiksmai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Veiksmas — Atlikti kontrolės veiksmai

- **Model:** `datasets/gov/vmi/kontroles_veiksmai/Veiksmas`[^manifest]
- **Dataset:** [Atlikti kontrolės veiksmai](../kontroles_veiksmai.md) (`datasets/gov/vmi/kontroles_veiksmai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/kontroles_veiksmai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/kontroles_veiksmai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/kontroles_veiksmai/Veiksmas` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | — |
| `evrk` | `ref` | [EkonominesVeiklosRusis](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) (`level=4 UUID`: `evrk._id`) | `4` | `open` | — | Ekonominės veiklos rūšies kodas | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės identifikavimo kodas | — |
| `mm_skaicius` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.
- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/kontroles_veiksmai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/kontroles_veiksmai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/kontroles_veiksmai (https://data.gov.lt/datasets/1300/)
