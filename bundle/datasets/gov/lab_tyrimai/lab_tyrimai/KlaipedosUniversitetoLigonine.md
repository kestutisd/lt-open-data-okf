---
type: Table
title: "KlaipedosUniversitetoLigonine — Klaipėdos universiteto ligoninės pacientams atlikti laboratoriniai tyrimai"
description: "Klaipėdos universiteto ligoninės sistemoje „LIS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/KlaipedosUniversitetoLigonine"
tags: [gov, lab_tyrimai, klaipedosuniversitetoligonine, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L920"
    title: "atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L920"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2700/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-02-23T00:00:00Z"
---

# KlaipedosUniversitetoLigonine — Klaipėdos universiteto ligoninės pacientams atlikti laboratoriniai tyrimai

Klaipėdos universiteto ligoninės sistemoje „LIS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. Rinkinyje pateikiami nuo 2015 metų gruodžio mėnesio sukaupti ir iki šiol atnaujinami duomenys. Duomenų rinkinį sudaro: užsakymo, jo tėvinės bei vaikinės analizių identifikatoriai, brūkšninis kodas, užsakymo ir jo analizės patvirtinimo laikai, paciento identifikatorius, kodas ir jo galimos rūšys, paciento gimimo metai ir lytis, tiek iš gimimo datos arba lyties stulpelių, tiek iš galiojančių asmens kodų, tyrimo arba jo analitės pavadinimas, originalus rezultato stulpelis, taip pat atskiri stulpeliai tekstiniams bei skaitiniams rezultatams, originalus rezultato normų režių stulpelis kartu su atskirais apatinės ir viršutinės normos stulpeliais, matavimo vienetas ir rezultato laikas. Vienas įrašas atitinka vieną užsakymo, užsakymo analizės, jos tėvinės analizės ir brūkšninio kodo kombinaciją. Visi panaudoti identifikatoriai užšifruoti konfidencialumo tikslais. Kai užsakymo analizės ir jos tėvinės analizės identifikatoriai sutampa, dalis reikšmių tyrimo arba analitės stulpelyje yra tyrimų pavadinimai, priešingu atveju – tik analičių pavadinimai. Tarp paciento kodo reikšmių yra ne tik Lietuvos fizinio asmens kodų, bet ir kitų identifikacinių kodų, pvz., „Sodros“ kodų. Trečdalio pacientų gimimo metai yra padidinti, kito trečdalio sumažinti vienais metais konfidencialumo tikslais. Kadangi tiek tekstiniai, tiek skaitiniai tyrimų bei analičių rezultatai įvairiais formatais saugomi viename stulpelyje, patogumo dėlei „Regex“ išraiškomis buvo sukurti stulpeliai atskirai saugoti tekstinius bei skaitinius rezultatus, todėl pastarųjų dviejų stulpelių vertės gali neatitikti originalaus rezultatų stulpelio duomenų. Dėl šios priežasties taip pat atskirų normos rėžių stulpelių reikšmės gali neatitikti originalaus normų rėžių stulpelio reikšmių. Duomenų teikėjas – VšĮ Klaipėdos universiteto ligoninė. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lab_tyrimai/lab_tyrimai/KlaipedosUniversitetoLigonine`[^manifest]
- **Dataset:** [Pacientams atliktų laboratorinių tyrimų rezultatai](../lab_tyrimai.md) (`datasets/gov/lab_tyrimai/lab_tyrimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lab_tyrimai/lab_tyrimai.csv#L920](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L920)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/KlaipedosUniversitetoLigonine` (`deployed`)[^manifest]
- **Provider:** `lab_tyrimai`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-02-23`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `uzsakymo_id` | `string` | — | `4` | `open` | — | Užsakymo identifikatorius | — |
| `uzsakymo_analizes_tevinis_id` | `string` | — | `4` | `open` | — | Užsakymo tėvinės analizės identifikatorius | — |
| `uzsakymo_analizes_id` | `string` | — | `4` | `open` | — | Užsakymo analizės identifikatorius | — |
| `barkodas` | `string` | — | `4` | `open` | — | Tyrimo barkodas | — |
| `uzsakymo_laikas` | `datetime` | `S` | `4` | `open` | — | Užsakymo data ir laikas | — |
| `uzsakymo_analizes_patvirtinimo_laikas` | `datetime` | `S` | `4` | `open` | — | Užsakymo analizės patvirtinimo data ir laikas | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento identifikatorius | — |
| `paciento_kodas` | `string` | — | `4` | `open` | — | Paciento kodas | — |
| `paciento_kodo_tipas` | `string` | — | `4` | `open` | — | Paciento kodo rūšis | — |
| `paciento_asmens_kodo_validacija` | `string` | — | `4` | `open` | — | Paciento Lietuvos fizinio asmens kodo validacija | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `vda_paciento_gimimo_metai_ak` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai iš asmens kodo | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `vda_paciento_lytis_ak` | `string` | — | `4` | `open` | — | Paciento lytis iš asmens kodo | — |
| `tyrimo_arba_analites_pavadinimas` | `string` | — | `3` | `open` | — | Tyrimo arba analitės pavadinimas | — |
| `originalus_rezultatas` | `string` | — | `3` | `open` | — | Analitės pradinis rezultato stulpelis | — |
| `tekstinis_rezultatas` | `string` | — | `3` | `open` | — | Analitės tekstinio rezultato stulpelis | — |
| `skaitinis_rezultatas` | `number` | — | `4` | `open` | — | Analitės skaitinio rezultato stulpelis | — |
| `originali_norma` | `string` | — | `3` | `open` | — | Analitės skaitinio rezultato normos pradinis stulpelis | — |
| `norma_nuo` | `number` | — | `4` | `open` | — | Analitės skaitinio rezultato apatinė norma | — |
| `norma_iki` | `number` | — | `4` | `open` | — | Analitės skaitinio rezultato viršutinė norma | — |
| `matavimo_vienetas` | `string` | — | `4` | `open` | — | Analitės skaitinio rezultato matavimo vienetas | — |
| `rezultato_laikas` | `datetime` | `S` | `4` | `open` | — | Analitės rezultato data su laiku | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_kodo_tipas` | `"Lietuviškas asmens kodas"` | — | — | Lietuviškas asmens kodas | — |
| `paciento_kodo_tipas` | `"Sodros kodas"` | — | — | Sodros kodas | — |
| `paciento_kodo_tipas` | `"Nenustatyta"` | — | — | Nenustatyta | — |
| `paciento_kodo_tipas` | `"Organizacijos kodas"` | — | — | Organizacijos kodas | — |
| `paciento_kodo_tipas` | `"ESI kodas"` | — | — | ESI kodas | — |
| `paciento_kodo_tipas` | `"Vidinis sistemos identifikatorius"` | — | — | Vidinis sistemos identifikatorius | — |
| `paciento_kodo_tipas` | `"Estiškas asmens kodas"` | — | — | Estiškas asmens kodas | — |
| `paciento_kodo_tipas` | `"Personalo kodas"` | — | — | Personalo kodas | — |
| `paciento_asmens_kodo_validacija` | `"Tinkamas"` | — | — | Tinkamas | — |
| `paciento_asmens_kodo_validacija` | `"Netinkamas ilgis"` | — | — | Netinkamas ilgis | — |
| `paciento_asmens_kodo_validacija` | `"Netinkama gimimo data"` | — | — | Netinkama gimimo data | — |
| `paciento_asmens_kodo_validacija` | `"Yra ne skaitmenų"` | — | — | Yra ne skaitmenų | — |
| `paciento_asmens_kodo_validacija` | `"Netinkamas kontrolinis skaitmuo"` | — | — | Netinkamas kontrolinis skaitmuo | — |
| `paciento_asmens_kodo_validacija` | `"Netinkamas pirmas skaitmuo"` | — | — | Netinkamas pirmas skaitmuo | — |
| `paciento_lytis` | `"V"` | — | — | Vyras | — |
| `paciento_lytis` | `"M"` | — | — | Moteris | — |
| `paciento_lytis` | `"N"` | — | — | Nežinoma | — |
| `vda_paciento_lytis_ak` | `"V"` | — | — | Vyras | — |
| `vda_paciento_lytis_ak` | `"M"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L920 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L920)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai (https://data.gov.lt/datasets/2700/)
