---
type: Table
title: "EvakuacijosPunktas"
description: "\"Gyventojų surinkimo punktai – tai vietos, į kurias turės susirinkti gyventojai.\""
resource: "https://get.data.gov.lt/datasets/gov/pagd/evakuacijos_punktai/EvakuacijosPunktas"
tags: [gov, pagd, evakuacijospunktas, deployed, level-4, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/evakuacijos_punktas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/pagd/evakuacijos_punktas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2879/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pagd/evakuacijos_punktai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# EvakuacijosPunktas

"Gyventojų surinkimo punktai – tai vietos, į kurias turės susirinkti gyventojai."[^manifest]

- **Model:** `datasets/gov/pagd/evakuacijos_punktai/EvakuacijosPunktas`[^manifest]
- **Dataset:** [pagd evakuacijos punktai](../evakuacijos_punktai.md) (`datasets/gov/pagd/evakuacijos_punktai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pagd/evakuacijos_punktas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/evakuacijos_punktas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/evakuacijos_punktai/EvakuacijosPunktas` (`deployed`)[^manifest]
- **Provider:** `pagd` — Priešgaisrinės apsaugos ir gelbėjimo departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `OTHER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | "valstybės duomenų agentūros įrašų identifikatorius" | — |
| `apskritis` | `string` | — | `4` | `open` | — | "Apskrities pavadinimas" | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | "Savivaldybės pavadinimas" | — |
| `seniunija` | `string` | — | `4` | `open` | — | "Seniūnijos pavadinimas" | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | "Gyvenvietės pavadinimas" | — |
| `gatve` | `string` | — | `4` | `open` | — | "Gatvės pavadinimas" | — |
| `namo_numeris` | `string` | — | `4` | `open` | — | "Namo numeris" | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | "Statinio, patalpos, inžinerinio įrenginio ar kito objekto, kuriame įrengtas evakavimo punktas, pavadinimas" | — |
| `valdytojas` | `string` | — | `4` | `open` | — | "Statinio, patalpos, inžinerinio įrenginio ar kito objekto, kuriame įrengtas evakavimo punktas, valdytojas" | — |
| `evakavimo_punkto_tipas` | `string` | — | `4` | `open` | — | "Gyventojų evakavimo punkto tipas (surinkimo, tarpinis, priėmimo)" | — |
| `plotas` | `number` | `m²` | `4` | `open` | — | "Evakuavimo punkto patalpų bendras plotas kv. m." | — |
| `gyventoju_skaicius` | `integer` | — | `4` | `open` | — | "Evakavimo punkte numatytas aptarnauti gyventojų skaičius" | — |
| `pritaikyta_asmenims_su_negalia` | `boolean` | — | `4` | `open` | — | "Ar evakavimo punktas pritaikytas asmenims su negalia? (TAIP-1)" | — |
| `sutampa_su_priedanga` | `boolean` | — | `4` | `open` | — | "Evakavimo punktas sutampa su priedanga (TAIP-1)" | — |
| `sutampa_su_kas` | `boolean` | — | `4` | `open` | — | "Evakavimo punktas sutampa su kolektyvinės apsaugos statiniu (TAIP-1)" | — |
| `kaupiamas_vanduo_maistas` | `boolean` | — | `4` | `open` | — | "Ar kaupiamos kitos atsargos (vanduo, maistas ir pan.) (TAIP-1)" | — |
| `atsargos` | `string` | — | `4` | `open` | — | "Kokios atsargos kaupiamos" | — |
| `kaupiamos_abc_priemones` | `boolean` | — | `4` | `open` | — | "Ar kaupiamos apsaugos priemonės nuo cheminių ar biologinių grėsmių (TAIP-1)" | — |
| `abc_priemones` | `string` | — | `4` | `open` | — | "Kokios priemonės nuo cheminių ir biologinių grėsmių kaupiamos" | — |
| `taskas_lks` | `geometry(3346)` | — | `4` | `open` | — | "Koordinate lks 94 formatu" | — |
| `taskas_wgs` | `geometry(4326)` | — | `4` | `open` | — | "Koordinate wgs 84 formatu" | — |
| `wgs_lon_ilguma` | `number` | — | `4` | `open` | — | "WGS koordinatė (ilguma) paskaičiuota iš normuotų LKS koordinačių" | — |
| `wgs_lat_platuma` | `number` | — | `4` | `open` | — | "WGS koordinatė (platuma) paskaičiuota iš normuotų LKS koordinačių" | — |
| `lks_x` | `integer` | — | `4` | `open` | — | "Sunormuota LKS x koordinatė (7 skaitmenys)" | — |
| `lks_y` | `integer` | — | `4` | `open` | — | "Sunormuota LKS y koordinatė (6 skaitmenys)" | — |
| `evakuacijos_punkto_nuotrauka` | `integer` | — | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/evakuacijos_punktas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/evakuacijos_punktas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pagd/evakuacijos_punktai (https://data.gov.lt/datasets/2879/)
