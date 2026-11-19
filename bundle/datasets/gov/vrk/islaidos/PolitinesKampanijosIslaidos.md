---
type: Table
title: "PolitinesKampanijosIslaidos"
description: "Spinta table datasets/gov/vrk/islaidos/PolitinesKampanijosIslaidos (34 columns)."
tags: [gov, vrk, politineskampanijosislaidos, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/islaidos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vrk/islaidos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# PolitinesKampanijosIslaidos

- **Model:** `datasets/gov/vrk/islaidos/PolitinesKampanijosIslaidos`[^manifest]
- **Dataset:** [datasets/gov/vrk/islaidos](../islaidos.md) (`datasets/gov/vrk/islaidos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/islaidos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/islaidos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `islaidu_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `islaidu_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `rinkimu_id` | `integer` | — | `4` | `open` | — | Rinkimų identifikatorius | — |
| `rinkimu_pavad` | `string` | — | `4` | `open` | — | Rinkimų pavadinimas | — |
| `rink_apyg_id` | `integer` | — | `4` | `open` | — | Rinkimų apygardos identifikatorius | — |
| `apyg_id` | `integer` | — | `4` | `open` | — | Apygardos identifikatorius | — |
| `apyg_nr` | `integer` | — | `4` | `open` | — | Apygardos numeris | — |
| `apyg_pavad` | `string` | — | `4` | `open` | — | Apygardos pavadinimas | — |
| `p_kamp_rusis` | `string` | — | `4` | `open` | — | Politinės kampanijos rūšis | Nurodoma politinė kampanijos rūšis (Seimo rinkimai / Savivaldybių tarybų rinkimai / Respublikos Prezidento rinkimai / rinkimai į Europos Parlamentą / Referendumas) |
| `p_kamp_id` | `integer` | — | `4` | `open` | — | Politinės kampanijos identifikatorius | — |
| `p_kamp_pavad` | `string` | — | `4` | `open` | — | Politinės kampanijos pavadinimas | — |
| `p_kamp_dal_id` | `integer` | — | `4` | `open` | — | Politinės kampanijos dalyvio identifikatorius | — |
| `p_kamp_dal_pavad` | `string` | — | `4` | `open` | — | Politinės kampanijos dalyvis | Politinės kampanijos dalyvio pavadinimas - pilnas pavadinimas |
| `pasl_teikejo_tipas` | `string` | — | `4` | `open` | — | Paslaugų teikėjo tipas (FA/JA) | Paslaugų teikėjo tipas (Fizinis asmuo/ Juridinis asmuo) arba (FA/JA) |
| `suma` | `number` | — | `4` | `open` | — | Išlaidų suma | — |
| `pasl_teikejo_ja_kodas` | `string` | — | `4` | `open` | — | Paslaugų teikėjo kodas | Nurodomas juridinio asmens kodas, jeigu dal_fiz_jur nurodytas juridinis asmuo |
| `pasl_teikejo_fa_hash_kodas` | `string` | — | `4` | `open` | — | Paslaugų teikėjo kodas | Fizinių asmenų atveju sugeneruojamas HASH kodas. |
| `pasl_teikejas` | `string` | — | `4` | `open` | — | Paslaugų teikėjo pavadinimas arba pavardė, jei fizinis asmuo | Nurodomas pavadinimas / pavardė (jei fizinis asmuo). |
| `pasl_teikejo_vardas` | `string` | — | `4` | `open` | — | Paslaugų teikėjo vardas, jei fizinis asmuo | Paslaugų teikėjo vardas |
| `islaidu_paskirties_kodas` | `string` | — | `4` | `open` | — | Išlaidų paskirties kodas | Išlaidų paskirties kodas (RT, RR, RS, RI, RIN, RK. S, ORG, KEL, NPK, IA, AUD, G, LB, PLL, BMA, TP, N, NK, TI, KI, K, RU) |
| `islaidu_paskirtis` | `string` | — | `4` | `open` | — | Išlaidų paskirties aprašymas (pavadinimas) | — |
| `dok_data` | `date` | `D` | `4` | `open` | — | Išlaidų dokumento data | Išlaidas pagrindžiančio dokumento data |
| `dok_nr` | `string` | — | `4` | `open` | — | Išlaidų dokumento serija, numeris | Išlaidas pagrindžiančio dokumento numeris |
| `apmok_is_p_kamp` | `number` | — | `4` | `open` | — | Suma, apmokėta iš politinės kampanijos sąskaitos | — |
| `apmok_ne_is_p_kamp` | `number` | — | `4` | `open` | — | Suma, apmokėta ne iš politinės kampanijos sąskaitos | — |
| `skola` | `number` | — | `4` | `open` | — | Skolos įsipareigojimų suma | — |
| `padengta_skola` | `number` | — | `4` | `open` | — | Padengta skolos įsipareigojimų suma po ataskaitos pateikimo | — |
| `padengimo_data` | `date` | `D` | `4` | `open` | — | Skolų įsipareigojimų (dalies jų) įvykdymo data | Rodoma paskutinė skolų įsipareigojimų padengimo data |
| `dal_tipo_kodas` | `string` | — | `4` | `open` | — | Politinės kampanijos dalyvio tipo kodas | Politinės kampanijos dalyvio tipo kodas (KS, FA, RO) |
| `dal_tipas` | `string` | — | `4` | `open` | — | Politinės kampanijos dalyvio registravimo būsena | Politinės kampanijos dalyvio tipas (Politinė partija / Politinės partijos keltas kandidatų sąrašas / Visuomeninis rinkimų komitetas/ Išsikėlęs kandidatas) |
| `vardas` | `string` | — | `4` | `open` | — | Kandidato vardas | — |
| `pavarde_saraso_pavad` | `string` | — | `4` | `open` | — | Kandidato pavardė/Kandidatų sąrašo pavadinimas | — |
| `dal_reg_busena` | `string` | — | `4` | `open` | — | Politinės kampanijos dalyvio registravimo būsena | Dalyvio registravimo būsena (Registruotas / Praradęs statusą) |
| `vrk_sprendimo_nr` | `string` | — | `4` | `open` | — | VRK sprendimo, kuriuo papildytas žiniaraštis, numeris | VRK sprendimo, kuriuo papildytas politinės kampanijos dalyvio finansavimo apskaitos žiniaraštis, numeris |
| `vrk_sprendimo_data` | `date` | `D` | `4` | `open` | — | VRK sprendimo, kuriuo papildytas žiniaraštis, data | VRK sprendimo, kuriuo papildytas politinės kampanijos dalyvio finansavimo apskaitos žiniaraštis, data |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `p_kamp_rusis` | `"REF"` | — | — | Referendumas | — |
| `p_kamp_rusis` | `"SAV"` | — | — | Savivaldybių tarybų rinkimai | — |
| `p_kamp_rusis` | `"SEI"` | — | — | Seimo rinkimai | — |
| `pasl_teikejo_tipas` | `"J"` | — | — | Juridinis asmuo | — |
| `pasl_teikejo_tipas` | `"F"` | — | — | Fizinis asmuo | — |
| `dal_tipo_kodas` | `"K"` | — | — | Kandidatas | — |
| `dal_tipo_kodas` | `"KS"` | — | — | Kandidatų sąrašas | — |
| `dal_tipo_kodas` | `"P"` | — | — | Pretendentas | — |
| `dal_tipo_kodas` | `"PP"` | — | — | Politinė partija | — |
| `dal_tipo_kodas` | `"RI"` | — | — | Referendumo iniciatorius | — |
| `dal_tipo_kodas` | `"V"` | — | — | Politinis komitetas | — |
| `dal_tipas` | `"Kandidatas"` | — | — | Kandidatas | — |
| `dal_tipas` | `"Kandidatų sąrašas"` | — | — | Kandidatų sąrašas | — |
| `dal_tipas` | `"Pretendentas"` | — | — | Pretendentas | — |
| `dal_tipas` | `"Politinė partija"` | — | — | Politinė partija | — |
| `dal_tipas` | `"Referendumo iniciatorius"` | — | — | Referendumo iniciatorius | — |
| `dal_tipas` | `"Politinis komitetas"` | — | — | Politinis komitetas | — |
| `dal_reg_busena` | `"Registruotas"` | — | — | Registruotas | — |
| `dal_reg_busena` | `"Panaikintas"` | — | — | Panaikintas/Praradęs statusą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/islaidos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/islaidos.csv#L4)
