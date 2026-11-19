---
type: Table
title: "Kliutis — Kliūtys kelyje"
description: "\"Duomenys apie kliūtis valstybinės reikšmės keliuose."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/Kliutis"
tags: [gov, via_lietuva, kliutis, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L40"
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv#L40"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1250/"
    title: "data.gov.lt DCAT-AP — datasets/gov/via_lietuva/eismo_ribojimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kliutis — Kliūtys kelyje

"Duomenys apie kliūtis valstybinės reikšmės keliuose. Vienoje lentelės eilutėje nurodoma viena kliūtis kelio atkarpoje. Lentelę sudaro: kliūties ir kelio atkarpos identifikaciniai numeriai, kelio atkarpos kilometras, eismo kryptis kelio atkarpoje, koordinatės taškas ir validacijos stulpelis, nurodantis, ar koordinatės taškas yra Lietuvos Respublikos ribose, kliūties pastebėjimo / užregistravimo ir kliūties pašalinimo datos ir laikai, poveikis eismui ir kelio kliūties aprašymas."[^manifest]

- **Model:** `datasets/gov/via_lietuva/eismo_ribojimai/Kliutis`[^manifest]
- **Dataset:** ["Eismo ribojimai valstybinės reikšmės keliuose"](../eismo_ribojimai.md) (`datasets/gov/via_lietuva/eismo_ribojimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/via_lietuva/eismo_ribojimai.csv#L40](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L40)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/Kliutis` (`deployed`)[^manifest]
- **Provider:** `via_lietuva` — AB „Via Lietuva“ (buv. LAKD) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kliuties_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `eismo_kryptis` | `"AB"` | — | — | Abi | — |
| `eismo_kryptis` | `"PR"` | — | — | Pirmyn | — |
| `eismo_kryptis` | `"AT"` | — | — | Atgal | — |
| `poveikis_eismui` | `"Labai svarbus"` | — | — | Labai svarbus | — |
| `poveikis_eismui` | `"Svarbus"` | — | — | Svarbus | — |
| `poveikis_eismui` | `"Vidutiniškai svarbus"` | — | — | Vidutiniškai svarbus | — |
| `poveikis_eismui` | `"Mažai svarbus"` | — | — | Mažai svarbus | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv#L40 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L40)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/via_lietuva/eismo_ribojimai (https://data.gov.lt/datasets/1250/)
