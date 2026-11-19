---
type: Table
title: "SveikatingumoUgdymas — Sveikatos, lytiškumo ugdymo ir rengimo šeimai bendrosios programos bei kenksmingų ir psichiką veikiančių medžiagų prevencijos programos vykdymas švietimo įstaigose"
description: "Viena eilutė atitinka programos įvykdymą švietimo įstaigoje atitinkamais mokslo metais."
resource: "https://get.data.gov.lt/datasets/gov/nsa/svis/prevencines_programos/SveikatingumoUgdymas"
tags: [gov, nsa, sveikatingumougdymas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/prevencines_programos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/nsa/svis/prevencines_programos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3890/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/svis/prevencines_programos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# SveikatingumoUgdymas — Sveikatos, lytiškumo ugdymo ir rengimo šeimai bendrosios programos bei kenksmingų ir psichiką veikiančių medžiagų...

Viena eilutė atitinka programos įvykdymą švietimo įstaigoje atitinkamais mokslo metais.[^manifest]

- **Model:** `datasets/gov/nsa/svis/prevencines_programos/SveikatingumoUgdymas`[^manifest]
- **Dataset:** [Prevencinių programų vykdymas švietimo įstaigose](../prevencines_programos.md) (`datasets/gov/nsa/svis/prevencines_programos`)[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/svis/prevencines_programos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/prevencines_programos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/svis/prevencines_programos/SveikatingumoUgdymas` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus pirminis raktas | — |
| `mokslo_metai` | `string` | — | `4` | `open` | — | Mokslo metai | — |
| `padalinio_grupe` | `string` | — | `4` | `open` | — | Padalinio grupė | — |
| `padalinio_priklausomybe` | `string` | — | `4` | `open` | — | Padalinio priklausomybė | — |
| `padalinio_savivaldybe` | `string` | — | `4` | `open` | — | Padalinio savivaldybė | — |
| `padalinio_pavadinimas` | `string` | — | `4` | `open` | — | Padalinio pavadinimas | — |
| `padalinio_kodas` | `string` | — | `4` | `open` | — | Padalinio kodas | — |
| `programos_kodas` | `string` | — | `4` | `open` | — | Programos kodas | — |
| `programos_pavadinimas` | `string` | — | `4` | `open` | — | Programos pavadinimas | — |
| `integr_mok_dal` | `boolean` | — | `4` | `open` | — | Programa integruojama į mokomųjų dalykų programų turinį | — |
| `spec_kurs_pasir` | `boolean` | — | `4` | `open` | — | Yra įvestas specialus kursas kaip pasirenkamasis dalykas kuriai nors klasei | — |
| `pap_ugd` | `boolean` | — | `4` | `open` | — | Yra integruojama į papildomą ugdymą | — |
| `neform_sviet` | `boolean` | — | `4` | `open` | — | Yra integruojama į neformaliojo švietimo programas | — |
| `klases_val` | `boolean` | — | `4` | `open` | — | Yra integruojama į klasės valandėles | — |
| `kitos_progr` | `boolean` | — | `4` | `open` | — | Yra integruojama į kitas programas | — |
| `kitu_budu` | `boolean` | — | `4` | `open` | — | Programa vykdoma kitu mokyklos pasirinktu būdu | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `padalinio_priklausomybe` | `"Savivaldybės"` | — | — | Savivaldybės | — |
| `padalinio_priklausomybe` | `"Nevalstybinė"` | — | — | Nevalstybinė | — |
| `padalinio_priklausomybe` | `"Valstybinė"` | — | — | Valstybinė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/svis/prevencines_programos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/prevencines_programos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/svis/prevencines_programos (https://data.gov.lt/datasets/3890/)
