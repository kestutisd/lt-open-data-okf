---
type: Table
title: "Uzmokestis — Rinkiminių komisijų nariams skirtas darbo užmokestis"
description: "Vyriausiosios rinkimų komisijos Sąmatų, darbo užmokesčio ir buhalterinės apskaitos posistemėje nuo 2011-12-19 kaupiami ir iki šiol atnaujinami rinkimų komisijų nariams skirtų mokėjimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vrk/mokejimai_komisiju_nariams/Uzmokestis"
tags: [gov, vrk, uzmokestis, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2807/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vrk/mokejimai_komisiju_nariams"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Uzmokestis — Rinkiminių komisijų nariams skirtas darbo užmokestis

Vyriausiosios rinkimų komisijos Sąmatų, darbo užmokesčio ir buhalterinės apskaitos posistemėje nuo 2011-12-19 kaupiami ir iki šiol atnaujinami rinkimų komisijų nariams skirtų mokėjimų duomenys. Duomenų rinkinys sudarytas iš mokejimo ir jo eilutės identifikatorių, vykdomų rinkimų identifikatoriaus ir pavadinimo, mokėjimo ir jo eilutės datų, mokėjimo būsenos, pseudonimizuoto komisijos nario identifikatoriaus, pareigų, apygardos, kurioje dirba, identifikatoriaus ir pavadinimo bei mokėjimo sumos. Vienas įrašas atitinka vieno mokėjimo eilutę vienam asmeniui. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vrk/mokejimai_komisiju_nariams/Uzmokestis`[^manifest]
- **Dataset:** [Rinkiminių komisijų nariams skirtas darbo užmokestis](../mokejimai_komisiju_nariams.md) (`datasets/gov/vrk/mokejimai_komisiju_nariams`)[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/mokejimai_komisiju_nariams/Uzmokestis` (`deployed`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `mokejimo_id` | `string` | — | `4` | `open` | — | Mokėjimo identifikatorius | — |
| `mokejimo_eil_id` | `string` | — | `4` | `open` | — | Mokėjimo eilutės identifikatorius | — |
| `vr_id` | `string` | — | `4` | `open` | — | Vykdomų rinkimų identifikatorius | — |
| `rinkimu_pav` | `string` | — | `4` | `open` | — | Vykdomų rinkimų pavadinimas | — |
| `mokejimo_data` | `datetime` | `S` | `4` | `open` | — | Mokėjimo data ir laikas | — |
| `mokejimo_eil_data` | `datetime` | `S` | `4` | `open` | — | Mokėjimo eilutės data ir laikas | — |
| `mokejimo_busena` | `string` | — | `4` | `open` | — | Mokėjimo būsena | — |
| `komisijos_nario_id` | `string` | — | `4` | `open` | — | Komisijos nario pseudonimizuotas identifikatorius | — |
| `komisijos_nario_apygardos_id` | `string` | — | `4` | `open` | — | Komisijos nario apygardos identifikatorius | — |
| `komisijos_nario_apygardos_pav` | `string` | — | `4` | `open` | — | Komisijos nario apygardos pavadinimas | — |
| `komisijos_nario_pareigos` | `string` | — | `4` | `open` | — | Komisijos nario pareigos | — |
| `mokejimo_suma` | `number` | — | `4` | `open` | — | Mokėjimo suma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/mokejimai_komisiju_nariams.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vrk/mokejimai_komisiju_nariams (https://data.gov.lt/datasets/2807/)
