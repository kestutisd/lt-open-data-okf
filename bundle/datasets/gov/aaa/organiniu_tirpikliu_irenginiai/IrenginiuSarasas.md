---
type: Table
title: "IrenginiuSarasas — Organinius tirpiklius naudojančių įrenginių sąrašas"
description: "Spinta table datasets/gov/aaa/organiniu_tirpikliu_irenginiai/IrenginiuSarasas (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/organiniu_tirpikliu_irenginiai/IrenginiuSarasas"
tags: [gov, aaa, irenginiusarasas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1635/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/organiniu_tirpikliu_irenginiai"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# IrenginiuSarasas — Organinius tirpiklius naudojančių įrenginių sąrašas

- **Model:** `datasets/gov/aaa/organiniu_tirpikliu_irenginiai/IrenginiuSarasas`[^manifest]
- **Dataset:** [Organinius tirpiklius naudojančių įrenginių sąrašas](../organiniu_tirpikliu_irenginiai.md) (`datasets/gov/aaa/organiniu_tirpikliu_irenginiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/organiniu_tirpikliu_irenginiai/IrenginiuSarasas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-02-25`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/organiniu_tirpikliu_irenginiai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/organiniu_tirpikliu_irenginiai (https://data.gov.lt/datasets/1635/)
