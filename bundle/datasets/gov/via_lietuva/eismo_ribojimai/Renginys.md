---
type: Table
title: "Renginys — Eismo ribojimai dėl renginių"
description: "Duomenys apie eismo ribojimus dėl renginių valstybinės reikšmės keliuose."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/Renginys"
tags: [gov, via_lietuva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L59"
    last_modified: "2026-11-11T14:39:20Z"
---

# Renginys — Eismo ribojimai dėl renginių

Duomenys apie eismo ribojimus dėl renginių valstybinės reikšmės keliuose. Viena lentelės eilutė atitinka vieną renginį, dėl kurio vykdomi eismo ribojimai tam tikru laiku, tam tikroje kelio atkarpoje. Lentelę sudaro: eismo ribojimo ir kelio atkarpos identifikaciniai numeriai, eismo kryptis, geometrijos stulpelis, nurodantis tašką, kuriame eismas ribojamas, validacijos stulpelis, nurodantis, ar koordinatės yra Lietuvos Respublikos ribose, ribojimo pradžios ir pabaigos data ir laikas, poveikis eismui, renginio, dėl kurio eismas yra ribojamas, aprašymas.

- **Model:** `datasets/gov/via_lietuva/eismo_ribojimai/Renginys`[^manifest]
- **Dataset:** [Eismo ribojimai valstybinės reikšmės keliuose](../eismo_ribojimai.md) (`datasets/gov/via_lietuva/eismo_ribojimai`)
- **Manifest CSV:** [datasets/gov/via_lietuva/eismo_ribojimai.csv#L59](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L59)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/Renginys`
- **Primary Key (`ref`):** `ribojimo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ribojimo_id` | `string` | — | `4` | `open` | — | Ribojimo dėl renginio identifikacinis numeris | — |
| `kelio_id` | `string` | — | `4` | `open` | — | Kelio atkarpos identifikacinis numeris | — |
| `kelio_km` | `number` | — | `4` | `open` | — | Kelio atkarpos kilometras | — |
| `eismo_kryptis` | `string` | — | `4` | `open` | — | Eismo kryptis kelio atkarpoje | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Ribojimo koordinatės taškas | LKS-94 WKT formato koordinatės taškas, kuriame ribojamas eismas dėl renginio |
| `geometrijos_validacija` | `boolean` | — | `4` | `open` | — | Koordinatės taško validacija | Valstybės duomenų agentūros sugeneruotas koordinatės validavimo stulpelis nurodantis ar koordinatės taškas yra Lietuvos Respublikos ribose |
| `data_laikas_nuo` | `datetime` | `T` | `4` | `open` | — | Eismo ribojimo dėl renginio pradžios data ir laikas | — |
| `data_laikas_iki` | `datetime` | `T` | `4` | `open` | — | Eismo ribojimo dėl renginio pabaigos data ir laikas | — |
| `poveikis_eismui` | `string` | — | `4` | `open` | — | Eismo ribojimo dėl renginio poeveikis eismui | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Renginio aprašymas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `eismo_kryptis` | `"AB"` | — | — | Abi | — |
| `eismo_kryptis` | `"PR"` | — | — | Pirmyn | — |
| `eismo_kryptis` | `"AT"` | — | — | Atgal | — |
| `poveikis_eismui` | `"Labai svarbus"` | — | — | — | — |
| `poveikis_eismui` | `"Svarbus"` | — | — | — | — |
| `poveikis_eismui` | `"Vidutiniškai svarbus"` | — | — | — | — |
| `poveikis_eismui` | `"Mažai svarbus"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv
