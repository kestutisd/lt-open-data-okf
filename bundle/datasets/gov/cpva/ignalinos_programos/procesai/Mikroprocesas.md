---
type: Table
title: "Mikroprocesas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ mikroprocesų sąrašas"
description: "Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu."
resource: "https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai/Mikroprocesas"
tags: [gov, cpva, mikroprocesas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L29"
    title: "atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv#L29"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3838/"
    title: "data.gov.lt DCAT-AP — datasets/gov/cpva/ignalinos_programos/procesai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Mikroprocesas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ mikroprocesų...

**Dataset Context:** Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu. Duomenys pateikiami iš Projektų valdymo informacinės sistemos „Apecs“, skirtos automatizuotai valdyti Ignalinos programos procesus ir kontrolės sistemą. Procesai suskirstyti į 3 kategorijas – procesus, subprocesus ir mikroprocesus, kurie ir pateikiami rinkinio atskirose 3-se lentelėse. „Procesas“ yra pati stambiausia procesų hierarchijos dalis. Jam priklauso subprocesai, o savo ruožtu, subprocesams priklauso mikroprocesai. Lentelės tarpusavyje jungiasi: mikroprocesai su subprocesais – mikroprocesai.priklauso_subprocesui = subprocesai.id; subrocesai su procesais – subprocesai.priklauso_procesui = procesai.id Duomenų atnaujinimas numatomas kas 3 mėn. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/cpva/ignalinos_programos/procesai/Mikroprocesas`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys](../procesai.md) (`datasets/gov/cpva/ignalinos_programos/procesai`)[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/ignalinos_programu_procesai.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L29)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai/Mikroprocesas` (`deployed`)[^manifest]
- **Provider:** `cpva` — VšĮ Centrinė projektų valdymo agentūra *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Mikroproceso identifikatorius | — |
| `priklauso_subprocesui` | `string` | — | `4` | `open` | — | Priklauso subprocesui | — |
| `mikroproceso_tipas` | `string` | — | `4` | `open` | — | Mikroproceso tipas | — |
| `mikroprocesas` | `string` | — | `4` | `open` | — | Mikroproceso pavadinimas | — |
| `mikroproceso_kodas` | `string` | — | `4` | `open` | — | Mikroproceso kodas | — |
| `mikroproceso_sukurimo_data` | `datetime` | `L` | `4` | `open` | — | Mikroproceso sukūrimo data | — |
| `atlikti_iki` | `datetime` | `L` | `4` | `open` | — | Mikroprocesą reikia atliki iki | — |
| `mikroproceso_kurejas` | `string` | — | `4` | `open` | — | Mikroproceso kūrėjo id | — |
| `statusas` | `string` | — | `4` | `open` | — | Mikroproceso statusas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv#L29 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L29)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/cpva/ignalinos_programos/procesai (https://data.gov.lt/datasets/3838/)
