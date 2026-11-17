---
type: Table
title: "Atsakymas — Laboratorijos tyrimų užsakymai ir atsakymai"
description: "Duomenys apie VULŽK (VšĮ Vilniaus universiteto ligoninės Žalgirio klinikų) laboratorijoje atliktus tyrimus."
resource: "https://get.data.gov.lt/datasets/gov/vulzk/lab_tyrimai/Atsakymas"
tags: [gov, vulzk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vulzk/lab_tyrimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/lab_tyrimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atsakymas — Laboratorijos tyrimų užsakymai ir atsakymai

Duomenys apie VULŽK (VšĮ Vilniaus universiteto ligoninės Žalgirio klinikų) laboratorijoje atliktus tyrimus. Informacija apie pacientą - gimimo metai, lytis, tyrimo atlikimo data. Pateikti tyrimų atsakymai, matavimo vienetai, norma, skyriai, iš kurių pateikti užsakymai.

Pateikiami duomenys nuo 2006 m.

- **Model:** `datasets/gov/vulzk/lab_tyrimai/Atsakymas`[^manifest]
- **Dataset:** [Laboratorijos tyrimų užsakymai ir atsakymai](../lab_tyrimai.md) (`datasets/gov/vulzk/lab_tyrimai`)
- **Manifest CSV:** [datasets/gov/vulzk/lab_tyrimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/lab_tyrimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vulzk/lab_tyrimai/Atsakymas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento identifikatorius | — |
| `gimimo_m` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `tyr_id` | `string` | — | `4` | `open` | — | Tyrimo identifikatorius | — |
| `tyr_data` | `date` | `D` | `4` | `open` | — | Tyrimo atlikimo data | — |
| `tyr_gr_id` | `string` | — | `4` | `open` | — | Tyrimo grupės identifikatorius | — |
| `tyr_gr` | `string` | — | `4` | `open` | — | Tyrimo grupė | — |
| `tyrimas` | `string` | — | `4` | `open` | — | Tyrimo pavadinimas | — |
| `ats` | `string` | — | `1` | `open` | — | Rezultatai | — |
| `ats_num` | `number` | — | `4` | `open` | — | Rezultatai (reikšmės tik skaitine išraiška) | — |
| `mat_vnt` | `string` | — | `4` | `open` | — | Matavimo vienetai | — |
| `norma_pastabos` | `string` | — | `4` | `open` | — | Tyrimo normos, papildomos pastabos | — |
| `skyrius` | `string` | — | `4` | `open` | — | Skyrius, iš kurio pateiktas užsakymas | — |
| `gyd` | `string` | — | `4` | `open` | — | Gydytojo, kuris užsakė tyrimą, identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tyrimas` | `update(property: "tyrimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `norma_pastabos` | `update(property: "norma_pastabos@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vulzk/lab_tyrimai.csv
