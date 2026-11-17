---
type: Table
title: "TubPacientoZalingasIprotis — Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai."
description: "Spinta table datasets/gov/santara/tub_pacientu_zalingi_iprociai/TubPacientoZalingasIprotis (20 columns)."
resource: "https://get.data.gov.lt/datasets/gov/santara/tub_pacientu_zalingi_iprociai/TubPacientoZalingasIprotis"
tags: [gov, santara, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# TubPacientoZalingasIprotis — Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai.

- **Model:** `datasets/gov/santara/tub_pacientu_zalingi_iprociai/TubPacientoZalingasIprotis`[^manifest]
- **Dataset:** [Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai.](../tub_pacientu_zalingi_iprociai.md) (`datasets/gov/santara/tub_pacientu_zalingi_iprociai`)
- **Manifest CSV:** [datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/santara/tub_pacientu_zalingi_iprociai/TubPacientoZalingasIprotis`
- **Primary Key (`ref`):** `paciento_id`
- **Level:** `4`

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
| `rukymas_id` | `string` | — | `4` | `open` | — | Rūkymo reikšmės identifikatorius šaltinyje | Šaltinyje nurodyti duomenys apie paciento suvartojamą tabako kiekį. Reikšmės: Iki 10 cigarečių per dieną - 1,11-20 cigarečių per dieną - 2,Virš 20 cigarečių per dieną - 3,Nerūko - 4,Eksrūkorius - 5. |
| `rukymas_reiksme` | `string` | — | `4` | `open` | — | Rūkymo reikšmė | Šaltinyje nurodyti duomenys apie paciento suvartojamą tabako kiekį. Reikšmės: Iki 10 cigarečių per dieną - 1,11-20 cigarečių per dieną - 2,Virš 20 cigarečių per dieną - 3,Nerūko - 4,Eksrūkorius - 5. |
| `rukymo_stazas_id` | `string` | — | `4` | `open` | — | Rūkymo stažo reikšmės identifikatorius šaltinyje | Tuberkulioze sergančio ligonio rūkymo stažas (pagal tai,kiek metų ligonis rūko). Reikšmės: Rūko iki 1 metų- 1,Rūko 1 - 10 metų -2,Rūko 11 - 20 metų – 3,Rūko virš 20 metų – 4. |
| `rukymo_stazas_reiksme` | `string` | — | `4` | `open` | — | Rūkymo stažo reikšmė | Tuberkulioze sergančio ligonio rūkymo stažas (pagal tai,kiek metų ligonis rūko). Reikšmės: Rūko iki 1 metų- 1,Rūko 1 - 10 metų -2,Rūko 11 - 20 metų – 3,Rūko virš 20 metų – 4. |
| `alkoholis_id` | `string` | — | `4` | `open` | — | Alkoholio reikšmės identifikatorius šaltinyje | Šaltinyje nurodyti duomenys apie žalingą įprotį - alkoholio vartojimą. Reikšmės: nevartoja - 1,vartoja retai - 2,girtauja - 3,alkoholikas - 4. |
| `alkoholis_reiksme` | `string` | — | `4` | `open` | — | Alkoholio vartojimo reikšmė | Šaltinyje nurodyti duomenys apie žalingą įprotį - alkoholio vartojimą. Reikšmės: nevartoja - 1,vartoja retai - 2,girtauja - 3,alkoholikas - 4. |
| `vda_ligos_kodai` | `string` | — | `4` | `open` | — | Pacientui diagnozuotos ligos | Visų pacientui diagnozuotų ligų kodų (TLK-10) reikšmės atskirtos kabliataškiais |
| `ligos_kodas` | `string` | — | `4` | `open` | — | Naujausios pacientui diagnozuotos ligos kodas | Ligos kodas pagal TLK-10 ligų klasifikatorių |
| `ar_mire_nuo_tub` | `boolean` | — | `4` | `open` | — | Paciento mirties nuo tuberkuliozės reikšmė (true/false) | — |
| `mirties_nuo_tub_d` | `date` | `D` | `4` | `open` | — | Paciento mirties nuo tuberkuliozės data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv
