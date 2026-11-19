---
type: Dataset
title: "Namuose balsuojančiųjų rinkėjų balsų rinkimo išvykos"
description: "Vyriausiosios rinkimų komisijos Rinkimų organizavimo posistemė kaupia balsų skaičiavimo išvykų rinkėjų namuose duomenis."
resource: "https://get.data.gov.lt/datasets/gov/vrk/balsu_skaiciavimo_isvykos"
tags: [gov, vrk, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2809/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vrk/balsu_skaiciavimo_isvykos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Namuose balsuojančiųjų rinkėjų balsų rinkimo išvykos

Vyriausiosios rinkimų komisijos Rinkimų organizavimo posistemė kaupia balsų skaičiavimo išvykų rinkėjų namuose duomenis. Duomenys kaupiami nuo 2011-12-29 ir yra atnaujinami. Duomenų rinkinys apima vykdomų rinkimų identifikatorių bei pavadinimą, vykdomų rinkimų turo identifikatorių ir numerį, išvykos identifikatorių, komisijos nario identifikatorių, pareigas, organizaciją, apygardų, apylinkių identifikatorius ir pavadinimus, kuriose dirba, ir apygardų, apylinkių, kuriose skaičiavo balsus. Rinkinyje taip pat yra duomenų apie numatytą aplankyti rinkėjų skaičių, grafiko būseną ir grafiko sukūrimo bei planuotą išvykos datas. Vienas rinkinio įrašas atitinka vieno nario išvyką atitinkamų rinkimų metu. Komisijos narių darbo apygardos bei apylinkės vietomis paliktos tuščios parodyti, ar atitinkamas narys priklauso centrinei komisijai, kuri neturi nei apygardos, nei apylinkės, ar yra apygardos darbuotojas, kai nurodyta tik apygarda, arba apylinkės darbuotojas, kai nurodyta tik apylinkė. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vrk/balsu_skaiciavimo_isvykos`[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/balsu_skaiciavimo_isvykos` (`deployed`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2809/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vrk/balsu_skaiciavimo_isvykos`[^dcat]
- **Portal Title (`@lt`):** Namuose balsuojančiųjų rinkėjų balsų rinkimo išvykos[^dcat]
- **Portal Title (`@en`):** Visits made to voters voting at home[^dcat]
- **Issued (`dct:issued`):** `2024-11-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-09-20` .. `2026-04-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Vyriausiosios rinkimų komisijos informacinė sistema kaupia balsavimo namuose grafiko duomenis. Duomenys surinkti pagal rinkimų apygardų ir apylinkių komisijų narių pateiktas ataskaitas. Balsavimo namuose grafiko duomenys kaupiami nuo 2019 metų ir atnaujinami kiekvienų rinkimų metu. Duomenų rinkinys apima rinkimų identifikacijos numerį ir pavadinimą, informaciją apie rinkimų turą ir jo identifikacijos numerį, rinkimų komisijos atvykimo pas rinkėjus į namus identifikacijos numerį, komisijos nario identifikacijos numerį, pareigas, organizaciją, apygardos ir apylinkės identifikacijos numerį ir pavadinimą, kuriose dirbo ir buvo atvykę pas rinkėjus į namus komisijos narys. Rinkinyje taip pat yra duomenų apie numatytą aplankyti rinkėjų skaičių, grafiko būseną ir grafiko sukūrimo bei planuoto atvykimo pas rinkėjus į namus datas. Vienos rinkinyje esančios eilutės įrašas atitinka vieną nario balsavimo namuose išvyką atitinkamų rinkimų metu. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The information system of the Central Electoral Commission collects data on the schedule of voting at home. The data was collected based on the reports submitted by the members of the election district and vicinity commissions. Voting at home schedule data has been collected since 2019 and is updated during each election. The data set includes the election identification number and name, information about the election round and its identification number, the identification number of the election commission's arrival at the voters homes, the commission member's identification number, position, organization, district and precinct identification number and name, where they worked and visited at the voter's house, a member of the commission. The set also includes data on the number of voters expected to be visited, the status of the schedule, and the dates when the schedule was created and scheduled to visit voters homes. One row entry in the set corresponds to one outing for a member to vote at home during the relevant election.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Isvyka](balsu_skaiciavimo_isvykos/Isvyka.md) | Namuose balsuojančiųjų rinkėjų balsų rinkimo išvykos | `4` | `vda_prime_key` | — | `21` | Vyriausiosios rinkimų komisijos Rinkimų organizavimo posistemėje nuo 2011-12-29 kaupiami ir iki šiol atnaujinami balsų skaičiavimo išvykų i rinkėjų namus... |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vrk/balsu_skaiciavimo_isvykos (https://data.gov.lt/datasets/2809/)
