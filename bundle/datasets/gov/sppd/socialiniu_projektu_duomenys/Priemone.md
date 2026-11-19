---
type: Table
title: "Priemone — Priemonių skirtų projektams įgyvendinti duomenys"
description: "Lentelėse pateikti Socialinių priežiūros paslaugų departamento projektų, priemonių projektams įgyvendinti bei projektų išlaidų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys/Priemone"
tags: [gov, sppd, priemone, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L52"
    title: "atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L52"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2908/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sppd/socialiniu_projektu_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Priemone — Priemonių skirtų projektams įgyvendinti duomenys

**Dataset Context:** Lentelėse pateikti Socialinių priežiūros paslaugų departamento projektų, priemonių projektams įgyvendinti bei projektų išlaidų duomenys. Projektų duomenys pateikiami nuo momento, kai paraiškos tampa aktualios tikrinimo procesui. Projektų išlaidų duomenys yra klasifikuojami pagal Lietuvos Respublikos valstybės ir savivaldybių biudžetų pajamų ir išlaidų klasifikatorių. Rinkinys sudarytas Valstybės duomenų agentūros. Projektų lentelės viena eilutė atitinka vieną paraišką, teiktą institucijos priemonės lėšoms gauti, priemonių lentelės – tam tikrą priemonę, skirtą projektui įgyvendinti, o projektų išlaidų lentelės – pinigų išleidimo faktą, susijusį su projektu. Atkreipiame dėmesį, kad duomenų eilutės yra nuolatos pildomos, o informacija jose yra tikslinama. Taip pat pažymime, kad įstaiga išlaidų duomenis suveda kas ketvirtį, todėl paskutinio mokėjimo data gali neatitikti realios paskutinio mokėjimo datos. Duomenys apima visoje Lietuvoje išsidėsčiusias organizacijas. Duomenų laiko aprėptis – nuo 2019 m. sausio 1d. Duomenų teikėjas – Socialinių priežiūros paslaugų departamentas prie Socialinės apsaugos ir darbo ministerijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/sppd/socialiniu_projektu_duomenys/Priemone`[^manifest]
- **Dataset:** [Socialinių projektu duomenys](../socialiniu_projektu_duomenys.md) (`datasets/gov/sppd/socialiniu_projektu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L52](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L52)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys/Priemone` (`deployed`)[^manifest]
- **Provider:** `sppd` — Socialinių paslaugų priežiūros departamentas prie SADM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `priemones_id` | `string` | — | `4` | `open` | — | Unikalus priemonės identifikatorius | Priemonei priskirta id reikšmė kuri unikaliai identifikuoja eilutę lentelėje |
| `priemones_kodas` | `string` | — | `4` | `open` | — | Priemonės kodas | Priemonės kodas kuris įeina į projekto kodo sudarymą |
| `pavadinimas` | `string` | — | `4` | `open` | — | Priemonės pavadinimas | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Priemonės aprašymas | Keli sakiniai apie priemonę |
| `tikslas` | `string` | — | `4` | `open` | — | Priemonės tikslas | Priemone siekiamas įgyvendinti uždavinys |
| `paskirtas_biudzetas` | `number` | — | `4` | `open` | — | Priemonės paskirtas biudžetas | Paskirtas biudžetas kuris išskirstomas kiekvienam projektui |
| `paraiskos_teikimo_nuo_data` | `date` | `D` | `4` | `open` | — | Paraiškų teikimo pradžios data | — |
| `paraiskos_teikimo_iki_data` | `date` | `D` | `4` | `open` | — | Paraiškų teikimo pabaigos data | — |
| `vykdymo_nuo_data` | `date` | `D` | `4` | `open` | — | Projektų su šia priemonė vykdymo pradžios data | — |
| `vykdymo_iki_data` | `date` | `D` | `4` | `open` | — | Projektų su šia priemonė vykdymo pabaigos data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paskirtas_biudzetas` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L52 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L52)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sppd/socialiniu_projektu_duomenys (https://data.gov.lt/datasets/2908/)
