---
type: Table
title: "Individ2008 — Asmens ūkio duomenys 2008m."
description: "Amžius, lytis, giminystės ryšiai, išsilavinimas, ekonominio aktyvumo statusas ir kt."
resource: "https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Individ2008"
tags: [gov, lsd, individ2008, deployed, cadence-quadrennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L159"
    title: "atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L159"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1630/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Individ2008 — Asmens ūkio duomenys 2008m.

Amžius, lytis, giminystės ryšiai, išsilavinimas, ekonominio aktyvumo statusas ir kt.[^manifest]

- **Model:** `datasets/gov/lsd/namu_ukio_biudzetas/Individ2008`[^manifest]
- **Dataset:** [Namų ūkių biudžeto statistinio tyrimo duomenys](../namu_ukio_biudzetas.md) (`datasets/gov/lsd/namu_ukio_biudzetas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/namu_ukio_biudzetas.csv#L159](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L159)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Individ2008` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUADRENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh_ident` | `integer` | — | — | `open` | — | Namų ūkio ID | — |
| `line` | `integer` | — | — | `open` | — | Namų ūkio nario eilės Nr. | — |
| `relation` | `integer` | — | — | `open` | — | Ryšys su namų ūkio galva | — |
| `mother` | `integer` | — | — | `open` | — | Motinos Eil. Nr. | — |
| `father` | `integer` | — | — | `open` | — | Tėvo Eil. Nr. | — |
| `partner` | `integer` | — | — | `open` | — | Sutuoktinio Eil. Nr. | — |
| `sex` | `integer` | `sex` | — | `open` | — | Lytis | — |
| `age` | `integer` | — | — | `open` | — | Amžius | — |
| `marital` | `integer` | — | — | `open` | — | Šeiminė padėtis | — |
| `educat2` | `integer` | — | — | `open` | — | Namų ūkio nario išsilavinimas | — |
| `study2` | `integer` | — | — | `open` | — | Mokymosi įstaiga, kurioje mokosi namų ūkio narys | — |
| `mainsour` | `integer` | — | — | `open` | — | Pagrindinis pajamų šaltinis | — |
| `whatdid` | `integer` | `enum: bool` | — | `open` | — | Ar per paskutines 7 dienas Jūs dirbote mokamą ar kitas pajamas (pelną) šeimai duodantį darbą? | — |
| `work` | `integer` | `enum: bool` | — | `open` | — | Gal Jūs turite darbą ar verslą, kurio praeitą savaitę nedirbote? | — |
| `act1` | `integer` | — | — | `open` | — | Dirbančio namų ūkio nario užimtumo statusas | — |
| `act_st` | `integer` | — | — | `open` | — | Namų ūkio nario ekonominis aktyvumas | — |
| `profes` | `string` | — | — | `open` | — | Kokia Jūsų profesija (pareigos) pagrindiniame darbe? | — |
| `work_1` | `integer` | — | — | `open` | — | Jūsų darbas | — |
| `work_day` | `integer` | `enum: bool` | — | `open` | — | Ar dirbate visą darbo dieną? | — |
| `lookjob` | `integer` | `enum: bool` | — | `open` | — | Ar aktyviai ieškojote darbo paskutines 4 savaites? | — |
| `ablewor` | `integer` | `enum: bool` | — | `open` | — | Jei būtumėte suradęs darbą, ar galėtumėte pradėti dirbti per artimiausias dvi savaites? | — |

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
| `marital` | `1` | — | — | Nevedęs / netekėjusi | — |
| `marital` | `2` | — | — | Vedęs / ištekėjusi | — |
| `marital` | `3` | — | — | Neregistruota santuoka | — |
| `marital` | `4` | — | — | Sutuoktinis gyvena atskirai | — |
| `marital` | `5` | — | — | Našlys (-ė) | — |
| `marital` | `6` | — | — | Išsituokęs (-usi) | — |
| `educat2` | `1` | — | — | Pradinis, nebaigė pradinės mokyklos | — |
| `educat2` | `2` | — | — | Pagrindinis | — |
| `educat2` | `3` | — | — | Vidurinis | — |
| `educat2` | `4` | — | — | Aukštesniojo ir aukštojo išsilavinimo nesuteikiantis povidurinis | — |
| `educat2` | `5` | — | — | Aukštesnysis ir aukštasis | — |
| `study2` | `0` | — | — | Vaikų darželis | — |
| `study2` | `1` | — | — | Bendrojo ugdymo mokykla | — |
| `study2` | `2` | — | — | Profesinio mokymo įstaiga | — |
| `study2` | `3` | — | — | Kolegija | — |
| `study2` | `4` | — | — | Universitetas | — |
| `study2` | `88` | — | — | Nesimoko | — |
| `mainsour` | `1` | — | — | Darbas asmeniniame žemės ūkyje | — |
| `mainsour` | `2` | — | — | Samdomasis darbas žemės ūkio valstybiniame sektoriuje | — |
| `mainsour` | `3` | — | — | Samdomasis darbas žemės ūkio privačiame sektoriuje | — |
| `mainsour` | `4` | — | — | Pajamos iš verslo, amatų | — |
| `mainsour` | `5` | — | — | Samdomasis darbas ne žemės ūkio valstybiniame sektoriuje | — |
| `mainsour` | `6` | — | — | Samdomasis darbas ne žemės ūkio privačiame sektoriuje | — |
| `mainsour` | `7` | — | — | Pajamos iš savarankiškos profesinės veiklos | — |
| `mainsour` | `8` | — | — | Nedarbo socialinio draudimo išmoka | — |
| `mainsour` | `9` | — | — | Stipendija | — |
| `mainsour` | `10` | — | — | Pensijos | — |
| `mainsour` | `11` | — | — | Socialinės išmokos | — |
| `mainsour` | `12` | — | — | Kitas pajamų šaltinis | — |
| `mainsour` | `13` | — | — | Išlaikytinis | — |
| `whatdid` | `1` | — | — | Taip | — |
| `whatdid` | `2` | — | — | Ne | — |
| `whatdid` | `1` | — | — | Vyras | — |
| `whatdid` | `2` | — | — | Moteris | — |
| `work` | `1` | — | — | Taip | — |
| `work` | `2` | — | — | Ne | — |
| `work` | `1` | — | — | Vyras | — |
| `work` | `2` | — | — | Moteris | — |
| `act1` | `1` | — | — | Samdomasis darbuotojas | — |
| `act1` | `2` | — | — | Savarankiškai dirbantis asmuo (išskyrus žemdirbius) | — |
| `act1` | `3` | — | — | Žemdirbys | — |
| `act1` | `4` | — | — | Dirbantis šeimos versle, ūkyje ir negaunantis atlyginimo | — |
| `act_st` | `1` | — | — | Dirbantis asmuo | — |
| `act_st` | `2` | — | — | Bedarbis | — |
| `act_st` | `3` | — | — | Senatvės pensininkas | — |
| `act_st` | `4` | — | — | Moksleivis, studentas | — |
| `act_st` | `5` | — | — | Namų šeimininkas (-ė), ekonomiškai neaktyvus asmuo | — |
| `act_st` | `6` | — | — | Neįgalus asmuo | — |
| `profes` | `"01"` | — | — | Ginkluotosios pajėgos | — |
| `profes` | `"11"` | — | — | Įstatymų leidėjai ir vyresnieji pareigūnai | — |
| `profes` | `"12"` | — | — | Direktoriai ir vyriausieji valdytojai | — |
| `profes` | `"13"` | — | — | Individualių įmonių savininkai | — |
| `profes` | `"21"` | — | — | Fizinių mokslų ir indžinierijos specialistai | — |
| `profes` | `"22"` | — | — | Gyvosios gamtos mokslų ir sveikatos priežiūros specialistai | — |
| `profes` | `"23"` | — | — | Mokymo specialistai | — |
| `profes` | `"24"` | — | — | Kiti specialistai | — |
| `profes` | `"31"` | — | — | Fizinių mokslų ir indžinierijos jaunesnieji specialistai | — |
| `profes` | `"32"` | — | — | Jaunesnieji gyvosios gamtos mokslų ir sveikatos priežiūros specialistai | — |
| `profes` | `"33"` | — | — | Mokymo jaunesnieji specialistai | — |
| `profes` | `"34"` | — | — | Kiti jaunesnieji specialistai | — |
| `profes` | `"41"` | — | — | Įstaigų tarnautojai | — |
| `profes` | `"42"` | — | — | Klientų aptarnavimo tarnautojai | — |
| `profes` | `"51"` | — | — | Paslaugų asmenims ir apsaugos darbuotojai | — |
| `profes` | `"52"` | — | — | Pardavėjai, madų ir prekių demonstruotojai | — |
| `profes` | `"61"` | — | — | Kvalifikuoti prekinio žemės ūkio ir žuvininkystės darbininkai | — |
| `profes` | `"62"` | — | — | Žemės ūkio ir žuvininkystės darbininkai, patys save išsilaikantys | — |
| `profes` | `"71"` | — | — | Gavybos ir statybos darbininkai | — |
| `profes` | `"72"` | — | — | Metalo apdirbimo,mašinų gamybos ir giminiškų prof.darbininkai | — |
| `profes` | `"73"` | — | — | Tiksliųjų prietaisų,rankų darbo gaminių,spausdinimo ir susijusių profesijų darbininkai | — |
| `profes` | `"74"` | — | — | Kiti amatininkai ir susijusių profesijų darbininkai | — |
| `profes` | `"81"` | — | — | Pramoninių įrenginių operatoriai | — |
| `profes` | `"82"` | — | — | Mašinų operatoriai ir surinkėjai | — |
| `profes` | `"83"` | — | — | Vairuotojai ir kilnojamųjų įrenginių operatoriai | — |
| `profes` | `"91"` | — | — | Prekybos ir aptarnavimo sferos nekvalif. darbuotojai | — |
| `profes` | `"92"` | — | — | Nekvalif. žemės ūki0,žuvininkystės darbininkai | — |
| `profes` | `"93"` | — | — | Nekvalif.gavybos,statybos,pramonės,transporto darbininkai | — |
| `profes` | `"99"` | — | — | Neatsakė | — |
| `work_1` | `1` | — | — | Nuolatinis | — |
| `work_1` | `2` | — | — | Laikinas | — |
| `work_day` | `1` | — | — | Taip | — |
| `work_day` | `2` | — | — | Ne | — |
| `work_day` | `1` | — | — | Vyras | — |
| `work_day` | `2` | — | — | Moteris | — |
| `lookjob` | `1` | — | — | Taip | — |
| `lookjob` | `2` | — | — | Ne | — |
| `lookjob` | `1` | — | — | Vyras | — |
| `lookjob` | `2` | — | — | Moteris | — |
| `ablewor` | `1` | — | — | Taip | — |
| `ablewor` | `2` | — | — | Ne | — |
| `ablewor` | `1` | — | — | Vyras | — |
| `ablewor` | `2` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv#L159 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L159)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/namu_ukio_biudzetas (https://data.gov.lt/datasets/1630/)
