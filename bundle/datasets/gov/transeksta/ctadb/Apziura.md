---
type: Table
title: "Apziura — Transporto priemonių techninės apžiūros duomenys"
description: "Lietuvos techninės apžiūros įmonių asociacijos „TRANSEKSTA“ centralizuotoji techninės apžiūros duomenų bazė kaupia kelių transporto priemonių techninių apžiūrų (TA) duomenis, vykdomų asocijuotųjų įmonių."
resource: "https://get.data.gov.lt/datasets/gov/transeksta/ctadb/Apziura"
tags: [gov, transeksta, apziura, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/transeksta/ctadb.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/transeksta/ctadb.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2721/"
    title: "data.gov.lt DCAT-AP — datasets/gov/transeksta/ctadb"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Apziura — Transporto priemonių techninės apžiūros duomenys

Lietuvos techninės apžiūros įmonių asociacijos „TRANSEKSTA“ centralizuotoji techninės apžiūros duomenų bazė kaupia kelių transporto priemonių techninių apžiūrų (TA) duomenis, vykdomų asocijuotųjų įmonių. Rinkinyje duomenys teikiami nuo 2015 m., atnaujinami kas savaitę. Duomenų rinkinys apima transporto priemonės (TP) pseudonimizuotus identifikatorius, valstybinį ir VIN (angl. vehicle identification number/liet. transporto priemonės identifikacinis numeris) numerius. Valstybiniui numeriui taip pat įtrauktas stulpelis, nurodantis, kuris neapdoroto valstybinio numerio simbolis atitinka raidę, skaitmenį arba spec. paskirties simbolį. Duomenų rinkinys taip pat apima TP markę, modelį, klasę, kėbulą, ar TP yra specialios paskirties, pagaminimo metus, kuro rūšis, dūmingumą, anglies monoksido taršą tiek prie įprasto, tiek prie padidinto variklio apsukų skaičiaus, ridą (bendrą TP nuvažiuotą atstumą), TA stoties pseudonimizuotą kodą, adreso savivaldybę, bei TA tipą, išvadą, ar TA išlaikyta, TA datą savaitės tikslumu.[^manifest]

- **Model:** `datasets/gov/transeksta/ctadb/Apziura`[^manifest]
- **Dataset:** [Transporto priemonių techninės apžiūros duomenys](../ctadb.md) (`datasets/gov/transeksta/ctadb`)[^manifest]
- **Manifest CSV:** [datasets/gov/transeksta/ctadb.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/transeksta/ctadb.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/transeksta/ctadb/Apziura` (`deployed`)[^manifest]
- **Provider:** `transeksta` — Lietuvos techninės apžiūros įmonių asociacija „Transeksta“ *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `tp_id` | `string` | — | `4` | `open` | — | Transporto priemonės identifikatorius | — |
| `tp_valst_nr` | `string` | — | `4` | `open` | — | Transporto priemonės valstybinis numeris | — |
| `tp_valst_nr_zymejimas` | `string` | — | `4` | `open` | — | Transporto priemonės valstybinio numerio raidžių, skaitmenų ir kitų simbolių žymėjimai | — |
| `tp_vin_nr` | `string` | — | `4` | `open` | — | Transporto priemonės VIN numeris | — |
| `tp_marke` | `string` | — | `4` | `open` | — | Transporto priemonės markė | — |
| `tp_modelis` | `string` | — | `4` | `open` | — | Transporto priemonės modelis | — |
| `tp_klase` | `string` | — | `4` | `open` | — | Transporto priemonės klasė | — |
| `tp_kebulas` | `string` | — | `4` | `open` | — | Transporto priemonės kėbulas | — |
| `tp_spc` | `string` | — | `4` | `open` | — | Transporto priemonės specialioji paskirtis | — |
| `tp_pag_metai` | `integer` | — | `4` | `open` | — | Transporto priemonės pagaminimo metai | — |
| `tp_kuras` | `string` | — | `4` | `open` | — | Transporto priemonės kuro rūšys | — |
| `tp_dumingumas` | `number` | `%` | `4` | `open` | — | Transporto priemonės dūmingumas | — |
| `tp_co_tarsa` | `number` | `%` | `4` | `open` | — | Transporto priemonės anglies monoksido tarša prie įprasto variklio apsukų skaičiaus | — |
| `tp_co_tarsa_2000` | `number` | `%` | `4` | `open` | — | Transporto priemonės anglies monoksido tarša prie padidinto (>2000 aps/min.) variklio apsukų skaičiaus | — |
| `tp_rida_km` | `integer` | `km` | `4` | `open` | — | Transporto priemonės rida | — |
| `ta_stoties_kodas` | `string` | — | `3` | `open` | — | Techninės apžiūros stoties kodas | — |
| `ta_stoties_savivaldybe` | `string` | — | `4` | `open` | — | Techninės apžiūros stoties savivaldybė | — |
| `ta_tipas` | `string` | — | `4` | `open` | — | Techninės apžiūros tipas | — |
| `ta_isvada` | `string` | — | `4` | `open` | — | Techninės apžiūros metu padaryta išvada apie transporto priemonės būklę | — |
| `ar_ta_islaikyta` | `boolean` | — | `4` | `open` | — | Ar techninė apžiūra išlaikyta | — |
| `ta_savaites_data` | `date` | `W` | `4` | `open` | — | Techninės apžiūros data savaitės tikslumu | — |
| `ta_periodiskumas_men` | `integer` | `M` | `4` | `open` | — | Techninės apžiūros periodiškumas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ta_isvada` | `"Be trūkumų"` | `Be trūkumų` | — | Be trūkumų | — |
| `ta_isvada` | `"Nedideli trūkumai"` | `Nedideli trūkumai` | — | Nedideli trūkumai | — |
| `ta_isvada` | `"Dideli trūkumai"` | `Dideli trūkumai` | — | Dideli trūkumai | — |
| `ta_isvada` | `"Pavojingi trūkumai"` | `Pavojingi trūkumai` | — | Pavojingi trūkumai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/transeksta/ctadb.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/transeksta/ctadb.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/transeksta/ctadb (https://data.gov.lt/datasets/2721/)
