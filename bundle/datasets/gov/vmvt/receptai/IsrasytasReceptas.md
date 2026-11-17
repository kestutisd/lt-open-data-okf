---
type: Table
title: "IsrasytasReceptas — Veterinarinių klinikų išrašyti vaistų receptai"
description: "Rinkinyje pateikiamas Valstybinė maisto ir veterinarijos tarnybos sistemos duomenys apie veterinarų išrašytus receptus gyvūnų vaistams įsigyti."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/receptai/IsrasytasReceptas"
tags: [gov, vmvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/receptai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/receptai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# IsrasytasReceptas — Veterinarinių klinikų išrašyti vaistų receptai

Rinkinyje pateikiamas Valstybinė maisto ir veterinarijos tarnybos sistemos duomenys apie veterinarų išrašytus receptus gyvūnų vaistams įsigyti. Pateikiama tokia informacija kaip recepto numeris, vaistas, gyvūno rūšies identifikacinis numeris, lytis bei koks veterinaras ar įstaiga išrašė receptą.

Viena eilutė atitinka vieno recepto vaistą.

Duomenys pateikiami nuo 2022 metų.

- **Model:** `datasets/gov/vmvt/receptai/IsrasytasReceptas`[^manifest]
- **Dataset:** [Duomenys apie veterinarinius vaistus bei jų išrašymus](../receptai.md) (`datasets/gov/vmvt/receptai`)
- **Manifest CSV:** [datasets/gov/vmvt/receptai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/receptai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/receptai/IsrasytasReceptas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikacinos numeris | — |
| `recepto_nr` | `string` | — | `4` | `open` | — | Recepto numeris | Šifruotas recepto numeris |
| `gyv_rusies_id` | `string` | — | `4` | `open` | — | Gyvūno rūšies id | — |
| `gyv_rusis` | `string` | — | `4` | `open` | — | Gyvūno rūšis | Kai atsiras duomenys, stulpelis bus užpildytas |
| `gyv_lytis` | `string` | — | `4` | `open` | — | Gyvūno lytis | — |
| `recepto_isdavimo_data` | `date` | `D` | `4` | `open` | — | Recepto išrašymo data | — |
| `recepto_ivykdymo_data` | `date` | `D` | `4` | `open` | — | Vaistų išdavimo data | — |
| `vaisto_id` | `string` | — | `4` | `open` | — | Vaisto ID iš Veterinarinių vaistų registro | — |
| `vaisto_pav` | `string` | — | `4` | `open` | — | Vaisto firminis pavadinimas | — |
| `vaisto_registruotojas` | `string` | — | `4` | `open` | — | Vaisto registruotojas | — |
| `vaisto_forma` | `string` | — | `4` | `open` | — | Vaisto forma | — |
| `vaisto_grupe` | `string` | — | `4` | `open` | — | Vaisto grupė | — |
| `vaisto_kiekis_pak` | `string` | — | `4` | `open` | — | Vaisto kiekis vienoje pakuotėje | — |
| `pakuotes_pav` | `string` | — | `4` | `open` | — | Pirminės pakuotės pavadinimas | — |
| `pakuociu_sk` | `integer` | — | `4` | `open` | — | Pirminių pakuočių skaičius (vienetais) | — |
| `pastabos_lt` | `string` | — | `3` | `open` | — | Pastabos | — |
| `istaigos_jar_kodas` | `string` | — | `4` | `open` | — | JAR kodas | Šifruotas įstaigos JAR kodas |
| `jar_validacija` | `boolean` | — | `4` | `open` | — | JAR kodo validacija | — |
| `veterinaro_sertifikato_nr` | `string` | — | `4` | `open` | — | Sertifikato numeris | Šifruotas veterinaro sertifikato numeris |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gyv_lytis` | `"F"` | — | — | Moteris | — |
| `gyv_lytis` | `"M"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pastabos_lt` | `update(property: "pastabos_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/receptai.csv
