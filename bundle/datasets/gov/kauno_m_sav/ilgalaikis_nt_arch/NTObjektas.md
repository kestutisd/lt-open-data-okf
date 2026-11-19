---
type: Table
title: "NTObjektas — Kauno miesto nekilnojamo turto objektai"
description: "Kauno miesto \"Nekilnojamojo ilgalaikio turto informacinė sistema\" skirta turto valdymui, naudojimui ir disponavimui administruoti."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/ilgalaikis_nt_arch/NTObjektas"
tags: [gov, kauno_m_sav, ntobjektas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/ilgalaikis_nt_arch.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/ilgalaikis_nt_arch.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2803/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/ilgalaikis_nt_arch"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# NTObjektas — Kauno miesto nekilnojamo turto objektai

Kauno miesto "Nekilnojamojo ilgalaikio turto informacinė sistema" skirta turto valdymui, naudojimui ir disponavimui administruoti. Archyviniai duomenys ir naujinami nebus.[^manifest]

- **Model:** `datasets/gov/kauno_m_sav/ilgalaikis_nt_arch/NTObjektas`[^manifest]
- **Dataset:** [Kauno miesto nekilnojamo turto objektai](../ilgalaikis_nt_arch.md) (`datasets/gov/kauno_m_sav/ilgalaikis_nt_arch`)[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/ilgalaikis_nt_arch.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/ilgalaikis_nt_arch.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/ilgalaikis_nt_arch/NTObjektas` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `obj_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `obj_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `objekto_pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnija | — |
| `gatve` | `string` | — | `4` | `open` | — | Gatvė | — |
| `namo_nr` | `string` | — | `4` | `open` | — | Namo numeris | — |
| `unikalusis_nr` | `string` | — | `4` | `open` | — | Objekto unikalus numeris | — |
| `inventorinis_nr` | `string` | — | `4` | `open` | — | Inventorinis numeris | — |
| `valdoma_dalis` | `string` | — | `4` | `open` | — | Valdomos dalies duomenys | — |
| `valdomas_plotas` | `number` | — | `4` | `open` | — | Valdomo ploto duomenys | — |
| `kategorija` | `string` | — | `4` | `open` | — | Objekto kategorija | — |
| `savivinkas` | `string` | — | `4` | `open` | — | Objekto savininkas | — |
| `turto_paskirtis` | `string` | — | `4` | `open` | — | Nekilnojamojo turto paskirtis | — |
| `naudojimo_sritis` | `string` | — | `4` | `open` | — | Objekto naudojimo sritis | — |
| `valdymo_forma` | `string` | — | `4` | `open` | — | Objekto valdymo informacoja | — |
| `busena` | `string` | — | `4` | `open` | — | Objekto būsena | — |
| `arhyvinis` | `string` | — | `4` | `open` | — | Archyvinio objekto identifikatorius | — |
| `arch_data` | `date` | `D` | `4` | `open` | — | Objekto perkėlimo į archyvą data | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Duomenų atnaujinimo data (vda) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/ilgalaikis_nt_arch.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/ilgalaikis_nt_arch.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/ilgalaikis_nt_arch (https://data.gov.lt/datasets/2803/)
