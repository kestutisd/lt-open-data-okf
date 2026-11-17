---
type: Table
title: "TelsiuvIrasas — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB \"Telšių vandenys\" vartotojų skolų įrašai."
description: "Spinta table datasets/gov/asmlis/skolu_irasai/TelsiuvIrasas (23 columns)."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/skolu_irasai/TelsiuvIrasas"
tags: [gov, asmlis, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/asmlis/skolu_irasai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skolu_irasai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# TelsiuvIrasas — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Telšių vandenys" vartotojų skolų įrašai.

- **Model:** `datasets/gov/asmlis/skolu_irasai/TelsiuvIrasas`[^manifest]
- **Dataset:** [Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Asmlis” ir „Mokesta” aptarnaujančios savivaldybes ir joms pavaldžias įstaigas vartotojų skolų įrašai.](../skolu_irasai.md) (`datasets/gov/asmlis/skolu_irasai`)
- **Manifest CSV:** [datasets/gov/asmlis/skolu_irasai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skolu_irasai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/skolu_irasai/TelsiuvIrasas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus lentelės raktas | — |
| `skolos_iraso_id` | `string` | — | `4` | `open` | — | Skolos įrašo indetifikatorius | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikatorius | — |
| `skolos_suma` | `number` | — | `4` | `open` | — | Skolos suma | — |
| `ar_delsp_neskaic` | `boolean` | — | `4` | `open` | — | Požymis ar neskaičiuojami delspinigiai | — |
| `skol_iras_data` | `date` | `D` | `4` | `open` | — | Skolos įrašo data | — |
| `bankroto_data` | `date` | `D` | `4` | `open` | — | Bankroto data | — |
| `moketojo_kodas` | `string` | — | `4` | `open` | — | Mokėtojo kodas | — |
| `moketojo_tipas` | `string` | — | `4` | `open` | — | Mokėtojo tipas | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `kitas_kodas` | `string` | — | `4` | `open` | — | Kodas nepraėjęs asmens kodo ir juridinio asmens kodo validacijų | — |
| `ar_pvm_moketojas` | `boolean` | — | `4` | `open` | — | Požymis ar PVM mokėtojas | — |
| `sutart_isigal_data` | `date` | `D` | `4` | `open` | — | Sutarties sudarymo data | — |
| `sutart_nutrauk_data` | `date` | `D` | `4` | `open` | — | Sutarties nutraukimo data | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Skolininko gimimo metai | — |
| `gim_metai_asmk` | `date` | `Y` | `4` | `open` | — | Skolininko gimimo metai iš asmens kodo | — |
| `mirties_metai` | `date` | `Y` | `4` | `open` | — | Skolininko mirties metai | — |
| `lytis_asmk` | `string` | — | `4` | `open` | — | Skolininko lytis iš asmens kodo | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Paslaugos teikimo vietos platumos koordinatė wgs | Pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą, sugeneruotą pagal normalųjį skirstinį |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Paslaugos teikimo vietos ilgumos koordinatė wgs | Pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą, sugeneruotą pagal normalųjį skirstinį |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Paslaugos teikimo vietos koordinatės | Pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą, sugeneruotą pagal normalųjį skirstinį |
| `tipas` | `string` | — | `4` | `open` | — | Paslaugos teikimo vietos koordinačių tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_asmk` | `"Moteris"` | — | — | Moteris | — |
| `lytis_asmk` | `"Vyras"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/skolu_irasai.csv
