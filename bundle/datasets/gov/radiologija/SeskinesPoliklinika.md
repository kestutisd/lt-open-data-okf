---
type: Table
title: "SeskinesPoliklinika — Šeškinės poliklinikos pacientams atlikti radiologiniai tyrimai"
description: "Šeškinės poliklinikos naudojamoje „MedDream“ IS kaupiami pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/SeskinesPoliklinika"
tags: [gov, radiologija, seskinespoliklinika, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L28"
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L28"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2762/"
    title: "data.gov.lt DCAT-AP — datasets/gov/radiologija"
    author: "team:vda"
    last_modified: "2026-10-26T00:00:00Z"
---

# SeskinesPoliklinika — Šeškinės poliklinikos pacientams atlikti radiologiniai tyrimai

Šeškinės poliklinikos naudojamoje „MedDream“ IS kaupiami pacientams atliktų radiologinių tyrimų duomenys. Kaupiamų duomenų aprėptis laike – nuo 2021 m., atnaujinant duomenis kasdien. Duomenų rinkinį sudaro: paciento pseudonimizuotas asmens kodas, tyrimo studijos identifikatorius ir data, paciento gimimo metai, lytis, svoris ir ūgis, tyrimo serijos identifikatorius, aprašymas ir modalumas, tirtos kūno dalies duomenys, medicininio atvaizdo identifikatorius, spinduliuotės dozė decigrėjais kvadratiniame centimetre, apšvita arksekundėmis ir fotometrinė interpretacija.[^manifest]

- **Model:** `datasets/gov/radiologija/SeskinesPoliklinika`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L28](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L28)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/SeskinesPoliklinika` (`deployed`)[^manifest]
- **Provider:** `radiologija`[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-26`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `paciento_asm_k` | `string` | — | `4` | `open` | — | Nuasmenintas paciento asmens kodas | — |
| `tyrimo_studijos_uuid` | `string` | — | `4` | `open` | — | Tyrimo studijos identifikatorius | — |
| `tyrimo_studijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo studijos data | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_svoris` | `number` | `kg` | `4` | `open` | — | Pacieno kūno svoris kilogramais | — |
| `paciento_ugis` | `number` | `m` | `4` | `open` | — | Paciento ūgis metrais | — |
| `tyrimo_serijos_uuid` | `string` | — | `4` | `open` | — | Tyrimo serijos identifikatorius | — |
| `tirta_kuno_dalis` | `string` | — | `4` | `open` | — | Tirta kūno dalis | — |
| `tyrimo_serijos_modalumas` | `string` | — | `4` | `open` | — | Tyrimo serijos modalumas | — |
| `tyrimo_serijos_aprasymas` | `string` | — | `4` | `open` | — | Tyrimo serijos aprašymas | — |
| `atvaizdo_uuid` | `string` | — | `4` | `open` | — | Atvaizdo unikalus identifikatorius | — |
| `apsvita` | `number` | `″` | `4` | `open` | — | Apšvita arksekundėmis | — |
| `spinduliuote` | `number` | `dGy/cm^2` | `4` | `open` | — | Spinduliuotė decigrėjais kvadratiniame centimetre | — |
| `fotometrine_interpretacija` | `string` | — | `4` | `open` | — | Fotometrinė interpretacija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"vyras"` | `V` | — | Vyras | — |
| `paciento_lytis` | `"moteris"` | `M` | — | Moteris | — |
| `paciento_lytis` | `"kita"` | `K` | — | Kita | — |
| `tyrimo_serijos_modalumas` | `"Skaitmeninė radiografija"` | `DX` | — | Skaitmeninė radiografija | — |
| `tyrimo_serijos_modalumas` | `"Mamografija"` | `MG` | — | Mamografija | — |
| `tyrimo_serijos_modalumas` | `"Panoraminis rentgenas"` | `PX` | — | Panoraminis rentgenas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L28 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L28)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/radiologija (https://data.gov.lt/datasets/2762/)
