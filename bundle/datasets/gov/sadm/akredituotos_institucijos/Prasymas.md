---
type: Table
title: "Prasymas — Prašymai istaigų, teikti akredituotas socialines paslaugas"
description: "Spinta table datasets/gov/sadm/akredituotos_institucijos/Prasymas (47 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sadm/akredituotos_institucijos/Prasymas"
tags: [gov, sadm, prasymas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/akredituotos_institucijos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/sadm/akredituotos_institucijos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4118/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sadm/akredituotos_institucijos"
    author: "team:vda"
    last_modified: "2026-10-22T00:00:00Z"
---

# Prasymas — Prašymai istaigų, teikti akredituotas socialines paslaugas

- **Model:** `datasets/gov/sadm/akredituotos_institucijos/Prasymas`[^manifest]
- **Dataset:** [Prašymai teikti akredituotas socialines paslaugas](../akredituotos_institucijos.md) (`datasets/gov/sadm/akredituotos_institucijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/akredituotos_institucijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/akredituotos_institucijos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/akredituotos_institucijos/Prasymas` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `prasymo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-22`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prasymo_id` | `string` | — | `4` | `open` | — | Įrašo ID | — |
| `submission_date` | `date` | `D` | `4` | `open` | — | Pateikimo data | — |
| `form_type` | `string` | — | `4` | `open` | — | Prašymai teikti akredituotas paslaugas | — |
| `organization_code` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `organization_name` | `string` | — | `4` | `open` | — | Juridinio asmens pavadinimas | — |
| `website` | `string` | — | `4` | `open` | — | Tinklalapio adresas | — |
| `decision_to_provide` | `string` | — | `4` | `open` | — | Sprendimo leisti teikti paslaugas data | — |
| `decision_to_stop` | `date` | `D` | `4` | `open` | — | Sprendimas stabdyti data | — |
| `decision_to_terminate` | `date` | `D` | `4` | `open` | — | Sprendimo nutraukti paslaugų teikimą data | — |
| `count_of_children` | `integer` | — | `4` | `open` | — | Priimamų asmenų skaičius | — |
| `employees_total` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius paslaugai teikti | — |
| `full_time_employment` | `number` | — | `4` | `open` | — | Etatų skaičius paslaugai teikti | — |
| `employees_with_specified_education` | `integer` | — | `4` | `open` | — | Socialiniai darbuotojai, įgiję įstatyme nurodytą išsilavinimą | — |
| `employees_assistants_with_specified_education` | `integer` | — | `4` | `open` | — | Socialinio darbuotojo padėjėjai, lankomosios priežiūros darbuotojai, įgiję reikalavimuose nustatytą išsilavinimą ar kvalifikaciją | — |
| `employees_assistants_with_introduction_training` | `integer` | — | `4` | `open` | — | Socialinio darbuotojo padėjėjai, lankomosios priežiūros darbuotojai, išklausę 40 a. val. įžanginius mokymus | — |
| `employees_care_coordinator` | `integer` | — | `4` | `open` | — | Globos koordinatoriai – globos centro specialistai, atestuoti asmenys, įgiję reikalavimuose nustatytą išsilavinimą | — |
| `employees_other` | `integer` | — | `4` | `open` | — | Kiti darbuotojai | — |
| `accept_with_physical_disabilities` | `boolean` | — | `4` | `open` | — | Gali priimti vaikus su fizine negalia | — |
| `accept_with_mental_disabilities` | `boolean` | — | `4` | `open` | — | Gali priimti vaikus su proto ir (ar) psichine negalia | — |
| `accept_with_emotional_disorders` | `boolean` | — | `4` | `open` | — | Gali priimti vaikus, turinčius elgesio, emocijų sutrikimus | — |
| `suitable_for_disabled` | `boolean` | — | `4` | `open` | — | Patalpos pritaikytos turintiems fizinę negalią | — |
| `negalios_pobudis_judejimo` | `boolean` | — | `4` | `open` | — | Negalios pobūdis (judėjimo) | — |
| `negalios_pobudis_regos` | `boolean` | — | `4` | `open` | — | Negalios pobūdis (regos) | — |
| `negalios_pobudis_intelekto` | `boolean` | — | `4` | `open` | — | Negalios pobūdis (intelekto) | — |
| `negalios_pobudis_psichikos` | `boolean` | — | `4` | `open` | — | Negalios pobūdis (psichikos) | — |
| `negalios_pobudis_klausos` | `boolean` | — | `4` | `open` | — | Negalios pobūdis (klausos) | — |
| `negalios_pobudis_kita` | `boolean` | — | `4` | `open` | — | Negalios pobūdis (kitas) | — |
| `neigalumo_lygis_lengvas` | `boolean` | — | `4` | `open` | — | Neįgalumo lygiai (lengvas) | — |
| `neigalumo_lygis_vidutinis` | `boolean` | — | `4` | `open` | — | Neįgalumo lygiai (vidutinis) | — |
| `neigalumo_lygis_sunkus` | `boolean` | — | `4` | `open` | — | Neįgalumo lygiai (sunkus) | — |
| `darbingumo_lygis_iki_25` | `boolean` | — | `4` | `open` | — | Darbingumo lygis (iki 25%) | — |
| `darbingumo_lygis_nuo_30_iki_40` | `boolean` | — | `4` | `open` | — | Darbingumo lygis (nuo 30% iki 40%) | — |
| `darbingumo_lygis_nuo_45_iki_55` | `boolean` | — | `4` | `open` | — | Darbingumo lygis (nuo 45% iki 55%) | — |
| `specialuju_poreikiu_lygis_vidutinis` | `boolean` | — | `4` | `open` | — | Spec.poreikių lygis (vidutinis) | — |
| `specialuju_poreikiu_lygis_didelis` | `boolean` | — | `4` | `open` | — | Spec.poreikių lygis (didelis) | — |
| `buveines_savivaldybe` | `string` | — | `4` | `open` | — | Buveinės savivaldybė | — |
| `platuma_wgs_buveines` | `number` | — | `4` | `open` | — | Buveinės WGS platuma | — |
| `ilguma_wgs_buveines` | `number` | — | `4` | `open` | — | Buveinės WGS ilguma | — |
| `x_koord_lks_buveines` | `integer` | — | `4` | `open` | — | Buveinės X koordinatės LKS sistemoje | — |
| `y_koord_lks_buveines` | `integer` | — | `4` | `open` | — | Buveinės Y koordinatės LKS sistemoje | — |
| `geometrija_buveines` | `geometry(point, 3346)` | — | `4` | `open` | — | Geometrija buveinės | — |
| `teikimo_savivaldybe` | `string` | — | `4` | `open` | — | Teikimo savivaldybė | — |
| `platuma_wgs_teikimo` | `number` | — | `4` | `open` | — | Teikimo WGS platuma | — |
| `ilguma_wgs_teikimo` | `number` | — | `4` | `open` | — | Teikimo WGS ilguma | — |
| `x_koord_lks_teikimo` | `integer` | — | `4` | `open` | — | Teikimo X koordinatės LKS sistemoje | — |
| `y_koord_lks_teikimo` | `integer` | — | `4` | `open` | — | Teikimo Y koordinatės LKS sistemoje | — |
| `geometrija_teikimo` | `geometry(point, 3346)` | — | `4` | `open` | — | Geometrija teikimo | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `form_type` | `"1"` | `1` | — | Prašymai teikti akredituotą socialinę priežiūrą (iki 2024-07-01) | — |
| `form_type` | `"2"` | `2` | — | Prašymai teikti akredituotą socialinę priežiūra ir laikino atokvėpio paslaugas. | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/akredituotos_institucijos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/akredituotos_institucijos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sadm/akredituotos_institucijos (https://data.gov.lt/datasets/4118/)
