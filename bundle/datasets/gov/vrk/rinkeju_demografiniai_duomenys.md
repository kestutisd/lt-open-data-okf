---
type: Dataset
title: "Rinkėjų demografiniai duomenys"
description: "Vyriausiosios rinkimų komisijos Rinkėjų sąrašų tvarkymo posistemėje kaupiami rinkėjų balsavimo žymėjimai."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys"
tags: [gov, vrk, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vrk/rinkeju_demografiniai_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Rinkėjų demografiniai duomenys

Vyriausiosios rinkimų komisijos Rinkėjų sąrašų tvarkymo posistemėje kaupiami rinkėjų balsavimo žymėjimai. Duomenys kaupiami nuo 2011-12-29 ir yra atnaujinami iki šiol. Duomenų rinkinys sudarytas iš 4 atskirų lentelių apie rinkėjus, rinkėjų žymėjimus, rinkimų apygardas ir vykdomus rinkimus. Lentelėse yra įtraukti išorinių raktų stulpeliai, leidžiantys apjungti jose esančius duomenis. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vrk/rinkeju_demografiniai_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys` (`deployed`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2808/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys`[^dcat]
- **Portal Title (`@lt`):** Rinkėjų demografiniai duomenys[^dcat]
- **Portal Title (`@en`):** Demographics of voters[^dcat]
- **Issued (`dct:issued`):** `2024-11-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-09-20` .. `2026-05-14`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Vyriausiosios rinkimų komisijos informacinė sistema kaupia žymėjimus apie rinkėjų balsavimą. Duomenų rinkinį sudaro keturios lentelės: „Rinkimų turai“, „Rinkimų apygardos“, „Rinkėjai“, „Rinkėjų žymėjimai“. Lentelėje „Rinkimų turai“ pateikiama rinkimų identifikacijos numeris, rinkimų pavadinimas, rinkimų turo identifikacijos numeris, rinkimų turo numeris, informacija apie einamuosius rinkimus bei rinkimų turo data. Lentelėje „Rinkimų apygardos“ galima rasti informaciją apie apygardos identifikacijos numerį ir apygardos pavadinimą tam tikrų rinkimų metu. Lentelėje „Rinkėjai“ viešinami atskirų rinkėjų pseudonimizuoti asmens kodai, asmens lytis ir gimimo metai (gimimo metų įrašai yra modifikuoti pridedant atsitiktines vertes siekiant užtikrinti konfidencialumą). Lentelėje „Rinkėjų žymėjimai“ pateikiama konkrečiais rinkimais tam tikro rinkėjo balsavimo žymėjimas. Lentelėje galima rasti pseudonimizuotų asmens kodų, vykdomų rinkimų turo ir apygardos, kurioje buvo balsuojama identifikacijos numerio informacija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The information system of the Central Electoral Commission accumulates notations about the voter's vote. The dataset consists of four tables: "Election Rounds", "Electoral Districts", "Voters", "Voter Markings". The table "Election rounds" contains the election identification number, election name, election round identification number, election round number, information about the current election and the date of the election round. In the table "Electoral districts" you can find information about the district identification number and the name of the district during certain elections. The "Voters" table publishes the pseudonymized personal codes, gender and year of birth of individual voters (year of birth records are modified by adding random values ​​to ensure confidentiality). The "Voter markings" table shows the marking of a certain voter's vote in specific elections. In the table you can find information about pseudonymized personal codes, the election round and the district where the vote was taken. For technical questions or possible errors, contact atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Rinkejas](rinkeju_demografiniai_duomenys/Rinkejas.md) | Rinkėjai | `4` | `rinkejo_asm_k` | — | `3` | Balso teisę turinčių rinkėjų lentelė. |
| [Zymejimas](rinkeju_demografiniai_duomenys/Zymejimas.md) | Rinkėjų žymėjimai | `4` | `vda_prime_key` | — | `4` | Rinkėjų balsų žymėjimų lentelė. |
| [Apygarda](rinkeju_demografiniai_duomenys/Apygarda.md) | Rinkimų apygardos | `4` | `apygardos_id` | — | `2` | Rinkimų apygardų lentelė. |
| [RinkimuTuras](rinkeju_demografiniai_duomenys/RinkimuTuras.md) | Rinkimų turai | `4` | `vda_prime_key` | — | `7` | Vykdomų rinkimų lentelė. Vienas įrašas atitinka vykdomų rinkimų ir jų turų kombinaciją. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vrk/rinkeju_demografiniai_duomenys (https://data.gov.lt/datasets/2808/)
