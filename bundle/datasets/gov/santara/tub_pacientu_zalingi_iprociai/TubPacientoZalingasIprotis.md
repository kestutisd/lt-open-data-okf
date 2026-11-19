---
type: Table
title: "TubPacientoZalingasIprotis — \"Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai.\""
description: "\"Lentelėje pateikti Tuberkuliozės valstybės informacinės sistemos (TVIS) duomenys apie tuberkuliozės liga diagnozuotus pacientus, jų žalingus įpročius, diagnozes ir mirtis."
resource: "https://get.data.gov.lt/datasets/gov/santara/tub_pacientu_zalingi_iprociai/TubPacientoZalingasIprotis"
tags: [gov, santara, tubpacientozalingasiprotis, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2871/"
    title: "data.gov.lt DCAT-AP — datasets/gov/santara/tub_pacientu_zalingi_iprociai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TubPacientoZalingasIprotis — "Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai."

**Dataset Context:** "Lentelėje pateikti Tuberkuliozės valstybės informacinės sistemos (TVIS) duomenys apie tuberkuliozės liga diagnozuotus pacientus, jų žalingus įpročius, diagnozes ir mirtis. Duomenų valdytojas - Nacionalinio visuomenės sveikatos centro prie Sveikatos apsaugos ministerijos (NVSC). Duomenų tvarkytojas - Vilniaus universiteto ligoninė Santaros klinikos (VULSK). Viena duomenų rinkinio eilutė atspindi vieną pacientą kuriam buvo diagnozuota tuberkuliozės liga. Duomenys apima visos Lietuvos tuberkuliozės liga sirgusius bei sergančius asmenis ir informacinėje sistemoje yra kaupiami nuo 2013 m. Atkreipiame dėmesį, kad paciento identifikacinis kodas nebūtinai reiškia unikalų paciento įrašą - vienas pacientas gali turėti kelis identifikacinius kodus, dėl gyvenamosios vietos pasikeitimo, dėl šios priežasties unikalius pacientų įrašus rekomenduojama nustatyti pagal paciento vardo, pavardės, gimimo datos, asmens kodo ir asmens kodo validacijos stulpelius. Taip pat pažymime kad paciento diagnozė gali kisti, paciento gydymo metu ar atliekant papildomus tyrimus. Be to, Pasaulio sveikatos organizacijos (PSO) tuberkuliozės duomenų kaupimo rekomendacijos keitėsi 1996, 1998, 2000, 2014 metais ir galėjo paveikti duomenų surinkimo metodikas bei surinktų duomenų kokybę.Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/santara/tub_pacientu_zalingi_iprociai/TubPacientoZalingasIprotis`[^manifest]
- **Dataset:** ["Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai."](../tub_pacientu_zalingi_iprociai.md) (`datasets/gov/santara/tub_pacientu_zalingi_iprociai`)[^manifest]
- **Manifest CSV:** [datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/santara/tub_pacientu_zalingi_iprociai/TubPacientoZalingasIprotis` (`deployed`)[^manifest]
- **Provider:** `santara` — VUL Santaros klinikos *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `paciento_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paciento_id` | `string` | — | `4` | `open` | — | Unikalus kodas identifikuojantis pacientą | — |
| `paciento_vardas` | `string` | — | `4` | `open` | — | Paciento vardas | Paciento pseudoniminta vardo reikšmė |
| `paciento_pavarde` | `string` | — | `4` | `open` | — | Paciento pavardė | Paciento pseudoniminta pavardės reikšmė |
| `paciento_gim_data` | `string` | — | `4` | `open` | — | Paciento gimimo data | Paciento pseudoniminta gimimo datos reikšmė |
| `paciento_asmens_kodas` | `string` | — | `4` | `open` | — | Paciento asmens kodas | Paciento pseudoniminta asmens kodo reikšmė |
| `vda_ak_validacija` | `string` | — | `4` | `open` | — | Paciento asmens kodo trūkumai | — |
| `vda_paciento_gim_metai_ak` | `date` | `Y` | `4` | `open` | — | Asmens kode nurodyti paciento gimimo metai | — |
| `paciento_gim_metai` | `date` | `Y` | `4` | `open` | — | Šaltinyje nurodyti Paciento gimimo metai | — |
| `vda_paciento_lytis_ak` | `string` | — | `4` | `open` | — | — | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Asmens kode nurodyta paciento lytis | — |
| `rukymas_id` | `string` | — | `4` | `open` | — | Rūkymo reikšmės identifikatorius šaltinyje | "Šaltinyje nurodyti duomenys apie paciento suvartojamą tabako kiekį. Reikšmės: Iki 10 cigarečių per dieną - 1,11-20 cigarečių per dieną - 2,Virš 20 cigarečių per dieną - 3,Nerūko - 4,Eksrūkorius - 5." |
| `rukymas_reiksme` | `string` | — | `4` | `open` | — | Rūkymo reikšmė | "Šaltinyje nurodyti duomenys apie paciento suvartojamą tabako kiekį. Reikšmės: Iki 10 cigarečių per dieną - 1,11-20 cigarečių per dieną - 2,Virš 20 cigarečių per dieną - 3,Nerūko - 4,Eksrūkorius - 5." |
| `rukymo_stazas_id` | `string` | — | `4` | `open` | — | Rūkymo stažo reikšmės identifikatorius šaltinyje | "Tuberkulioze sergančio ligonio rūkymo stažas (pagal tai,kiek metų ligonis rūko). Reikšmės: Rūko iki 1 metų- 1,Rūko 1 - 10 metų -2,Rūko 11 - 20 metų – 3,Rūko virš 20 metų – 4." |
| `rukymo_stazas_reiksme` | `string` | — | `4` | `open` | — | Rūkymo stažo reikšmė | "Tuberkulioze sergančio ligonio rūkymo stažas (pagal tai,kiek metų ligonis rūko). Reikšmės: Rūko iki 1 metų- 1,Rūko 1 - 10 metų -2,Rūko 11 - 20 metų – 3,Rūko virš 20 metų – 4." |
| `alkoholis_id` | `string` | — | `4` | `open` | — | Alkoholio reikšmės identifikatorius šaltinyje | "Šaltinyje nurodyti duomenys apie žalingą įprotį - alkoholio vartojimą. Reikšmės: nevartoja - 1,vartoja retai - 2,girtauja - 3,alkoholikas - 4." |
| `alkoholis_reiksme` | `string` | — | `4` | `open` | — | Alkoholio vartojimo reikšmė | "Šaltinyje nurodyti duomenys apie žalingą įprotį - alkoholio vartojimą. Reikšmės: nevartoja - 1,vartoja retai - 2,girtauja - 3,alkoholikas - 4." |
| `vda_ligos_kodai` | `string` | — | `4` | `open` | — | Pacientui diagnozuotos ligos | Visų pacientui diagnozuotų ligų kodų (TLK-10) reikšmės atskirtos kabliataškiais |
| `ligos_kodas` | `string` | — | `4` | `open` | — | Naujausios pacientui diagnozuotos ligos kodas | Ligos kodas pagal TLK-10 ligų klasifikatorių |
| `ar_mire_nuo_tub` | `boolean` | — | `4` | `open` | — | Paciento mirties nuo tuberkuliozės reikšmė (true/false) | — |
| `mirties_nuo_tub_d` | `date` | `D` | `4` | `open` | — | Paciento mirties nuo tuberkuliozės data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vda_ak_validacija` | `"Tinkamas"` | — | — | — | — |
| `vda_ak_validacija` | `"Netinkamas ilgis"` | — | — | — | — |
| `vda_ak_validacija` | `"Netinkamas kontrolinis skaitmuo"` | — | — | — | — |
| `vda_ak_validacija` | `"Netinkama gimimo data"` | — | — | — | — |
| `vda_paciento_lytis_ak` | `"Vyras"` | — | — | — | — |
| `vda_paciento_lytis_ak` | `"Moteris"` | — | — | — | — |
| `paciento_lytis` | `"V"` | — | — | — | — |
| `paciento_lytis` | `"M"` | — | — | — | — |
| `rukymas_id` | `"0"` | — | — | — | — |
| `rukymas_id` | `"1"` | — | — | Iki 10 cigarečių per dieną | — |
| `rukymas_id` | `"2"` | — | — | 11-20 cigarečių per dieną | — |
| `rukymas_id` | `"3"` | — | — | Virš 20 cigarečių per dieną | — |
| `rukymas_id` | `"4"` | — | — | Nerūko | — |
| `rukymas_id` | `"5"` | — | — | Eksrūkorius | — |
| `rukymas_reiksme` | `"Iki 10 cigarečių per dieną"` | — | — | id reikšmė šaltinyje: 1 | — |
| `rukymas_reiksme` | `"11-20 cigarečių per dieną"` | — | — | id reikšmė šaltinyje: 2 | — |
| `rukymas_reiksme` | `"Virš 20 cigarečių per dieną"` | — | — | id reikšmė šaltinyje: 3 | — |
| `rukymas_reiksme` | `"Nerūko"` | — | — | id reikšmė šaltinyje: 4 | — |
| `rukymas_reiksme` | `"Eksrūkorius"` | — | — | id reikšmė šaltinyje: 5 | — |
| `rukymo_stazas_id` | `"0"` | — | — | — | — |
| `rukymo_stazas_id` | `"1"` | — | — | iki 1 metų | — |
| `rukymo_stazas_id` | `"2"` | — | — | 1 - 10 metų | — |
| `rukymo_stazas_id` | `"3"` | — | — | 11 - 20 metų | — |
| `rukymo_stazas_id` | `"4"` | — | — | Virš 20 metų | — |
| `rukymo_stazas_reiksme` | `"iki 1 metų"` | — | — | id reikšmė šaltinyje: 1 | — |
| `rukymo_stazas_reiksme` | `"1 - 10 metų"` | — | — | id reikšmė šaltinyje: 2 | — |
| `rukymo_stazas_reiksme` | `"11 - 20 metų"` | — | — | id reikšmė šaltinyje: 3 | — |
| `rukymo_stazas_reiksme` | `"Virš 20 metų"` | — | — | id reikšmė šaltinyje: 4 | — |
| `alkoholis_id` | `"0"` | — | — | — | — |
| `alkoholis_id` | `"1"` | — | — | Nevartoja | — |
| `alkoholis_id` | `"2"` | — | — | Vartoja retai | — |
| `alkoholis_id` | `"3"` | — | — | Girtauja | — |
| `alkoholis_id` | `"4"` | — | — | Alkoholikas | — |
| `alkoholis_reiksme` | `"Nevartoja"` | — | — | id reikšmė šaltinyje: 1 | — |
| `alkoholis_reiksme` | `"Vartoja retai"` | — | — | id reikšmė šaltinyje: 2 | — |
| `alkoholis_reiksme` | `"Girtauja"` | — | — | id reikšmė šaltinyje: 3 | — |
| `alkoholis_reiksme` | `"Alkoholikas"` | — | — | id reikšmė šaltinyje: 4 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/santara/tub_pacientu_zalingi_iprociai (https://data.gov.lt/datasets/2871/)
