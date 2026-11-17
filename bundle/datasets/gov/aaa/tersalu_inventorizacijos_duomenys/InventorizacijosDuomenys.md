---
type: Table
title: "InventorizacijosDuomenys — Aplinkos oro taršos šaltinių ir iš jų išmetamų teršalų inventorizacijos ataskaitos"
description: "Pateikiama informacija apie priimtas ir pratęstas aplinkos oro taršos šaltinių ir iš jų išmetamų teršalų invetorizacijos ataskaitas ar patikslintus inventorizacijos duomenis"
resource: "https://get.data.gov.lt/datasets/gov/aaa/tersalu_inventorizacijos_duomenys/InventorizacijosDuomenys"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# InventorizacijosDuomenys — Aplinkos oro taršos šaltinių ir iš jų išmetamų teršalų inventorizacijos ataskaitos

Pateikiama informacija apie priimtas ir pratęstas aplinkos oro taršos šaltinių ir iš jų išmetamų teršalų invetorizacijos ataskaitas ar patikslintus inventorizacijos duomenis

- **Model:** `datasets/gov/aaa/tersalu_inventorizacijos_duomenys/InventorizacijosDuomenys`[^manifest]
- **Dataset:** [datasets/gov/aaa/tersalu_inventorizacijos_duomenys](../tersalu_inventorizacijos_duomenys.md) (`datasets/gov/aaa/tersalu_inventorizacijos_duomenys`)
- **Manifest CSV:** [datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/tersalu_inventorizacijos_duomenys/InventorizacijosDuomenys`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `savivaldybe` | `string` | — | `4` | `open` | `manifest:1263` | Savivaldybė | Nurodomas pavadinimas savivaldybės, kurioje yra įrenginys(objektas), turintis priimtą/pratęstą inventorizacijos ataskaitą. Savivaldybė – įstatymo nustatytas valstybės teritorijos administracinis vienetas, kurio bendruomenė turi Konstitucijos laiduotą savivaldos teisę, įgyvendinamą per to valstybės teritorijos administracinio vieneto nuolatinių gyventojų išrinktą savivaldybės tarybą, kuri sudaro jai atskaitingas vykdomąją ir kitas savivaldybės institucijas ir įstaigas įstatymams, Lietuvos Respublikos Vyriausybės (toliau – Vyriausybė) ir savivaldybės tarybos sprendimams tiesiogiai įgyvendinti. Savivaldybė yra viešasis juridinis asmuo (LR Vietos savivaldos įst. 3 str.). |
| `vykdytojas` | `string` | — | `4` | `open` | — | Veiklos vykdytojas | Nurodomas veiklos vykdytojo, kurio eksploatuojamo įrenginio (objekto) inventorizacijos ataskaita arba patikslinti inventorizacijos duomenys primti ar pratęsti, pavadinimas. Veiklos vykdytojas - tai fizinis/juridinis asmuo, vykdantis ūkinę ar kitokią veiklą, kurios vykdymo metu iš eksploatuojamų taršos šaltinių išmetami teršalai į aplinkos orą. |
| `objektas` | `string` | — | `4` | `open` | — | Įrenginio (objekto) pavadinimas | Nurodomas įrenginio (objekto) pavadinimas. Įrenginys – stacionarus technikos objektas, kuriame vykdoma viena arba kelių rūšių tiesiogiai ir techniškai susijusi ūkinė veikla (Aplinkos oro taršos šaltinių ir iš jų išmetamų teršalų inventorizacijos ir ataskaitų teikimo taisykles, patvirtintas Lietuvos Respublikos aplinkos ministro 2002 m. birželio 27 d. įsakymu Nr. 340, 3 str.) |
| `adresas` | `string` | — | `4` | `open` | — | Įrenginio (objekto) adresas | Nurodomas tikslus ūkinės veiklos įrenginio (objekto) adresas |
| `metai` | `integer` | — | `4` | `open` | — | Inventorizacijos ataskaitos priėmimo/pratęsimo metai | Informacija atveriama nuo 2019 metų |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `4` | — | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv
