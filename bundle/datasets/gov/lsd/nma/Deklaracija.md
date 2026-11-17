---
type: Table
title: "Deklaracija — Pasėlių heterogeniškumo vertinimų duomenys"
description: "Rinkinyje skelbiami Automatinės laukų nuolatinio stebėjimo sistemos (ALNSIS) pasėlių heterogeniškumo (netolygumo) vertinimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsd/nma/Deklaracija"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/nma/zem_uk_paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nma/zem_uk_paraiskos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Deklaracija — Pasėlių heterogeniškumo vertinimų duomenys

Rinkinyje skelbiami Automatinės laukų nuolatinio stebėjimo sistemos (ALNSIS) pasėlių heterogeniškumo (netolygumo) vertinimų duomenys. Algoritmas naudoja pikselinę klasifikaciją ir mašininio mokymo metodus, pagrįstus Sentinel-1 ir Sentinel-2 palydovų duomenimis, siekiant identifikuoti skirtingus augalų tipus, augimo fazes ir netolygumus pasėlių laukuose. Analizė padeda nustatyti pasėlių sudėtį bei galimas problemas, tokias kaip piktžolės ar nevienodas augimas.

Algoritmo pagalba galima nustatyti, kokia yra reali augalų sudėtis deklaruotame pasėlyje – apskaičiuojamas skirtingų augalų tipų procentinis pasiskirstymas lauko viduje. Taip pat galima įvertinti, kokią dalį ploto faktiškai užima deklaruotas pasėlis, palyginti su kitais augalais ar žemės dangos elementais.

Pateikiami duomenys apie pareiškėją, deklaruojamą lauką (žemės ūkio valdos atpažinties kodas, plotas, savivaldybė ir seniūnija) ir algoritmo būdu nustatytus pasėlių plotus, išreikštus procentais nuo viso ploto.

Duomenų teikėjas: Nacionalinė mokėjimo agentūra prie Žemės ūkio ministerijos..

- **Model:** `datasets/gov/lsd/nma/Deklaracija`[^manifest]
- **Dataset:** [Nacionalinė mokėjimų agentūra](../nma.md) (`datasets/gov/lsd/nma`)
- **Manifest CSV:** [datasets/gov/lsd/nma/zem_uk_paraiskos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nma/zem_uk_paraiskos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/nma/Deklaracija`
- **Primary Key (`ref`):** `paraiskos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paraiskos_id` | `string` | — | `4` | `open` | — | Paraiškos identifikacinis numeris | — |
| `nma_id` | `string` | — | `4` | `open` | — | Nacionalinės mokėjimų agentūros paraiškos numeris | — |
| `pareiskejas` | `string` | — | `4` | `open` | — | Paraišką teikęs asmuo. | Gali būti fizinis arba juridinis asmuo. |
| `valdos_numeris` | `string` | — | `4` | `open` | — | Žemės ūkio valdos atpažinties kodas, suteikiamas Lietuvos Respublikos žemės ūkio ir kaimo verslo registre | — |
| `plotas_ha` | `number` | `ha` | `4` | `open` | — | Deklaruojamo lauko plotas hektarais. | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Deklaruojamo lauko savivaldybė | — |
| `seniunija` | `string` | — | `4` | `open` | — | Deklaruojamo lauko seniūnija | — |
| `deklaruotas_pas` | `string` | — | `4` | `open` | — | Deklaruoto pasėlio pavadinimas | — |
| `kvv_proc` | `number` | `%` | `4` | `open` | — | Vasarinių kviečių procentas | — |
| `avi_proc` | `number` | `%` | `4` | `open` | — | Avižų procentras | — |
| `gri_proc` | `number` | `%` | `4` | `open` | — | Grikių procentas | — |
| `krz_proc` | `number` | `%` | `4` | `open` | — | Žieminių kvietrugių procentas | — |
| `kvz_proc` | `number` | `%` | `4` | `open` | — | Žieminių kviečių procentas | — |
| `miz_proc` | `number` | `%` | `4` | `open` | — | Žieminius miežių procentas | — |
| `rav_proc` | `number` | `%` | `4` | `open` | — | Vasarinių rapsų procentas | — |
| `raz_proc` | `number` | `%` | `4` | `open` | — | Žieminių rapsų procentas | — |
| `ruz_proc` | `number` | `%` | `4` | `open` | — | Žieminių rugių procentas | — |
| `pup_proc` | `number` | `%` | `4` | `open` | — | Pupų procentas | — |
| `zir_proc` | `number` | `%` | `4` | `open` | — | Žirnių procentas | — |
| `dgp_proc` | `number` | `%` | `4` | `open` | — | Daugiametės ganyklos arba pievos, daugiametės žolės (eraičinai, miglės, motiejukai, svidrės, smilgos, pašiaušėliai, avižuolės, šunažolės, visgės, erainčinsvidrės, dryžučiai, dirsuolės ir kt.) procentas | — |
| `kita_proc` | `number` | `%` | `4` | `open` | — | Kitų pasėlių procentas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/nma/zem_uk_paraiskos.csv
