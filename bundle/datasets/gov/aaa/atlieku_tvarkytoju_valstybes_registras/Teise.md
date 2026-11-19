---
type: Table
title: "Teise — Teises išrašyti gaminių, pakuočių atliekų sutvarkymą įrodančius dokumentus turintys atliekų tvarkytojai"
description: "Teisės išrašyti atliekų sutvarkymą įrodančius dokumentus"
resource: "https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Teise"
tags: [gov, aaa, teise, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L73"
    title: "atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L73"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3840/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Teise — Teises išrašyti gaminių, pakuočių atliekų sutvarkymą įrodančius dokumentus turintys atliekų tvarkytojai

Teisės išrašyti atliekų sutvarkymą įrodančius dokumentus[^manifest]

- **Model:** `datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Teise`[^manifest]
- **Dataset:** [Atliekų tvarkytojų valstybės registro duomenys](../atlieku_tvarkytoju_valstybes_registras.md) (`datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L73](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L73)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Teise` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `teises_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teises_id` | `string` | — | `4` | `open` | — | Įgytos teisės identifikatorius | — |
| `teises_tipas` | `string` | — | `4` | `open` | — | Įgytos teisės išrašyti gaminių ir (ar) pakuočių atliekų sutvarkymą įrodančius dokumentus tipas (srautas) | — |
| `teises_igijimo_data` | `date` | `D` | `4` | `open` | — | Teisės įgijimo data | — |
| `teises_netekimo_data` | `date` | `D` | `4` | `open` | — | Teisės netekimo data | — |
| `atlieku_tvarkymo_veikla` | `string` | — | `4` | `open` | — | Įgyta teisė išrašyti dokumentus nurodytai atliekų tvarkymo veiklai | — |
| `apmokestinamojo_gaminio_pavadinimas` | `string` | — | `4` | `open` | — | Įgyta teisė išrašyti dokumentus apmokestinamajam gaminiui | — |
| `elektronikos_irangos_kategorija` | `string` | — | `4` | `open` | — | Įgyta teisė išrašyti dokumentus elektros ir elektronikos įrangos kategorijos tipui | — |
| `pakuociu_medziaga` | `string` | — | `4` | `open` | — | Įgyta teisė išrašyti dokumentus pakuotėms iš nurodytos medžiagos | — |
| `ar_komunalinis_srautas` | `boolean` | — | `4` | `open` | — | Požymis, ar gaminiai ir pakuotės, kuriems suteikta teisė išrašyti dokumentus, priklauso komunaliniam srautui? | — |
| `ar_surinkimas_platinimo_vietose` | `boolean` | — | `4` | `open` | — | Požymis, kad suteikta teisė surinkti gaminius ir pakuotes platinimo vietose | — |
| `atliekos_kodas` | `string` | — | `4` | `open` | — | Atliekos kodas (Atliekų reikšmės gali būti nepriskirtos srautui (null reikšmė), jeigu tvarkymo vietoje nėra registruotos to srauto/srauto rūšies/kategorijos atliekos, už kurią galima išrašyti gaminių ir (ar) pakuočių atliekų sutvarkymą įrodančius dokumentus su tvarkymo veikla, dėl kurios suteikta teisė (tvarkymo vietoje pagal registraciją to srauto atliekų tvarkymas nevykdomas) arba tais atvejais, kai teisė suteikta mišrių komunalinių atliekų apdorotojams ar surinkėjams dėl veiklų su 20 kodo atliekomis, iš kurių generuojamos gaminių ar pakuočių atliekos) | — |
| `atliekos_pavadinimas` | `string` | — | `4` | `open` | — | Atliekos pavadinimas | — |
| `teise_veikti_savivaldybese` | `string` | — | `4` | `open` | — | Tvarkytojo teisė išrašyti dokumentus gaunamiems gaminiams ir pakuotėms iš savivaldybių (kai dirbama komunaliniame sraute) | — |
| `tvarkytojo_kodas_atvr_sistemoje` | `string` | — | `4` | `open` | — | Tvarkytojo kodas ATVR sistemoje | — |
| `tvarkytojo_juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Atliekų tvarkytojo juridinio asmens kodas | — |
| `tvarkytojo_pavadinimas` | `string` | — | `4` | `open` | — | Tvarkytojo pavadinimas | — |
| `tvarkytojo_isregistravimo_data` | `date` | `D` | `4` | `open` | — | Tvarkytojo išregistravimo data | — |
| `tvarkytojo_adresas` | `string` | — | `4` | `open` | — | Tvarkytojo adresas | — |
| `tvarkymo_vietos_numeris_atvr_sistemoje` | `string` | — | `4` | `open` | — | Tvarkymo vietos numeris ATVR | — |
| `tvarkymo_vietos_pavadinimas` | `string` | — | `4` | `open` | — | Tvarkymo vietos pavadinimas | — |
| `tvarkymo_vietos_isregistravimo_data` | `date` | `D` | `4` | `open` | — | Tvarkymo vietos išregistravimo data | — |
| `tvarkymo_vietos_busena` | `string` | — | `4` | `open` | — | Tvarkymo vietos būsena | — |
| `tvarkymo_vietos_adresas` | `string` | — | `4` | `open` | — | Tvarkymo vietos adresas, sugeneruotas VDA pagal GPAIS duomenis | — |
| `tvarkymo_vietos_koordinates_lks` | `string` | — | `4` | `open` | — | Tvarkymo vietos koordinatės lks sistemoje | — |
| `tvarkymo_vietos_tikslumas_balais` | `number` | — | `4` | `open` | — | Tvarkymo vietos tikslumas balais | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tvarkymo_vietos_busena` | `"Patvirtinta"` | — | — | — | — |
| `tvarkymo_vietos_busena` | `"Išregistruota"` | — | — | — | — |
| `tvarkymo_vietos_busena` | `"Tikslinama"` | — | — | — | — |
| `tvarkymo_vietos_busena` | `"Išregistruojama"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L73 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L73)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras (https://data.gov.lt/datasets/3840/)
