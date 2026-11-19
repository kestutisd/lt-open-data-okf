---
type: Table
title: "VartIslaid2016B — Natūrinės namų ūkio vartojimo išlaidos (mėnesinės) 2016m."
description: "Natūrinės vartojimo išlaidos, sugrupuotos pagal COICOP klasifikatoriaus klases (keturių ženklų lygiu)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/VartIslaid2016B"
tags: [gov, lsd, vartislaid2016b, deployed, cadence-quadrennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L1643"
    title: "atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L1643"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1630/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VartIslaid2016B — Natūrinės namų ūkio vartojimo išlaidos (mėnesinės) 2016m.

Natūrinės vartojimo išlaidos, sugrupuotos pagal COICOP klasifikatoriaus klases (keturių ženklų lygiu).[^manifest]

- **Model:** `datasets/gov/lsd/namu_ukio_biudzetas/VartIslaid2016B`[^manifest]
- **Dataset:** [Namų ūkių biudžeto statistinio tyrimo duomenys](../namu_ukio_biudzetas.md) (`datasets/gov/lsd/namu_ukio_biudzetas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/namu_ukio_biudzetas.csv#L1643](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L1643)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/VartIslaid2016B` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUADRENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh_ident` | `integer` | — | — | `open` | — | Namų ūkio ID | — |
| `bhe00` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Visos namų ūkio vartojimo išlaidos (mėnesinės) | — |
| `bhe01` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Maisto produktai ir nealkoholiniai gėrimai | — |
| `bhe011` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Maisto produktai | — |
| `bhe0111` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Grūdų produktai | — |
| `bhe0112` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Mėsa ir mėsos produktai | — |
| `bhe0113` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Žuvis | — |
| `bhe0114` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Pienas pieno produktai ir kiaušiniai | — |
| `bhe0115` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Aliejus ir riebalai | — |
| `bhe0116` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Vaisiai ir uogos | — |
| `bhe0117` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Daržovės | — |
| `bhe0118` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Cukrus uogienė medus šokoladas ir saldumynai | — |
| `bhe0119` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Niekur kitur nepriskirti maisto produktai | — |
| `bhe012` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Nealkoholiniai gėrimai | — |
| `bhe0122` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Mineraliniai vandenys gaivieji gėrimai ir sultys | — |
| `bhe02` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Alkoholiniai gėrimai ir tabako gaminiai | — |
| `bhe021` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Alkoholiniai gėrimai | — |
| `bhe0211` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Spirituoti gėrimai | — |
| `bhe04` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Būstas vanduo elektra dujos ir kitas kuras | — |
| `bhe044` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Vandentieka ir kitos įvairios su būstu susijusios paslaugos | — |
| `bhe0441` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Vandentieka | — |
| `bhe0444` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Kitos niekur kitur nepriskirtos su būstu susijusios paslaugos | — |
| `bhe045` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Elektra dujos ir kitas kuras | — |
| `bhe0455` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Šiluminė energija | — |
| `bhe06` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Sveikatos priežiūra | — |
| `bhe061` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Medicinos produktai reikmenys ir įranga | — |
| `bhe0611` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Farmacijos gaminiai | — |
| `bhe0613` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Terapiniai aparatai ir įranga | — |
| `bhe063` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Ligoninių paslaugos | — |
| `bhe07` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Transportas | — |
| `bhe072` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Asmeninių transporto priemonių eksploatacija | — |
| `bhe0722` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Degalai ir tepalai | — |
| `bhe0723` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Priežiūra ir taisymas | — |
| `bhe08` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Ryšiai | — |
| `bhe083` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Telefono ir telefakso paslaugos | — |
| `bhe0830` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Telefono ir telefakso paslaugos | — |
| `bhe10` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Švietimas | — |
| `bhe101` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Ikimokyklinis ir pradinis mokymas | — |
| `bhe1010` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Ikimokyklinis ir pradinis mokymas | — |
| `bhe105` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Švietimo paslaugos neskaidomos pagal lygmenis | — |
| `bhe1050` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Švietimo paslaugos neskaidomos pagal lygmenis | — |
| `bhe11` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Restoranai ir viešbučiai | — |
| `bhe111` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Maitinimo paslaugos | — |
| `bhe1112` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Valgyklos | — |
| `bhe12` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Įvairios prekės ir paslaugos | — |
| `bhe121` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Asmeninė priežiūra | — |
| `bhe1211` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Moterų ir vyrų kirpyklos ir asmens priežiūros įstaigos | — |
| `bhe124` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Socialinės apsaugos paslaugos | — |
| `bhe1240` | `number` | — | — | `open` | — | Natūrinės vartojimo išlaidos.Socialinės apsaugos paslaugos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L1643 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L1643)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas (https://data.gov.lt/datasets/1630/)
