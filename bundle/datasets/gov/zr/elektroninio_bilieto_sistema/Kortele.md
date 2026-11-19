---
type: Table
title: "Kortele — VšĮ Žaliojo regiono elektroninių bilietų kortelių duomenys"
description: "Lentelėje pateikti elektroninio bilieto sistemos duomenys apie elektroninių bilietų korteles nuo 2023 metų, teikiami VšĮ Žaliojo regiono apie Jurbarko, Šilalės, Tauragės rajonus ir Pagėgius."
resource: "https://get.data.gov.lt/datasets/gov/zr/elektroninio_bilieto_sistema/Kortele"
tags: [gov, zr, kortele, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zr/elektroninio_bilieto_sistema.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/zr/elektroninio_bilieto_sistema.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4060/"
    title: "data.gov.lt DCAT-AP — datasets/gov/zr/elektroninio_bilieto_sistema"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kortele — VšĮ Žaliojo regiono elektroninių bilietų kortelių duomenys

Lentelėje pateikti elektroninio bilieto sistemos duomenys apie elektroninių bilietų korteles nuo 2023 metų, teikiami VšĮ Žaliojo regiono apie Jurbarko, Šilalės, Tauragės rajonus ir Pagėgius. Informacija atnaujinama kas mėnesį. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/zr/elektroninio_bilieto_sistema/Kortele`[^manifest]
- **Dataset:** [VšĮ Žaliojo Regiono elektroninių bilietų pardavimai](../elektroninio_bilieto_sistema.md) (`datasets/gov/zr/elektroninio_bilieto_sistema`)[^manifest]
- **Manifest CSV:** [datasets/gov/zr/elektroninio_bilieto_sistema.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zr/elektroninio_bilieto_sistema.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/zr/elektroninio_bilieto_sistema/Kortele` (`deployed`)[^manifest]
- **Provider:** `zr` — VšĮ Žaliojo Regiono sistemų duomenys *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `korteles_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `korteles_id` | `string` | — | `4` | `open` | — | Kortelės pirminis raktas | — |
| `korteles_nr` | `string` | — | `4` | `open` | — | Kortelės numeris | — |
| `korteles_tipas` | `string` | — | `4` | `open` | — | Kortelės tipas | — |
| `korteles_busena` | `string` | — | `4` | `open` | — | Kortelės statusas | — |
| `lengvata` | `string` | — | `4` | `open` | — | Kortelės lengvatos tipas | — |
| `korteles_pridejimo_data` | `datetime` | `L` | `4` | `open` | — | Kortelės pridėjimo datos ir laiko žymė | — |
| `korteles_galiojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Korteles galiojimo pabaiga | — |
| `korteles_atnaujinimo_data` | `datetime` | `L` | `4` | `open` | — | Atnaujinimo datos ir laiko žymė | — |
| `kortele_blokuota_komentaras` | `string` | — | `4` | `open` | — | Kortelės blokavimo priežasties aprašymas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Kortelės pirkimo savivaldybė / miestas | — |
| `korteles_pirkimo_vietove` | `string` | — | `4` | `open` | — | Kortelės pirkimo vietovė | — |
| `korteles_pirkimo_adresas` | `string` | — | `4` | `open` | — | Kortelės pirkimo vietovės adresas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `korteles_tipas` | `"Fizinė"` | — | — | Fizinė | — |
| `korteles_tipas` | `"Mobilioji"` | — | — | Mobilioji | — |
| `korteles_tipas` | `"Mokinio pažymėjimas"` | — | — | Mokinio pažymėjimas | — |
| `korteles_busena` | `"Neaktyvi"` | — | — | Neaktyvi | — |
| `korteles_busena` | `"Aktyvi"` | — | — | Aktyvi | — |
| `korteles_busena` | `"Blokuota"` | — | — | Blokuota | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zr/elektroninio_bilieto_sistema.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zr/elektroninio_bilieto_sistema.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/zr/elektroninio_bilieto_sistema (https://data.gov.lt/datasets/4060/)
