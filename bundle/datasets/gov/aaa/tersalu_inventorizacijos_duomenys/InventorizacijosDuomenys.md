---
type: Table
title: "InventorizacijosDuomenys — Aplinkos oro taršos šaltinių ir iš jų išmetamų teršalų inventorizacijos ataskaitos"
description: "Pateikiama informacija apie priimtas ir pratęstas aplinkos oro taršos šaltinių ir iš jų išmetamų teršalų invetorizacijos ataskaitas ar patikslintus inventorizacijos duomenis"
resource: "https://get.data.gov.lt/datasets/gov/aaa/tersalu_inventorizacijos_duomenys/InventorizacijosDuomenys"
tags: [gov, aaa, inventorizacijosduomenys, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1789/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/tersalu_inventorizacijos_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# InventorizacijosDuomenys — Aplinkos oro taršos šaltinių ir iš jų išmetamų teršalų inventorizacijos ataskaitos

Pateikiama informacija apie priimtas ir pratęstas aplinkos oro taršos šaltinių ir iš jų išmetamų teršalų invetorizacijos ataskaitas ar patikslintus inventorizacijos duomenis[^manifest]

- **Model:** `datasets/gov/aaa/tersalu_inventorizacijos_duomenys/InventorizacijosDuomenys`[^manifest]
- **Dataset:** [Ūkio subjektų aplinkos oro taršos šaltinių ir iš jų išmetamų teršalų inventorizacijų sąrašas](../tersalu_inventorizacijos_duomenys.md) (`datasets/gov/aaa/tersalu_inventorizacijos_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/tersalu_inventorizacijos_duomenys/InventorizacijosDuomenys` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `4` | — | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/tersalu_inventorizacijos_duomenys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/tersalu_inventorizacijos_duomenys (https://data.gov.lt/datasets/1789/)
