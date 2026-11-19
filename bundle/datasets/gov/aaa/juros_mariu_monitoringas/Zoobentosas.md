---
type: Table
title: "Zoobentosas — Kuršių marių ir Baltijos jūros zoobentoso tyrimų duomenys"
description: "Spinta table datasets/gov/aaa/juros_mariu_monitoringas/Zoobentosas (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/Zoobentosas"
tags: [gov, aaa, zoobentosas, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L84"
    title: "atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv#L84"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1790/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/juros_mariu_monitoringas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Zoobentosas — Kuršių marių ir Baltijos jūros zoobentoso tyrimų duomenys

- **Model:** `datasets/gov/aaa/juros_mariu_monitoringas/Zoobentosas`[^manifest]
- **Dataset:** [Kuršių marių ir Baltijos jūros valstybinio monitoringo duomenys](../juros_mariu_monitoringas.md) (`datasets/gov/aaa/juros_mariu_monitoringas`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/juros_mariu_monitoringas.csv#L84](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L84)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/Zoobentosas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `reg_nr`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv#L84 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L84)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/juros_mariu_monitoringas (https://data.gov.lt/datasets/1790/)
