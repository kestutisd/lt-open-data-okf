---
type: Table
title: "VartIsl2008C — Visos namų ūkio vartojimo išlaidos (mėnesinės) 2008m."
description: "Visos vartojimo išlaidos, sugrupuotos pagal COICOP klasifikatoriaus klases (keturių ženklų lygiu)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/VartIsl2008C"
tags: [gov, lsd, vartisl2008c, deployed, cadence-quadrennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L549"
    title: "atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L549"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1630/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VartIsl2008C — Visos namų ūkio vartojimo išlaidos (mėnesinės) 2008m.

Visos vartojimo išlaidos, sugrupuotos pagal COICOP klasifikatoriaus klases (keturių ženklų lygiu).[^manifest]

- **Model:** `datasets/gov/lsd/namu_ukio_biudzetas/VartIsl2008C`[^manifest]
- **Dataset:** [Namų ūkių biudžeto statistinio tyrimo duomenys](../namu_ukio_biudzetas.md) (`datasets/gov/lsd/namu_ukio_biudzetas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/namu_ukio_biudzetas.csv#L549](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L549)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/VartIsl2008C` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUADRENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh_ident` | `integer` | — | — | `open` | — | Namų ūkio ID | — |
| `che00` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Visos namų ūkio vartojimo išlaidos (mėnesinės) | — |
| `che01` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Maisto produktai ir nealkoholiniai gėrimai | — |
| `che011` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Maisto produktai | — |
| `che0111` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Grūdų produktai | — |
| `che0112` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Mėsa ir mėsos produktai | — |
| `che0113` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Žuvis | — |
| `che0114` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Pienas, pieno produktai ir kiaušiniai | — |
| `che0115` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Aliejus ir riebalai | — |
| `che0116` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Vaisiai ir uogos | — |
| `che0117` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Daržovės | — |
| `che0118` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Cukrus, uogienė, medus, šokoladas ir saldumynai | — |
| `che0119` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Niekur kitur nepriskirti maisto produktai | — |
| `che012` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Nealkoholiniai gėrimai | — |
| `che0121` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kava, arbata ir kakava | — |
| `che0122` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Mineraliniai vandenys, gaivieji gėrimai ir sultys | — |
| `che02` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Alkoholiniai gėrimai ir tabako gaminiai | — |
| `che021` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Alkoholiniai gėrimai | — |
| `che0211` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Spirituoti gėrimai | — |
| `che0212` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Vynas | — |
| `che0213` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Alus | — |
| `che022` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Tabakas | — |
| `che0221` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Tabako gaminiai | — |
| `che023` | `integer` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Narkotikai | — |
| `che03` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Apranga ir avalynė | — |
| `che031` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Apranga | — |
| `che0311` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Aprangos medžiagos | — |
| `che0312` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Drabužiai | — |
| `che0313` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kiti aprangos gaminiai ir aprangos reikmenys | — |
| `che0314` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Aprangos valymas, taisymas ir nuoma | — |
| `che032` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Avalynė | — |
| `che0321` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Batai ir kita avalynė | — |
| `che0322` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Avalynės taisymas ir nuoma | — |
| `che04` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Būstas, vanduo, elektra, dujos ir kitas kuras | — |
| `che041` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Būsto nuomos mokesčiai | — |
| `che0411` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Nuomininkų mokami nuomos mokesčiai | — |
| `che0412` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kiti nuomos mokesčiai | — |
| `che043` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Būsto priežiūra ir remontas | — |
| `che0431` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Gaminiai ir medžiagos būsto priežiūrai ir remontui | — |
| `che0432` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Būsto priežiūros ir remonto paslaugos | — |
| `che044` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Vandentieka ir kitos įvairios su būstu susijusios paslaugos | — |
| `che0441` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Vandentieka | — |
| `che0442` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Atliekų rinkimas | — |
| `che0444` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kitos, niekur kitur nepriskirtos, su būstu susijusios paslaugos | — |
| `che045` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Elektra, dujos ir kitas kuras | — |
| `che0451` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Elektra | — |
| `che0452` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Dujos | — |
| `che0453` | `integer` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Skystasis kuras | — |
| `che0454` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kietasis kuras | — |
| `che0455` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Šiluminė energija | — |
| `che05` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Būsto apstatymas, namų apyvokos įranga ir kasdienė namų priežiūra | — |
| `che051` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Baldai ir apstatymas, grindų dangos | — |
| `che0511` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Baldai ir būsto apstatymo reikmenys | — |
| `che0512` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kilimai ir kitos grindų dangos | — |
| `che0513` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Baldų, būsto apstatymo reikmenų ir grindų dangų remontas | — |
| `che052` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Namų ūkio tekstilė | — |
| `che0521` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Namų ūkio tekstilė | — |
| `che053` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Namų apyvokos prietaisai | — |
| `che0531` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Elektriniai ir neelektriniai pagrindiniai namų apyvokos prietaisai | — |
| `che0532` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Smulkūs elektriniai namų apyvokos prietaisai | — |
| `che0533` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Namų apyvokos prietaisų taisymas | — |
| `che054` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Stiklo dirbiniai, stalo reikmenys ir namų rakandai | — |
| `che0541` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Stiklo dirbiniai, stalo reikmenys ir namų rakandai | — |
| `che055` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Namų ir sodininkystės įrankiai bei įranga | — |
| `che0551` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Pagrindiniai buitiniai įrankiai ir įranga | — |
| `che0552` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Smulkūs įrankiai ir įvairūs pagalbiniai reikmenys | — |
| `che056` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Neilgalaikio naudojimo namų apyvokos prekės | — |
| `che0561` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Trumpalaikio naudojimo namų apyvokos prekės | — |
| `che0562` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Namų priežiūros paslaugos | — |
| `che06` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Sveikatos priežiūra | — |
| `che061` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Medicinos produktai, reikmenys ir įranga | — |
| `che0611` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Farmacijos gaminiai | — |
| `che0612` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kiti medicinos gaminiai | — |
| `che0613` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Terapiniai aparatai ir įranga | — |
| `che062` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Ambulatorinės paslaugos | — |
| `che0621` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Gydytojų paslaugos | — |
| `che0622` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Odontologijos paslaugos | — |
| `che0623` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kitos medicinos paslaugos | — |
| `che063` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Ligoninių paslaugos | — |
| `che07` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Transportas | — |
| `che071` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Transporto priemonių pirkimas | — |
| `che0711` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Automobiliai | — |
| `che0712` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Motociklai | — |
| `che0713` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Dviračiai | — |
| `che072` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Asmeninių transporto priemonių eksploatacija | — |
| `che0721` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Atsarginės dalys ir aksesuarai | — |
| `che0722` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Degalai ir tepalai | — |
| `che0723` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Priežiūra ir taisymas | — |
| `che0724` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kitos paslaugos, susijusios su asmeninio transporto priemonėmis | — |
| `che073` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Transporto paslaugos | — |
| `che0731` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Keleivių vežimas geležinkeliu | — |
| `che0732` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Keleivių vežimas keliais | — |
| `che0733` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Keleivių vežimas oru | — |
| `che0734` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Keleivių vežimas jūrų ir vidaus vandenimis | — |
| `che0735` | `integer` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Mišrusis keleivių vežimas | — |
| `che0736` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kitos transporto paslaugos | — |
| `che08` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Ryšiai | — |
| `che081` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Pašto paslaugos | — |
| `che0811` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Pašto paslaugos | — |
| `che082` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Telefonų ir telefaksų įranga | — |
| `che0821` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Telefonų ir telefaksų įranga | — |
| `che083` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Telefono ir telefakso paslaugos | — |
| `che0831` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Telefono ir telefakso paslaugos | — |
| `che09` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Laisvalaikis ir kultūra | — |
| `che091` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Audiovizualiniai, fotografavimo ir duomenų apdorojimo įrenginiai | — |
| `che0911` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Garso ir vaizdo priėmimo, įrašymo ir atkūrimo įrenginiai | — |
| `che0912` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Fotografavimo ir filmavimo įrenginiai ir optiniai prietaisai | — |
| `che0913` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Duomenų apdorojimo įranga | — |
| `che0914` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Įrašų laikmenos | — |
| `che0915` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Audiovizualinių, fotografavimo ir duomenų apdorojimo įrenginių taisymas | — |
| `che092` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kiti ilgalaikio naudojimo reikmenys, skirti laisvalaikiui ir kultūrai | — |
| `che0921` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Pagrindiniai laivalaikiui lauke skirti ilgalaikio naudojimo reikmenys | — |
| `che0922` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Muzikos instrumentai ir pagrindiniai ilgalaikio naudojimo reikmenys, skirti laisvalaikiui patalpose | — |
| `che0923` | `integer` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kitų laisvalaikiui ir kultūrai skirtų pagrindinių ilgalaikio naudojimo reikmenų techninė priežiūra ir remontas | — |
| `che093` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kiti laisvalaikio reikmenys ir įrenginiai, sodininkystės prekės, naminiai gyvūnėliai ir jų priežiūros prekės | — |
| `che0931` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Žaidimai, žaislai ir kolekcionavimo reikmenys | — |
| `che0932` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Įrenginiai sportui, stovyklavimui ir laisvalaikiui lauke | — |
| `che0933` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Gėlės, kiti dekoratiniai augalai | — |
| `che0934` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Naminiai gyvūnėliai ir su jais susiję gaminiai | — |
| `che0935` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Veterinarijos ir kitokios paslaugos, susijusios su naminiais gyvūnėliais | — |
| `che094` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Laisvalaikio ir kultūros paslaugos | — |
| `che0941` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Laisvalaikio ir sporto paslaugos | — |
| `che0942` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kultūros paslaugos | — |
| `che0943` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Azartiniai lošimai | — |
| `che095` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Laikraščiai, knygos ir raštinės reikmenys | — |
| `che0951` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Knygos | — |
| `che0952` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Laikraščiai ir periodiniai leidiniai | — |
| `che0953` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Įvairūs spaudiniai | — |
| `che0954` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Raštinės reikmenys ir piešimo medžiagos | — |
| `che096` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Atostogų išvykos | — |
| `che10` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Švietimas | — |
| `che101` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Ikimokyklinis ir pradinis mokymas | — |
| `che1011` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Ikimokyklinis ir pradinis mokymas | — |
| `che102` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Vidurinis mokymas | — |
| `che1021` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Vidurinis mokymas | — |
| `che103` | `integer` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Aukštojo mokslo laipsnio nesuteikiantis mokymas, baigus vidurinį mokymą | — |
| `che1031` | `integer` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Aukštojo mokslo laipsnio nesuteikiantis mokymas, baigus vidurinį mokymą | — |
| `che104` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Aukštasis mokymas | — |
| `che1041` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Aukštasis mokslas | — |
| `che105` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Švietimo paslaugos, neskaidomos pagal lygmenis | — |
| `che1051` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Švietimo paslaugos, neskaidomos pagal lygmenis | — |
| `che11` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Restoranai ir viešbučiai | — |
| `che111` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Maitinimo paslaugos | — |
| `che1111` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Restoranai, kavinės ir kita | — |
| `che1112` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Valgyklos | — |
| `che112` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Apgyvendinimo paslaugos | — |
| `che1121` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Apgyvendinimo paslaugos | — |
| `che12` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Įvairios prekės ir paslaugos | — |
| `che121` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Asmeninė priežiūra | — |
| `che1211` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Moterų ir vyrų kirpyklos ir asmens priežiūros įstaigos | — |
| `che1212` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Elektriniai asmens priežiūros prietaisai | — |
| `che1213` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kiti neelektriniai asmens priežiūros prietaisai, reikmenys ir priemonės | — |
| `che123` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kiti, niekur kitur nepriskirti, asmeniniai daiktai | — |
| `che1231` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Juvelyriniai dirbiniai ir laikrodžiai | — |
| `che1232` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kiti asmeniniai daiktai | — |
| `che124` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Socialinės apsaugos paslaugos | — |
| `che1241` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Socialinės apsaugos paslaugos | — |
| `che125` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Draudimas | — |
| `che1252` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Namų, turto draudimas | — |
| `che1253` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Sveikatos draudimas | — |
| `che1254` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Transporto priemonių draudimas | — |
| `che1255` | `integer` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kitas draudimas | — |
| `che126` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Banko (finansinės) paslaugos | — |
| `che1262` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Banko (finansinės) paslaugos | — |
| `che127` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kitos, niekur kitur nepriskirtos, paslaugos | — |
| `che1271` | `number` | — | — | `open` | — | Visos (piniginės ir natūrinės) vartojimo išlaidos.Kitos, niekur kitur nepriskirtos, paslaugos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L549 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L549)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas (https://data.gov.lt/datasets/1630/)
