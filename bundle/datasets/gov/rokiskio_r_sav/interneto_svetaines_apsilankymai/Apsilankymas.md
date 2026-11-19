---
type: Table
title: "Apsilankymas — Interneto svetainės „rokiskis.lt“ puslapių skilčių apsilankymai"
description: "Lentelėje pateikta informacija apie interneto svetainės „rokiskis.lt“ puslapių skilčių apsilankymus iš Rokiškio rajono savivaldybės interneto turinio valdymo sistemos (ITVS)."
resource: "https://get.data.gov.lt/datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai/Apsilankymas"
tags: [gov, rokiskio_r_sav, apsilankymas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2844/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Apsilankymas — Interneto svetainės „rokiskis.lt“ puslapių skilčių apsilankymai

Lentelėje pateikta informacija apie interneto svetainės „rokiskis.lt“ puslapių skilčių apsilankymus iš Rokiškio rajono savivaldybės interneto turinio valdymo sistemos (ITVS). Duomenų laiko aprėptis - nuo 2020 metų. Informacija lentelėje papildoma kas mėnesį. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai/Apsilankymas`[^manifest]
- **Dataset:** [Interneto svetainės „rokiskis.lt“ puslapių skilčių apsilankymai](../interneto_svetaines_apsilankymai.md) (`datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai/Apsilankymas` (`deployed`)[^manifest]
- **Provider:** `rokiskio_r_sav` — Rokiškio rajono savivaldybė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `puslapio_id` | `string` | — | `4` | `open` | — | Puslapio (skilties) identifikatorius | — |
| `uri` | `string` | — | `4` | `open` | — | Puslapio (skilties) nuoroda | — |
| `tipas` | `string` | — | `4` | `open` | — | Puslapio (skilties) tipas | — |
| `data` | `date` | `D` | `4` | `open` | — | Data | — |
| `apsilankymu_skaicius` | `integer` | `U` | `4` | `open` | — | Apsilankymų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rokiskio_r_sav/interneto_svetaines_apsilankymai (https://data.gov.lt/datasets/2844/)
