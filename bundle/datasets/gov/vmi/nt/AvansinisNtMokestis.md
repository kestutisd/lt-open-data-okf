---
type: Table
title: "AvansinisNtMokestis — Avansinio NT mokesčio duomenys"
description: "Spinta table datasets/gov/vmi/nt/AvansinisNtMokestis (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/nt/AvansinisNtMokestis"
tags: [gov, vmi, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/nt.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L34"
    last_modified: "2026-11-11T14:39:20Z"
---

# AvansinisNtMokestis — Avansinio NT mokesčio duomenys

- **Model:** `datasets/gov/vmi/nt/AvansinisNtMokestis`[^manifest]
- **Dataset:** [Nekilnojamo turto mokesčio duomenų rinkinys](../nt.md) (`datasets/gov/vmi/nt`)
- **Manifest CSV:** [datasets/gov/vmi/nt.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L34)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/nt/AvansinisNtMokestis`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Eilutės numeris | — |
| `sav_kodas` | `integer` | — | `2` | `open` | — | Savivaldybės kodas | Savivaldybės kodas (t. y. savivaldybės kodas, kuriame yra deklaruojamas avansinis NTM) |
| `sav_pav` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `tarifas` | `number` | `%` | `4` | `open` | — | Savivaldybės nustatytas mokesčio tarifas procentais | — |
| `avansinio_ntm_metai` | `integer` | — | `2` | `open` | — | Avansinio NTM metai | — |
| `pozymis_nt_verte` | `string` | — | `2` | `open` | — | Požymis nurodantis NT vertę nurodytais metais ar mėnesį | Požymis, nurodantis ar NT vertė deklaruota už visus metus, ar NT vertė deklaruota pamėnesiui |
| `nt_verte` | `number` | — | `4` | `open` | — | Nuosavo NT vertė nurodytų metų sausio 1 d. arba nurodyto mėnesio 1 d. | Nuosavo NT vertė avansinio NTM metų sausio 1 d. arba nurodyto mėnesio 1 d. (pildo tik juridiniai asmenys, kai apskaičiuota už visus metus NTM suma viršija 500 eurų, priešingu atveju nepildoma) |
| `eilutes_nr_ffdata` | `integer` | — | `2` | `open` | — | Mėnuo. Sutampa su deklaracijos XML paketo eilutės Nr. (eilutės numeris lape pagal FFData numeraciją) | Mėnuo, kurį keitėsi (padidėjo ar sumažėjo) apmokestinamo avansinio NTM vertės (t. y. kai vertė kito metų eigoje, tai pildoma už visus mėnesius atskirai) |
| `avansas_pozymis` | `string` | — | `2` | `open` | — | Požymis nurodantis avansinio mokesčio suma už konkretų ketvirtį ar mėnesį | Požymis, nurodantis ar avansinio mokesčio suma už NTM deklaracijoje nurodytą ketvirtį, ar už mėnesį |
| `avansas` | `number` | — | `4` | `open` | — | Avansinio mokesčio suma už A3 laukelyje įrašytų metų konkretų ketvirtį ar mėnesį | Avansinio mokesčio suma už NTM deklaracijoje nurodytus metus, t. y. avansinio NTM suma už NTM deklaracijos KIT711A priedo A3 laukelyje įrašytų metų konkretų ketvirtį ar mėnesį |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "id")` | `ref` | `4` | `open` | — | — | — |
| `sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `sav_pav` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `4` | — | — | — | — |
| `avansinio_ntm_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `pozymis_nt_verte` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |
| `nt_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `eilutes_nr_ffdata` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |
| `avansas_pozymis` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |
| `avansas` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/nt.csv
