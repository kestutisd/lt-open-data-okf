---
type: Dataset
title: "Pacientams atliktų laboratorinių tyrimų rezultatai"
description: "Laboratorinių tyrimų informacinės sistemos, kaip OpenLIMS, sLIS, POLIS kaupia asmens sveikatos priežiūros įstaigose, naudojančiose kurią nors iš laboratorinių tyrimų sistemų, pacientams atliktų laboratorinių tyrimų duomenis."
resource: "https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai"
tags: [gov, lab_tyrimai, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2700/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-02-23T00:00:00Z"
---

# Pacientams atliktų laboratorinių tyrimų rezultatai

- **Namespace:** `datasets/gov/lab_tyrimai/lab_tyrimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lab_tyrimai/lab_tyrimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai` (`deployed`)[^manifest]
- **Provider:** `lab_tyrimai`[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `38` (38 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2700/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Pacientams atliktų laboratorinių tyrimų rezultatai[^dcat]
- **Portal Title (`@en`):** Results of laboratory tests performed in patients[^dcat]
- **Issued (`dct:issued`):** `2024-07-03`[^dcat]
- **Last Modified (`dct:modified`):** `2026-02-23`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-10-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Laboratorinių tyrimų informacinės sistemos, kaip OpenLIMS, sLIS, POLIS kaupia asmens sveikatos priežiūros įstaigose, naudojančiose kurią nors iš laboratorinių tyrimų sistemų, pacientams atliktų laboratorinių tyrimų duomenis. Duomenų rinkinių struktūros ir laiko aprėptys gali skirtis, priklausomai nuo įstaigos ir sistemos, tačiau įprastai juose duomenys kaupiami nuo 2-ojo dešimtmečio ir iki šiol vis atnaujinami. Į duomenų rinkinius patenka įstaigos pavadinimas, paciento identifikatorius, lytis, gimimo metai, tyrimo data, rezultatų skaitinė reikšmė, tyrimo analitės pavadinimas, tyrimo rezultatų normų ribos, matavimo vienetai, paciento pagrindinės diagnozės pavadinimas ir TLK-10-AM kodas. Duomenų teikėjas – Asmens sveikatos priežiūros įstaigos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt. PASTABA: Dėl Atvirų duomenų portalo techninių galimybių, Kauno miesto poliklinikos duomenų rinkinys yra publikuojamas nepilna apimtimi (pateikiamas tik jo fragmentas, kurį sudaro ~12.5% eilučių). Dėl šios problemos kreiptis į Valstybės skaitmeninių sprendimų agentūrą info@vssa.lt. Kauno miesto poliklinikos ir Dainų pirminės sveikatos priežiūros centro duomenyse asmenų gimimo metai „triukšminti“ (gimimo metai nurodomi su +-1 metų paklaida).[^dcat]

### Portal Description (`@en`)

The laboratory testing information system, such as OpenLIMS, sLIS, POLIS, collects data from laboratory tests performed on patients in individual health care institutions using one of the laboratory testing systems. The structure and timing of datasets may vary depending on the institution and system, but they have generally been collecting data since the 1980 s and are still being updated. Data sets include the name of the institution, patient identifier, gender, year of birth, date of study, numerical value of results, name of the study analyte, limits of test results, units of measure, name of the patient's main diagnosis and TLK-10-AM code. Contact the atverimas@stat.gov.lt for technical questions or possible errors. NOTE: Due to the technical feasibility of the Open Data Portal, the data set of Kaunas City Polyclinic is published in incomplete scope (only a fragment of it, consisting of ~ 12.5% of the lines, is provided). Contact the State Digital Solutions Agency for this problem info@vssa.lt In the data of Kaunas City Polyclinic and Song Primary Health Care Centre, the year of birth is “noisy” (year of birth is indicated with + 1 year error)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [RokiskioRajonoLigonine](lab_tyrimai/RokiskioRajonoLigonine.md) | Rokiškio raj. ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai | `4` | `vda_prime_key` | — | `14` | Rokiškio rajono ligoninės OpenLIMS sistema kaupia pacientams atliktų laboratorinių tyrimų duomenis. |
| [AnyksciuRajonoLigonine](lab_tyrimai/AnyksciuRajonoLigonine.md) | Anykščių raj. ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai | `4` | `vda_prime_key` | — | `14` | Anykščių rajono ligoninės OpenLIMS sistema kaupia pacientams atliktų laboratorinių tyrimų duomenis. |
| [MykoloMarcinkeviciausLigonine](lab_tyrimai/MykoloMarcinkeviciausLigonine.md) | Mykolo Marcinkevičiaus ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai | `4` | `vda_prime_key` | — | `15` | Mykolo Marcinkevičiaus ligoninės sLIS sistema kaupia duomenis apie Mykolo Marcinkevičiaus ligoinėje įvykdytus laboratorinius tyrimus pacientams. |
| [PasvalioLigonine](lab_tyrimai/PasvalioLigonine.md) | Pasvalio ligoninėje pacientams atliktų laboratorinių tyrimų duomenys | `4` | `vda_prime_key` | — | `14` | Pasvalio ligoninės OpenLIMS sistema kaupia pacientams atliktų laboratorinių tyrimų duomenis. |
| [DainuPSPC](lab_tyrimai/DainuPSPC.md) | Dainų pirminės sveikatos priežiūros centro pacientams atliktų laboratorinių tyrimų duomenys | `4` | `vda_primary_key` | — | `15` | VšĮ Dainų pirminės sveikatos priežiūros centro POLIS sistema kaupia pacientams atliktų laboratorinių tyrimų duomenis. |
| [KaunoMiestoPoliklinika](lab_tyrimai/KaunoMiestoPoliklinika.md) | Kauno miesto poliklinikos pacientams atliktų laboratorinių tyrimų duomenys | `4` | `vda_primary_key` | — | `15` | VšĮ Kauno miesto poliklinikos (KMP) POLIS sistema kaupia pacientams atliktų laboratorinių tyrimų duomenis. |
| [SirvintuRajonoSavivaldybesSC](lab_tyrimai/SirvintuRajonoSavivaldybesSC.md) | Širvintų savivaldybes rajono sveikatos centro pacientams atliktų laboratorinių tyrimų duomenys | `4` | `vda_prime_key` | — | `14` | Širvintų rajono savivaldybės sveikatos centro OpenLIMS sistemoje nuo 2017 m. kaupiami ir iki šiol atnaujinami pacientams atliktų laboratorinių tyrimų duomenys. |
| [KedainiuPSPC](lab_tyrimai/KedainiuPSPC.md) | Kėdainių pirminės sveikatos priežiūros centro pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `14` | Kėdainių pirminės sveikatos priežiūros centro OpenLIMS sistemoje nuo 2021 m. kaupiami ir iki šiol atnaujinami pacientams atliktų laboratorinių tyrimų duomenys. |
| [KupiskioLigonine](lab_tyrimai/KupiskioLigonine.md) | Kupiškio ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai | — | `vda_prime_key` | — | `16` | Kupiškio ligoninės OpenLIMS sistemoje kaupiami Kupiškio ligoninės pacientams atliktų laboratorinių tyrimų duomenys, kaupiami nuo 2012 m. ir atnaujinami iki... |
| [ElektrenuLigonine](lab_tyrimai/ElektrenuLigonine.md) | Elektrėnų ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai | — | `vda_prime_key` | — | `16` | Elektrėnų ligoninės OpenLIMS sistemoje kaupiami Elektrėnų ligoninės klinikinėje diagnostinėje laboratorijoje pacientams atliktų laboratorinių tyrimų... |
| [RegionineTelsiuLigonine](lab_tyrimai/RegionineTelsiuLigonine.md) | Regioninėje Telšių ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai | — | `vda_prime_key` | — | `16` | Regioninės Telšių ligoninės (RTL) OpenLIMS sistemoje kaupiami RTL pacientams atliktų laboratorinių tyrimų duomenys, atnaujinami iki šiol. |
| [RegionineMazeikiuLigonine](lab_tyrimai/RegionineMazeikiuLigonine.md) | Regioninėje Mažeikių ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai | — | `vda_prime_key` | — | `16` | Regioninės Mažeikių ligoninės (RML) OpenLIMS sistemoje kaupiami RML pacientams atliktų laboratorinių tyrimų duomenys, atnaujinami iki šiol. |
| [DruskininkuLigonine](lab_tyrimai/DruskininkuLigonine.md) | Druskininkų ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai | — | `vda_prime_key` | — | `16` | Druskininkų ligoninės OpenLIMS sistemoje kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys, kaupiami nuo 2019 ir atnaujinami iki šiol. |
| [RespublikinePanevezioLigonine](lab_tyrimai/RespublikinePanevezioLigonine.md) | Respublikinėje Panevėžio ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai | — | `vda_prime_key` | — | `16` | Respublikinės Panevėžio ligoninės OpenLIMS sistemoje kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys, kaupiami nuo 2015 ir atnaujinami... |
| [KedainiuLigonine](lab_tyrimai/KedainiuLigonine.md) | Kėdainių ligoninėje pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Kėdainių ligoninės sistemoje „OpenLIMS“ nuo 2012 metų kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [UkmergesLigonine](lab_tyrimai/UkmergesLigonine.md) | Ukmergės ligoninėje pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `15` | Ukmergės ligoninės sistemoje „sLIS“ nuo 2018 metų kaupiami pacientams atliktų laboratorinių tyrimų duomenys. |
| [MarijampolesLigonine](lab_tyrimai/MarijampolesLigonine.md) | Marijampolės ligoninėje pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Marijampolės ligoninės sistemoje „OpenLIMS“ nuo 2014 metų kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [VilkaviskioLigonine](lab_tyrimai/VilkaviskioLigonine.md) | Vilkaviškio ligoninėje pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Vilkaviškio ligoninės sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [KazluRudosPSPC](lab_tyrimai/KazluRudosPSPC.md) | Kazlų Rūdos pirminės sveikatos priežiūros centro pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Kazlų Rūdos pirminės sveikatos priežiūros centro sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [MarijampolesPSPC](lab_tyrimai/MarijampolesPSPC.md) | Marijampolės pirminės sveikatos priežiūros centro pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Marijampolės pirminės sveikatos priežiūros centro sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [VilkaviskioPSPC](lab_tyrimai/VilkaviskioPSPC.md) | Vilkaviškio pirminės sveikatos priežiūros centro pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Vilkaviškio pirminės sveikatos priežiūros centro sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [SventoRokoLigonine](lab_tyrimai/SventoRokoLigonine.md) | Šv. Roko ligoninės pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Šv. Roko ligoninės sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [SeskinesPoliklinika](lab_tyrimai/SeskinesPoliklinika.md) | Šeškinės poliklinikos pacientams atliktų laboratorinių tyrimų duomenys | `4` | `vda_prime_key` | — | `16` | Šeškinės poliklinikos sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [JonavosLigonine](lab_tyrimai/JonavosLigonine.md) | Jonavos ligoninės pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Jonavos ligoninės sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [RaseiniuLigonine](lab_tyrimai/RaseiniuLigonine.md) | Raseinių ligoninės pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Raseinių ligoninės sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [PrienuLigonine](lab_tyrimai/PrienuLigonine.md) | Prienų ligoninės pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Prienų ligoninės sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [KaisiadoriuSSC](lab_tyrimai/KaisiadoriuSSC.md) | Kaišiadorių rajono savivaldybės sveikatos centro pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Kaišiadorių rajono savivaldybės sveikatos centro sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [AlytausSKudirkosLigonine](lab_tyrimai/AlytausSKudirkosLigonine.md) | Alytaus apskrities S. Kudirkos ligoninės pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Alytaus aps. S. Kudirkos ligoninės sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [LazdijuRSSC](lab_tyrimai/LazdijuRSSC.md) | Lazdijų rajono savivaldybės sveikatos centro pacientams atliktų laboratorinių tyrimų duomenys | — | `vda_prime_key` | — | `16` | Lazdijų raj. sav. sveikatos centro sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [CentroPoliklinika](lab_tyrimai/CentroPoliklinika.md) | Centro poliklinikos pacientams atliktų laboratorinių tyrimų rezultatai | `4` | `vda_prime_key` | — | `15` | Centro poliklinikos sistemoje „sLIS“ kaupiami pacientams atliktų laboratorinių tyrimų duomenys. |
| [RespublikineSiauliuLigonine](lab_tyrimai/RespublikineSiauliuLigonine.md) | Respublikinės Šiaulių ligoninės pacientams atlikti laboratoriniai tyrimai | `4` | `vda_prime_key` | — | `17` | Duomenų rinkinyje pateikiami nuo 2020 metų informacinėje sistemoje „PanelLIMS“ kaupiami ir iki šiol atnaujinami Respublikinės Šiaulių ligoninės atliktų... |
| [BirzuPoliklinika](lab_tyrimai/BirzuPoliklinika.md) | Biržų rajono savivaldybės poliklinikos pacientams atlikti laboratoriniai tyrimai | `4` | `vda_prime_key` | — | `16` | Biržų raj. sav. poliklinikos sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [KupiskioPASPC](lab_tyrimai/KupiskioPASPC.md) | Kupiškio rajono savivaldybės pirminės asmens sveikatos priežiūros centro pacientams atlikti laboratoriniai tyrimai | `4` | `vda_prime_key` | — | `16` | Kupiškio raj. sav. PASPC sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [RokiskioPASPC](lab_tyrimai/RokiskioPASPC.md) | Rokiškio pirminės asmens sveikatos priežiūros centro pacientams atlikti laboratoriniai tyrimai | `4` | `vda_prime_key` | — | `16` | Rokiškio PASPC sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [KlaipedosUniversitetoLigonine](lab_tyrimai/KlaipedosUniversitetoLigonine.md) | Klaipėdos universiteto ligoninės pacientams atlikti laboratoriniai tyrimai | `4` | `vda_prime_key` | — | `24` | Klaipėdos universiteto ligoninės sistemoje „LIS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [RespublikineVilniausUniversitetineLigonine](lab_tyrimai/RespublikineVilniausUniversitetineLigonine.md) | Respublikinės Vilniaus universitetinės ligoninės pacientams atliktų laboratorinių tyrimų rezultatai | `4` | `vda_prime_key` | — | `15` | Respublikinės VU ligoninės sistemoje „LIS“ kaupiami pacientams atliktų laboratorinių tyrimų duomenys. |
| [JonavosPSPC](lab_tyrimai/JonavosPSPC.md) | Jonavos pirminės asmens sveikatos priežiūros centro pacientams atlikti laboratoriniai tyrimai | `4` | `vda_prime_key` | — | `16` | Jonavos PSPC sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |
| [RaseiniuPSPC](lab_tyrimai/RaseiniuPSPC.md) | Raseinių pirminės sveikatos priežiūros centro pacientams atlikti laboratoriniai tyrimai | `4` | `vda_prime_key` | — | `16` | Raseinių PSPC sistemoje „OpenLIMS“ kaupiami įstaigos pacientams atliktų laboratorinių tyrimų duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai (https://data.gov.lt/datasets/2700/)
