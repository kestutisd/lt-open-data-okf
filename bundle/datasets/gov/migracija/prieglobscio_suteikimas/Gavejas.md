---
type: Table
title: "Gavejas — Duomenys apie prieglobsčio gavėjus"
description: "Duomenys apie prieglobsčio prašytojus, prieglobstį gavusius užsieniečius, pateiktus prašymus suteikti prieglobstį ir priimtus sprendimus, duomenys apie užsieniečius, dėl kurių buvo išsiųsti ar gauti paklausimai (ir/ar atsakymai) dėl jų perėmimo savo žinion ar atsiėmimo pagal..."
resource: "https://get.data.gov.lt/datasets/gov/migracija/prieglobscio_suteikimas/Gavejas"
tags: [gov, migracija, gavejas, deployed, level-3, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/prieglobscio_suteikimas.csv#L13"
    title: "atviriduomenys/manifest — datasets/gov/migracija/prieglobscio_suteikimas.csv#L13"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1941/"
    title: "data.gov.lt DCAT-AP — datasets/gov/migracija/prieglobscio_suteikimas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Gavejas — Duomenys apie prieglobsčio gavėjus

**Dataset Context:** Duomenys apie prieglobsčio prašytojus, prieglobstį gavusius užsieniečius, pateiktus prašymus suteikti prieglobstį ir priimtus sprendimus, duomenys apie užsieniečius, dėl kurių buvo išsiųsti ar gauti paklausimai (ir/ar atsakymai) dėl jų perėmimo savo žinion ar atsiėmimo pagal Dublino III reglamentą, duomenys apie užsieniečių perdavimą pagal Dublino III reglamentą.[^manifest]

- **Model:** `datasets/gov/migracija/prieglobscio_suteikimas/Gavejas`[^manifest]
- **Dataset:** [Duomenys apie prieglobsčio suteikimą](../prieglobscio_suteikimas.md) (`datasets/gov/migracija/prieglobscio_suteikimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/prieglobscio_suteikimas.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/prieglobscio_suteikimas.csv#L13)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/prieglobscio_suteikimas/Gavejas` (`deployed`)[^manifest]
- **Provider:** `migracija` — Migracijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `registracija` | `string` | — | `2` | `open` | — | Prašymo prieglobsčiui gauti registracijos data | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis byloje | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Asmens amžiaus grupė pagal gimimo datą, nurodytą byloje | — |
| `pilietybe` | `string` | — | `3` | `open` | — | Asmens pilietybė | — |
| `sprendimas` | `date` | `D` | `4` | `open` (inherited) | — | Sprendimo suteikti prieglobstį registravimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"Šeima"` | — | — | Šeima | Kai kurie prieglobsčio prašymai tenkinami ne asmeniui, o visai šeimai. Dėl to tokie jungtiniai prašymai šeimoms žymimi atskirai. |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/prieglobscio_suteikimas.csv#L13 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/prieglobscio_suteikimas.csv#L13)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/migracija/prieglobscio_suteikimas (https://data.gov.lt/datasets/1941/)
