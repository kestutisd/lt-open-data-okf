---
type: Table
title: "Priedanga"
description: "Priedanga skirta trumpalaikei (iki kelių valandų) apsaugai kilus oro pavojui, nuo tiesioginio ir netiesioginio apšaudymo grėsmės karinės agresijos metu."
resource: "https://get.data.gov.lt/datasets/gov/pagd/priedangos/Priedanga"
tags: [gov, pagd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pagd/priesgaisrines_apsaugos_ir_gelbejimo_departamento_priedangos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/priesgaisrines_apsaugos_ir_gelbejimo_departamento_priedangos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priedanga

Priedanga skirta trumpalaikei (iki kelių valandų) apsaugai kilus oro pavojui, nuo tiesioginio ir netiesioginio apšaudymo grėsmės karinės agresijos metu.

- **Model:** `datasets/gov/pagd/priedangos/Priedanga`[^manifest]
- **Dataset:** [Priesgaisrines apsaugos ir gelbejimo departamento priedangos](../priedangos.md) (`datasets/gov/pagd/priedangos`)
- **Manifest CSV:** [datasets/gov/pagd/priesgaisrines_apsaugos_ir_gelbejimo_departamento_priedangos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/priesgaisrines_apsaugos_ir_gelbejimo_departamento_priedangos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/priedangos/Priedanga`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | valstybės duomenų agentūros įrašų identifikatorius | — |
| `priedangos_nuotrauka` | `integer` | — | `4` | `open` | — | Priedangos nuotrauka (tuščias) | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `gatve` | `string` | — | `4` | `open` | — | Gatvės pavadinimas | — |
| `namo_numeris` | `string` | — | `4` | `open` | — | Namo numeris | — |
| `apskritis` | `string` | — | `4` | `open` | — | Apskrities pavadinimas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | Gyvenvietės pavadinimas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Statinio, patalpos, inžinerinio įrenginio ar kito objekto, kuriame įrengta priedanga, pavadinimas | — |
| `valdytojas` | `string` | — | `4` | `open` | — | Statinio, patalpos, inžinerinio įrenginio ar kito objekto, kuriame įrengta priedanga, valdytojas | — |
| `patalpu_apsvietimas` | `boolean` | — | `4` | `open` | — | Ar patalpose yra apšvietimas? (TAIP-1) | — |
| `patalpu_sanitariniai_mazgai` | `boolean` | — | `4` | `open` | — | Ar patalpose yra veikiantys sanitariniai mazgai? (TAIP-1) | — |
| `patalpu_ventiliacija` | `boolean` | — | `4` | `open` | — | Ar patalpose yra ventiliacija? (TAIP-1) | — |
| `taskas_lks` | `geometry(3346)` | — | `4` | `open` | — | Kordinate lks 94 formatu | — |
| `taskas_wgs` | `geometry(4326)` | — | `4` | `open` | — | Kordinate wgs 84 formatu | — |
| `lks_x` | `integer` | — | `4` | `open` | — | Sunormuota LKS x koordinatė (7 skaitmenys) | — |
| `lks_y` | `integer` | — | `4` | `open` | — | Sunormuota LKS y koordinatė (6 skaitmenys) | — |
| `wgs_lon_ilguma` | `number` | — | `4` | `open` | — | WGS koordinatė (ilguma) paskaičiuota iš normuotų LKS koordinačių | — |
| `wgs_lat_platuma` | `number` | — | `4` | `open` | — | WGS koordinatė (platuma) paskaičiuota iš normuotų LKS koordinačių | — |
| `atnaujinimo_data` | `date` | `D` | `4` | `open` | — | Informacijos atnaujinimo data, (metai (Y) menuo(M) diena(D)) | — |
| `gyventoju_skaicius` | `integer` | — | `4` | `open` | — | Priedangoje talpinamų gyventojų skaičius | — |
| `plotas` | `number` | — | `4` | `open` | — | Priedangos plotas kv. m | — |
| `sutampa_su_kas` | `boolean` | — | `4` | `open` | — | Priedanga sutampa su kolektyvinės apsaugos statiniu (TAIP-1) | — |
| `pritaikyta_asmenims_su_negalia` | `boolean` | — | `4` | `open` | — | Ar priedanga pritaikyta asmenims su negalia? (TAIP-1) | — |
| `darbo_valandos` | `string` | — | `4` | `open` | — | Jei ribojamas patekimas, nurodytos valandos, kada galima patekti į patalpas | — |
| `pazenklinta` | `boolean` | — | `4` | `open` | — | Priedanga paženklinta (TAIP-1) | — |
| `patekimas_visa_para` | `boolean` | — | `4` | `open` | — | Ar į patalpas galima patekti visą parą? (TAIP-1) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/priesgaisrines_apsaugos_ir_gelbejimo_departamento_priedangos.csv
