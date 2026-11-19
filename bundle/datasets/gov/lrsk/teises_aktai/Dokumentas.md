---
type: Table
title: "Dokumentas — Teisės aktų registro duomenys"
description: "Pateikiami duomenys apie teisės aktų objektus, juos parengusius ir priėmusius subjektus, identifikacinius kodus, objektų rūšis, pavadinimus ir jų chronologijas (teisės akto priėmimo data, registravimo Registre data, paskelbimo data, įsigaliojimo data, pakeitimo ar papildymo..."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai/Dokumentas"
tags: [gov, lrsk, dokumentas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/teises_aktai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2613/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/teises_aktai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Dokumentas — Teisės aktų registro duomenys

Pateikiami duomenys apie teisės aktų objektus, juos parengusius ir priėmusius subjektus, identifikacinius kodus, objektų rūšis, pavadinimus ir jų chronologijas (teisės akto priėmimo data, registravimo Registre data, paskelbimo data, įsigaliojimo data, pakeitimo ar papildymo data, pripažinimo netekusiu galios data, galiojimo sustabdymo data, galiojimo terminas).[^manifest]

- **Model:** `datasets/gov/lrsk/teises_aktai/Dokumentas`[^manifest]
- **Dataset:** [Teisės aktų registro duomenys](../teises_aktai.md) (`datasets/gov/lrsk/teises_aktai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/teises_aktai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai/Dokumentas` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `dokumento_id` | `string` | — | `4` | `open` | — | Dokumento unikalus identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Dokumento pavadinimas | — |
| `nuoroda` | `string` | — | `4` | `open` | — | URL nuoroda į teisės aktą. Galioja tik tuo atveju, kai teisės aktas yra paskelbtas ar registruotas teisės aktų registre. | — |
| `alt_pavadinimas` | `string` | — | `4` | `open` | — | Alternatyvus dokumento pavadinimas | — |
| `tekstas_lt` | `string` | — | `2` | `open` | — | Teisės akto naujausios suvestinės tekstas | — |
| `dok_busena` | `string` | — | `4` | `open` | — | Dokumento būsena | — |
| `dok_grupe` | `string` | — | `4` | `open` | — | Dokumento grupė (TAR; klasifikatoriaus reikšmės identifikatorius) | — |
| `pobudis` | `string` | — | `4` | `open` | — | Dokumento pobūdis | — |
| `galioj_busena` | `string` | — | `4` | `open` | — | Teisės akto galiojimo būsena (TAR; klasifikatoriaus reikšmės identifikatorius) | — |
| `parengusi_inst` | `string` | — | `4` | `open` | — | Dokumentą parengusių institucijų pavadinimai (rūšiavimui) | — |
| `priemusi_inst` | `string` | — | `4` | `open` | — | Dokumentą priėmusių (priimančių) institucijų pavadinimai (rūšiavimui) | — |
| `tar_kodas` | `string` | — | `4` | `open` | — | TA registro (TAR) kodas | — |
| `rusis` | `string` | — | `4` | `open` | — | Rūšis (Teisės akto rūšis) | — |
| `atv_dok_nr` | `string` | — | `2` | `open` | — | Atvaizduojamas dokumento numeris | — |
| `registracija` | `date` | `D` | `4` | `open` | — | Registracijos data (TA registracijos data ) | — |
| `isigal_sal_lt` | `string` | — | `2` | `open` | — | Teisės akto įsigaliojimo sąlygos | — |
| `termino_sal` | `string` | — | `2` | `open` | — | Teisės akto termino datos sąlygos | — |
| `es_teises_aktas` | `integer` | — | `4` | `open` | — | Nuorodų į ES teisės aktus skaičius | — |
| `priimtas` | `date` | `D` | `4` | `open` | — | Teisės akto priėmimo data | — |
| `prisijungta` | `date` | `D` | `4` | `open` | — | Teisės akto prijungimo data | — |
| `pakeista` | `string` | — | `2` | `open` | — | Teisės akto pakeitimo data | — |
| `ratifikuota` | `date` | `D` | `4` | `open` | — | Teisės akto ratifikavimo data | — |
| `patvirtinta` | `date` | `D` | `4` | `open` | — | Teisės akto patvirtinimo data | — |
| `paskelbta_tar` | `date` | `D` | `4` | `open` | — | Registravimo teisės aktų registre data | — |
| `isigalioja` | `date` | `D` | `4` | `open` | — | Teisės akto įsigaliojimo data | — |
| `isigalioja_po_salygu` | `date` | `D` | `4` | `open` | — | Įsigaliojimo po sąlygų įvykdymo data | — |
| `negalioja` | `date` | `D` | `4` | `open` | — | Teisės akto termino data | — |
| `negalioja_po_salygu` | `date` | `D` | `4` | `open` | — | Teisės akto termino po sąlygų įvykdymo data | — |
| `pask_atitaisymas` | `date` | `D` | `4` | `open` | — | Teisės akto paskutinio atitaisymo data | — |
| `paviesinimas` | `date` | `D` | `4` | `open` | — | Teisės akto, kito dokumento paviešinimo data | — |
| `ar_nacionalinis` | `boolean` | — | `4` | `open` | — | Požymis, ar dokumentas nacionalinis (True –nacionalinis, False – savivaldybių) | — |
| `ar_verslo_reg` | `boolean` | — | `4` | `open` | — | Verslo sąlygų reguliavimo požymis (True – taip, False – ne) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dok_busena` | `"registruotas TA registre"` | — | — | — | — |
| `dok_busena` | `"nepriimtas"` | — | — | — | — |
| `dok_busena` | `"paskelbtas"` | — | — | — | — |
| `dok_busena` | `"sunaikintas (loginis trynimas)"` | — | — | — | — |
| `dok_busena` | `"atsiimtas"` | — | — | — | — |
| `dok_busena` | `"parengtas"` | — | — | — | — |
| `dok_busena` | `"sudarytas"` | — | — | — | — |
| `dok_busena` | `"įsegtas"` | — | — | — | — |
| `dok_busena` | `"priimtas registruoti"` | — | — | — | — |
| `dok_busena` | `"išsegtas (dokumentas modifikuojamas)"` | — | — | — | — |
| `dok_grupe` | `"valstybės institucijų ir įstaigų teisės aktai"` | — | — | — | — |
| `dok_grupe` | `"savivaldybių teisės aktai"` | — | — | — | — |
| `dok_grupe` | `"teismų dokumentai"` | — | — | — | — |
| `dok_grupe` | `"tarptautiniai dokumentai"` | — | — | — | — |
| `dok_grupe` | `"kiti"` | — | — | — | — |
| `pobudis` | `"norminis"` | — | — | — | — |
| `pobudis` | `"teisės taikymo"` | — | — | — | — |
| `galioj_busena` | `"galioja"` | — | — | — | — |
| `galioj_busena` | `"negalioja"` | — | — | — | — |
| `galioj_busena` | `"neįsigaliojęs"` | — | — | — | — |
| `galioj_busena` | `"neviešas"` | — | — | — | — |
| `galioj_busena` | `"sustabdytas"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tekstas_lt` | `update(property: "tekstas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `isigal_sal_lt` | `update(property: "isigal_sal_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `pakeista` | `"update(property: ""pakeista[]"", type: ""array"", source: ""Pakeista"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/teises_aktai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/teises_aktai (https://data.gov.lt/datasets/2613/)
