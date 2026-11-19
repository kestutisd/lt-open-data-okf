---
type: Table
title: "SakiuSilumaIrasas — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB \"Šakių šiluma\" vartotojų skolų įrašai."
description: "Savivaldybių MOKESTA ir ASMLIS sistemų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/asmlis/skolu_irasai/SakiuSilumaIrasas"
tags: [gov, asmlis, sakiusilumairasas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skolu_irasai.csv#L87"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/skolu_irasai.csv#L87"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2930/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/skolu_irasai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SakiuSilumaIrasas — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB "Šakių šiluma" vartotojų...

**Dataset Context:** Savivaldybių MOKESTA ir ASMLIS sistemų duomenys[^manifest]

- **Model:** `datasets/gov/asmlis/skolu_irasai/SakiuSilumaIrasas`[^manifest]
- **Dataset:** [Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Asmlis” ir „Mokesta”...](../skolu_irasai.md) (`datasets/gov/asmlis/skolu_irasai`)[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/skolu_irasai.csv#L87](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skolu_irasai.csv#L87)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/skolu_irasai/SakiuSilumaIrasas` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Paslaugos teikimo vietos platumos koordinatė wgs | "Pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą, sugeneruotą pagal normalųjį skirstinį" |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Paslaugos teikimo vietos ilgumos koordinatė wgs | "Pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą, sugeneruotą pagal normalųjį skirstinį" |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Paslaugos teikimo vietos koordinatės | "Pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą, sugeneruotą pagal normalųjį skirstinį" |
| `tipas` | `string` | — | `4` | `open` | — | Paslaugos teikimo vietos koordinačių tipas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_asmk` | `"Moteris"` | — | — | Moteris | — |
| `lytis_asmk` | `"Vyras"` | — | — | Vyras | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/skolu_irasai.csv#L87 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skolu_irasai.csv#L87)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/skolu_irasai (https://data.gov.lt/datasets/2930/)
