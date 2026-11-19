---
type: Table
title: "NaudojimosiITStatistika"
description: "Spinta table datasets/gov/ivpk/statistika/NaudojimosiITStatistika (46 columns)."
tags: [gov, ivpk, naudojimosiitstatistika, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/statistika.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/statistika.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# NaudojimosiITStatistika

- **Model:** `datasets/gov/ivpk/statistika/NaudojimosiITStatistika`[^manifest]
- **Dataset:** [IVPK statistikos portalo duomenys](../statistika.md) (`datasets/gov/ivpk/statistika`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/statistika.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/statistika.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr, metai, pusmetis`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai kada daryta apklausa | — |
| `pusmetis` | `string` | — | `3` | `open` | — | Pusmetis | — |
| `eil_nr` | `integer` | — | `3` | `open` | — | — | — |
| `b1` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės internetu, nesvarbu kur – namuose, darbe, mokymo įstaigoje, bibliotekoje ar kur nors kitur? | — |
| `b2` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs bent kartą lankėtės tokiose viešųjų institucijų interneto svetainėse, kurios pateiktos kortelėje b5? (rodyti kortelę b5 su paslaugų lentele) | — |
| `b3a` | `integer` | — | `1` | `open` | — | Dėl kokių priežasčių jūs nesilankote viešųjų institucijų interneto svetainėse? (Galimi keli atsakymai) | — |
| `b3b` | `integer` | — | `1` | `open` | — | Kokiu tikslu jūs lankėtės bei kokios informacijos ar paslaugų ieškojote viešųjų institucijų interneto svetainėse? (Galimi keli atsakymai) | — |
| `b4` | `integer` | — | `4` | `open` | — | Kaip jūs vertinate viešųjų institucijų interneto svetainėse pateikiamos informacijos kokybę? | — |
| `b5_1a` | `integer` | — | `4` | `open` | — | — | — |
| `b5_1b` | `integer` | — | `4` | `open` | — | Kaip jūs vertinate šios elektroninės paslaugos kokybę, t.y. Pateikiamos informacijos aiškumą, naudingumą bei patogumą naudotis? | Vertinimui naudokite 10 balų skalę, kur „1“ reiškia „labai žema kokybė“, o „10“ - labai aukšta kokybė“. |
| `b5_2a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – darbo ar darbo skelbimų paieška internetu užimtumo tarnybos tinklalapyje? | — |
| `b5_2b` | `integer` | — | `4` | `open` | — | Kaip jūs vertinate šios elektroninės paslaugos kokybę, t.y. Pateikiamos informacijos aiškumą, naudingumą bei patogumą naudotis? | Vertinimui naudokite 10 balų skalę, kur „1“ reiškia „labai žema kokybė“, o „10“ - labai aukšta kokybė“. |
| `b5_3a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – socialinės apsaugos pašalpų ir išmokų užsakymas / gavimas internetu iš sodros ir savivaldybių? | — |
| `b5_3b` | `integer` | — | `4` | `open` | — | Kaip jūs vertinate 10 balų skalėje šios elektroninės paslaugos kokybę, t.y. Pateikiamos informacijos aiškumą, naudingumą bei patogumą naudotis? | — |
| `b5_4a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – informacijos apie asmens dokumentų išdavimą gavimas internetu ir pasitikrinimas internete dėl tokių dokumentų išdavimo eigos? | — |
| `b5_4b` | `integer` | — | `4` | `open` | — | Kaip jūs vertinate 10 balų skalėje šios elektroninės paslaugos kokybę, t.y. Pateikiamos informacijos aiškumą, naudingumą bei patogumą naudotis? | — |
| `b5_5a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – kelių transporto priemonių registravimo paslaugos? | — |
| `b5_5b` | `integer` | — | `4` | `open` | — | — | — |
| `b5_6a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – statybos leidimų ir kitų su statyba susijusių dokumentų gavimas internetu? | — |
| `b5_6b` | `integer` | — | `4` | `open` | — | — | — |
| `b5_7a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – skundų, pranešimų apie nusikaltimus pateikimas policijai internetu? | — |
| `b5_7b` | `integer` | — | `4` | `open` | — | — | — |
| `b5_8a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – leidinių, publikacijų, esančių viešosiose bibliotekose, paieška, užsakymas, gavimas ir grąžinimas? | — |
| `b5_8b` | `integer` | — | `4` | `open` | — | — | — |
| `b5_9a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – gimimo, mirties, santuokos, ištuokos liudijimų užsakymas internetu? | — |
| `b5_9b` | `integer` | — | `4` | `open` | — | — | — |
| `b5_10a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – paraiškų stoti į aukštąsias mokyklas pateikimas internetu? | — |
| `b5_10b` | `integer` | — | `4` | `open` | — | — | — |
| `b5_11a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – gyvenamosios vietos deklaravimas ar adreso pakeitimas internetu? | — |
| `b5_11b` | `integer` | — | `4` | `open` | — | Kaip jūs vertinate 10 balų skalėje šios elektroninės paslaugos kokybę, t.y. Pateikiamos informacijos aiškumą, naudingumą bei patogumą naudotis? | — |
| `b5_12a` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojotės tokia elektronine paslauga – su sveikatos apsauga susijusios paslaugos internetu? | — |
| `b5_12b` | `integer` | — | `4` | `open` | — | Kaip jūs vertinate 10 balų skalėje šios elektroninės paslaugos kokybę, t.y. Pateikiamos informacijos aiškumą, naudingumą bei patogumą naudotis? | — |
| `b6` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs bent kartą lankėtės elektroninių valdžios vartų portale (www.epaslaugos.lt) ? | — |
| `b7` | `integer` | — | `1` | `open` | — | Kokiu tikslu jūs lankėtės elektroninių valdžios vartų portale (www.epaslaugos.lt)? (Galimi keli atsakymai) | — |
| `b8` | `string` | — | `1` | `open` | — | Kaip jūs vertinate šio elektroninių valdžios vartų portalo su kokybe susijusius atskirus aspektus? | Vertinimui naudokite 10 balų skalę, kur „1“ reiškia „labai žema kokybė“, o „10“ - labai aukšta kokybė“. |
| `b8_1` | `integer` | — | `4` | `open` | — | Elektroninių valdžios vartų portale pateikiamas turinys yra aiškus | — |
| `b8_2` | `integer` | — | `4` | `open` | — | Elektroninių valdžios vartų portale pateikiama informacija yra naudinga | — |
| `b8_3` | `integer` | — | `4` | `open` | — | Elektroninių valdžios vartų portalo navigacija, funkcionalumas, informacijos pateikimas bei turinys yra patogūs vartotojui (8.3) | — |
| `b9` | `integer` | — | `1` | `open` | — | Ar per paskutinius 12 mėnesių jūs susidūrėte su saugos problemomis bendraudami su valstybės ir savivaldybių institucijomis bei įstaigomis internetu, pvz., Susidūrėte su neteisėtu asmens duomenų panaudojimu ar paviešinimu? (Galimi keli atsakymai) | — |
| `b10` | `integer` | — | `4` | `open` | — | Ar jūs pasitikite ar nepasitikite elektroninio bendravimo su viešosiomis institucijomis saugumu? | — |
| `b11` | `string` | — | `1` | `open` | — | Ar per paskutinius 12 mėnesių jūs bent kartą naudojotės šiomis elektroninėmis paslaugomis? | — |
| `b11_1` | `integer` | — | `4` | `open` | — | Lietuvos kultūros paveldo elektroninės paslaugos | — |
| `b11_2` | `integer` | — | `4` | `open` | — | Su lietuvių kalba susijusios elektroninės paslaugos (teksto vertimas, kalbų atpažinimas, žodynai ir pan.) | — |
| `b12` | `integer` | — | `1` | `open` | — | Ar per paskutinius 12 mėnesių jums teko dalyvauti veiklose, susijusiose su elektroninės demokratijos procesais? | Pavyzdžiui, atlikote tam tikrus veiksmus viešojo sektoriaus institucijų svetainėse ar specialiai šiam tikslui sukurtose viešojo sektoriaus institucijų administruojamose svetainėse. |
| `b13` | `integer` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių jūs naudojote asmens tapatybės kortelę tapatybei nustatyti ir / ar patvirtinti elektroninėje erdvėje? | — |
| `b14` | `integer` | — | `4` | `open` | — | Ar jūs jaučiatės saugiai, naudodamiesi internetu? | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `b1` | `1` | — | — | Taip | — |
| `b1` | `2` | — | — | Ne | — |
| `b1` | `9` | — | — | (Neskaityti) Nežino, neatsakė | — |
| `b2` | `1` | — | — | Taip, lankėtės | — |
| `b2` | `2` | — | — | Ne, nesilankėte | — |
| `b2` | `9` | — | — | (Neskaityti) Nežino, neatsakė | — |
| `b3a` | `1` | — | — | Nerandu man reikiamos informacijos (b3a.1) | — |
| `b3a` | `2` | — | — | Pateikiama informacija yra nekokybiška (b3a.2) | — |
| `b3a` | `3` | — | — | Per daug sudėtina naudotis elektroninėmis paslaugomis (b3a.3) | — |
| `b3a` | `4` | — | — | Kitas - Kas? (Nurodyti) (b3a.4) | — |
| `b3a` | `9` | — | — | (Neskaityti) Nežino, neatsakė (b3a.9) | — |
| `b3b` | `1` | — | — | Bendrosios informacijos apie viešąją instituciją ir jos veiklos sritis paieška (b3b.1) | — |
| `b3b` | `2` | — | — | Darbuotojų, jų kontaktinės informacijos paieška (b3b.2) | — |
| `b3b` | `3` | — | — | Informacijos apie viešosios institucijos teikiamas viešąsias paslaugas, jų gavimo tvarką paieška (b3b.3) | — |
| `b3b` | `4` | — | — | Informacijos apie teisės aktus, nutarimus, reikalavimus ir panašios informacijos paieška (b3b.4) | — |
| `b3b` | `5` | — | — | Naudojimasis elektronine viešąja paslauga (b3b.5) | — |
| `b3b` | `6` | — | — | Prašymų, formų ar kitų dokumentų, skirtų pildyti popieriuje, parsisiuntimas (b3b.6) | — |
| `b3b` | `7` | — | — | Paklausimų viešojo sektoriaus institucijai teikimas ar kreipimasis dėl informacijos per elektroninį paštą | — |
| `b3b` | `8` | — | — | Informacijos apie Galimybių pasą paieška ir jo aktyvavimas internetu | — |
| `b3b` | `9` | — | — | Kita – Kas? (Nurodyti) | — |
| `b3b` | `99` | — | — | (Neskaityti) Nežino, neatsakė | — |
| `b4` | `1` | — | — | Teigiamai | — |
| `b4` | `2` | — | — | Greičiau teigiamai | — |
| `b4` | `3` | — | — | Nei teigiamai, nei neigiamai | — |
| `b4` | `4` | — | — | Greičiau neigiamai | — |
| `b4` | `5` | — | — | Neigiamai | — |
| `b4` | `6` | — | — | (Neskaityti) Nežino, neatsakė | — |
| `b5_1a` | `1` | — | — | Taip | — |
| `b5_1a` | `2` | — | — | Ne / neatsakė | — |
| `b5_1b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_1b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_1b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_1b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_1b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_1b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_1b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_1b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_1b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_1b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_1b` | `99` | — | — | N/N | — |
| `b5_2a` | `1` | — | — | Taip | — |
| `b5_2a` | `2` | — | — | Ne / neatsakė | — |
| `b5_2b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_2b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_2b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_2b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_2b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_2b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_2b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_2b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_2b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_2b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_2b` | `99` | — | — | N/N | — |
| `b5_3a` | `1` | — | — | Taip | — |
| `b5_3a` | `2` | — | — | Ne / neatsakė | — |
| `b5_3b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_3b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_3b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_3b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_3b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_3b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_3b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_3b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_3b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_3b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_3b` | `99` | — | — | N/N | — |
| `b5_4a` | `1` | — | — | Taip | — |
| `b5_4a` | `2` | — | — | Ne / neatsakė | — |
| `b5_4b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_4b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_4b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_4b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_4b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_4b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_4b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_4b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_4b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_4b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_4b` | `99` | — | — | N/N | — |
| `b5_5a` | `1` | — | — | Taip | — |
| `b5_5a` | `2` | — | — | Ne / neatsakė | — |
| `b5_5b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_5b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_5b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_5b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_5b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_5b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_5b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_5b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_5b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_5b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_5b` | `99` | — | — | N/N | — |
| `b5_6a` | `1` | — | — | Taip | — |
| `b5_6a` | `2` | — | — | Ne / neatsakė | — |
| `b5_6b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_6b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_6b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_6b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_6b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_6b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_6b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_6b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_6b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_6b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_6b` | `99` | — | — | N/N | — |
| `b5_7a` | `1` | — | — | Taip | — |
| `b5_7a` | `2` | — | — | Ne / neatsakė | — |
| `b5_7b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_7b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_7b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_7b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_7b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_7b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_7b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_7b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_7b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_7b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_7b` | `99` | — | — | N/N | — |
| `b5_8a` | `1` | — | — | Taip | — |
| `b5_8a` | `2` | — | — | Ne / neatsakė | — |
| `b5_8b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_8b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_8b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_8b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_8b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_8b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_8b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_8b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_8b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_8b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_8b` | `99` | — | — | N/N | — |
| `b5_9a` | `1` | — | — | Taip | — |
| `b5_9a` | `2` | — | — | Ne / neatsakė | — |
| `b5_9b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_9b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_9b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_9b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_9b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_9b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_9b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_9b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_9b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_9b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_9b` | `99` | — | — | N/N | — |
| `b5_10a` | `1` | — | — | Taip | — |
| `b5_10a` | `2` | — | — | Ne / neatsakė | — |
| `b5_10b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_10b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_10b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_10b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_10b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_10b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_10b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_10b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_10b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_10b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_10b` | `99` | — | — | N/N | — |
| `b5_11a` | `1` | — | — | Taip | — |
| `b5_11a` | `2` | — | — | Ne / neatsakė | — |
| `b5_11b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_11b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_11b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_11b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_11b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_11b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_11b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_11b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_11b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_11b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_11b` | `99` | — | — | N/N | — |
| `b5_12a` | `1` | — | — | Taip | — |
| `b5_12a` | `2` | — | — | Ne / neatsakė | — |
| `b5_12b` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_12b` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_12b` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_12b` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_12b` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_12b` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_12b` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_12b` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_12b` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_12b` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b5_12b` | `99` | — | — | N/N | — |
| `b6` | `1` | — | — | Taip | — |
| `b6` | `2` | — | — | Ne | — |
| `b6` | `9` | — | — | (Neskaityti) Nežino, neatsakė | — |
| `b7` | `1` | — | — | Užsisakėte ar pasinaudojote elektronine viešąja paslauga (b7.1) | — |
| `b7` | `2` | — | — | Ieškojote informacijos apie institucijų teikiamas elektronines viešąsias paslaugas (b7.2) | — |
| `b7` | `3` | — | — | Ieškojote informacijos apie teisinį elektroninės viešosios paslaugos reglamentavimą (b7.3) | — |
| `b7` | `4` | — | — | Ieškojote informacijos apie viešąją paslaugą teikiančią įstaigą (b7.4) | — |
| `b7` | `5` | — | — | Kita priešastis – Kokia? (Nurodyti) (b7.5) | — |
| `b7` | `9` | — | — | (Neskaityti) Nežino, neatsakė (b7.9) | — |
| `b8` | `"Elektroninių valdžios vartų portale pateikiamas turinys yra aiškus"` | — | — | Elektroninių valdžios vartų portale pateikiamas turinys yra aiškus (8.1) | — |
| `b8` | `"Elektroninių valdžios vartų portale pateikiama informacija yra naudinga"` | — | — | Elektroninių valdžios vartų portale pateikiama informacija yra naudinga (8.2) | — |
| `b8` | `"Elektroninių valdžios vartų portalo navigacija, funkcionalumas, informacijos pateikimas bei turinys yra patogūs vartotojui"` | — | — | Elektroninių valdžios vartų portalo navigacija, funkcionalumas, informacijos pateikimas bei turinys yra patogūs vartotojui (8.3) | — |
| `b8_1` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_1` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_1` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_1` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_1` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_1` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_1` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_1` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_1` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_1` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_1` | `99` | — | — | N/N | — |
| `b8_2` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_2` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_2` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_2` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_2` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_2` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_2` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_2` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_2` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_2` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_2` | `99` | — | — | N/N | — |
| `b8_3` | `1` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_3` | `2` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_3` | `3` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_3` | `4` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_3` | `5` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_3` | `6` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_3` | `7` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_3` | `8` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_3` | `9` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_3` | `10` | — | — | Labai žema kokybė/Labai aukšta kokybė | — |
| `b8_3` | `99` | — | — | N/N | — |
| `b9` | `1` | — | — | Taip, susidūriau su elektroninių viešųjų paslaugų neprieinamumu (b9.1) | — |
| `b9` | `2` | — | — | Taip, susidūriau su duomenų sunaikinimu ar iškraipymu (b9.2) | — |
| `b9` | `3` | — | — | Taip, susidūriau su konfidencialių duomenų atskleidimu (b9.3) | — |
| `b9` | `4` | — | — | Ne, saugos problemų nekilo (b9.4) | — |
| `b9` | `9` | — | — | (Neskaityti) Nežino, neatsakė (b9.9) | — |
| `b10` | `1` | — | — | Visiškai pasitikiu | — |
| `b10` | `2` | — | — | Greičiau pasitikiu | — |
| `b10` | `3` | — | — | Nei pasitikiu, nei nepasitikiu | — |
| `b10` | `4` | — | — | Greičiau nepasitikiu | — |
| `b10` | `5` | — | — | Visiškai nepasitikiu | — |
| `b10` | `9` | — | — | (Neskaityti) Nežino, neatsakė | — |
| `b11` | `"Lietuvos kultūros paveldo elektroninės paslaugos"` | — | — | Lietuvos kultūros paveldo elektroninės paslaugos | — |
| `b11` | `"Su lietuvių kalba susijusios elektroninės paslaugos (teksto vertimas, kalbų atpažinimas, žodynai ir pan.)"` | — | — | Su lietuvių kalba susijusios elektroninės paslaugos (teksto vertimas, kalbų atpažinimas, žodynai ir pan.) | — |
| `b11_1` | `1` | — | — | Taip | — |
| `b11_1` | `2` | — | — | Ne | — |
| `b11_1` | `9` | — | — | Nežino, Neatsakė | — |
| `b11_2` | `1` | — | — | Taip | — |
| `b11_2` | `2` | — | — | Ne | — |
| `b11_2` | `9` | — | — | Nežino, Neatsakė | — |
| `b12` | `1` | — | — | Ieškojote informacijos internete apie viešojo sektoriaus institucijų priimtus ar planuojamus priimti sprendim (b12.1) | — |
| `b12` | `2` | — | — | Pareiškėte savo nuomonę internete dėl viešojo sektoriaus institucijų priimtų ar planuojamų priimti sprendimų (pvz., dalyvavote internete diskusijose, apklausose ar pan.) (b12.2) | — |
| `b12` | `3` | — | — | Pateikėte pasiūlymus internetu dėl viešojo sektoriaus institucijų sprendimų projektų tobulinimo (b12.3) | — |
| `b12` | `4` | — | — | Pats / pati pateikėte (iniciavote) viešojo sektoriaus institucijų sprendimų projektus (b12.4) | — |
| `b12` | `5` | — | — | Kita – Kas? (Nurodyti) (b12.5) | — |
| `b12` | `9` | — | — | (Neskaityti) Nežino, neatsakė (b12.9) | — |
| `b13` | `1` | — | — | Taip, naudojotės | — |
| `b13` | `2` | — | — | Ne, nesinaudojote | — |
| `b13` | `9` | — | — | (Neskaityti) Nežino, neatsakė | — |
| `b14` | `1` | — | — | Visiškai saugiai | — |
| `b14` | `2` | — | — | Greičiau saugiai | — |
| `b14` | `3` | — | — | Nei saugiai, nei nesaugiai | — |
| `b14` | `4` | — | — | Greičiau nesaugiai | — |
| `b14` | `5` | — | — | Visiškai nesaugiai | — |
| `b14` | `9` | — | — | (Neskaityti) Nežino, neatsakė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/statistika.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/statistika.csv#L6)
