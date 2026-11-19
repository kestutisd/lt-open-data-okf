---
type: Table
title: "Remontas — Kelių remonto darbai"
description: "\"Duomenys apie kelių remonto darbus valstybinės reikšmės keliuose."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/Remontas"
tags: [gov, via_lietuva, remontas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L17"
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv#L17"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1250/"
    title: "data.gov.lt DCAT-AP — datasets/gov/via_lietuva/eismo_ribojimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Remontas — Kelių remonto darbai

"Duomenys apie kelių remonto darbus valstybinės reikšmės keliuose. Vienoje lentelės eilutėje nurodoma vieno kelių priežiūros remonto informacija. Lentelę sudaro: darbų ir kelio atkarpos identifikaciniai numeriai, eismo kryptis, pradžios ir pabaigos kilometras kelio atkarpoje, kelio atkarpos pradžios ir pabaigos koordinatės ir jų validacijos stulpelis, nurodantis, ar koordinatės yra Lietuvos Respublikos ribose, geometrijos stulpelis, nurodantis, linijines kelio koordinates, kelio priežiūros darbų pradžios ir pabaigos data ir laikas, požymis, nurodantis, ar eismas yra leidžiamas, bei poveikis eismui. Aprašymo stulpelyje detaliau aprašomi atliekami darbai."[^manifest]

- **Model:** `datasets/gov/via_lietuva/eismo_ribojimai/Remontas`[^manifest]
- **Dataset:** ["Eismo ribojimai valstybinės reikšmės keliuose"](../eismo_ribojimai.md) (`datasets/gov/via_lietuva/eismo_ribojimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/via_lietuva/eismo_ribojimai.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L17)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai/Remontas` (`deployed`)[^manifest]
- **Provider:** `via_lietuva` — AB „Via Lietuva“ (buv. LAKD) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `darbo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `darbo_id` | `string` | — | `4` | `open` | — | Kelių priežiūros darbo identifikacinis numeris | — |
| `kelio_id` | `string` | — | `4` | `open` | — | Kelio atkarpos identifikacinis numeris | — |
| `eismo_kryptis` | `string` | — | `4` | `open` | — | Eismo kryptis kelio atkarpoje | — |
| `km_nuo` | `number` | — | `4` | `open` | — | Atkarpos kilometras nuo | Kelio priežiūros darbų kelio atkarpos pradžios kilometras |
| `km_iki` | `number` | — | `4` | `open` | — | Atkarpos kilometras iki | Kelio priežiūros darbų kelio atkarpos pabaigos kilometras |
| `nuo_koord_lks` | `geometry(3346)` | — | `4` | `open` | — | Atkarpos koordinatė nuo | LKS-94 WKT formato koordinatės taškas nurodantis kelio priežiūros darbų pradžios lokaciją |
| `iki_koord_lks` | `geometry(3346)` | — | `4` | `open` | — | Atkarpos koordinatė iki | LKS-94 WKT formato koordinatės taškas nurodantis kelio priežiūros darbų pabaigos lokaciją |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Atkarpos linijinės koordinatės | LKS-94 WKT formato linijinės koordinatės nurodančios kelio priežiūros darbų atkarpos lokaciją |
| `koord_validacija` | `boolean` | — | `4` | `open` | — | Koordinačių validavimo stulpelis | Valstybės duomenų agentūros sugeneruotas koordinatės validavimo stulpelis nurodantis ar koordinačių pradžios ir pabaigos taškai yra Lietuvos Respublikos ribose |
| `data_nuo` | `datetime` | `H` | `4` | `open` | — | Data ir laikas nuo kada vykdomi kelio priežiūros darbai | — |
| `data_iki` | `datetime` | `H` | `4` | `open` | — | Data ir laikas iki kada vykdomi kelio priežiūros darbai | — |
| `eismas_leidziamas` | `boolean` | — | `4` | `open` | — | "Požymis ,nurodantis, ar eismas yra leidžiamas" | — |
| `poveikis_eismui` | `string` | — | `4` | `open` | — | Kelio priežiūros darbų poveikis eismui | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Kelio priežiūros darbų aprašymas | — |

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

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv#L17 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L17)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/via_lietuva/eismo_ribojimai (https://data.gov.lt/datasets/1250/)
