---
type: Table
title: "Atsakymas — Laboratorijos tyrimų užsakymai ir atsakymai"
description: "Duomenys apie VULŽK (VšĮ Vilniaus universiteto ligoninės Žalgirio klinikų) laboratorijoje atliktus tyrimus."
resource: "https://get.data.gov.lt/datasets/gov/vulzk/lab_tyrimai/Atsakymas"
tags: [gov, vulzk, atsakymas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/lab_tyrimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vulzk/lab_tyrimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2658/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vulzk/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Atsakymas — Laboratorijos tyrimų užsakymai ir atsakymai

Duomenys apie VULŽK (VšĮ Vilniaus universiteto ligoninės Žalgirio klinikų) laboratorijoje atliktus tyrimus. Informacija apie pacientą - gimimo metai, lytis, tyrimo atlikimo data. Pateikti tyrimų atsakymai, matavimo vienetai, norma, skyriai, iš kurių pateikti užsakymai. Pateikiami duomenys nuo 2006 m.[^manifest]

- **Model:** `datasets/gov/vulzk/lab_tyrimai/Atsakymas`[^manifest]
- **Dataset:** [Laboratorijos tyrimų užsakymai ir atsakymai](../lab_tyrimai.md) (`datasets/gov/vulzk/lab_tyrimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vulzk/lab_tyrimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/lab_tyrimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vulzk/lab_tyrimai/Atsakymas` (`deployed`)[^manifest]
- **Provider:** `vulzk` — VšĮ Vilniaus universiteto ligoninės Žalgirio klinika *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vulzk/lab_tyrimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/lab_tyrimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vulzk/lab_tyrimai (https://data.gov.lt/datasets/2658/)
