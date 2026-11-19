---
type: Table
title: "MoletuRajonas — Molėtų rajono savivaldybės kapinėse palaidotų velionių duomenys"
description: "Rinkinyje pateikiami suskaitmenintose Lietuvos savivaldybėms priklausančiose kapinėse palaidotų velionių duomenys iš savivaldybių CEMETY ir LIKSGIS informacinių sistemų."
resource: "https://get.data.gov.lt/datasets/gov/kapines/registras/velioniai/MoletuRajonas"
tags: [gov, kapines, moleturajonas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/velionys.csv#L441"
    title: "atviriduomenys/manifest — datasets/gov/kapines/velionys.csv#L441"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# MoletuRajonas — Molėtų rajono savivaldybės kapinėse palaidotų velionių duomenys

**Dataset Context:** Rinkinyje pateikiami suskaitmenintose Lietuvos savivaldybėms priklausančiose kapinėse palaidotų velionių duomenys iš savivaldybių CEMETY ir LIKSGIS informacinių sistemų. Nurodomos velionio charakteristikos (vardas, pavardė, lytis, gimimo, mirties ir palaidojimo datos) ir su jo kapaviete susiję duomenys (ryšys su kitais kapavietėje palaidotais asmenimis, kapą prižiūrinčiu asmeniu, kapo gylis, vieta bendrame kapinių plane). Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt[^manifest]

- **Model:** `datasets/gov/kapines/registras/velioniai/MoletuRajonas`[^manifest]
- **Dataset:** [Duomenys apie velionis, palaidotus savivaldybių kapinėse](../velioniai.md) (`datasets/gov/kapines/registras/velioniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kapines/velionys.csv#L441](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/velionys.csv#L441)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kapines/registras/velioniai/MoletuRajonas` (`deployed`)[^manifest]
- **Provider:** `kapines` — Savivaldybių kapinių registro duomenys *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `kapo_id` | `string` | — | `4` | `open` | — | Kapavietės identifikatorius | — |
| `ar_neatpazintas` | `boolean` | — | `4` | `open` | — | Neatpažinto velionio požymis | — |
| `ar_perlaidotas` | `boolean` | — | `4` | `open` | — | Požymis, ar velionis buvo perlaidotas | — |
| `ar_urnoje` | `boolean` | — | `4` | `open` | — | Požymis, ar velionis palaidotas urnoje | — |
| `vardas` | `string` | — | `4` | `open` | — | Velionio vardas | — |
| `pavarde` | `string` | — | `4` | `open` | — | Velionio pavardė | — |
| `lytis` | `string` | — | `4` | `open` | — | Velionio lytis, išskaičiuota iš asmens kodo. | — |
| `ar_izymybe` | `boolean` | — | `4` | `open` | — | Požymis, ar velionis buvo žinomas asmuo | — |
| `veikla_lt` | `string` | — | `1` | `open` | — | Velionio veiklos duomenys | — |
| `aprasymas_lt` | `string` | — | `1` | `open` | — | Velionio gyvenimo veiklos aprašymas | — |
| `gimimo_data` | `date` | `D` | `4` | `open` | — | Velionio gimimo data | — |
| `mirties_data` | `date` | `D` | `4` | `open` | — | Velionio mirties data | — |
| `laidojimo_data` | `date` | `D` | `4` | `open` | — | Velionio laidojimo data | — |
| `liudijimo_isdavimas` | `date` | `D` | `4` | `open` | — | Velionio mirties liudijimo išdavimo data | — |
| `isdavimo_vieta` | `string` | — | `4` | `open` | — | Velionio mirties liudijimo išdavimo vieta | — |
| `kapo_gylis_m` | `integer` | `m` | `4` | `open` | — | Velionio kapo gylis | — |
| `rysys_su_palaidotu` | `string` | — | `4` | `open` | — | Velionio ryšys su kitu kapavietėje palaidotu asmeniu | — |
| `kapa_priziuri` | `string` | — | `4` | — | — | Kapą prižiūrinčio asmens ryšys su velioniu | — |
| `sektorius` | `string` | — | `4` | `open` | — | Velionio kapavietės sektoriaus identifikatorius. Tai yra kapinėse esantis kvartalas, dažnu atveju išskiriamas pagal matomus takus kapinėse arba pagal pateiktą informaciją iš savivaldybių/ seniūnijų. Mažose kapinėse dažniausiai būna tik vienas kvartalas be jokių skirstymų. | — |
| `eile` | `string` | — | `4` | `open` | — | Velionio kapavietės eilė kapinėse, jei ji egzistuoja (ypač naudojama tvarkingo išplanavimo ir naujose kapinėse). Jeigu kapinėse nebuvo naudojamos eilės, tuomet žymima 000. | — |
| `kapaviete` | `string` | — | `4` | `open` | — | Velionio kapavietės numeris kapinėse | — |
| `vieta_kape` | `integer` | — | `4` | `open` | — | Velionio palaidojimo vieta kapavietėje. Pavyzdžiui, 3 vietų kapavietėje per vidurį laidojamam velioniui būtų žymima 2. | — |
| `geometrija` | `geometry(3857)` | — | `4` | `open` | — | Velionio kapavietės vietos taško koordinatės pagal WGS84 / Pseudo-Mercator koordinačių sistemą. | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veikla_lt` | `update(property: "veikla_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/kapines/velionys.csv#L441 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/velionys.csv#L441)
