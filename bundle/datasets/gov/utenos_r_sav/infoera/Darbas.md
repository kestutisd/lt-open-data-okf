---
type: Table
title: "Darbas — Utenos rajono savivaldybės administracijos georeferenciniai duomenys"
description: "Spinta table datasets/gov/utenos_r_sav/infoera/Darbas (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/utenos_r_sav/infoera/Darbas"
tags: [gov, utenos_r_sav, darbas, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/infoera.csv#L19"
    title: "atviriduomenys/manifest — datasets/gov/utenos_r_sav/infoera.csv#L19"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4115/"
    title: "data.gov.lt DCAT-AP — datasets/gov/utenos_r_sav/infoera"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Darbas — Utenos rajono savivaldybės administracijos georeferenciniai duomenys

- **Model:** `datasets/gov/utenos_r_sav/infoera/Darbas`[^manifest]
- **Dataset:** [Utenos rajono savivaldybės administracijos georeferencinių duomenų sistema](../infoera.md) (`datasets/gov/utenos_r_sav/infoera`)[^manifest]
- **Manifest CSV:** [datasets/gov/utenos_r_sav/infoera.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/infoera.csv#L19)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/utenos_r_sav/infoera/Darbas` (`deployed`)[^manifest]
- **Provider:** `utenos_r_sav` — Utenos rajono savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `darbo_apimtis` | `number` | — | `4` | `open` | — | Darbo apimtis hektarais | — |
| `darbo_apimties_vnt` | `string` | — | `4` | `open` | — | Darbo apimties vienetai (ha - hektarai) | — |
| `prasymo_pridavimo_data` | `date` | `D` | `4` | `open` | — | Prašymo pridavimo data | — |
| `leidimo_isdavimo_data` | `date` | `D` | `4` | `open` | — | Leidimo išdavimo data | — |
| `leidimo_priemimo_data` | `date` | `D` | `4` | `open` | — | Leidimo priėmimo data | — |
| `numatoma_darbo_pradzia` | `date` | `D` | `4` | `open` | — | Prašyme numatoma darbo pradžios data | — |
| `numatoma_darbo_pabaiga` | `date` | `D` | `4` | `open` | — | Prašyme numatoma darbo pabaigos data | — |
| `atlikto_darbo_failo_data` | `date` | `D` | `4` | `open` | — | Atlikto darbo failo data | — |
| `atlikto_darbo_data` | `date` | `D` | `4` | `open` | — | Atlikto darbo data | — |
| `leidimo_priemejas` | `string` | — | `4` | `open` | — | Leidimo priėmėjas | — |
| `darbo_vykdytojas` | `string` | — | `4` | `open` | — | Geodezinio darbo vykdytojas | — |
| `prasoma_geometry` | `string` | — | `4` | `open` | — | Prašyme darbo geometrija LKS koordinatėse | — |
| `leista_geometry` | `string` | — | `4` | `open` | — | Leidime darbo geometrija LKS koordinatėse | — |
| `atlikta_geometry` | `string` | — | `4` | `open` | — | Atlikto darbo geometrija LKS koordinatėse | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/utenos_r_sav/infoera.csv#L19 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/infoera.csv#L19)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/utenos_r_sav/infoera (https://data.gov.lt/datasets/4115/)
