---
type: Table
title: "Dokumentas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Toltec“ duomenys"
description: "Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu."
resource: "https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/dokumentai/Dokumentas"
tags: [gov, cpva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_dokumentai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_dokumentai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dokumentas — VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Toltec“ duomenys

Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu. Duomenys pateikiami iš Projektų valdymo informacinės sistemos „Toltec“, skirtos rengti Ignalinos programos lėšomis finansuojamų viešųjų pirkimų dokumentus.

Rinkinį sudaro 1 lentelė apie sistemos pagalba sukurtus dokumentus. Viena eilutė atitinka vieną sukurtą dokumentą. Rinkinyje galima rasti tokią informaciją kaip dokumentą kūrusi įstaiga, dokumento pavadinimas, dokumento tipas, aktualios su dokumentu susijusios datos ir pan.

Duomenų atnaujinimas numatomas kas 3 mėn.

- **Model:** `datasets/gov/cpva/ignalinos_programos/dokumentai/Dokumentas`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys](../dokumentai.md) (`datasets/gov/cpva/ignalinos_programos/dokumentai`)
- **Manifest CSV:** [datasets/gov/cpva/ignalinos_programu_dokumentai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_dokumentai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/dokumentai/Dokumentas`
- **Primary Key (`ref`):** `document_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `document_id` | `string` | — | `4` | `open` | — | Dokumento identifikatorius | — |
| `istaiga` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `dok_pav_lt` | `string` | — | `4` | `open` | — | Pirkimo dokumento pavadinimas | — |
| `dok_tipas` | `string` | — | `4` | `open` | — | Pirkimo dokumento tipas | — |
| `sukurimo_data` | `datetime` | `L` | `4` | `open` | — | Įrašo sukūrimo data | — |
| `sukures_vartotojas` | `string` | — | `4` | `open` | — | Įrašą sukūrusio vartotojo identifikatorius | — |
| `patvirtinimo_data` | `datetime` | `L` | `4` | `open` | — | Pirkimo dokumento patvirtinimo data | — |
| `patvirtines_vartotojas` | `string` | — | `4` | `open` | — | Dokumentą patvirtinusio asmens naudotojo vardas | — |
| `statusas` | `string` | — | `4` | `open` | — | Statusas | — |
| `failu_skaicius` | `integer` | — | `4` | `open` | — | Failų skaičius dokumente | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_pav_lt` | `update(property: "dok_pav_lt@lt", type: "text")` | `type` | `4` | `open` | — | Pirkimo dokumento pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_dokumentai.csv
