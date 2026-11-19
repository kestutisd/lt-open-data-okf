---
type: Table
title: "RespublikinePanevezioLigonine — Respublikinėje Panevėžio ligoninės pacientams atlikti radiologiniai tyrimai"
description: "Informacinėje sistemoje „JiveX“ kaupiami Respublikinės Panevėžio ligoninės pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/RespublikinePanevezioLigonine"
tags: [gov, radiologija, respublikinepanevezioligonine, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L99"
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L99"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2762/"
    title: "data.gov.lt DCAT-AP — datasets/gov/radiologija"
    author: "team:vda"
    last_modified: "2026-10-26T00:00:00Z"
---

# RespublikinePanevezioLigonine — Respublikinėje Panevėžio ligoninės pacientams atlikti radiologiniai tyrimai

Informacinėje sistemoje „JiveX“ kaupiami Respublikinės Panevėžio ligoninės pacientams atliktų radiologinių tyrimų duomenys. Duomenų rinkinyje pateikiami duomenys nuo 1998 metų. Vienas įrašas atitinka vieną tyrimo seriją (visų tyrimo serijų identifikatoriai unikalūs). Duomenų rinkinį sudaro: paciento pseudonimizuotas identifikatorius, lytis, gimimo metai, tyrimo studijos identifikatorius ir data, tyrimo serijos identifikatorius ir data, paciento kūno padėtis, tirta kūno dalis, tyrimo serijos modalumas ir protokolas. Pacientų gimimo metai paimti iš validžių asmens kodų, jei asmens kodai nevalidūs – iš gimimo datos stulpelio. Duomenų teikėjas – VšĮ Respublikinė Panevėžio ligoninė. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/radiologija/RespublikinePanevezioLigonine`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L99](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L99)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/RespublikinePanevezioLigonine` (`deployed`)[^manifest]
- **Provider:** `radiologija`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-26`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Pseudonimizuotas paciento identifikatorius | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `tyrimo_studijos_id` | `string` | — | `4` | `open` | — | Tyrimo studijos identifikatorius | — |
| `tyrimo_studijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo studijos data | — |
| `tyrimo_serijos_id` | `string` | — | `4` | `open` | — | Tyrimo serijos identifikatorius | — |
| `tyrimo_serijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo serijos data | — |
| `paciento_kuno_padetis` | `string` | — | `4` | `open` | — | Paciento kūno padėtis tyrimo metu | — |
| `tirta_paciento_kuno_dalis` | `string` | — | `4` | `open` | — | Tirta paciento kūno dalis | — |
| `tyrimo_serijos_modalumas` | `string` | — | `4` | `open` | — | Tyrimo serijos modalumas | — |
| `tyrimo_serijos_protokolas` | `string` | — | `2` | `open` | — | Tyrimo serijos protokolas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"M"` | — | — | Moteris | — |
| `paciento_lytis` | `"V"` | — | — | Vyras | — |
| `paciento_lytis` | `"K"` | — | — | Kita | — |
| `paciento_lytis` | `"N"` | — | — | Nežinoma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L99 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L99)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/radiologija (https://data.gov.lt/datasets/2762/)
