---
type: Table
title: "MokyklosPatalpa — Bendrojo ugdymo institucijų kitų patalpų (pvz.: valgyklų, sporto salių, bibliotekų) duomenys"
description: "Lentelėje pateikti bendrojo ugdymo institucijų turimų kitų, ne klasės tipo, patalpų (pvz.: valgyklų, sporto salių, bibliotekų) skaičiai kiekvienų mokslo metų spalio 1 d. (pradedant 2013-2014 mokslo metais)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/svis/mokyklu_kitos_patalpos/MokyklosPatalpa"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# MokyklosPatalpa — Bendrojo ugdymo institucijų kitų patalpų (pvz.: valgyklų, sporto salių, bibliotekų) duomenys

Lentelėje pateikti bendrojo ugdymo institucijų turimų kitų, ne klasės tipo, patalpų (pvz.: valgyklų, sporto salių, bibliotekų) skaičiai kiekvienų mokslo metų spalio 1 d. (pradedant 2013-2014 mokslo metais). Duomenys paimti iš Nacionalinės švietimo agentūros (NŠA) Švietimo valdymo informacinės sistemos (ŠVIS). Duomenys atsinaujina kiekvieno mėnesio pirmąją dieną.

- **Model:** `datasets/gov/nsa/svis/mokyklu_kitos_patalpos/MokyklosPatalpa`[^manifest]
- **Dataset:** [Bendrojo ugdymo institucijų kitų patalpų (pvz.: valgyklų, sporto salių, bibliotekų) duomenys](../mokyklu_kitos_patalpos.md) (`datasets/gov/nsa/svis/mokyklu_kitos_patalpos`)
- **Manifest CSV:** [datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/svis/mokyklu_kitos_patalpos/MokyklosPatalpa`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `mokslo_metai` | `string` | — | `4` | `open` | — | Mokslo metai | — |
| `inst_kodas` | `string` | — | `4` | `open` | — | Institucijos arba padalinio juridinio asmens kodas | — |
| `inst_pavadinimas` | `string` | — | `4` | `open` | — | Institucijos arba padalinio pavadinimas | — |
| `inst_priklausomybe` | `string` | — | `4` | `open` | — | Institucijos arba padalinio administracinė priklausomybė | — |
| `inst_tipas` | `string` | — | `4` | `open` | — | Institucijos arba padalinio tipas | — |
| `inst_savivaldybe` | `string` | — | `4` | `open` | — | Institucijos arba padalinio savivaldybė | — |
| `koord_x` | `number` | — | `4` | `open` | — | Institucijos arba padalinio x koordinatė (LKS-94) | — |
| `koord_y` | `number` | — | `4` | `open` | — | Institucijos arba padalinio y koordinatė (LKS-94) | — |
| `valgykla` | `integer` | `U` | `4` | `open` | — | Valgyklų skaičius (vnt.) | — |
| `medicinos_kabinetas` | `integer` | `U` | `4` | `open` | — | Medicinos kabinetų skaičius (vnt.) | — |
| `sporto_sale` | `integer` | `U` | `4` | `open` | — | Sporto salių skaičius (vnt.) | — |
| `aerobikos_sale` | `integer` | `U` | `4` | `open` | — | Aerobikos salių skaičius (vnt.) | — |
| `atletines_gimnastikos_sale` | `integer` | `U` | `4` | `open` | — | Atletinės gimnastikos salių skaičius (vnt.) | — |
| `biblioteka` | `integer` | `U` | `4` | `open` | — | Bibliotekų skaičius (vnt.) | — |
| `skaitykla` | `integer` | `U` | `4` | `open` | — | Skaityklų skaičius (vnt.) | — |
| `mokomosios_dirbtuves` | `integer` | `U` | `4` | `open` | — | Mokomųjų dirbtuvių skaičius (vnt.) | — |
| `mokyklos_muziejus` | `integer` | `U` | `4` | `open` | — | Mokyklos muziejų skaičius (vnt.) | — |
| `baseinas` | `integer` | `U` | `4` | `open` | — | Baseinų skaičius (vnt.) | — |
| `stadionas` | `integer` | `U` | `4` | `open` | — | Stadionų skaičius (vnt.) | — |
| `aikstynas` | `integer` | `U` | `4` | `open` | — | Aikštynų skaičius (vnt.) | — |
| `aikste` | `integer` | `U` | `4` | `open` | — | Aikščių skaičius (vnt.) | — |
| `mokyklos_autobusu_skaicius` | `integer` | `U` | `4` | `open` | — | Mokyklos autobusų skaičius (vnt.) | — |
| `is_ju_geltonuju_autobusu_skaicius` | `integer` | `U` | `4` | `open` | — | Mokyklos geltonųjų autobusų skaičius (vnt.) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `inst_kodas` | `create(property: "ja_kodas", type: "ref", ref: "datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/svis/mokyklu_kitos_patalpos.csv
