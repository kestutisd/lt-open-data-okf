---
type: Table
title: "VilkaviskioLigonine — Vilkaviškio ligoninės pacientams atlikti radiologiniai tyrimai"
description: "Informacinėje sistemoje „JiveX“ kaupiami Vilkaviškio ligoninės pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/VilkaviskioLigonine"
tags: [gov, radiologija, vilkaviskioligonine, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L642"
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L642"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2762/"
    title: "data.gov.lt DCAT-AP — datasets/gov/radiologija"
    author: "team:vda"
    last_modified: "2026-10-26T00:00:00Z"
---

# VilkaviskioLigonine — Vilkaviškio ligoninės pacientams atlikti radiologiniai tyrimai

Informacinėje sistemoje „JiveX“ kaupiami Vilkaviškio ligoninės pacientams atliktų radiologinių tyrimų duomenys. Rinkinyje pateikti duomenys yra nuo 2009 m. sausio mėnesio ir atnaujinami kasdien. Vienas įrašas atitinka vieną tyrimo seriją (visų tyrimo serijų identifikatoriai unikalūs). Duomenų rinkinį sudaro: paciento pseudonimizuotas identifikatorius, lytis, gimimo metai, tyrimo studijos identifikatorius ir data, tyrimo serijos identifikatorius ir data, paciento kūno padėtis, tirta kūno dalis, tyrimo serijos modalumas ir protokolas. Pacientų gimimo metai paimti iš galiojančių asmens kodų, o, jeigu asmens kodas negalioja – iš gimimo datos stulpelio. Duomenų teikėjas – VšĮ Vilkaviškio ligoninė. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/radiologija/VilkaviskioLigonine`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L642](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L642)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/VilkaviskioLigonine` (`deployed`)[^manifest]
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
| `tyrimo_serijos_protokolas` | `string` | — | `4` | `open` | — | Tyrimo serijos protokolas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"M"` | — | — | Moteris | — |
| `paciento_lytis` | `"V"` | — | — | Vyras | — |
| `paciento_lytis` | `"K"` | — | — | Kita | — |
| `tyrimo_serijos_modalumas` | `"CR"` | — | — | Kompiuterinė radiografija | — |
| `tyrimo_serijos_modalumas` | `"CT"` | — | — | Kompiuterinė tomografija | — |
| `tyrimo_serijos_modalumas` | `"MG"` | — | — | Mamografija | — |
| `tyrimo_serijos_modalumas` | `"DX"` | — | — | Skaitmeninė radiografija | — |
| `tyrimo_serijos_modalumas` | `"SR"` | — | — | SR dokumentas | — |
| `tyrimo_serijos_modalumas` | `"SC"` | — | — | Nežinoma | — |
| `tyrimo_serijos_modalumas` | `"PR"` | — | — | Prezentacijos būsena | — |
| `tyrimo_serijos_modalumas` | `"DOC"` | — | — | Dokumentas | — |
| `tyrimo_serijos_modalumas` | `"OT"` | — | — | Kita | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L642 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L642)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/radiologija (https://data.gov.lt/datasets/2762/)
