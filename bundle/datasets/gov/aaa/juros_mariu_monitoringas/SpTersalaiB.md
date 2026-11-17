---
type: Table
title: "SpTersalaiB — Specifinių teršalų tyrimai Kuršių marių ir Baltijos jūros biotoje"
description: "Spinta table datasets/gov/aaa/juros_mariu_monitoringas/SpTersalaiB (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/SpTersalaiB"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L160"
    last_modified: "2026-11-11T14:39:20Z"
---

# SpTersalaiB — Specifinių teršalų tyrimai Kuršių marių ir Baltijos jūros biotoje

- **Model:** `datasets/gov/aaa/juros_mariu_monitoringas/SpTersalaiB`[^manifest]
- **Dataset:** [datasets/gov/aaa/juros_mariu_monitoringas](../juros_mariu_monitoringas.md) (`datasets/gov/aaa/juros_mariu_monitoringas`)
- **Manifest CSV:** [datasets/gov/aaa/juros_mariu_monitoringas.csv#L160](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L160)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/SpTersalaiB`
- **Primary Key (`ref`):** `reg_nr`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_nr` | `string` | — | `2` | `open` | — | Tyrimo registracijos numeris | Registracijos nr. nėra unikalus |
| `data` | `datetime` | `D` | `4` | `open` | — | Mėginio paėmimo data | — |
| `telkinio_pav` | `string` | — | `3` | `open` | — | Vandens telkinio pavadinimas | — |
| `m_vietos_kodas` | `string` | — | `3` | `open` | — | Monitoringo vietos kodas | — |
| `m_vietos_pav` | `string` | — | `3` | `open` | — | Monitoringo vietos pavadinimas | — |
| `tyrim_objektas` | `string` | — | `3` | `open` | — | Tyrimų objektas | Tyrimų objektas visada Biota |
| `detalizacija` | `string` | — | `3` | `open` | — | Tyrimų objekto detalizacija | — |
| `gylis` | `string` | — | `2` | `open` | — | Gylis, iš kurio paimtas mėginys, metrais | — |
| `rusis_lt_lot` | `string` | — | `3` | `open` | — | Rūšies pavadinimas, kurioje atliekamas tyrimas, lietuvių ir lotynų kalbomis | — |
| `ind_eil_nr` | `string` | — | `2` | `open` | — | Individo grupės eilės numeris | — |
| `ilgio_gr` | `string` | — | `2` | `open` | — | Ilgio grupė, išreikšta milimetrais | — |
| `individ_sk_submeginy` | `string` | — | `2` | `open` | — | Individų skaičius submėginyje | — |
| `parametro_pav` | `string` | — | `3` | `open` | — | Tiriamo parametro pavadinimas | — |
| `maziau_ribos` | `boolean` | — | `4` | `open` | — | Simbolis "<", žymintis, kad rezultatas yra žemiau kiekybinio įvertinimo ribos | — |
| `rezultatas` | `number` | — | `4` | `open` | — | Parametro tyrimo rezultatas | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Matavimo vienetai (sauso svorio) | — |
| `tyr_metodas` | `string` | — | `3` | `open` | — | Tyrimų metodas | — |
| `pastabos` | `string` | — | `2` | `open` | — | Pateikiama su tyrimu susijusi svarbi informacija | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pastabos` | `update(property: "pastabos@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv
