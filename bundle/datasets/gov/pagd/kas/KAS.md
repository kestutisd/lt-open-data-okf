---
type: Table
title: "KAS"
description: "\"Kolektyvinės apsaugos statiniai yra skirti laikinam gyventojų prieglobsčiui saugantis nuo žalingo aplinkos poveikio bei evakuotų gyventojų apsaugai ekstremaliųjų situacijų ar karo metu.\""
resource: "https://get.data.gov.lt/datasets/gov/pagd/kas/KAS"
tags: [gov, pagd, kas, deployed, level-4, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/kas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/pagd/kas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2878/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pagd/kas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KAS

"Kolektyvinės apsaugos statiniai yra skirti laikinam gyventojų prieglobsčiui saugantis nuo žalingo aplinkos poveikio bei evakuotų gyventojų apsaugai ekstremaliųjų situacijų ar karo metu."[^manifest]

- **Model:** `datasets/gov/pagd/kas/KAS`[^manifest]
- **Dataset:** [pagd kolektyvinės apsaugos statiniai](../kas.md) (`datasets/gov/pagd/kas`)[^manifest]
- **Manifest CSV:** [datasets/gov/pagd/kas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/kas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/kas/KAS` (`deployed`)[^manifest]
- **Provider:** `pagd` — Priešgaisrinės apsaugos ir gelbėjimo departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `OTHER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | "valstybės duomenų agentūros įrašų identifikatorius" | — |
| `kas_nuotrauka` | `integer` | — | `4` | `open` | — | "Kolektyvinės apsaugos statinio nuotrauka (tuščia)" | — |
| `seniunija` | `string` | — | `4` | `open` | — | "Seniūnijos pavadinimas" | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | "Gyvenvietės pavadinimas" | — |
| `gatve` | `string` | — | `4` | `open` | — | "Gatvės pavadinimas" | — |
| `namo_numeris` | `string` | — | `4` | `open` | — | "Namo numeris" | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | "Savivaldybės pavadinimas" | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | "Statinio ar patalpos kuriame įrengtas kolektyvinės apsaugos statinys pavadinimas" | — |
| `valdytojas` | `string` | — | `4` | `open` | — | "Statinio ar patalpos kuriame įrengtas kolektyvinės apsaugos statinys valdytojas" | — |
| `darbo_valandos` | `string` | — | `4` | `open` | — | "Jei ribojamas patekimas nurodytos valandos kada galima patekti į patalpas" | — |
| `taskas_lks` | `geometry(3346)` | — | `4` | `open` | — | "Koordinate lks 94 formatu" | — |
| `taskas_wgs` | `geometry(4326)` | — | `4` | `open` | — | "Koordinate wgs 84 formatu" | — |
| `lks_x` | `integer` | — | `4` | `open` | — | "Sunormuota LKS x koordinatė (7 skaitmenys)" | — |
| `lks_y` | `integer` | — | `4` | `open` | — | "Sunormuota LKS y koordinatė (6 skaitmenys)" | — |
| `wgs_lon_ilguma` | `number` | — | `4` | `open` | — | "WGS koordinatė (ilguma) paskaičiuota iš normuotų LKS koordinačių" | — |
| `wgs_lat_platuma` | `number` | — | `4` | `open` | — | "WGS koordinatė (platuma) paskaičiuota iš normuotų LKS koordinačių" | — |
| `apskritis` | `string` | — | `4` | `open` | — | "Apskrities pavadinimas" | — |
| `plotas` | `number` | — | `4` | `open` | — | "Kolektyvinės apsaugos statinio plotas kv. m." | — |
| `atnaujinimo_data` | `date` | `D` | `4` | `open` | — | "Duomenų atnaujinimo data" | — |
| `patekimas_visa_para` | `boolean` | — | `4` | `open` | — | "Ar į patalpas galima patekti visą parą? (TAIP-1)" | — |
| `patalpu_sanitariniai_mazgai` | `boolean` | — | `4` | `open` | — | "Ar patalpose yra veikiantys sanitariniai mazgai? (TAIP-1)" | — |
| `patalpu_apsvietimas` | `boolean` | — | `4` | `open` | — | "Ar patalpose yra apšvietimas? (TAIP-1)" | — |
| `patalpu_ventiliacija` | `boolean` | — | `4` | `open` | — | "Ar patalpose yra ventiliacija? (TAIP-1)" | — |
| `gyventoju_skaicius` | `integer` | — | `4` | `open` | — | "Kolektyvinės apsaugos statinyje talpinamų gyventojų skaičius" | — |
| `evakuavimo_schemos` | `boolean` | — | `4` | `open` | — | "Ar yra evakuavimo schemos (TAIP-1)" | — |
| `pazenklinta` | `boolean` | — | `4` | `open` | — | "Kolektyvinės apsaugos statinys paženklintas (TAIP-1)" | — |
| `sutampa_su_priedanga` | `boolean` | — | `4` | `open` | — | "Kolektyvinės apsaugos statinys sutampa su priedanga (TAIP-1)" | — |
| `kaupiamos_abc_priemones` | `boolean` | — | `4` | `open` | — | "Ar kaupiamos apsaugos priemonės nuo cheminių ar biologinių grėsmių (TAIP-1)" | — |
| `kaupiamas_vanduo_maistas` | `boolean` | — | `4` | `open` | — | "Ar kaupiamos kitos atsargos (vanduo maistas ir t.t.) (TAIP-1)" | — |
| `pritaikyta_asmenims_su_negalia` | `boolean` | — | `4` | `open` | — | "Ar kolektyvinės apsaugos statinys pritaikytas asmenims su negalia? (TAIP-1)" | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/kas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/kas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pagd/kas (https://data.gov.lt/datasets/2878/)
