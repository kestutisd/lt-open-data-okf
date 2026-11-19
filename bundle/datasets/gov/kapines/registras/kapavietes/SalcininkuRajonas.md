---
type: Table
title: "SalcininkuRajonas — Šalčininkų rajono savivaldybės kapinių kapaviečių duomenys"
description: "Pateikiami suskaitmenintų Lietuvos savivaldybėms priklausančių kapinių kapaviečių duomenys iš savivaldybių CEMETY ir LIKSGIS informacinių sistemų."
resource: "https://get.data.gov.lt/datasets/gov/kapines/registras/kapavietes/SalcininkuRajonas"
tags: [gov, kapines, salcininkurajonas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/kapavietes.csv#L653"
    title: "atviriduomenys/manifest — datasets/gov/kapines/kapavietes.csv#L653"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2779/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kapines/registras/kapavietes"
    author: "team:vda"
    last_modified: "2026-04-09T00:00:00Z"
---

# SalcininkuRajonas — Šalčininkų rajono savivaldybės kapinių kapaviečių duomenys

**Dataset Context:** Pateikiami suskaitmenintų Lietuvos savivaldybėms priklausančių kapinių kapaviečių duomenys iš savivaldybių CEMETY ir LIKSGIS informacinių sistemų. Aprašomos kapaviečių charakteristikos: ilgis, plotis, dydis, palaidotų velionių skaičius, kapavietės vietos koordinatės bei papildomo pobūdžio informacija. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/kapines/registras/kapavietes/SalcininkuRajonas`[^manifest]
- **Dataset:** [Duomenys apie kapavietes savivaldybių kapinėse](../kapavietes.md) (`datasets/gov/kapines/registras/kapavietes`)[^manifest]
- **Manifest CSV:** [datasets/gov/kapines/kapavietes.csv#L653](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/kapavietes.csv#L653)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kapines/registras/kapavietes/SalcininkuRajonas` (`deployed`)[^manifest]
- **Provider:** `kapines` — Savivaldybių kapinių registro duomenys *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-09`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `kapines` | `string` | — | `4` | `open` | — | Kapavietės kapinių pavadinimas | — |
| `kapo_id` | `string` | — | `4` | `open` | — | Kapavietės identifikatorius | — |
| `kapavietes_dydis` | `number` | `m^2` | `4` | `open` | — | Kapavietės plotas | — |
| `matavimo_vnt` | `string` | — | `3` | `open` | — | Ploto matavimo vienetai | — |
| `palaidotu_sk` | `integer` | `U` | `4` | `open` | — | Kapavietėje palaidotų velionių skaičius | — |
| `maks_velioniu_sk` | `integer` | `U` | `4` | `open` | — | Maksimalus leidžiamas kapavietėje laidoti velionių skaičius | — |
| `tipas` | `string` | — | `4` | `open` | — | Kapavietės tipas | Gali būti kapavietė arba kolumbariumas |
| `ilgis_m` | `number` | `m` | `4` | `open` | — | Kapavietės ilgis, nurodytas metrais. | Kai kapavietės tipas kolumbariumas, stulpelis įgija reikšmę "1". |
| `plotis_m` | `number` | `m` | `4` | `open` | — | Kapavietės plotis, nurodytas metrais | — |
| `geometrija` | `geometry(3857)` | — | `4` | `open` | — | Kapavietės vietos taško koordinatės pagal WGS84 / Pseudo-Mercator koordinačių sistemą. | — |
| `ar_nestandartinis_dydis` | `boolean` | — | `4` | `open` | — | Požymis, ar kapavietė yra nestandartinio dydžio | — |
| `ar_kulturos_paveldas` | `boolean` | — | `4` | `open` | — | Požymis, ar kapavietė yra kultūros paveldo objektas | — |
| `paveldo_kodas` | `string` | — | `4` | `open` | — | Jei kapavietė yra kultūros paveldo objektas, nurodomas paveldo kodas. | — |
| `paveldo_aprasymas_lt` | `string` | — | `2` | `open` | — | Jei kapavietė yra kultūros paveldo objektas, nurodomas aprašymas. | — |
| `pastaba_lt` | `string` | — | `2` | `open` | — | Papildomos pastabos apie kapavietę | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"kapavietė"` | — | — | — | — |
| `tipas` | `"kolumbariumas"` | — | — | Kolumbariumo niša | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paveldo_aprasymas_lt` | `update(property: "paveldo_aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `pastaba_lt` | `update(property: "pastaba_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/kapines/kapavietes.csv#L653 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/kapavietes.csv#L653)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kapines/registras/kapavietes (https://data.gov.lt/datasets/2779/)
