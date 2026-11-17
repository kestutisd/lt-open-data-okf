---
type: Dataset
title: "Socialinių projektu duomenys"
description: "Lentelėse pateikti Socialinių priežiūros paslaugų departamento projektų, priemonių projektams įgyvendinti bei projektų išlaidų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys"
tags: [gov, sppd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Socialinių projektu duomenys

Lentelėse pateikti Socialinių priežiūros paslaugų departamento projektų, priemonių projektams įgyvendinti bei projektų išlaidų duomenys. Projektų duomenys pateikiami nuo momento, kai paraiškos tampa aktualios tikrinimo procesui. Projektų išlaidų duomenys yra klasifikuojami pagal Lietuvos Respublikos valstybės ir savivaldybių biudžetų pajamų ir išlaidų klasifikatorių. Rinkinys sudarytas Valstybės duomenų agentūros. Projektų lentelės viena eilutė atitinka vieną paraišką, teiktą institucijos priemonės lėšoms gauti, priemonių lentelės – tam tikrą priemonę, skirtą projektui įgyvendinti, o projektų išlaidų lentelės – pinigų išleidimo faktą, susijusį su projektu. Atkreipiame dėmesį, kad duomenų eilutės yra nuolatos pildomos, o informacija jose yra tikslinama. Taip pat pažymime, kad įstaiga išlaidų duomenis suveda kas ketvirtį, todėl paskutinio mokėjimo data gali neatitikti realios paskutinio mokėjimo datos. Duomenys apima visoje Lietuvoje išsidėsčiusias organizacijas. Duomenų laiko aprėptis – nuo 2019 m. sausio 1d. Duomenų teikėjas – Socialinių priežiūros paslaugų departamentas prie Socialinės apsaugos ir darbo ministerijos.

- **Namespace:** `datasets/gov/sppd/socialiniu_projektu_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys`
- **Parent Namespace (`ns`):** Socialinių paslaugų priežiūros departamentas prie SADM (`datasets/gov/sppd`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Projektas](socialiniu_projektu_duomenys/Projektas.md) | Organizacijų bei socialinių projektų duomenys | `4` | `vda_id` | — | 26 | — |
| [Priemone](socialiniu_projektu_duomenys/Priemone.md) | Priemonių skirtų projektams įgyvendinti duomenys | `4` | `vda_id` | — | 11 | — |
| [ProjektoPirkimas](socialiniu_projektu_duomenys/ProjektoPirkimas.md) | Projekto išlaidų duomenys | `4` | `vda_id` | — | 8 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv
