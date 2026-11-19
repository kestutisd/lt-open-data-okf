---
type: Table
title: "Prasymas — Vaikų priėmimo į Kauno miesto bendrojo ugdymo įstaigas prašymai"
description: "Lentelėje pateikti duomenys apie Kauno miesto savivaldybės vaikų priėmimo į bendrojo ugdymo įstaigas prašymus."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai/Prasymas"
tags: [gov, kauno_m_sav, prasymas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2736/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Prasymas — Vaikų priėmimo į Kauno miesto bendrojo ugdymo įstaigas prašymai

Lentelėje pateikti duomenys apie Kauno miesto savivaldybės vaikų priėmimo į bendrojo ugdymo įstaigas prašymus. Duomenys paimti iš Kauno miesto savivaldybės Prašymų priimti į bendrojo ugdymo mokyklas pateikimo informacinės sistemos. Duomenys atnaujinami kas mėnesį.[^manifest]

- **Model:** `datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai/Prasymas`[^manifest]
- **Dataset:** [Vaikų priėmimo į Kauno miesto bendrojo ugdymo įstaigas prašymai](../priemimo_i_mokyklas_prasymai.md) (`datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai/Prasymas` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `prasymo_id` | `string` | — | `4` | `open` | — | Prašymo identifikatorius | — |
| `vaiko_ak` | `string` | — | `4` | `open` | — | Vaiko asmens kodas | — |
| `vaiko_ak_validacija` | `string` | — | `4` | `open` | — | Vaiko asmens kodo validacija | — |
| `vaiko_gim_metai_ak` | `date` | `Y` | `4` | `open` | — | Vaiko gimimo metai (gauti iš asmens kodo) | — |
| `vaiko_lytis_ak` | `string` | — | `4` | `open` | — | Vaiko lytis (gauta iš asmens kodo) | — |
| `tevo_ak` | `string` | — | `4` | `open` | — | Vieno iš vaiko tėvų asmens kodas | — |
| `tevo_ak_validacija` | `string` | — | `4` | `open` | — | Vieno iš vaiko tėvų asmens kodo validacija | — |
| `prasymo_inst_kodas` | `string` | — | `4` | `open` | — | Institucijos, į kurią prašoma priimti vaiką mokintis, juridinio asmens kodas | — |
| `ins_pavad_lt` | `string` | — | `4` | `open` | — | Institucijos, į kurią prašoma priimti vaiką mokintis, pavadinimas | — |
| `ins_tipas` | `string` | — | `4` | `open` | — | Institucijos, į kurią prašoma priimti vaiką mokintis, tipas (-ai) | — |
| `prasymo_klase` | `string` | — | `4` | `open` | — | Klasė, į kurią prašoma priimti vaiką mokintis | — |
| `prasymo_reg_laikas` | `datetime` | `S` | `4` | `open` | — | Prašymo registracijos laikas | — |
| `prasymas_galioja_iki` | `date` | `D` | `4` | `open` | — | Prašymo galiojimo data | — |
| `pirmumo_nr` | `string` | — | `4` | `open` | — | Prašymui suteiktas pirmumo numeris | — |
| `pirmumo_priezastis` | `string` | — | `4` | `open` | — | Pirmumo priežastis | — |
| `pirmumas_nuo` | `datetime` | `S` | `4` | `open` | — | Laikas, nuo kada galioja pirmumas | — |
| `pirmumas_iki` | `date` | `D` | `4` | `open` | — | Laikas, iki kada galioja pirmumas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vaiko_lytis_ak` | `"Vyras"` | — | — | Vyras | — |
| `vaiko_lytis_ak` | `"Moteris"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prasymo_inst_kodas` | `create(property: "ja_kodas", type: "ref", ref: "datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/priemimo_i_mokyklas_prasymai (https://data.gov.lt/datasets/2736/)
