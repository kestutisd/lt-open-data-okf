---
type: Table
title: "Individ2012 — Asmens duomenys 2012m."
description: "Amžius, lytis, giminystės ryšiai, išsilavinimas, ekonominio aktyvumo statusas ir kt."
resource: "https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Individ2012"
tags: [gov, lsd, individ2012, deployed, cadence-quadrennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L757"
    title: "atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L757"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1630/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Individ2012 — Asmens duomenys 2012m.

Amžius, lytis, giminystės ryšiai, išsilavinimas, ekonominio aktyvumo statusas ir kt.[^manifest]

- **Model:** `datasets/gov/lsd/namu_ukio_biudzetas/Individ2012`[^manifest]
- **Dataset:** [Namų ūkių biudžeto statistinio tyrimo duomenys](../namu_ukio_biudzetas.md) (`datasets/gov/lsd/namu_ukio_biudzetas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/namu_ukio_biudzetas.csv#L757](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L757)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Individ2012` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUADRENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh_ident` | `integer` | — | — | `open` | — | — | — |
| `line` | `integer` | — | — | `open` | — | — | — |
| `age` | `integer` | — | — | `open` | — | — | — |
| `sex` | `integer` | `sex` | — | `open` | — | — | — |
| `relation` | `integer` | — | — | `open` | — | — | — |
| `partner` | `integer` | — | — | `open` | — | — | — |
| `father` | `integer` | — | — | `open` | — | — | — |
| `mother` | `integer` | — | — | `open` | — | — | — |
| `marital` | `integer` | — | — | `open` | — | — | — |
| `study2` | `integer` | — | — | `open` | — | — | — |
| `educat2` | `integer` | — | — | `open` | — | — | — |
| `whatdid` | `integer` | `enum: bool` | — | `open` | — | — | — |
| `work` | `integer` | `enum: bool` | — | `open` | — | — | — |
| `work_day` | `integer` | `enum: bool` | — | `open` | — | — | — |
| `soc_gru1` | `integer` | — | — | `open` | — | — | — |
| `work_1` | `integer` | — | — | `open` | — | — | — |
| `work_pr` | `integer` | — | — | `open` | — | — | — |
| `profes` | `integer` | — | — | `open` | — | — | — |
| `soc_gru2` | `integer` | — | — | `open` | — | — | — |
| `lookjob` | `integer` | `enum: bool` | — | `open` | — | — | — |
| `ablewor` | `integer` | `enum: bool` | — | `open` | — | — | — |
| `act_st` | `integer` | — | — | `open` | — | — | — |
| `filter_` | `integer` | — | — | `open` | — | — | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `relation` | `1` | — | — | Namų ūkio galva | — |
| `relation` | `2` | — | — | Vyras / žmona / sugyventinis (-ė) | — |
| `relation` | `3` | — | — | Sūnus /duktė / įsūnis / įdukra / posūnis / podukra / globotinis (-ė) | — |
| `relation` | `4` | — | — | Tėvas / motina / įtėvis / įmotė / patėvis / pamotė / globėjas (-a) | — |
| `relation` | `5` | — | — | Sutuoktinio (-ės) / sugyventinio (-ės) tėvas / motina | — |
| `relation` | `6` | — | — | Brolis / sesuo | — |
| `relation` | `7` | — | — | Žentas / marti | — |
| `relation` | `8` | — | — | Vaikaitis (-ė) | — |
| `relation` | `9` | — | — | Kitas (-a) giminaitis (-ė) | — |
| `relation` | `10` | — | — | Ne giminė | — |
| `marital` | `1` | — | — | Niekada nebuvo susituokęs (-usi) | — |
| `marital` | `2` | — | — | Susituokęs (-usi) | — |
| `marital` | `3` | — | — | Neregistruota santuoka | — |
| `marital` | `4` | — | — | Našlys (-ė) | — |
| `marital` | `5` | — | — | Išsituokęs (-usi) | — |
| `study2` | `1` | — | — | Bendrojo ugdymo mokykla | — |
| `study2` | `2` | — | — | Profesinio mokymo įstaiga | — |
| `study2` | `3` | — | — | Kolegija | — |
| `study2` | `4` | — | — | Universitetas | — |
| `study2` | `5` | — | — | Lanko kursus (kalbų, kompiuterių, kt.) | — |
| `educat2` | `1` | — | — | Pradinis, nebaigė pradinės mokyklos | — |
| `educat2` | `2` | — | — | Pagrindinis | — |
| `educat2` | `3` | — | — | Vidurinis | — |
| `educat2` | `4` | — | — | Aukštesniojo ir aukštojo išsilavinimo nesuteikiantis povidurinis | — |
| `educat2` | `5` | — | — | Aukštesnysis ir aukštasis | — |
| `whatdid` | `1` | — | — | Taip | — |
| `whatdid` | `2` | — | — | Ne | — |
| `whatdid` | `1` | — | — | Vyras | — |
| `whatdid` | `2` | — | — | Moteris | — |
| `work` | `1` | — | — | Taip | — |
| `work` | `2` | — | — | Ne | — |
| `work` | `1` | — | — | Vyras | — |
| `work` | `2` | — | — | Moteris | — |
| `work_day` | `1` | — | — | Taip | — |
| `work_day` | `2` | — | — | Ne | — |
| `work_day` | `1` | — | — | Vyras | — |
| `work_day` | `2` | — | — | Moteris | — |
| `soc_gru1` | `1` | — | — | Samdomasis darbuotojas (dirbantis pagal rašytinę darbo sutartį ar žodinį susitarimą ir gaunantis atlyginimą, išrinktas į Seimą, politinės partijos vadovus ar pan.) | — |
| `soc_gru1` | `2` | — | — | Savarankiškai dirbantis ir samdantis darbuotojus asmuo | — |
| `soc_gru1` | `3` | — | — | Savarankiškai, be samdomųjų darbuotojų dirbantis asmuo | — |
| `soc_gru1` | `4` | — | — | Ūkininkas su samdomaisiais darbuotojais | — |
| `soc_gru1` | `5` | — | — | Ūkininkas be samdomųjų darbuotojų, smulkus žemdirbys | — |
| `soc_gru1` | `6` | — | — | Padedantis šeimos narys, dirbantis šeimos įmonėje ar ūkyje (negaunantis atlyginimo, bet turintis pelno, pajamų) | — |
| `work_1` | `1` | — | — | Nuolatinis, nes dirbate pagal neterminuotą darbo sutartį | — |
| `work_1` | `2` | — | — | Laikinas, nes dirbate pagal terminuotą darbo sutartį arba be sutarties | — |
| `work_pr` | `1` | — | — | Viešoji (daugiau kaip 50 % kapitalo priklauso valstybei) | — |
| `work_pr` | `2` | — | — | Privati (daugiau kaip 50 % kapitalo priklauso privatiems asmenims) | — |
| `profes` | `1` | — | — | Ginkluotųjų pajėgų karininkai, generolai ir admirolai | — |
| `profes` | `2` | — | — | Ginkluotųjų pajėgų puskarininkiai, seržantai ir viršilos | — |
| `profes` | `3` | — | — | Ginkluotųjų pajėgų profesijos, kiti laipsniai | — |
| `profes` | `11` | — | — | Teisės aktų leidėjai, vyresnieji valstybės tarnautojai, įmonių, įstaigų, organizacijų ir kiti vadovai | — |
| `profes` | `12` | — | — | Administravimo ir komercijos vadovai | — |
| `profes` | `13` | — | — | Gamybos ir specializuotų paslaugų srities vadovai | — |
| `profes` | `14` | — | — | Viešbučių ir restoranų, mažmeninės prekybos ir kitų paslaugų srities vadovai | — |
| `profes` | `21` | — | — | Fizinių mokslų ir inžinerijos specialistai | — |
| `profes` | `22` | — | — | Sveikatos specialistai | — |
| `profes` | `23` | — | — | Mokymo specialistai | — |
| `profes` | `24` | — | — | Verslo ir administravimo specialistai | — |
| `profes` | `25` | — | — | Informacinių technologijų ir ryšių sistemų specialistai | — |
| `profes` | `26` | — | — | Teisės, socialinės ir kultūros sričių specialistai | — |
| `profes` | `31` | — | — | Jaunesnieji fizinių mokslų ir inžinerijos specialistai | — |
| `profes` | `32` | — | — | Jaunesnieji sveikatos specialistai | — |
| `profes` | `33` | — | — | Jaunesnieji verslo ir administravimo specialistai | — |
| `profes` | `34` | — | — | Jaunesnieji teisės, socialinės srities, kultūros ir giminiškų profesijų specialistai | — |
| `profes` | `35` | — | — | Informacinių ir ryšių sistemų technikai | — |
| `profes` | `41` | — | — | Tarnautojai ir klavišinių įtaisų operatoriai, atliekantys bendras funkcijas | — |
| `profes` | `42` | — | — | Klientų aptarnavimo tarnautojai | — |
| `profes` | `43` | — | — | Apskaitos, statistikos, finansų ir materialinių vertybių apskaitos tarnautojai | — |
| `profes` | `44` | — | — | Kiti tarnautojai | — |
| `profes` | `51` | — | — | Paslaugų asmenims darbuotojai | — |
| `profes` | `52` | — | — | Pardavėjai | — |
| `profes` | `53` | — | — | Asmens priežiūros darbuotojai | — |
| `profes` | `54` | — | — | Apsaugos darbuotojai | — |
| `profes` | `61` | — | — | Kvalifikuoti prekinio žemės ūkio darbuotojai | — |
| `profes` | `62` | — | — | Kvalifikuoti prekinio miškų, žuvininkystės ir medžioklės ūkio darbuotojai | — |
| `profes` | `63` | — | — | Natūraliojo ūkio augalų ir gyvulių augintojai, žvejai, miško gėrybių ir vaistažolių rinkėjai | — |
| `profes` | `71` | — | — | Statybininkai ir giminiškų profesijų darbininkai (išskyrus elektrikus) | — |
| `profes` | `72` | — | — | Metalo apdirbimo, mašinų gamybos ir giminiškų profesijų darbininkai | — |
| `profes` | `73` | — | — | Amatininkai ir spausdinimo darbininkai | — |
| `profes` | `74` | — | — | Elektromechaninių ir elektroninių įrenginių mechanikai | — |
| `profes` | `75` | — | — | Maisto gamintojai, medienos meistrai, siuvėjai ir kiti giminiškų profesijų darbininkai ir amatininkai | — |
| `profes` | `81` | — | — | Stacionariųjų įrenginių ir mašinų operatoriai | — |
| `profes` | `82` | — | — | Surinkėjai | — |
| `profes` | `83` | — | — | Vairuotojai ir judamųjų įrenginių operatoriai | — |
| `profes` | `91` | — | — | Valytojai ir pagalbininkai | — |
| `profes` | `92` | — | — | Nekvalifikuoti žemės, miškų ir žuvininkystės ūkio darbininkai | — |
| `profes` | `93` | — | — | Nekvalifikuoti gavybos, statybos, pramonės ir transporto darbininkai | — |
| `profes` | `94` | — | — | Maisto ruošimo padėjėjai | — |
| `profes` | `95` | — | — | Gatvės pardavėjai, gatvėje teikiamų paslaugų teikėjai | — |
| `profes` | `96` | — | — | Buitinių atliekų surinkėjai ir kiti nekvalifikuoti darbininkai | — |
| `profes` | `99` | — | — | Neatsakė | — |
| `soc_gru2` | `1` | — | — | Bedarbis | — |
| `soc_gru2` | `2` | — | — | Senatvės pensininkas | — |
| `soc_gru2` | `3` | — | — | Moksleivis, studentas | — |
| `soc_gru2` | `4` | — | — | Namų šeimininkas, ekonomiškai neaktyvus asmuo | — |
| `soc_gru2` | `5` | — | — | Neįgalus asmuo | — |
| `lookjob` | `1` | — | — | Taip | — |
| `lookjob` | `2` | — | — | Ne | — |
| `lookjob` | `1` | — | — | Vyras | — |
| `lookjob` | `2` | — | — | Moteris | — |
| `ablewor` | `1` | — | — | Taip | — |
| `ablewor` | `2` | — | — | Ne | — |
| `ablewor` | `1` | — | — | Vyras | — |
| `ablewor` | `2` | — | — | Moteris | — |
| `act_st` | `1` | — | — | Dirbantis asmuo | — |
| `act_st` | `2` | — | — | Bedarbis | — |
| `act_st` | `3` | — | — | Senatvės pensininkas | — |
| `act_st` | `4` | — | — | Moksleivis, studentas | — |
| `act_st` | `5` | — | — | Namų šeimininkas, ekonomiškai neaktyvus asmuo | — |
| `act_st` | `6` | — | — | Neįgalus asmuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L757 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L757)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas (https://data.gov.lt/datasets/1630/)
