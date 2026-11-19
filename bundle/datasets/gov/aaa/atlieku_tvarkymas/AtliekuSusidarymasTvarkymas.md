---
type: Table
title: "AtliekuSusidarymasTvarkymas — Atliekų susidarymo ir tvarkymo duomenys"
description: "Spinta table datasets/gov/aaa/atlieku_tvarkymas/AtliekuSusidarymasTvarkymas (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkymas/AtliekuSusidarymasTvarkymas"
tags: [gov, aaa, atliekususidarymastvarkymas, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkymas.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkymas.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/460/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkymas"
    author: "team:vda"
    last_modified: "2026-02-02T00:00:00Z"
---

# AtliekuSusidarymasTvarkymas — Atliekų susidarymo ir tvarkymo duomenys

- **Model:** `datasets/gov/aaa/atlieku_tvarkymas/AtliekuSusidarymasTvarkymas`[^manifest]
- **Dataset:** [Atliekų susidarymo ir tvarkymo duomenys](../atlieku_tvarkymas.md) (`datasets/gov/aaa/atlieku_tvarkymas`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/atlieku_tvarkymas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkymas.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkymas/AtliekuSusidarymasTvarkymas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-02-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | Ataskaitiniai metai |
| `atl_kodas` | `string` | — | `2` | `open` | — | Atliekos kodas | Atliekų klasifikavimo ir atitinkamo kodo pasirinkimo tvarka nurodyta 1 priede, kurio naujausia redakcija išdėstyta įsakyme Nr. D1-1061 "Dėl Lietuvos Respublikos aplinkos ministro 1999 m. liepos 14 d. įsakymo Nr. 217 "Dėl Atliekų tvarkymo taisyklių patvirtinimo" pakeitimo" |
| `pavojingumas` | `boolean` | — | `4` | `open` | — | Pavojingumas | Žymimos pavojingosios atliekos, pagal Atliekų tvarkymo taisykles, kurių naujausia redakcija išdėstyta įsakyme Nr. D1-1061 "Dėl Lietuvos Respublikos aplinkos ministro 1999 m. liepos 14 d. įsakymo Nr. 217 "Dėl Atliekų tvarkymo taisyklių patvirtinimo" pakeitimo" |
| `atl_pavad` | `string` | — | `2` | `open` | — | Atliekos pavadinimas | Atitinkamo kodo atliekų pavadinimas pagal Atliekų tvarkymo taisykles, kurių naujausia redakcija išdėstyta įsakyme Nr. D1-1061 "Dėl Lietuvos Respublikos aplinkos ministro 1999 m. liepos 14 d. įsakymo Nr. 217 "Dėl Atliekų tvarkymo taisyklių patvirtinimo" pakeitimo" |
| `stat_kodas` | `string` | — | `2` | `open` | — | Statistinis kodas | Pagal Europos Parlamento ir Tarybos reglamentą (EB) Nr. 2150/2002 |
| `stat_kodo_pavad` | `string` | — | `2` | `open` | — | Statistinio kodo pavadinimas | Pagal Europos Parlamento ir Tarybos reglamentą (EB) Nr. 2150/2002 |
| `surinkta` | `number` | `t` | `4` | `open` | — | Surinkta | Iš atliekų darytojų ataskaitiniais metais surinktas atliekų kiekis tonomis |
| `susidare` | `number` | `t` | `4` | `open` | — | Susidarė atliekų apdorojimo metu | Kitų atliekų tvarkymo metu atliekų tvarkymo įrenginiuose susidaręs kiekis tonomis |
| `salinim_sav` | `number` | `t` | `4` | `open` | — | Šalinimas sąvartynuose (D1, D5) | Ataskaitiniais metais D1, D5 būdais pašalintas atliekų kiekis tonomis (veiklos būdų kodų reikšmės aprašytos Atliekų tvarkymo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 1999 m. liepos 14 d. įsakymu Nr. 217 "Dėl atliekų tvarkymo taisyklių patvirtinimo", 2 priede) |
| `salinim_kt` | `number` | `t` | `4` | `open` | — | Apdorojimas žemėje (D2), giluminis įpurškimas (D4), surinkimas į telkinius žemės paviršiuje (D6) | Ataskaitiniais metais kitomis šalinimo veiklomis (D2, D4, D6) pašalintas atliekų kiekis tonomis (veiklos būdų kodų reikšmės aprašytos Atliekų tvarkymo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 1999 m. liepos 14 d. įsakymu Nr. 217 "Dėl atliekų tvarkymo taisyklių patvirtinimo", 2 priede) |
| `deg_sausuma` | `number` | `t` | `4` | `open` | — | Deginimas sausumoje (D10) | Ataskaitiniais metais sausumoje sudegintas (D10) atliekų kiekis tonomis (veiklos būdų kodų reikšmės aprašytos Atliekų tvarkymo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 1999 m. liepos 14 d. įsakymu Nr. 217 "Dėl atliekų tvarkymo taisyklių patvirtinimo", 2 priede) |
| `deg_kuras` | `number` | `t` | `4` | `open` | — | Deginimas, naudojant kaip kurą ar kt. būdais energijai gauti (R1) | Ataskaitiniais metais sunaudotas deginant kaip kurą ar kitais būdais išgaunant energiją (R1) atliekų kiekis tonomis (veiklos būdų kodų reikšmės aprašytos Atliekų tvarkymo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 1999 m. liepos 14 d. įsakymu Nr. 217 "Dėl atliekų tvarkymo taisyklių patvirtinimo", 2 priede) |
| `perdirbimas` | `number` | `t` | `4` | `open` | — | Perdirbimas (R2-R9) | Ataskaitiniais metais perdirbtas atliekų kiekis tonomis R2-R9 ir R10' būdais (veiklos būdų kodų reikšmės aprašytos Atliekų tvarkymo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 1999 m. liepos 14 d. įsakymu Nr. 217 "Dėl atliekų tvarkymo taisyklių patvirtinimo", 2 priede) |
| `naudojimas` | `number` | `t` | `4` | `open` | — | Naudojimas (R10, R11) | Ataskaitiniais metais panaudotas (apdorojimas žemėje, naudingas žemės ūkiui ar gerinantis aplinkos būklę (R10), arba atliekų, gautų vykdant bet kurią iš R1– R10 veiklų, panaudojimas (R11) atliekų kiekis tonomis (veiklos būdų kodų reikšmės aprašytos Atliekų tvarkymo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 1999 m. liepos 14 d. įsakymu Nr. 217 "Dėl atliekų tvarkymo taisyklių patvirtinimo", 2 priede) |
| `apdorojimas` | `number` | `t` | `4` | `open` | — | Apdorojimas (D8, D9, D14, R12, S5) | Ataskaitiniais metais apdorotų (tarpinio tvarkymo veiklos būdais D8, D9, D14, R12, S5) atliekų kiekis tonomis (veiklos būdų kodų reikšmės aprašytos Atliekų tvarkymo taisyklių, patvirtintų Lietuvos Respublikos aplinkos ministro 1999 m. liepos 14 d. įsakymu Nr. 217 "Dėl atliekų tvarkymo taisyklių patvirtinimo", 2 priede) |
| `eksportuota` | `number` | `t` | `4` | `open` | — | Eksportuota (S4) | Ataskaitiniais metais eksportuotas atliekų kiekis tonomis |
| `atnaujinta` | `date` | `D` | `4` | `open` | — | Įrašo atnaujinimo data | Duomenų eilutės paskutinio atnaujinimo data |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkymas.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkymas.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkymas (https://data.gov.lt/datasets/460/)
