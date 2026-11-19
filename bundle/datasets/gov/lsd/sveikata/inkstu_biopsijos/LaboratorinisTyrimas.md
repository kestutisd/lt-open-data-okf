---
type: Table
title: "LaboratorinisTyrimas — Laboratorinių tyrimų duomenys"
description: "\"Pacientų inkstų funkciją apibūdinantys laboratoriniai tyrimai (kreatininas serume, glomerulų filtracijos greitis, albumino-kreatinino santykis šlapime), jų atlikimo data, tyrimo ir analitės pavadinimai, analitės rezultatai, apatiniai, viršutiniai normos rėžiai bei matavimo..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/LaboratorinisTyrimas"
tags: [gov, lsd, laboratorinistyrimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L64"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L64"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4573/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/inkstu_biopsijos"
    author: "team:vda"
    last_modified: "2026-03-17T00:00:00Z"
---

# LaboratorinisTyrimas — Laboratorinių tyrimų duomenys

"Pacientų inkstų funkciją apibūdinantys laboratoriniai tyrimai (kreatininas serume, glomerulų filtracijos greitis, albumino-kreatinino santykis šlapime), jų atlikimo data, tyrimo ir analitės pavadinimai, analitės rezultatai, apatiniai, viršutiniai normos rėžiai bei matavimo vienetai."[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/inkstu_biopsijos/LaboratorinisTyrimas`[^manifest]
- **Dataset:** ["Pacientų, kuriems atlikta inkstų biopsija, duomenys"](../inkstu_biopsijos.md) (`datasets/gov/lsd/sveikata/inkstu_biopsijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L64](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L64)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/LaboratorinisTyrimas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-03-17`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | "Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius sudarytas iš stulpelių - asmens_kodas, tyrimo_data, tyr_pavadinimas, tyrimo_analite, analites_rezultatas" |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `tyrimo_data` | `date` | `D` | `4` | `open` | — | Laboratorinio tyrimo atlikimo data | — |
| `tyr_pavadinimas` | `string` | — | `4` | `open` | — | Tyrimo pavadinimas | — |
| `tyrimo_analite` | `string` | — | `4` | `open` | — | Tyrimo analitė | — |
| `analites_rezultatas` | `number` | — | `4` | `open` | — | Analitės rezultatas | — |
| `analites_norma_nuo` | `number` | — | `4` | `open` | — | Apatiniai normos rėžiai | — |
| `analites_norma_iki` | `number` | — | `4` | `open` | — | Viršutiniai normos rėžiai | — |
| `matavimo_vienetai` | `string` | — | `4` | `open` | — | Matavimo vienetai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L64 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L64)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/inkstu_biopsijos (https://data.gov.lt/datasets/4573/)
