---
type: Table
title: "Gyvunas — Lietuvos zoologijos sodo gyvūnų kolekcijos sąrašas"
description: "Rinkinyje pateikiami duomenys apie Lietuvos zoologijos sode laikomus gyvūnus einamiesiems metams."
resource: "https://get.data.gov.lt/datasets/gov/zoo/gyvunai/Gyvunas"
tags: [gov, zoo, gyvunas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zoo/gyvunai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zoo/gyvunai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2734/"
    title: "data.gov.lt DCAT-AP — datasets/gov/zoo/gyvunai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Gyvunas — Lietuvos zoologijos sodo gyvūnų kolekcijos sąrašas

Rinkinyje pateikiami duomenys apie Lietuvos zoologijos sode laikomus gyvūnus einamiesiems metams. Rinkinio objektas - individas arba gyvūnų grupė. Nurodoma informacija apie gyvūną (gyvūnų grupę): lotyniškas ir angliškas pavadinimas, lytis, gimimo data, aplinkybės ir vieta, esamas savininkas, aptvaras, kuriame gyvūnas laikomas bei taksonominė gyvūno klasifikacija.[^manifest]

- **Model:** `datasets/gov/zoo/gyvunai/Gyvunas`[^manifest]
- **Dataset:** [Lietuvos zoologijos sodo gyvūnų kolekcijos sąrašas](../gyvunai.md) (`datasets/gov/zoo/gyvunai`)[^manifest]
- **Manifest CSV:** [datasets/gov/zoo/gyvunai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zoo/gyvunai.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/zoo/gyvunai/Gyvunas` (`deployed`)[^manifest]
- **Provider:** `zoo` — Lietuvos zoologijos sodas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros unikalus įrašo identifikatorius | — |
| `gyv_tipas` | `string` | — | `4` | `open` | — | Įrašo apie gyvūną tipas. Tai yra, ar aprašomas individualus gyvūnas ar tos pačios rūšies gyvūnų grupė. | — |
| `pavadinimas_lot` | `string` | — | `4` | `open` | — | Lotyniškas gyvūno pavadinimas | — |
| `pavadinimas_en` | `string` | — | `4` | `open` | — | Angliškas gyvūno pavadinimas | — |
| `lytis` | `string` | — | `4` | `open` | — | Gyvūno lytis. Jeigu įrašas apie gyvūnų grupę, tuomet stulpelyje nurodytas lyčių skaičius pagal schemą: patinas.patelė.nenustatyta. | — |
| `kiekis` | `number` | `U` | `4` | `open` | — | Bendras gyvūnų rūšies skaičius zoologijos sode | — |
| `gim_data` | `date` | `D` | `4` | `open` | — | Gimimo data | — |
| `gim_aplinkybes` | `string` | — | `4` | `open` | — | Gyvūno gimimo aplinkybės. | — |
| `gim_vieta` | `string` | — | `4` | `open` | — | Gimimo vieta | — |
| `savininkas` | `string` | — | `4` | `open` | — | Paskutinis savininkas | — |
| `aptvaras` | `string` | — | `4` | `open` | — | Aptvaras, kuriame laikomas gyvūnas Lietuvos zoologijos sode. | — |
| `laikymas` | `string` | — | `4` | `open` | — | Požymis, ar gyvūnas laikomas lankytojams matomuose aptvaruose, ar karantine. Karantine gyvūnai gali būti laikomi ligų prevencijai, aklimatizacijai arba dėl kitų priežasčių siekiant izoliuoti gyvūną. | — |
| `rangas` | `string` | — | `4` | `open` | — | Taksonominis rangas, pagal kurį klasifikuojamas gyvūnas | — |
| `karalyste_lot` | `string` | — | `4` | `open` | — | Lotyniškas biologinės karalystės pavadinimas | — |
| `tipas_lot` | `string` | — | `4` | `open` | — | Lotyniškas biologinio tipo pavadinimas | — |
| `klase_lot` | `string` | — | `4` | `open` | — | Lotyniškas biologinės klasės pavadinimas | — |
| `burys_lot` | `string` | — | `4` | `open` | — | Lotyniškas biologinio būrio pavadinimas | — |
| `seima_lot` | `string` | — | `4` | `open` | — | Lotyniškas biologinės šeimos pavadinimas | — |
| `gentis_lot` | `string` | — | `4` | `open` | — | Lotyniškas biologinės genties pavadinimas | — |
| `rusis_lot` | `string` | — | `4` | `open` | — | Lotyniškas biologinės rūšies pavadinimas | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gyv_tipas` | `"Individas"` | — | — | — | — |
| `gyv_tipas` | `"Gyvūnų grupė"` | — | — | — | — |
| `lytis` | `"Patelė"` | — | — | — | — |
| `lytis` | `"Patinas"` | — | — | — | — |
| `lytis` | `"Nenustatyta"` | — | — | — | — |
| `gim_aplinkybes` | `"Gimimas nelaisvėje"` | — | — | — | — |
| `gim_aplinkybes` | `"Nenustatyta"` | — | — | — | — |
| `gim_aplinkybes` | `"Netikslu/neaišku"` | — | — | — | — |
| `gim_aplinkybes` | `"Gimimas gamtoje"` | — | — | — | — |
| `laikymas` | `"Viešai prieinamas"` | — | — | — | — |
| `laikymas` | `"Laikomas karantine"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas_lot` | `update(property: "pavadinimas_lot@la", type: "text")` | `type` | `4` | `open` | — | — | — |
| `pavadinimas_en` | `update(property: "pavadinimas_en@en", type: "text")` | `type` | `4` | `open` | — | — | — |
| `karalyste_lot` | `update(property: "karalyste_lot@la", type: "text")` | `type` | `4` | `open` | — | — | — |
| `tipas_lot` | `update(property: "tipas_lot@la", type: "text")` | `type` | `4` | `open` | — | — | — |
| `klase_lot` | `update(property: "klase_lot@la", type: "text")` | `type` | `4` | `open` | — | — | — |
| `burys_lot` | `update(property: "burys_lot@la", type: "text")` | `type` | `4` | `open` | — | — | — |
| `seima_lot` | `update(property: "seima_lot@la", type: "text")` | `type` | `4` | `open` | — | — | — |
| `gentis_lot` | `update(property: "gentis_lot@la", type: "text")` | `type` | `4` | `open` | — | — | — |
| `rusis_lot` | `update(property: "rusis_lot@la", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zoo/gyvunai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zoo/gyvunai.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/zoo/gyvunai (https://data.gov.lt/datasets/2734/)
