---
type: Table
title: "Zoobentosas — Kuršių marių ir Baltijos jūros zoobentoso tyrimų duomenys"
description: "Spinta table datasets/gov/aaa/juros_mariu_monitoringas/Zoobentosas (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/Zoobentosas"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L84"
    last_modified: "2026-11-11T14:39:20Z"
---

# Zoobentosas — Kuršių marių ir Baltijos jūros zoobentoso tyrimų duomenys

- **Model:** `datasets/gov/aaa/juros_mariu_monitoringas/Zoobentosas`[^manifest]
- **Dataset:** [datasets/gov/aaa/juros_mariu_monitoringas](../juros_mariu_monitoringas.md) (`datasets/gov/aaa/juros_mariu_monitoringas`)
- **Manifest CSV:** [datasets/gov/aaa/juros_mariu_monitoringas.csv#L84](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L84)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/Zoobentosas`
- **Primary Key (`ref`):** `reg_nr`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_nr` | `string` | — | `2` | `open` | — | Tyrimo registracijos numeris | Registracijos nr. nėra unikalus |
| `data` | `datetime` | `D` | `4` | `open` | — | Mėginio paėmimo data | — |
| `telkinio_pav` | `string` | — | `3` | `open` | — | Vandens telkinio pavadinimas | — |
| `m_vietos_kodas` | `string` | — | `3` | `open` | — | Monitoringo vietos kodas | — |
| `m_vietos_pav` | `string` | — | `3` | `open` | — | Monitoringo vietos pavadinimas | — |
| `m_koordinate` | `geometry(point, 3346)` | — | `3` | `open` | — | Monitoringo vietos koordinatės (LKS-94) | — |
| `tyrim_objektas` | `string` | — | `3` | `open` | — | Tyrimų objektas | — |
| `gylis` | `number` | `m` | `4` | `open` | — | Gylis, iš kurio paimtas mėginys, metrais | — |
| `individu_klase` | `string` | — | `3` | `open` | — | Lotyniškas individų klasės pavadinimas, kuriai priklauso nustatytas taksonas (rūšis) | — |
| `taksonas_rusis` | `string` | — | `3` | `open` | — | Lotyniškas taksono (rūšies) pavadinimas | Kai individas neįdentifikuojamas iki rūšies, nurodomas aukštesnis biologinės klasifikacijos pavadinimas (pvz.: gentis arba šeima arba būrys ir t.t.). |
| `nustatymo_zyme` | `string` | — | `4` | `open` | — | Specialus žymėjimas nenustačius individo iki rūšies | Šis žymėjimas nepriklauso nuo tyrimo metodo. Galimi žymėjimo variantai SP, SPP, VARIA. SP - žymima, kai nėra galimybės arba nereikia nurodyti konkretaus rūšies pavadinimo, SPP - reiškia kelias nenustatytas tos pačios genties rūšis, VARIA - žymima, kai individai idetifikuojami iki klasės. |
| `vystymosi_stadija` | `string` | — | `3` | `open` | — | Taksono (rūšies) vystymosi stadija | — |
| `paemimo_metodas` | `string` | — | `3` | `open` | — | Mėginio paėmimo metodas | — |
| `substrat_biotop` | `string` | — | `3` | `open` | — | Vyraujantis gruntas dugne | — |
| `gausumas` | `number` | — | `3` | `open` | — | Taksono (rūšies) gausumo rezultatas, išreikštas vienetais kvadratiniame metre | — |
| `biomase` | `number` | `g/m^2` | `4` | `open` | — | Taksono (rūšies) biomasės rezultatas, išreikštas gramais kvadratiniame metre | — |
| `tyr_metodas` | `string` | — | `3` | `open` | — | Tyrimų metodas | — |
| `pastabos` | `string` | — | `2` | `open` | — | Pateikiama su tyrimu susijusi svarbi informacija | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gausumas` | `update(ref: "vnt./m^2")` | `ref` | `4` | — | — | — | — |
| `pastabos` | `update(property: "pastabos@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv
