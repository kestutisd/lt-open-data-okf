---
type: Table
title: "Hidrochemija — Kuršių marių ir Baltijos jūros hidrocheminių parametrų tyrimai vandenyje"
description: "Spinta table datasets/gov/aaa/juros_mariu_monitoringas/Hidrochemija (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/Hidrochemija"
tags: [gov, aaa, hidrochemija, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L13"
    title: "atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv#L13"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1790/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/juros_mariu_monitoringas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Hidrochemija — Kuršių marių ir Baltijos jūros hidrocheminių parametrų tyrimai vandenyje

- **Model:** `datasets/gov/aaa/juros_mariu_monitoringas/Hidrochemija`[^manifest]
- **Dataset:** [Kuršių marių ir Baltijos jūros valstybinio monitoringo duomenys](../juros_mariu_monitoringas.md) (`datasets/gov/aaa/juros_mariu_monitoringas`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/juros_mariu_monitoringas.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L13)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/Hidrochemija` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `reg_nr`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_nr` | `string` | — | `2` | `open` | — | Tyrimo registracijos numeris | Registracijos nr. nėra unikalus |
| `data` | `datetime` | `D` | `4` | `open` | — | Mėginio paėmimo data | — |
| `telkinio_pav` | `string` | — | `3` | `open` | — | Vandens telkinio pavadinimas | — |
| `m_vietos_kodas` | `string` | — | `3` | `open` | — | Monitoringo vietos kodas | — |
| `m_vietos_pav` | `string` | — | `3` | `open` | — | Monitoringo vietos pavadinimas | — |
| `m_koordinate` | `geometry(point, 3346)` | — | `3` | `open` | — | Monitoringo vietos koordinatės (LKS-94) | — |
| `tyrim_objektas` | `string` | — | `3` | `open` | — | Tyrimų objektas | Tyrimų objektas visiems Kuršių marių ir Baltijos jūros tyrimams, išskyrus Specifinių teršalų tyrimus biotoje - paviršinis vanduo. |
| `horizontas` | `string` | — | `3` | `open` | — | Vandens sluoksnis, iš kurio paimtas mėginys | Horizontas/Sluoksnis: Paviršinis sluoksnis, Tarpinis sluoksnis, Priedugnis, Integruotas, Sudėtinis. Monitoringo vietoje gali būti keli Tarpiniai sluoksniai, priklausomai nuo jos gylio. |
| `gylis` | `number` | `m` | `4` | `open` | — | Gylis, iš kurio paimtas mėginys, metrais | — |
| `parametro_pav` | `string` | — | `3` | `open` | — | Tiriamo parametro pavadinimas | — |
| `maziau_ribos` | `boolean` | — | `4` | `open` | — | Simbolis "<", žymintis, kad rezultatas yra žemiau kiekybinio įvertinimo ribos | — |
| `rezultatas` | `number` | — | `4` | `open` | — | Parametro tyrimo rezultatas | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Matavimo vienetai | Matavimo vienetas priklauso nuo tiriamo parametro. |
| `tyr_metodas` | `string` | — | `3` | `open` | — | Tyrimų metodas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv#L13 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L13)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/juros_mariu_monitoringas (https://data.gov.lt/datasets/1790/)
