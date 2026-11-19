---
type: Table
title: "DaiktoPaieska — Policijos ieškomų daiktų duomenys"
description: "Lentelėje pateikiami Policijos departamento prie LR vidaus reikalų ministerijos Ieškomų ir rastų numeruotų bei individualius požymius turinčių daiktų ir dokumentų registro (INDR) duomenys."
resource: "https://get.data.gov.lt/datasets/gov/pd/policijos_ieskomi_daiktai/DaiktoPaieska"
tags: [gov, pd, daiktopaieska, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/policijos_ieskomi_daiktai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/pd/policijos_ieskomi_daiktai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3805/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pd/policijos_ieskomi_daiktai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# DaiktoPaieska — Policijos ieškomų daiktų duomenys

Lentelėje pateikiami Policijos departamento prie LR vidaus reikalų ministerijos Ieškomų ir rastų numeruotų bei individualius požymius turinčių daiktų ir dokumentų registro (INDR) duomenys. Informacija lentelėje atnaujinama kas mėnesį. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/pd/policijos_ieskomi_daiktai/DaiktoPaieska`[^manifest]
- **Dataset:** [Policijos ieškomų daiktų duomenys](../policijos_ieskomi_daiktai.md) (`datasets/gov/pd/policijos_ieskomi_daiktai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pd/policijos_ieskomi_daiktai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/policijos_ieskomi_daiktai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pd/policijos_ieskomi_daiktai/DaiktoPaieska` (`deployed`)[^manifest]
- **Provider:** `pd` — Policijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `iraso_sukurimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo (duomenų eilutės) sukūrimo data | — |
| `iraso_atnaujinimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo (duomenų eilutės) atnaujinimo data | — |
| `paieskos_statusas` | `string` | — | `4` | `open` | — | Paieškos statusas | — |
| `nacionalinis_id` | `string` | — | `4` | `open` | — | Nacionalinis identifikatorius | — |
| `obekto_tipas` | `string` | — | `4` | `open` | — | Ieškomo objekto (daikto) tipas | — |
| `daikto_grupe` | `string` | — | `4` | `open` | — | Daikto grupė | — |
| `daikto_kategorija` | `string` | — | `4` | `open` | — | Daikto kategorija | — |
| `daikto_indvidualus_numeris` | `string` | — | `4` | `open` | — | Daikto individualus numeris | — |
| `daikto_kiti_numeriai` | `string` | — | `4` | `open` | — | Kitas daikto identifikacinis numeris | — |
| `paieskos_priezastis_lt` | `string` | — | `4` | `open` | — | Paieškos priežastis | — |
| `paieska_paskelbusi_valstybe` | `string` | — | `4` | `open` | — | Paiešką paskelbusi valstybė | — |
| `praradimo_data` | `datetime` | `S` | `4` | `open` | — | Daikto praradimo data | — |
| `paieskos_pradzia` | `datetime` | `S` | `4` | `open` | — | Daikto paieškos pradžia | — |
| `paieskos_pabaiga` | `date` | `D` | `4` | `open` | — | Daikto paieškos pabaiga | — |
| `suradimo_laikas` | `datetime` | `S` | `4` | `open` | — | Daikto suradimo laikas | — |
| `nutraukimo_data` | `datetime` | `S` | `4` | `open` | — | Paieškos nutraukimo data | — |
| `nutraukimo_pagrindas_lt` | `string` | — | `4` | `open` | — | Paieškos nutraukimo pagrindas | — |
| `nutraukimo_pagrindas_kt_lt` | `string` | — | `4` | `open` | — | Kitas paieškos nutraukimo pagrindas | — |
| `archyvavimo_data` | `date` | `D` | `4` | `open` | — | Įrašo archyvavimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paieskos_priezastis_lt` | `update(property: "paieskos_priezastis_lt@lt", type: "text")` | `type` | — | — | — | — | — |
| `nutraukimo_pagrindas_lt` | `update(property: "nutraukimo_pagrindas_lt@lt", type: "text")` | `type` | — | — | — | — | — |
| `nutraukimo_pagrindas_kt_lt` | `update(property: "nutraukimo_pagrindas_kt_lt@lt", type: "text")` | `type` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/policijos_ieskomi_daiktai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/policijos_ieskomi_daiktai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pd/policijos_ieskomi_daiktai (https://data.gov.lt/datasets/3805/)
