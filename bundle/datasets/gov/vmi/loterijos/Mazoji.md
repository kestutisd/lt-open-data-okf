---
type: Table
title: "Mazoji — Mažųjų verslo loterijų ir lošimų mokesčio deklaracijų duomenys"
description: "Iki 2020-04-30: loterija, kurios organizatorius turi savivaldybės, kurios teritorijoje organizuojama loterija, vykdomosios institucijos licenciją, išduotą vadovaujantis šio Įstatymo reikalavimais, kai loterijos bilietai platinami ir..."
resource: "https://get.data.gov.lt/datasets/gov/vmi/loterijos/Mazoji"
tags: [gov, vmi, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/loterijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/loterijos.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# Mazoji — Mažųjų verslo loterijų ir lošimų mokesčio deklaracijų duomenys

Iki 2020-04-30: loterija, kurios organizatorius turi savivaldybės, kurios teritorijoje organizuojama loterija, vykdomosios institucijos licenciją, išduotą vadovaujantis šio Įstatymo reikalavimais, kai loterijos bilietai platinami ir loterija organizuojama sporto varžybų, kultūros arba kito viešo renginio metu ir laimėjimai išduodami iki renginio pabaigos, ir kurios numatomų išplatinti bilietų nominali vertė neviršija 30 000 eurų.

Nuo 2020-05-01: loterija, kurios bilietai platinami sporto varžybose, kultūros arba kituose viešuose renginiuose, nominalioji numatomų išplatinti bilietų vertė neviršija 30 000 eurų, o piniginiai laimėjimai išmokami, daiktiniai laimėjimai išduodami ar neatlyginama paslauga suteikiama iš karto arba ne vėliau kaip iki renginio pabaigos.

- **Model:** `datasets/gov/vmi/loterijos/Mazoji`[^manifest]
- **Dataset:** [Loterijų verslo loterijų ir lošimų mokesčio deklaracijų (forma FR0583) duomenys](../loterijos.md) (`datasets/gov/vmi/loterijos`)
- **Manifest CSV:** [datasets/gov/vmi/loterijos.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/loterijos.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/loterijos/Mazoji`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ketvirtis` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, ketvirtis | — |
| `metai` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, metai | — |
| `mokescio_suma_b_visa` | `number` | — | `2` | `open` | — | Mokesčio suma | — |
| `moketoju_sk` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mokescio_suma_b_visa` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/loterijos.csv
