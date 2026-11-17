---
type: Table
title: "IrenginiuSarasas — Organinius tirpiklius naudojančių įrenginių sąrašas"
description: "Spinta table datasets/gov/aaa/organiniu_tirpikliu_irenginiai/IrenginiuSarasas (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/organiniu_tirpikliu_irenginiai/IrenginiuSarasas"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# IrenginiuSarasas — Organinius tirpiklius naudojančių įrenginių sąrašas

- **Model:** `datasets/gov/aaa/organiniu_tirpikliu_irenginiai/IrenginiuSarasas`[^manifest]
- **Dataset:** [datasets/gov/aaa/organiniu_tirpikliu_irenginiai](../organiniu_tirpikliu_irenginiai.md) (`datasets/gov/aaa/organiniu_tirpikliu_irenginiai`)
- **Manifest CSV:** [datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/organiniu_tirpikliu_irenginiai/IrenginiuSarasas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `regionas` | `string` | — | `4` | `open` | — | Įrenginio vietos adresas, nurodant regioną | — |
| `vykdytojas` | `string` | — | `4` | `open` | — | Veiklos vykdytojo pavadinimas, veiklos vykdymo vietos (-ų) adresas | — |
| `veikla` | `string` | — | `4` | `open` | — | Vykdomos veiklos rūšies pavadinimas | Nurodoma veiklos rūšis vadovaujantis Lakiųjų organinių junginių, susidarančių naudojant organinius tirpiklius tam tikrų veiklos rūšių įrenginiuose, išmetimo ribojimo ir įrenginių registravimo taisyklėmis, patvirtintomis Lietuvos Respublikos aplinkos ministro 2002 m. gruodžio 5 d. įsakymu Nr. 620 „Dėl Lakiųjų organinių junginių, susidarančių naudojant organinius tirpiklius tam tikrų veiklos rūšių įrenginiuose, išmetimo ribojimo ir įrenginių registravimo taisyklių patvirtinimo“, https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.205122/asr |
| `irenginys` | `string` | — | `4` | `open` | — | Įrenginio pavadinimas, vietos adresas | — |
| `iregistruota` | `string` | — | `4` | `open` | — | Įrenginio įregistravimo data | Organinius tirpiklius naudojantys įrenginiai registruojami vadovaujantis Lakiųjų organinių junginių, susidarančių naudojant organinius tirpiklius tam tikrų veiklos rūšių įrenginiuose, išmetimo ribojimo ir įrenginių registravimo taisyklėmis, patvirtintomis Lietuvos Respublikos aplinkos ministro 2002 m. gruodžio 5 d. įsakymu Nr. 620 „Dėl Lakiųjų organinių junginių, susidarančių naudojant organinius tirpiklius tam tikrų veiklos rūšių įrenginiuose, išmetimo ribojimo ir įrenginių registravimo taisyklių patvirtinimo“. Pateikus įrenginio registracijos duomenis (Taisyklių 6 priede nurodytą informaciją), įrenginys įrašomas į Organinius tirpiklius naudojančių įrenginių sąrašą, https://aaa.lrv.lt/lt/veiklos-sritys/tarsos-prevencija/tirpiklius-naudojantys-irenginiai |
| `tikslinta` | `date` | `D` | `4` | `open` | — | Įrenginio registracijos duomenų patikslinimo pateikimo data (-os) | — |
| `isregistruota` | `date` | `D` | `4` | `open` | — | Įrenginio išregistravimo data | — |
| `suvartojimo_riba` | `string` | — | `4` | `open` | — | Vykdomos veiklos rūšies organinio tirpiklio suvartojimo riba, t/m | Nurodomos Taisyklių 2 priede kiekvienai veiklos rūšiai nurodytų organizuotai ir neorganizuotai išmetamų LOJ ribinės vertės arba bendro išmetamų LOJ kiekio ribinės vertės |
| `ja_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `sprendimas` | `string` | — | `4` | `open` | — | Įrenginio registracijos, jo patikslinimo ar išregistravimo data, sprendimo/rašto išsiuntimo data ir Nr. | — |
| `pastabos` | `string` | — | `4` | `open` | — | Papildoma informacija | — |
| `budas` | `string` | — | `4` | `open` | — | Vykdomo monitoringo būdas | Pateikiamas Taisyklių 33 punkte nurodytas monitoringo būdas (skaičiavimo arba matavimo) ir dažnumas, taikomos išmetamų LOJ (Lakiųjų organinių junginių) ribinės vertės |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iregistruota` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `ja_kodas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `base` | `4` | `open` | — | — | — |
| `pastabos` | `update(property: "pastabos@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv
