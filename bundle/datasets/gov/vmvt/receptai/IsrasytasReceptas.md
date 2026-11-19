---
type: Table
title: "IsrasytasReceptas — Veterinarinių klinikų išrašyti vaistų receptai"
description: "Rinkinyje pateikiamas Valstybinė maisto ir veterinarijos tarnybos sistemos duomenys apie veterinarų išrašytus receptus gyvūnų vaistams įsigyti."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/receptai/IsrasytasReceptas"
tags: [gov, vmvt, israsytasreceptas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/receptai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/receptai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2820/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/receptai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# IsrasytasReceptas — Veterinarinių klinikų išrašyti vaistų receptai

Rinkinyje pateikiamas Valstybinė maisto ir veterinarijos tarnybos sistemos duomenys apie veterinarų išrašytus receptus gyvūnų vaistams įsigyti. Pateikiama tokia informacija kaip recepto numeris, vaistas, gyvūno rūšies identifikacinis numeris, lytis bei koks veterinaras ar įstaiga išrašė receptą. Viena eilutė atitinka vieno recepto vaistą. Duomenys pateikiami nuo 2022 metų. PASITEIRAVIMUI: Valstybės duomenų valdysenos atvėrimo komanda: atverimas@stat.gov.lt[^manifest]

- **Model:** `datasets/gov/vmvt/receptai/IsrasytasReceptas`[^manifest]
- **Dataset:** [Duomenys apie veterinarinius vaistus bei jų išrašymus](../receptai.md) (`datasets/gov/vmvt/receptai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/receptai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/receptai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/receptai/IsrasytasReceptas` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gyv_lytis` | `"F"` | — | — | Moteris | — |
| `gyv_lytis` | `"M"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pastabos_lt` | `update(property: "pastabos_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/receptai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/receptai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/receptai (https://data.gov.lt/datasets/2820/)
