---
type: Table
title: "NtrInzinerinisStatinys"
description: "Spinta table datasets/gov/rc/ntr/ntr_inzineriniai_statiniai/NtrInzinerinisStatinys (57 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_inzineriniai_statiniai/NtrInzinerinisStatinys"
tags: [gov, rc, ntrinzinerinisstatinys, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_inzineriniai_statiniai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_inzineriniai_statiniai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1814/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_inzineriniai_statiniai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# NtrInzinerinisStatinys

- **Model:** `datasets/gov/rc/ntr/ntr_inzineriniai_statiniai/NtrInzinerinisStatinys`[^manifest]
- **Dataset:** [Nekilnojamojo turto registre įregistruotų inžinerinių statinių duomenys pagal savivaldybes](../ntr_inzineriniai_statiniai.md) (`datasets/gov/rc/ntr/ntr_inzineriniai_statiniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_inzineriniai_statiniai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_inzineriniai_statiniai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_inzineriniai_statiniai/NtrInzinerinisStatinys` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikatorius | Inžinerinio statinio identifikatorius šiame duomenų rinkinyje |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybė | Savivaldybės, kurioje yra inžinerinis statinys, pavadinimas |
| `seniunija` | `ref` | [Seniunija](../../ar/seniunija/Seniunija.md) (`level=4 UUID`: `seniunija._id`) | `4` | `open` | — | Seniūnija | Savivaldybėje esančios seniūnijos, kurioje yra inžinerinis statinys, pavadinimas |
| `statinio_kategorija` | `integer` | — | `3` | `open` | — | Statinio kategorija | Statinio rūšis pagal LR statybos įstatymą. Nuo statinio kategorijos priklauso koks projektas turi būti parengtas, kokie reikalavimai keliami projekto vadovui ir kitiems statybos techninės veiklos pagrindinių sričių (STVPS) vadovams ir statybą leidžiančio dokumento (SLD) privalomumas. |
| `obje_tipas` | `ref` | [NtrObjektoTipas](../ntr_objektai/NtrObjektoTipas.md) (`level=4 UUID`: `obje_tipas._id`) | `4` | `open` | — | Objekto tipas | Inžinerinio statinio tipas |
| `pask_tipas` | `ref` | [NtrPaskirtiesTipas](../ntr_paskirtys/NtrPaskirtiesTipas.md) (`level=4 UUID`: `pask_tipas._id`) | `4` | `open` | — | Paskirties tipas | Inžinerinio statinio paskirtis |
| `stat_pradzios_metai` | `integer` | — | `3` | `open` | — | Statybos pradžios metai | Inžinerinio statinio statybos pradžios metai |
| `stat_pabaigos_metai` | `integer` | — | `3` | `open` | — | Statybos pabaigos metai | Inžinerinio statinio statybos užbaigimo metai |
| `rekonstr_pradzios_metai` | `integer` | — | `3` | `open` | — | Rekonstrukcijos pradžios metai | Inžinerinio statinio rekonstrukcijos pradžios metai |
| `rekonstr_pabaigos_metai` | `integer` | — | `3` | `open` | — | Rekonstrukcijos pabaigos metai | Inžinerinio statinio rekonstrukcijos pabaigos metai |
| `kap_remonto_pradzios_metai` | `integer` | — | `3` | `open` | — | Kapitalinio remonto pradžios metai | Inžinerinio statinio kapitalinio remonto pradžios metai |
| `kap_remonto_pabaigos_metai` | `integer` | — | `3` | `open` | — | Kapitalinio remonto pabaigos metai | Inžinerinio statinio kapitalinio remonto pabaigos metai |
| `baigtumo_proc` | `integer` | — | `3` | `open` | — | Baigtumas | Inžinerinio statinio statybos užbaigtumo procentas |
| `plotas` | `number` | — | `3` | `open` | — | Plotas | Inžinerinio statinio plotas |
| `turis` | `number` | — | `3` | `open` | — | Tūris | Inžinerinio statinio tūris |
| `ilgis` | `number` | — | `3` | `open` | — | Ilgis | Inžinerinio statinio ilgis |
| `aukstis` | `number` | — | `3` | `open` | — | Aukštis | Inžinerinio statinio aukštis |
| `plotis` | `number` | — | `3` | `open` | — | Plotis | Inžinerinio statinio plotis |
| `medziaga` | `integer` | — | `3` | `open` | — | Medžiaga | Medžiaga, iš kurios pastatytas inžinerinis statinys |
| `gylis` | `integer` | — | `3` | `open` | — | Gylis | Gylis, kuriame yra pastatytas inžinerinis statinys |
| `kiekis` | `number` | — | `3` | `open` | — | Kiekis | Inžinerinio statinio dalių kiekis |
| `danga` | `integer` | — | `3` | `open` | — | Danga | Inžinerinio statinio danga |
| `diametras` | `integer` | — | `3` | `open` | — | Diametras | Inžinerinio statinio diametras |
| `skerspjuvis` | `integer` | — | `3` | `open` | — | Skerspjūvis | Inžinerinio statinio skerspjūvis |
| `stadiono_tipas` | `integer` | — | `2` | `open` | — | Stadiono tipas | Inžinerinio statinio-stadiono tipas |
| `stadiono_rusis` | `integer` | — | `2` | `open` | — | Stadiono rūšis | Inžinerinio statinio-stadiono rūšis |
| `sedimu_vietu_sk` | `integer` | `U` | `4` | `open` | — | Sėdimų vietų skaičius | Inžinerinio statinio-stadiono sėdimų vietų skaičius |
| `stovimu_vietu_sk` | `integer` | `U` | `4` | `open` | — | Stovimu vietų skaičius | Inžinerinio statinio-stadiono stovimų vietų skaičius |
| `sporto_aiksteles_rusis` | `integer` | — | `2` | `open` | — | Sporto aikštelės rūšis | Inžinerinio statinio-sporto aikštelės rūšis |
| `sporto_trasos_rusis` | `integer` | — | `2` | `open` | — | Sporto trasos rūšis | Inžinerinio statinio-sporto trasos rūšis |
| `prieplaukos_rusis` | `integer` | — | `2` | `open` | — | Prieplaukos rūšis | Inžinerinio statinio-prieplaukos rūšis |
| `hidrotechninio_statinio_rusis` | `integer` | — | `2` | `open` | — | Hidrotechninio statinio rūšis | Hidrotechninio statinio rūšis |
| `kelio_reiksme` | `integer` | — | `2` | `open` | — | Kelio reikšmė | Inžinerinio statinio-kelio reikšmė |
| `kelio_kategorija` | `integer` | — | `2` | `open` | — | Kelio kategorija | Inžinerinio statinio-kelio kategorija |
| `gelezinkelio_reiksme` | `integer` | — | `2` | `open` | — | Geležinkelio reikšmė | Inžinerinio statinio-geležinkelio reikšmė |
| `kelio_kliutis` | `integer` | — | `2` | `open` | — | Kelio kliūtis | Inžinerinio statinio-kelio kliūtis |
| `gylis_grimzle` | `integer` | — | `2` | `open` | — | Gylis (grimzlė) | Inžinerinio statinio gylis (grimzlė) |
| `gabaritas` | `integer` | — | `2` | `open` | — | Gabaritas | Inžinerinio statinio gabaritas |
| `oro_uosto_kategorija` | `integer` | — | `2` | `open` | — | Oro uosto kategorija | Inžinerinio statinio-oro uosto kategorija |
| `oro_uosto_dangos_kodas` | `integer` | — | `2` | `open` | — | Oro uosto dangos kodas | Inžinerinio statinio-oro uosto dangos kodas |
| `orlaivio_tako_rusis` | `integer` | — | `2` | `open` | — | Orlaivių tako rūšis | Inžinerinio statinio-orlaivių tako rūšis |
| `vandens_uosto_rusis` | `integer` | — | `2` | `open` | — | Vandens uosto rūšis | Inžinerinio statinio-vandens uosto rūšis |
| `sulinio_tipas` | `integer` | — | `2` | `open` | — | Šulinio tipas | Šulinio tipas |
| `dujotiekio_linijos_reiksme` | `integer` | — | `2` | `open` | — | Dujotiekio linijos reikšmė | Dujotiekio linijos reikšmė |
| `vandentiekio_linijos_reiksme` | `integer` | — | `2` | `open` | — | Vandentiekio linijos reikšmė | Vandentiekio linijos reikšmė |
| `sil_tiekimo_linijos_reiksme` | `integer` | — | `2` | `open` | — | Šilumos tiekimo linijos reikšmė | Šilumos tiekimo linijos reikšmė |
| `nuoteku_linijos_reiksme` | `integer` | — | `2` | `open` | — | Nuotekų linijos reikšmė | Nuotekų linijos reikšmė |
| `nuoteku_linijos_rusis` | `integer` | — | `2` | `open` | — | Nuotekų linijos rūšis | Nuotekų linijos rūšis |
| `nuoteku_linijos_budas` | `integer` | — | `2` | `open` | — | Nuotekų linijos būdas | Nuotekų linijos tiesimo būdas |
| `nuoteku_irenginio_reiksme` | `integer` | — | `2` | `open` | — | Nuotekų įrenginio reikšmė | Nuotekų įrenginio reikšmė |
| `elektros_linijos_reiksme` | `integer` | — | `2` | `open` | — | Elektros linijos reikšmė | Elektros linijos reikšmė |
| `itampa` | `integer` | — | `2` | `open` | — | Įtampa | Elektros linijos įtampa |
| `elektros_linijos_pobudis` | `integer` | — | `2` | `open` | — | Elektros linijos pobūdis | Elektros linijos pobūdis |
| `kanalo_reiksme` | `integer` | — | `2` | `open` | — | Kanalo reikšmė | Kanalo reikšmė |
| `vamzdziu_kiekis_kanale` | `integer` | — | `2` | `open` | — | Vamzdžių kiekis kanale | Vamzdžių kiekis kanale |
| `naftotiekio_linijos_reiksme` | `integer` | — | `2` | `open` | — | Naftotiekio linijos reikšmė | Naftotiekio linijos reikšmė |
| `irenginiu_parko_rusis` | `integer` | — | `2` | `open` | — | Įrenginių parko rūšis | Įrenginių parko rūšis |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_inzineriniai_statiniai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_inzineriniai_statiniai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_inzineriniai_statiniai (https://data.gov.lt/datasets/1814/)
