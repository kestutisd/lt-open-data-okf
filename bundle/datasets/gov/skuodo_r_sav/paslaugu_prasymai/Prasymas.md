---
type: Table
title: "Prasymas — Skuodo rajono savivaldybės prašymai priimti į ugdymo ir socialinių paslaugų įstaigas"
description: "Skuodo rajono savivaldybės centralizuoto vaikų priėmimo į ikimokyklines įstaigas informacinė sistema yra skirta valdyti registraciją ir priėmimą į tokias įstaigas kaip darželiai, sporto ir meno mokyklos bei socialinės priežiūros ir..."
resource: "https://get.data.gov.lt/datasets/gov/skuodo_r_sav/paslaugu_prasymai/Prasymas"
tags: [gov, skuodo_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/skuodo_r_sav/paslaugu_prasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/skuodo_r_sav/paslaugu_prasymai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Skuodo rajono savivaldybės prašymai priimti į ugdymo ir socialinių paslaugų įstaigas

Skuodo rajono savivaldybės centralizuoto vaikų priėmimo į ikimokyklines įstaigas informacinė sistema yra skirta valdyti registraciją ir priėmimą į tokias įstaigas kaip darželiai, sporto ir meno mokyklos bei socialinės priežiūros ir paslaugų šeimai centrai. Rinkinyje pateikiama prašymai nuo 2011 metų iki dabar. Sistemoje duomenis pildo ugdymo ir paslaugų įstaigos, kurios atsako už duomenų kokybę.

- **Model:** `datasets/gov/skuodo_r_sav/paslaugu_prasymai/Prasymas`[^manifest]
- **Dataset:** [Skuodo rajono savivaldybės prašymai priimti į ugdymo ir socialinių paslaugų įstaigas](../paslaugu_prasymai.md) (`datasets/gov/skuodo_r_sav/paslaugu_prasymai`)
- **Manifest CSV:** [datasets/gov/skuodo_r_sav/paslaugu_prasymai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/skuodo_r_sav/paslaugu_prasymai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/skuodo_r_sav/paslaugu_prasymai/Prasymas`
- **Primary Key (`ref`):** `prasymo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prasymo_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `prasymo_data` | `date` | `D` | `4` | `open` | — | Prašymo data | — |
| `prasymo_registravimo_data` | `date` | `D` | `4` | `open` | — | Prašymo registracijos data | — |
| `prasymas_paslaugos_nuo` | `date` | `D` | `4` | `open` | — | Prašyme nurodyta paslaugos pradžios data | — |
| `asm_kodas` | `string` | — | `4` | `open` | — | Šifruotas asmens kodas | — |
| `asm_kodas_tinkamas` | `string` | — | `4` | `open` | — | Ar asmens kodas validus | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai | — |
| `gimimo_metai_ak` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai iš asmens kodo | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | — |
| `paslauga_teikiama_nuo` | `date` | `D` | `4` | `open` | — | Ugdymo įstaigos lankymo pradžios data | — |
| `paslauga_teikiama_iki` | `date` | `D` | `4` | `open` | — | Ugdymo įstaigos lankymo pabaigos data | — |
| `paslaugos_teikejas` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `grupes_pavadinimas` | `string` | — | `2` | `open` | — | Grupės pavadinimas | — |
| `vietu_sk_grupeje` | `integer` | — | `4` | `open` | — | Vietų skaičius | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/skuodo_r_sav/paslaugu_prasymai.csv
