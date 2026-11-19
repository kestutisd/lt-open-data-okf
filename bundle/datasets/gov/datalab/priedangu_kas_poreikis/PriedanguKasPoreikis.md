---
type: Table
title: "PriedanguKasPoreikis — Priedangų KAS poreikis"
description: "Spinta table datasets/gov/datalab/priedangu_kas_poreikis/PriedanguKasPoreikis (25 columns)."
resource: "https://get.data.gov.lt/datasets/gov/datalab/priedangu_kas_poreikis/PriedanguKasPoreikis"
tags: [gov, datalab, priedangukasporeikis, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/priedangu_kas_poreikis.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/datalab/priedangu_kas_poreikis.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3913/"
    title: "data.gov.lt DCAT-AP — datasets/gov/datalab/priedangu_kas_poreikis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PriedanguKasPoreikis — Priedangų KAS poreikis

- **Model:** `datasets/gov/datalab/priedangu_kas_poreikis/PriedanguKasPoreikis`[^manifest]
- **Dataset:** [Priedangų KAS poreikis](../priedangu_kas_poreikis.md) (`datasets/gov/datalab/priedangu_kas_poreikis`)[^manifest]
- **Manifest CSV:** [datasets/gov/datalab/priedangu_kas_poreikis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/priedangu_kas_poreikis.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/datalab/priedangu_kas_poreikis/PriedanguKasPoreikis` (`deployed`)[^manifest]
- **Provider:** `datalab` — Valstybės duomenų agentūra (DataLab) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `administracine_teritorija_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `administracine_teritorija_id` | `string` | — | `4` | `open` | — | Administracinės teritorijos unikalus identifikatorius | — |
| `administracine_teritorija` | `string` | — | `4` | `open` | — | Administracinės teritorijos pavadinimas | — |
| `kaimas_population` | `integer` | — | `4` | `open` | — | Gyventojų skaičius kaimo vietovėse | — |
| `miestas_population` | `integer` | — | `4` | `open` | — | Gyventojų skaičius miesto vietovėse | — |
| `miestas_proporcija` | `number` | — | `4` | `open` | — | Miesto gyventojų dalis nuo bendro gyventojų skaičiaus | — |
| `miestas_ir_kaimas_population` | `integer` | — | `4` | `open` | — | Bendras miesto ir kaimo gyventojų skaičius | — |
| `laikotarpis` | `string` | — | `4` | `open` | — | Duomenų laikotarpis | — |
| `koeficientas` | `number` | — | `4` | `open` | — | Skaičiavimuose naudojamas koeficientas | — |
| `priedangos_atitinka_reikalavimus` | `boolean` | — | `4` | `open` | — | Ar atitinka reikalavimus | — |
| `priedangos_reikalingas_plotas` | `number` | — | `4` | `open` | — | Reikalingas priedangos plotas gyventojams (kv. m) | — |
| `priedangos_poreikis` | `number` | — | `4` | `open` | — | Priedangos poreikis | — |
| `priedangos_plotas` | `number` | — | `4` | `open` | — | Priedangos plotas | — |
| `priedangos_poreikio_patenkinimas` | `number` | — | `4` | `open` | — | Priedangos poreikio patenkinimas | — |
| `kas_g_b` | `integer` | — | `4` | `open` | — | Bendras gyventojų skaičius, kuriems reikalingos KAS (kolektyvinės apsaugos statiniai) | — |
| `kas_g_b_25` | `integer` | — | `4` | `open` | — | 25% prioritetinių gyventojų dalis, kuriems būtini KAS | — |
| `kas_g` | `integer` | — | `4` | `open` | — | Gyventojų skaičius, kuriems realiai skirta KAS | — |
| `kas_plotas` | `number` | — | `4` | `open` | — | Bendras esamas plotas (kv. m) | — |
| `kas_poreikis_kv_m` | `number` | — | `4` | `open` | — | Reikalingas plotas (kv. m) | — |
| `kas_atitinka_reikalavimus` | `boolean` | — | `4` | `open` | — | Ar esamas plotas atitinka reikalavimus | — |
| `kas_skirtumas` | `number` | — | `4` | `open` | — | Skirtumas tarp esamo ir reikalingo KAS ploto (kv. m) | — |
| `kas_poreikio_patenkinimas` | `number` | — | `4` | `open` | — | KAS poreikio patenkinimo lygi | — |
| `kas_g_n` | `integer` | — | `4` | `open` | — | Gyventojų skaičius, kuriems KAS neprieinami | — |
| `kas_g_v` | `integer` | — | `4` | `open` | — | Gyventojų skaičius, turinčių prieigą prie visaverčių KAS | — |
| `kas_g_s` | `integer` | — | `4` | `open` | — | Gyventojų skaičius, turinčių prieigą prie sąlyginai tinkamų KAS | — |
| `priedangos_kas_atitinka_reikalavimus` | `boolean` | — | `4` | `open` | — | Ar atitinka reikalavimus | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/datalab/priedangu_kas_poreikis.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/priedangu_kas_poreikis.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/datalab/priedangu_kas_poreikis (https://data.gov.lt/datasets/3913/)
