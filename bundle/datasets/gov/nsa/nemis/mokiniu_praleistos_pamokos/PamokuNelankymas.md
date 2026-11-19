---
type: Table
title: "PamokuNelankymas — Mokyklos nelankančių mokinių praleistos pamokos"
description: "Lentelėje pateikti mokyklos nelankančių mokinių praleistų pamokų skaičiai konkretiems mėnesiams iš Nacionalinės švietimo agentūros (NŠA) Nesimokančių vaikų ir mokyklos nelankančių mokinių informacinės sistemos (NEMIS)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos/PamokuNelankymas"
tags: [gov, nsa, pamokunelankymas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2863/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PamokuNelankymas — Mokyklos nelankančių mokinių praleistos pamokos

Lentelėje pateikti mokyklos nelankančių mokinių praleistų pamokų skaičiai konkretiems mėnesiams iš Nacionalinės švietimo agentūros (NŠA) Nesimokančių vaikų ir mokyklos nelankančių mokinių informacinės sistemos (NEMIS). Duomenys pateikiami nuo jų kaupimo sistemoje pradžios (2010 metų) atnaujinant kas mėnesį. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos/PamokuNelankymas`[^manifest]
- **Dataset:** [Mokyklos nelankančių mokinių praleistos pamokos](../mokiniu_praleistos_pamokos.md) (`datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos`)[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos/PamokuNelankymas` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `mok_id` | `string` | — | `4` | `open` | — | Mokinio identifikatorius | — |
| `ak_gim_metai` | `date` | `Y` | `4` | `open` | — | Mokinio gimimo metai (iš asmens kodo) | — |
| `ak_lytis` | `string` | — | `4` | `open` | — | Mokinio lytis (iš asmens kodo) | — |
| `nel_metai` | `string` | — | `4` | `open` | — | Mokyklos nelankymo metai | — |
| `nel_menuo` | `string` | — | `4` | `open` | — | Mokyklos nelankymo mėnuo | — |
| `nel_metai_menuo` | `date` | `M` | `4` | `open` | — | Mokyklos nelankymo metai ir mėnuo | — |
| `nel_pralei_pamoku_skcs` | `number` | `U` | `4` | `open` | — | Praleistų pamokų skaičius | — |
| `nel_priez_lt` | `string` | — | `4` | `open` | — | Mokyklos nelankymo priežastys | — |
| `nel_datak` | `string` | — | `4` | `open` | — | įrašo koregavimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ak_lytis` | `"Vyras"` | — | — | Vyras | — |
| `ak_lytis` | `"Moteris"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nel_priez_lt` | `update(property: "nel_priez_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/nemis/mokiniu_praleistos_pamokos (https://data.gov.lt/datasets/2863/)
