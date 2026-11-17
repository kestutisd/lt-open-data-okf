---
type: Table
title: "Projektas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Medici“ projektų sąrašas"
description: "Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu."
resource: "https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/projektai/Projektas"
tags: [gov, cpva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_projektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_projektai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Projektas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Medici“ projektų sąrašas

Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu. Duomenys pateikiami iš Projektų valdymo informacinės sistemos „Medici“, skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su Ignalinos programos projektais.

Rinkinį sudaro 1 lentelė, kurioje pateikiamas užbaigtų projektų sąrašas. Rinkinyje galima rasti tokią informaciją kaip projektą vykdžiusi įstaiga, projekto pavadinimas, projekto tikslas, finansavimo būdai ir pan.

Duomenų atnaujinimas numatomas kas 3 mėn.

- **Model:** `datasets/gov/cpva/ignalinos_programos/projektai/Projektas`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys](../projektai.md) (`datasets/gov/cpva/ignalinos_programos/projektai`)
- **Manifest CSV:** [datasets/gov/cpva/ignalinos_programu_projektai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_projektai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/projektai/Projektas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `istaiga` | `string` | — | `4` | `open` | — | Naudos gavėjo įstaiga | — |
| `projekto_pav_en` | `string` | — | `3` | `open` | — | Projekto pavadinimas (angliškai) | — |
| `statusas` | `string` | — | `4` | `open` | — | Statusas | — |
| `tikslas_en` | `string` | — | `2` | `open` | — | Projekto tikslas (angliškai) | — |
| `sutarciu_kiekis` | `integer` | — | `4` | `open` | — | Sutarčių kiekis projekte | — |
| `finasavimo_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Finansavimo pasirašymo data | — |
| `finansavimas` | `boolean` | — | `4` | `open` | — | Ar skirtas finansavimas | — |
| `ek_pateikimo_data` | `date` | `D` | `4` | `open` | — | Europos komisijai pateikimo data | — |
| `ek_patvirtinimo_data` | `date` | `D` | `4` | `open` | — | Europos komisijos patvirtinimo data | — |
| `finansavimo_mechanizmas` | `string` | — | `4` | `open` | — | Finansavimo mechanizmas | — |
| `projekto_biudzetas` | `number` | — | `4` | `open` | — | Projekto biudžetas | — |
| `valiuta` | `string` | — | `4` | `open` | — | Valiuta | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `projekto_pav_en` | `update(property: "projekto_pav_en@en", type: "text")` | `type` | `3` | `open` | — | Projekto pavadinimas (angliškai) | — |
| `tikslas_en` | `update(property: "tikslas_en@en", type: "text")` | `type` | `3` | `open` | — | Projekto tikslas (angliškai) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_projektai.csv
