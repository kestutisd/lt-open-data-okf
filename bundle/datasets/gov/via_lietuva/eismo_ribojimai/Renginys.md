---
type: Table
title: "Renginys — Eismo ribojimai dėl renginių"
description: "\"Duomenys apie eismo ribojimus dėl renginių valstybinės reikšmės keliuose."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/Renginys"
tags: [gov, via_lietuva, renginys, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L59"
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv#L59"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1250/"
    title: "data.gov.lt DCAT-AP — datasets/gov/via_lietuva/eismo_ribojimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Renginys — Eismo ribojimai dėl renginių

"Duomenys apie eismo ribojimus dėl renginių valstybinės reikšmės keliuose. Viena lentelės eilutė atitinka vieną renginį, dėl kurio vykdomi eismo ribojimai tam tikru laiku, tam tikroje kelio atkarpoje. Lentelę sudaro: eismo ribojimo ir kelio atkarpos identifikaciniai numeriai, eismo kryptis, geometrijos stulpelis, nurodantis tašką, kuriame eismas ribojamas, validacijos stulpelis, nurodantis, ar koordinatės yra Lietuvos Respublikos ribose, ribojimo pradžios ir pabaigos data ir laikas, poveikis eismui, renginio, dėl kurio eismas yra ribojamas, aprašymas."[^manifest]

- **Model:** `datasets/gov/via_lietuva/eismo_ribojimai/Renginys`[^manifest]
- **Dataset:** ["Eismo ribojimai valstybinės reikšmės keliuose"](../eismo_ribojimai.md) (`datasets/gov/via_lietuva/eismo_ribojimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/via_lietuva/eismo_ribojimai.csv#L59](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L59)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/Renginys` (`deployed`)[^manifest]
- **Provider:** `via_lietuva` — AB „Via Lietuva“ (buv. LAKD) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ribojimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ribojimo_id` | `string` | — | `4` | `open` | — | Ribojimo dėl renginio identifikacinis numeris | — |
| `kelio_id` | `string` | — | `4` | `open` | — | Kelio atkarpos identifikacinis numeris | — |
| `kelio_km` | `number` | — | `4` | `open` | — | Kelio atkarpos kilometras | — |
| `eismo_kryptis` | `string` | — | `4` | `open` | — | Eismo kryptis kelio atkarpoje | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Ribojimo koordinatės taškas | "LKS-94 WKT formato koordinatės taškas, kuriame ribojamas eismas dėl renginio" |
| `geometrijos_validacija` | `boolean` | — | `4` | `open` | — | Koordinatės taško validacija | Valstybės duomenų agentūros sugeneruotas koordinatės validavimo stulpelis nurodantis ar koordinatės taškas yra Lietuvos Respublikos ribose |
| `data_laikas_nuo` | `datetime` | `T` | `4` | `open` | — | Eismo ribojimo dėl renginio pradžios data ir laikas | — |
| `data_laikas_iki` | `datetime` | `T` | `4` | `open` | — | Eismo ribojimo dėl renginio pabaigos data ir laikas | — |
| `poveikis_eismui` | `string` | — | `4` | `open` | — | Eismo ribojimo dėl renginio poeveikis eismui | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Renginio aprašymas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `eismo_kryptis` | `"AB"` | — | — | Abi | — |
| `eismo_kryptis` | `"PR"` | — | — | Pirmyn | — |
| `eismo_kryptis` | `"AT"` | — | — | Atgal | — |
| `poveikis_eismui` | `"Labai svarbus"` | — | — | — | — |
| `poveikis_eismui` | `"Svarbus"` | — | — | — | — |
| `poveikis_eismui` | `"Vidutiniškai svarbus"` | — | — | — | — |
| `poveikis_eismui` | `"Mažai svarbus"` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv#L59 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L59)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/via_lietuva/eismo_ribojimai (https://data.gov.lt/datasets/1250/)
