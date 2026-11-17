---
type: Table
title: "Kandidatas — Kauno miesto savivaldybės seniūnaičių rinkimų rezultatai"
description: "Duomenų rinkinyje pateikiami Kauno miesto savivaldybės nuo 2023 m. organizuotų seniūnaičių rinkimų 56 seniūnaitijose rezultatai."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/seniunaiciai/Kandidatas"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/rinkimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/rinkimai.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kandidatas — Kauno miesto savivaldybės seniūnaičių rinkimų rezultatai

Duomenų rinkinyje pateikiami Kauno miesto savivaldybės nuo 2023 m. organizuotų seniūnaičių rinkimų 56 seniūnaitijose rezultatai. Seniūnaičių rinkimai vyksta kas ketverius metus ir yra organizuojami Kauno miesto savivaldybės seniūnaičių rinkimų komisijos pagal administracijos direktoriaus parengtą tvarkos aprašą (https://www.e-tar.lt/portal/lt/legalAct/08e28540a29211ebb9bbd96a0c51af2c/asr). Seniūnaitis – tai bendruomenės atstovas, dirbantis visuomeniniais pagrindais. Kandidatus į seniūnaičius kelia seniūnaitijos gyventojai ir veikiančios bendruomeninės organizacijos. Savo balsą rinkimuose gali išreikšti pilnamečiai seniūnaitijos gyventojai, turintys teisę rinkti Savivaldybės tarybą, balsuodami seniūnijos patalpose arba internetu per tris rinkimų dienas. Dėl šios priežasties rinkimų rezultatai atvaizduojami pagal rinkimų dieną ir kandidatą. Rinkinyje taip pat pateikiama su kandidatu susijusi informacija: kandidatavimo data, kas iškėlė kandidatą ir kandidato identifikatorius, gaunamas užšifravus vardą ir pavardę.

- **Model:** `datasets/gov/kauno_m_sav/seniunaiciai/Kandidatas`[^manifest]
- **Dataset:** [Kauno miesto savivaldybės seniūnaičių rinkimų rezultatai](../seniunaiciai.md) (`datasets/gov/kauno_m_sav/seniunaiciai`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/rinkimai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/rinkimai.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/seniunaiciai/Kandidatas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros unikalus įrašo identifikatorius | — |
| `rinkimu_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `seniunaitija` | `string` | — | `4` | `open` | — | Seniūnaitijos pavadinimas | — |
| `kandidatavimo_data` | `date` | `D` | `4` | `open` | — | Kandidatavimo data | — |
| `kandidatas` | `string` | — | `4` | `open` | — | Kandidato identifikatorius, sudarytas užšifravus kandidato vardą ir pavardę. | — |
| `iskele_lt` | `string` | — | `1` | `open` | — | Sąlygos, kuriomis kandidatas buvo pasiūlytas į seniūnaičius | — |
| `ar_isrinko` | `boolean` | — | `4` | `open` | — | Požymis, ar kandidatas buvo išrinktas į seniūnaičius rinkimų metu | — |
| `viso_balsu` | `integer` | — | `4` | `open` | — | Bendras kandidato surinktų balsų skaičius | — |
| `balsai_internetu_1` | `integer` | — | `4` | `open` | — | Kandidatas į seniūnaitį gavo balsų internetu pirmą balsavimo dieną | — |
| `balsai_seniunijoje_1` | `integer` | — | `4` | `open` | — | Kandidatas į seniūnaitį gavo balsų seniūnijoje pirmą balsavimo dieną | — |
| `balsai_internetu_2` | `integer` | — | `4` | `open` | — | Kandidatas į seniūnaitį gavo balsų internetu antrą balsavimo dieną | — |
| `balsai_seniunijoje_2` | `integer` | — | `4` | `open` | — | Kandidatas į seniūnaitį gavo balsų seniūnijoje antrą balsavimo dieną | — |
| `balsai_internetu_3` | `integer` | — | `4` | `open` | — | Kandidatas į seniūnaitį gavo balsų internetu trečią balsavimo dieną | — |
| `balsai_seniunijoje_3` | `integer` | — | `4` | `open` | — | Kandidatas į seniūnaitį gavo balsų seniūnijoje trečią balsavimo dieną | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iskele_lt` | `update(property: "iskele_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/rinkimai.csv
