---
type: Table
title: "Lakstas — ATA knygelės lakštai"
description: "Informacija apie muitinės postuose registruojamus ATA knygelių lakštus"
resource: "https://get.data.gov.lt/datasets/gov/muitine/ata_knygeles_lakstai/Lakstas"
tags: [gov, muitine, lakstas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/ata_knygeles_lakstai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/muitine/ata_knygeles_lakstai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2817/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/ata_knygeles_lakstai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lakstas — ATA knygelės lakštai

Informacija apie muitinės postuose registruojamus ATA knygelių lakštus[^manifest]

- **Model:** `datasets/gov/muitine/ata_knygeles_lakstai/Lakstas`[^manifest]
- **Dataset:** [ATA knygelės lakštai](../ata_knygeles_lakstai.md) (`datasets/gov/muitine/ata_knygeles_lakstai`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/ata_knygeles_lakstai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/ata_knygeles_lakstai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/ata_knygeles_lakstai/Lakstas` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `laksto_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `laksto_id` | `string` | — | `4` | `open` | — | ATA knygelės lakšto identifikatorius | — |
| `laksto_tipas` | `string` | — | `4` | `open` | — | ATA knygelės lakšto tipas | — |
| `laksto_galiojimo_data` | `date` | `D` | `4` | `open` | — | ATA knygelės lakšto galiojimo pabaigos data | — |
| `laksto_registracijos_data` | `date` | `D` | `4` | `open` | — | ATA knygelės lakšto registracijos data | — |
| `knygeles_id` | `string` | — | `4` | `open` | — | ATA knygelės identifikatorius | — |
| `knygeles_numeris` | `string` | — | `4` | `open` | — | ATA knygelės numeris | — |
| `knygeles_galiojimo_data` | `date` | `D` | `4` | `open` | — | ATA knygelės galiojimo pabaigos data | — |
| `asociacija_isdavusi_knygele` | `string` | — | `4` | `open` | — | Asociacija išdavusi ATA knygelę | — |
| `asociacijos_salis` | `string` | — | `4` | `open` | — | Šalis, kurioje įsisteigusi asociacija | — |
| `knygeles_pastabos` | `string` | — | `4` | `open` | — | Pastabos apie knygelę | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `laksto_tipas` | `"IMPORTAS"` | — | — | — | — |
| `laksto_tipas` | `"REEKSPORTAS"` | — | — | — | — |
| `laksto_tipas` | `"EKSPORTAS"` | — | — | — | — |
| `laksto_tipas` | `"REIMPORTAS"` | — | — | — | — |
| `laksto_tipas` | `"TRANZITAS"` | — | — | — | — |
| `knygeles_pastabos` | `"ATA knygelės dublikatas"` | — | — | — | — |
| `knygeles_pastabos` | `"Asociacijos išduota papildoma ATA knygelė"` | — | — | — | — |
| `knygeles_pastabos` | `"Asociacijos išduota antrinė (pakaitinė) ATA knygelė"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/ata_knygeles_lakstai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/ata_knygeles_lakstai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/ata_knygeles_lakstai (https://data.gov.lt/datasets/2817/)
