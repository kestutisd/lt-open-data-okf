---
type: Table
title: "EvakuacijosPunktas"
description: "Gyventojų surinkimo punktai – tai vietos, į kurias turės susirinkti gyventojai."
resource: "https://get.data.gov.lt/datasets/gov/pagd/evakuacijos_punktai/EvakuacijosPunktas"
tags: [gov, pagd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pagd/evakuacijos_punktas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/evakuacijos_punktas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# EvakuacijosPunktas

Gyventojų surinkimo punktai – tai vietos, į kurias turės susirinkti gyventojai.

- **Model:** `datasets/gov/pagd/evakuacijos_punktai/EvakuacijosPunktas`[^manifest]
- **Dataset:** [pagd evakuacijos punktai](../evakuacijos_punktai.md) (`datasets/gov/pagd/evakuacijos_punktai`)
- **Manifest CSV:** [datasets/gov/pagd/evakuacijos_punktas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/evakuacijos_punktas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/evakuacijos_punktai/EvakuacijosPunktas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | valstybės duomenų agentūros įrašų identifikatorius | — |
| `apskritis` | `string` | — | `4` | `open` | — | Apskrities pavadinimas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | Gyvenvietės pavadinimas | — |
| `gatve` | `string` | — | `4` | `open` | — | Gatvės pavadinimas | — |
| `namo_numeris` | `string` | — | `4` | `open` | — | Namo numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Statinio, patalpos, inžinerinio įrenginio ar kito objekto, kuriame įrengtas evakavimo punktas, pavadinimas | — |
| `valdytojas` | `string` | — | `4` | `open` | — | Statinio, patalpos, inžinerinio įrenginio ar kito objekto, kuriame įrengtas evakavimo punktas, valdytojas | — |
| `evakavimo_punkto_tipas` | `string` | — | `4` | `open` | — | Gyventojų evakavimo punkto tipas (surinkimo, tarpinis, priėmimo) | — |
| `plotas` | `number` | `m²` | `4` | `open` | — | Evakuavimo punkto patalpų bendras plotas kv. m. | — |
| `gyventoju_skaicius` | `integer` | — | `4` | `open` | — | Evakavimo punkte numatytas aptarnauti gyventojų skaičius | — |
| `pritaikyta_asmenims_su_negalia` | `boolean` | — | `4` | `open` | — | Ar evakavimo punktas pritaikytas asmenims su negalia? (TAIP-1) | — |
| `sutampa_su_priedanga` | `boolean` | — | `4` | `open` | — | Evakavimo punktas sutampa su priedanga (TAIP-1) | — |
| `sutampa_su_kas` | `boolean` | — | `4` | `open` | — | Evakavimo punktas sutampa su kolektyvinės apsaugos statiniu (TAIP-1) | — |
| `kaupiamas_vanduo_maistas` | `boolean` | — | `4` | `open` | — | Ar kaupiamos kitos atsargos (vanduo, maistas ir pan.) (TAIP-1) | — |
| `atsargos` | `string` | — | `4` | `open` | — | Kokios atsargos kaupiamos | — |
| `kaupiamos_abc_priemones` | `boolean` | — | `4` | `open` | — | Ar kaupiamos apsaugos priemonės nuo cheminių ar biologinių grėsmių (TAIP-1) | — |
| `abc_priemones` | `string` | — | `4` | `open` | — | Kokios priemonės nuo cheminių ir biologinių grėsmių kaupiamos | — |
| `taskas_lks` | `geometry(3346)` | — | `4` | `open` | — | Koordinate lks 94 formatu | — |
| `taskas_wgs` | `geometry(4326)` | — | `4` | `open` | — | Koordinate wgs 84 formatu | — |
| `wgs_lon_ilguma` | `number` | — | `4` | `open` | — | WGS koordinatė (ilguma) paskaičiuota iš normuotų LKS koordinačių | — |
| `wgs_lat_platuma` | `number` | — | `4` | `open` | — | WGS koordinatė (platuma) paskaičiuota iš normuotų LKS koordinačių | — |
| `lks_x` | `integer` | — | `4` | `open` | — | Sunormuota LKS x koordinatė (7 skaitmenys) | — |
| `lks_y` | `integer` | — | `4` | `open` | — | Sunormuota LKS y koordinatė (6 skaitmenys) | — |
| `evakuacijos_punkto_nuotrauka` | `integer` | — | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/evakuacijos_punktas.csv
