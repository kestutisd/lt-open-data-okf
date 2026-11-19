---
type: Table
title: "Sandoris — Duomenys apie įkeitimus ir hipotekas (hipotekos/įkeitimų rūšys, vieta, vertė, terminai)"
description: "Spinta table datasets/gov/rc/stsr/sandoriai/Sandoris (19 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/stsr/sandoriai/Sandoris"
tags: [gov, rc, sandoris, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/sandoriai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/stsr/sandoriai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2135/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/stsr/sandoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sandoris — Duomenys apie įkeitimus ir hipotekas (hipotekos/įkeitimų rūšys, vieta, vertė, terminai)

- **Model:** `datasets/gov/rc/stsr/sandoriai/Sandoris`[^manifest]
- **Dataset:** [STSR duomenys apie įkeitimus ir hipotekas](../sandoriai.md) (`datasets/gov/rc/stsr/sandoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/stsr/sandoriai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/sandoriai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/stsr/sandoriai/Sandoris` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Hipotekos / įkeitimo dirbtinis identifikatorius šiame duomenų rinkinyje | — |
| `tipas` | `string` | — | `3` | `open` | — | Hipotekos / įkeitimo tipas šiame duomenų rinkinyje | — |
| `ireg_ketv` | `date` | `Q` | `4` | `open` | — | Hipotekos / įkeitimo įregistravimo data (metai - ketvirtis) | — |
| `isreg_ketv` | `date` | `Q` | `4` | `open` | — | Hipotekos / įkeitimo išregistravimo data (metai - ketvirtis) | — |
| `iraso_priezastis` | `string` | — | `3` | `open` | — | Hipotekos / įkeitimo paskutinio įregistruoto įrašo tipas Sutarčių ir teisių suvaržymų registre | — |
| `sudarymo_vieta` | `string` | — | `3` | `open` | — | Hipotekos / įkeitimo sudarymo vieta (sav.; apskr.) | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Hipotekos / įkeitimo sudarymo vietos savivaldybės kodas iš Adresų registro (tik didmiesčių savivaldybės) | — |
| `apskritis` | `ref` | [Apskritis](../../ar/apskritis/Apskritis.md) (`level=4 UUID`: `apskritis._id`) | `4` | `open` | — | Hipotekos / įkeitimo sudarymo vietos apskrities kodas iš Adresų registro | — |
| `pri_dydis_rez` | `string` | — | `3` | `open` | — | Prievolės rėžių dydžiai | — |
| `objektu_verte_rez` | `string` | — | `3` | `open` | — | Bendras įkeičiamų daiktų įkainojimas (rėžiai) | — |
| `pri_terminas_metai` | `date` | `Y` | `4` | `open` | — | Prievolės įvykdymo terminas (metai) | — |
| `maksimalus` | `integer` | — | `4` | `open` | — | Ar maksimalioji hipoteka (1 - taip; 0 - ne) | — |
| `paprastas` | `integer` | — | `4` | `open` | — | Ar paprastoji hipoteka (1 - taip; 0 - ne) | — |
| `jungtinis` | `integer` | — | `4` | `open` | — | Ar jungtinė hipoteka (1 - taip; 0 - ne) | — |
| `svetimas` | `integer` | — | `4` | `open` | — | Ar svetimo turto hipoteka (1 - taip; 0 - ne) | — |
| `bendras` | `integer` | — | `4` | `open` | — | Ar bendroji hipoteka (1 - taip; 0 - ne) | — |
| `salyginis` | `integer` | — | `4` | `open` | — | Ar sąlyginė hipoteka (1 - taip; 0 - ne) | — |
| `pareikstinis` | `integer` | — | `4` | `open` | — | Ar pareikštinė (1 - taip; 0 - ne) | — |
| `imones` | `integer` | — | `4` | `open` | — | Ar įmonės hipoteka (1 - taip; 0 - ne) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `maksimalus` | `0` | — | — | Ne | — |
| `maksimalus` | `1` | — | — | Taip | — |
| `paprastas` | `0` | — | — | Ne | — |
| `paprastas` | `1` | — | — | Taip | — |
| `jungtinis` | `0` | — | — | Ne | — |
| `jungtinis` | `1` | — | — | Taip | — |
| `svetimas` | `0` | — | — | Ne | — |
| `svetimas` | `1` | — | — | Taip | — |
| `bendras` | `0` | — | — | Ne | — |
| `bendras` | `1` | — | — | Taip | — |
| `salyginis` | `0` | — | — | Ne | — |
| `salyginis` | `1` | — | — | Taip | — |
| `pareikstinis` | `0` | — | — | Ne | — |
| `pareikstinis` | `1` | — | — | Taip | — |
| `imones` | `0` | — | — | Ne | — |
| `imones` | `1` | — | — | Taip | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/stsr/sandoriai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/sandoriai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/stsr/sandoriai (https://data.gov.lt/datasets/2135/)
