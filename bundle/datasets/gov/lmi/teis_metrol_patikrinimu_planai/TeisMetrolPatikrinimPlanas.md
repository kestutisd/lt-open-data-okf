---
type: Table
title: "TeisMetrolPatikrinimPlanas — Lietuvos metrologijos inspekcijos įmonių patikrinimų ketvirčio planai"
description: "Duomenų rinkinyje kaupiami Lietuvos metrologijos inspekcijos įmonių patikrinimo ketvirčio planų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lmi/teis_metrol_patikrinimu_planai/TeisMetrolPatikrinimPlanas"
tags: [gov, lmi, teismetrolpatikrinimplanas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2832/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lmi/teis_metrol_patikrinimu_planai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# TeisMetrolPatikrinimPlanas — Lietuvos metrologijos inspekcijos įmonių patikrinimų ketvirčio planai

Duomenų rinkinyje kaupiami Lietuvos metrologijos inspekcijos įmonių patikrinimo ketvirčio planų duomenys. Viena eilutė rinkinyje atitinka vieną planuojamą patikrinimą. Rinkinyje nurodomos įmonės, jų rizika, adresas ir (arba) veiklos vieta, veiklos rūšis pagal ekonominės veiklos rūšies klasifikatoriaus antrąją redakciją. Rinkinį sudaro nuo 2021 metų sausio 1 dienos sukaupti duomenys. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lmi/teis_metrol_patikrinimu_planai/TeisMetrolPatikrinimPlanas`[^manifest]
- **Dataset:** [Lietuvos metrologijos inspekcijos įmonių patikrinimų ketvirčio planai](../teis_metrol_patikrinimu_planai.md) (`datasets/gov/lmi/teis_metrol_patikrinimu_planai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lmi/teis_metrol_patikrinimu_planai/TeisMetrolPatikrinimPlanas` (`deployed`)[^manifest]
- **Provider:** `lmi` — Lietuvos metrologijos inspekcija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikacinis kodas | — |
| `plano_metai` | `date` | `Y` | `4` | `open` | — | Metai, kada pateiktas patikrinimų planas | — |
| `plano_ketvirtis` | `integer` | — | `4` | `open` | — | Ketvirtis, kada pateiktas patikrinimų planas | — |
| `numatomas_patikrinimo_menuo` | `string` | — | `4` | `open` | — | Numatomas patikrinimo mėnuo | — |
| `skyrius` | `string` | — | `4` | `open` | — | Skyrius | — |
| `rizika` | `string` | — | `4` | `open` | — | Įmonės rizika (kuo įmonės veikla gali sukelti didesnę žalą, tuo jos rizika yra didesnė ir patikrinimai yra vykdomi dažniau) | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės kodas | — |
| `ukio_subjekto_pavadinimas` | `string` | — | `4` | `open` | — | Ūkio subjekto/įmonės pavadinimas | — |
| `ekonomines_veiklos_rusis_pagal_evrk_2_red` | `string` | — | `4` | `open` | — | Tikrinamos įmonės ekonominės veiklos rūšies pavadinimas pagal EVRK 2 redakciją | — |
| `ukio_subjekto_adresas_jar` | `string` | — | `4` | `open` | — | Ūkio subjekto/įmonės adresas juridinių asmenų registre | — |
| `veiklaviete` | `string` | — | `4` | `open` | — | Įmonės veiklos vietos adresas | — |
| `pastabos` | `string` | — | `4` | `open` | — | Profesijos kodas pagal Lietuvos profesijų klasifikatorių | — |
| `plano_pataisymo_nr` | `integer` | — | `2` | `open` | — | Plano pataisymo numeris (jei yra) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `skyrius` | `"Rytų regiono skyrius"` | — | — | Rytų regiono skyrius | — |
| `skyrius` | `"Vakarų regiono skyrius"` | — | — | Vakarų regiono skyrius | — |
| `rizika` | `"Didelės rizikos"` | — | — | Didelė įmonės rizika | — |
| `rizika` | `"Vidutinės rizikos"` | — | — | Vidutinė įmonės rizika | — |
| `rizika` | `"Mažos rizikos"` | — | — | Maža įmonės rizika | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lmi/teis_metrol_patikrinimu_planai (https://data.gov.lt/datasets/2832/)
