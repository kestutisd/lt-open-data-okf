---
type: Table
title: "EismoIvykis"
description: "Spinta table datasets/gov/pd/eiis/EismoIvykis (51 columns)."
tags: [gov, pd, eismoivykis, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/pd/eiis.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# EismoIvykis

- **Model:** `datasets/gov/pd/eiis/EismoIvykis`[^manifest]
- **Dataset:** [datasets/gov/pd/eiis](../eiis.md) (`datasets/gov/pd/eiis`)[^manifest]
- **Manifest CSV:** [datasets/gov/pd/eiis.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pd` — Policijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `registrokodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `registrokodas` | `string` | — | `3` | `open` | — | Registro kodas | — |
| `data_laikas` | `datetime` | `T` | `4` | `open` | — | Įvykio data ir laikas | — |
| `registravimo_data` | `datetime` | `T` | `4` | `open` | — | Registravimo data | — |
| `paskutinio_redagavimo_laikas` | `datetime` | `T` | `4` | `open` | — | Paskutinio redagavimo data | — |
| `iskaitinis` | `integer` | — | `4` | `open` | — | Įskaitinis | — |
| `rusis` | `string` | — | `3` | `open` | — | Įvykio rūšis | — |
| `schema1` | `string` | — | `3` | `open` | — | Schema 1 - detalesnis įvykio aprašymas | — |
| `schema2` | `string` | — | `3` | `open` | — | Schema 2 - detalesnis įvykio aprašymas | — |
| `dalyviu_skaicius` | `integer` | `U` | `4` | `open` | — | Dalyvių skaičius | — |
| `zuvusiu_skaicius` | `integer` | `U` | `4` | `open` | — | Žuvusių skaičius | — |
| `zuvo_vaiku` | `integer` | `U` | `4` | `open` | — | Žuvusių vaikų skaičius | — |
| `suzeistu_skaicius` | `integer` | `U` | `4` | `open` | — | Sužeistų skaičius | — |
| `suzeista_vaiku` | `integer` | `U` | `4` | `open` | — | Sužeistų vaikų skaičius | — |
| `tp_skaicius` | `integer` | `U` | `4` | `open` | — | Transporto priemonių skaičius | — |
| `policijos_tp_skaicius` | `integer` | `U` | `4` | `open` | — | Policijos transporto priemonių skaičius | — |
| `apgadintu_tp_skaicius` | `integer` | `U` | `4` | `open` | — | Apgadintų transporto priemonių skaičius | — |
| `apgadintu_policijos_tp_skaic` | `integer` | `U` | `4` | `open` | — | Apgadintų policijos transporto priemonių skaičius | — |
| `policijos_istaiga_l1` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=3`: `policijos_istaiga_l1.ja_pavadinimas`) | `3` | `open` | — | Policijos įstaiga 1 | — |
| `policijos_istaiga_l2` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=3`: `policijos_istaiga_l2.ja_pavadinimas`) | `3` | `open` | — | Policjos įstaiga 2 | — |
| `iforminusi_istaiga_l1` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=3`: `iforminusi_istaiga_l1.ja_pavadinimas`) | `3` | `open` | — | Įforminusi įstaiga 1 | — |
| `iforminusi_istaiga_l2` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=3`: `iforminusi_istaiga_l2.ja_pavadinimas`) | `3` | `open` | — | Įformunusi įstaiga 2 | — |
| `ivykio_vieta` | `string` | — | `3` | `open` | — | Įvykio vieta | — |
| `vietos_savivaldybe_tipas` | `string` | — | `4` | `open` | — | Savivaldybės tipas | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=2` scalar) | `2` | `open` | — | Savivaldybė | — |
| `gatve` | `ref` | [Gatve](../../rc/ar/gatve/Gatve.md) (`level=2` scalar) | `2` | `open` | — | Gatvė | — |
| `namas` | `ref` | [Patalpa](../../rc/ar/patalpa/Patalpa.md) (`level=2` scalar) | `2` | `open` | — | Namas | — |
| `kita_gatve_sankryzoje` | `string` | — | `3` | `open` | — | Kita gatvė (Jei įvykis įvyko sankryžoje) | — |
| `kelio_pavadinimas` | `ref` | [StateRoad](../../lakd/keliai/StateRoad.md) (`level=2` scalar) | `2` | `open` | — | Kelio pavadinimas | — |
| `kelio_reiksme` | `string` | — | `4` | `open` | — | Kelio reikšmė | — |
| `atstumas` | `number` | — | `3` | `open` | — | Atstumas | — |
| `dangos_rusis` | `string` | — | `4` | `open` | — | Kelio dangos rūšis | — |
| `dangos_bukle` | `string` | — | `4` | `open` | — | Kelio dangos būklė | — |
| `paros_metas` | `string` | — | `4` | `open` | — | Paros metas | — |
| `kelio_apsvietimas` | `string` | — | `4` | `open` | — | Kelio apšvietimas | — |
| `meteo_salygos` | `string` | — | `4` | `open` | — | Meteorologinės sąlygos | — |
| `kitos_oro_salygos[]` | `string` | — | `3` | `open` | — | Oro sąlygos | — |
| `kelio_gatves_kreive` | `string` | — | `4` | `open` | — | Kelio gatvės kreivė | — |
| `nulemiantis_veiksnys` | `string` | — | `3` | `open` | — | Nulemiantis veiksnys | — |
| `kiti_nul_veiksnys[]` | `string` | — | `3` | `open` | — | Papildomi nulemiantys veiksniai | — |
| `atitvarai` | `string` | — | `4` | `open` | — | Atitvarai | — |
| `sankryzos_tipas` | `string` | — | `4` | `open` | — | Sankryžos tipas | — |
| `kelio_elementas1` | `string` | — | `3` | `open` | — | Kelio elementas 1 | — |
| `kelio_elementas2` | `string` | — | `3` | `open` | — | Kelio elementas 2 | — |
| `privalomas_leistinas_greitis` | `integer` | `km/h` | `4` | `open` | — | Privalomas leistinas greitis | — |
| `leistinas_greitis` | `integer` | `km/h` | `4` | `open` | — | Leistinas gretis | — |
| `neblaivus_kaltininkai` | `string` | — | `4` | `open` | — | Neblaivūs kaltininkai | — |
| `apsvaige_kaltininkai` | `string` | — | `4` | `open` | — | Apsvaige kaltininkai | — |
| `atsisake_tikrintis_kaltininkai` | `string` | — | `4` | `open` | — | Atsisake tikrintis balivumą kaltininkai | — |
| `ilguma` | `integer` | — | `3` | `open` | — | Ilguma | — |
| `platuma` | `integer` | — | `3` | `open` | — | Platuma | — |
| `koordinates_lks94` | `geometry(point, 3346)` | `m` | — | — | — | Koordinatės | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `iskaitinis` | `true` | `1` | — | Taip | — |
| `iskaitinis` | `false` | `0` | — | Ne | — |
| `vietos_savivaldybe_tipas` | `"SAVIVALDYBE"` | — | — | Savivaldybė | — |
| `vietos_savivaldybe_tipas` | `"MIESTO_SAVIVALDYBE"` | — | — | Miesto savivaldybė | — |
| `kelio_reiksme` | `"Rajoniniai keliai"` | — | — | Rajoniniai keliai | — |
| `kelio_reiksme` | `"Magistraliniai keliai"` | — | — | Magistraliniai keliai | — |
| `kelio_reiksme` | `"Vietiniai keliai"` | — | — | Vietiniai keliai | — |
| `kelio_reiksme` | `"Krašto keliai"` | — | — | — | — |
| `dangos_rusis` | `"Asfaltbetonis, cementbetonis"` | — | — | Asfaltbetonis, cementbetonis | — |
| `dangos_rusis` | `"Žvyrkelis"` | — | — | Žvyrkelis | — |
| `dangos_rusis` | `"Grindinys"` | — | — | Grindinys | — |
| `dangos_rusis` | `"Be dangos"` | — | — | Be dangos | — |
| `dangos_bukle` | `"Šlapia"` | — | — | Šlapia | — |
| `dangos_bukle` | `"Sausa"` | — | — | Sausa | — |
| `dangos_bukle` | `"Apledėjusi"` | — | — | Apledėjusi | — |
| `dangos_bukle` | `"Apsnigta"` | — | — | Apsnigta | — |
| `paros_metas` | `"Tamsus paros metas"` | — | — | Tamsus paros metas | — |
| `paros_metas` | `"Sutemos"` | — | — | Sutemos | — |
| `paros_metas` | `"Diena"` | — | — | Diena | — |
| `kelio_apsvietimas` | `"Įjungtas"` | — | — | Įjungtas | — |
| `kelio_apsvietimas` | `"Neįrengtas"` | — | — | Neįrengtas | — |
| `kelio_apsvietimas` | `"Neįjungtas"` | — | — | Neįjungtas | — |
| `meteo_salygos` | `"Giedra"` | — | — | — | — |
| `meteo_salygos` | `"Apsiniaukę"` | — | — | — | — |
| `meteo_salygos` | `"Lietus"` | — | — | — | — |
| `meteo_salygos` | `"Sniegas, kruša"` | — | — | — | — |
| `meteo_salygos` | `"Stiprus vėjas"` | — | — | — | — |
| `meteo_salygos` | `"Lijundra"` | — | — | — | — |
| `meteo_salygos` | `"Rūkas"` | — | — | — | — |
| `kelio_gatves_kreive` | `"Tiesus horizontalus ruožas"` | — | — | Tiesus horizontalus ruožas | — |
| `kelio_gatves_kreive` | `"Horizontalus vingis"` | — | — | Horizontalus vingis | — |
| `kelio_gatves_kreive` | `"Tiesi įkalnė"` | — | — | Tiesi įkalnė | — |
| `kelio_gatves_kreive` | `"Tiesi nuokalnė"` | — | — | Tiesi nuokalnė | — |
| `kelio_gatves_kreive` | `"Vingiuota įkalnė"` | — | — | Vingiuota įkalnė | — |
| `kelio_gatves_kreive` | `"Vingiuota nuokalnė"` | — | — | Vingiuota nuokalnė | — |
| `atitvarai` | `"Yra"` | — | — | Atitvarai yra | — |
| `atitvarai` | `"Nėra"` | — | — | Atitvarų nėra | — |
| `sankryzos_tipas` | `"PRIE_SANKRYZOS"` | — | — | Prie sankryžos | — |
| `sankryzos_tipas` | `"NEREGULIUOJAMA"` | — | — | Nereguliuojama | — |
| `sankryzos_tipas` | `"REGULIUOJAMA"` | — | — | Reguliuojama | — |
| `neblaivus_kaltininkai` | `"Ne"` | — | — | Ne | — |
| `neblaivus_kaltininkai` | `"Taip"` | — | — | Taip | — |
| `apsvaige_kaltininkai` | `"Ne"` | — | — | Ne | — |
| `apsvaige_kaltininkai` | `"Taip"` | — | — | Taip | — |
| `atsisake_tikrintis_kaltininkai` | `"Ne"` | — | — | Ne | — |
| `atsisake_tikrintis_kaltininkai` | `"Taip"` | — | — | Taip | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/eiis.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L9)
