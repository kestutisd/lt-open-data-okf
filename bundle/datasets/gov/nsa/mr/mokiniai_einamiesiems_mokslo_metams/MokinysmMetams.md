---
type: Table
title: "MokinysmMetams — Mokiniai einamiesiems mokslo metams"
description: "Lentelėje pateikta informacija apie einamųjų mokslo metų bendrojo, profesinio, ikimokyklinio, priešmokyklinio, neformalaus ugdymo mokinius iš Nacionalinės Švietimo agentūros (NŠA) Mokinių registro (MR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams/MokinysmMetams"
tags: [gov, nsa, mokinysmmetams, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2687/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MokinysmMetams — Mokiniai einamiesiems mokslo metams

Lentelėje pateikta informacija apie einamųjų mokslo metų bendrojo, profesinio, ikimokyklinio, priešmokyklinio, neformalaus ugdymo mokinius iš Nacionalinės Švietimo agentūros (NŠA) Mokinių registro (MR). Šioje lentelėje matoma informacija tik tų mokinių, kurių mokymosi pradžios data yra lygi arba senesnė einamųjų mokslo metų pabaigos datai ir kurių mokymosi pabaigos data yra naujesnė arba lygi einamųjų mokslo metų pradžios datai arba yra tuščia, dar neįrašyta (galioja_nuo ? einamųjų mokslo metų pabaiga IR (galioja_iki ? einamųjų mokslo metų pradžia ARBA galioja_iki - neįrašyta, tuščia)). Pavyzdžiui, kai einamieji mokslo metai yra nuo 2023-09-01 iki 2024-08-31, lentelėje bus matomi įrašai tų mokinių, kurie pradėjo mokytis tam tikroje klasėje arba būrelyje no 2023-09-01 ir baigė mokytis 2024-06-01, tačiau nebus matomi įrašai tų mokinių, kurie pradėjo mokytis 2022-09-01 ir baigė mokytis 2023-06-01. Siekiant sustiprinti asmens duomenų apsaugą duomenys buvo triukšminti.[^manifest]

- **Model:** `datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams/MokinysmMetams`[^manifest]
- **Dataset:** [Mokiniai einamiesiems mokslo metams](../mokiniai_einamiesiems_mokslo_metams.md) (`datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams`)[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams/MokinysmMetams` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `asm_kodas` | `string` | — | `4` | `open` | — | Šifruotas asmens kodo identifikatorius | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Šifruotas asmens vardo ir pavardės identifikatorius | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Asmens lytis | — |
| `kilme` | `string` | — | `4` | `open` | — | Asmens kilmė | — |
| `inst_kodas` | `string` | — | `4` | `open` | — | Institucijos juridinis asmens kodas | — |
| `inst_pavadinimas_lt` | `string` | — | `4` | `open` | — | Institucijos arba individualią mokymo veiklą vykdančio asmens pavadinimas | — |
| `inst_tipas` | `string` | — | `4` | `open` | — | Institucijos arba individualią mokymo veiklą vykdančio asmens tipas | — |
| `inst_savivaldybe` | `string` | — | `4` | `open` | — | Institucijos arba individualią mokymo veiklą vykdančio asmens savivaldybė | — |
| `inst_apsk_pav` | `string` | — | `4` | `open` | — | Institucijos arba individualią mokymo veiklą vykdančio asmens apskritis | — |
| `mokymo_tipas` | `string` | — | `4` | `open` | — | Mokymo tipas | — |
| `mokymosi_organizavimo_budas` | `string` | — | `4` | `open` | — | Mokymosi organizavimo būdas | — |
| `mokomoji_kalba` | `string` | — | `4` | `open` | — | Mokomoji kalba | — |
| `klase_tipas` | `string` | — | `4` | `open` | — | Klasės tipas | — |
| `klase_pakopa_pav` | `string` | — | `4` | `open` | — | Klasės pakopa | — |
| `klase_nr` | `string` | — | `4` | `open` | — | Klasės numeris | — |
| `klases_paskirtis` | `string` | — | `4` | `open` | — | Klasės paskirtis | — |
| `irasas_galioja_nuo` | `date` | `D` | `4` | `open` | — | Įrašo galiojimo pradžios data | — |
| `irasas_galioja_iki` | `date` | `D` | `4` | `open` | — | Įrašo galiojimo pabaigos data | — |
| `einam_mokslo_metupradzia` | `date` | `D` | `4` | `open` | — | Einamųjų mokslo metų pradžios data | — |
| `einam_mokslo_metupabaiga` | `date` | `D` | `4` | `open` | — | Einamųjų mokslo metų pabaigos data | — |
| `duomenu_atnaujinimo_data` | `datetime` | `L` | `4` | `open` | — | Duomenų atnaujinimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `kilme` | `"Užsienio valstybė"` | — | — | Užsienio valstybė | — |
| `kilme` | `"Lietuvos Respublika"` | — | — | Lietuvos Respublika | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `inst_kodas` | `create(property: "ja_kodas", type: "ref", ref: "datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `inst_pavadinimas_lt` | `update(property: "inst_pavadinimas_lt@lt", type: "text")` | `type` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams (https://data.gov.lt/datasets/2687/)
