---
type: Table
title: "ZemelapisRysys — Vilniaus miesto žemėlapių nuorodos į istorines gatves"
description: "\"Duomenys iš „ID Vilnius“ apie žemėlapių ir istorinių gatvių ryšius."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/ZemelapisRysys"
tags: [gov, id_vilnius, zemelapisrysys, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L106"
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L106"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# ZemelapisRysys — Vilniaus miesto žemėlapių nuorodos į istorines gatves

"Duomenys iš „ID Vilnius“ apie žemėlapių ir istorinių gatvių ryšius. Viena lentelės eilutė nurodo vieną ryšį tarp žemėlapio (istorinio šaltinio) ir istorinės gatvės, referuojančios į tą žemėlapį. Eilutės informaciją sudaro žemėlapio ir istorinės gatvės identifikaciniai numeriai."[^manifest]

- **Model:** `datasets/gov/id_vilnius/vilniaus_dnr/ZemelapisRysys`[^manifest]
- **Dataset:** [Vilniaus miesto istoriniai duomenys - Vilniaus DNR](../vilniaus_dnr.md) (`datasets/gov/id_vilnius/vilniaus_dnr`)[^manifest]
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L106](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L106)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/ZemelapisRysys` (`deployed`)[^manifest]
- **Provider:** `id_vilnius`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | "Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius (pirminis raktas) sudarytas iš stulpelių zemelapio_id ir istorine_gatve_id" |
| `zemelapio_id` | `string` | — | `4` | `open` | — | Žemėlapio identifikacinis numeris | — |
| `istorine_gatve_id` | `string` | — | `4` | `open` | — | Istorinės gatvės identifikacinis numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L106 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L106)
