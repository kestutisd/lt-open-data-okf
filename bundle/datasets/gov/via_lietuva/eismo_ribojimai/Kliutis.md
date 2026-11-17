---
type: Table
title: "Kliutis — Kliūtys kelyje"
description: "Duomenys apie kliūtis valstybinės reikšmės keliuose."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/Kliutis"
tags: [gov, via_lietuva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L40"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kliutis — Kliūtys kelyje

Duomenys apie kliūtis valstybinės reikšmės keliuose. Vienoje lentelės eilutėje nurodoma viena kliūtis kelio atkarpoje. Lentelę sudaro: kliūties ir kelio atkarpos identifikaciniai numeriai, kelio atkarpos kilometras, eismo kryptis kelio atkarpoje, koordinatės taškas ir validacijos stulpelis, nurodantis, ar koordinatės taškas yra Lietuvos Respublikos ribose, kliūties pastebėjimo / užregistravimo ir kliūties pašalinimo datos ir laikai, poveikis eismui ir kelio kliūties aprašymas.

- **Model:** `datasets/gov/via_lietuva/eismo_ribojimai/Kliutis`[^manifest]
- **Dataset:** [Eismo ribojimai valstybinės reikšmės keliuose](../eismo_ribojimai.md) (`datasets/gov/via_lietuva/eismo_ribojimai`)
- **Manifest CSV:** [datasets/gov/via_lietuva/eismo_ribojimai.csv#L40](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L40)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/Kliutis`
- **Primary Key (`ref`):** `kliuties_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kliuties_id` | `string` | — | `4` | `open` | — | Kliūties kelyje identifikacinis numeris | — |
| `kelio_id` | `string` | — | `4` | `open` | — | Kelio atkarpos identifikacinis numeris | — |
| `kelio_km` | `number` | — | `4` | `open` | — | Kelio atkarpos kilometras kuriame yra kelio kliūtis | — |
| `eismo_kryptis` | `string` | — | `4` | `open` | — | Eismo kryptis kelio atkarpoje | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Kliūties koordinatė | LKS-94 WKT formato koordinatės taškas kuriame yra kliūtis |
| `geometrijos_validacija` | `boolean` | — | `4` | `open` | — | Koordinačių validacija | Valstybės duomenų agentūros sugeneruotas koordinatės validavimo stulpelis nurodantis ar koordinatės taškas yra Lietuvos Respublikos ribose |
| `uzregistruota_data_laikas` | `datetime` | `H` | `4` | `open` | — | Kliūties data ir laikas | Data ir laikas kada kliūtis kelyje buvo užregistruota |
| `pasalinta_data_laikas` | `datetime` | `H` | `4` | `open` | — | Data ir laikas kada kliūtis buvo pašalinta | — |
| `poveikis_eismui` | `string` | — | `4` | `open` | — | Kliūties poveikis eismui | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Kelio kliūties aprašymas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `eismo_kryptis` | `"AB"` | — | — | Abi | — |
| `eismo_kryptis` | `"PR"` | — | — | Pirmyn | — |
| `eismo_kryptis` | `"AT"` | — | — | Atgal | — |
| `poveikis_eismui` | `"Labai svarbus"` | — | — | Labai svarbus | — |
| `poveikis_eismui` | `"Svarbus"` | — | — | Svarbus | — |
| `poveikis_eismui` | `"Vidutiniškai svarbus"` | — | — | Vidutiniškai svarbus | — |
| `poveikis_eismui` | `"Mažai svarbus"` | — | — | Mažai svarbus | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv
