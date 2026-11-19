---
type: Dataset
title: "Rinkėjo puslapio naudotojo paveikslas"
description: "Duomenų rinkinys sudarytas iš Vyriausiosios rinkimų komisijos informacinės sistemos (VRKIS) kaupiamų prisijungimo prie VRK tvarkomo projekto „Rinkėjo puslapis“ seansų duomenų ir pasaulinio masto IP adresų pagal geografinę vietovę rinkinio."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkejo_puslapis"
tags: [gov, vrk, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2759/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vrk/rinkejo_puslapis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Rinkėjo puslapio naudotojo paveikslas

Duomenų rinkinys sudarytas iš Vyriausiosios rinkimų komisijos informacinės sistemos (VRKIS) kaupiamų prisijungimo prie VRK tvarkomo projekto „Rinkėjo puslapis“ seansų duomenų ir pasaulinio masto IP adresų pagal geografinę vietovę rinkinio. VRKIS duomenys saugomi nuo 2011 m. ir yra atnaujinami kasdien, o iki 2024 m. buvęs aktualus IP adresų rinkinys nebėra atnaujinamas. Duomenų rinkinį sudaro: prisijungimo seanso identifikatorius, pseudonimizuotas rinkėjo asmens kodas, gimimo metai, lytis, pagal IP adresą nustatytos tikėtina prisijungimo valstybė ir vietovė, prisijungimo ir atsijungimo laikas bei atsijungimo priežastis.[^manifest]

- **Namespace:** `datasets/gov/vrk/rinkejo_puslapis`[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkejo_puslapis` (`deployed`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2759/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vrk/rinkejo_puslapis`[^dcat]
- **Portal Title (`@lt`):** Rinkėjo puslapio naudotojo paveikslas[^dcat]
- **Portal Title (`@en`):** User's image on the "Voters page"[^dcat]
- **Issued (`dct:issued`):** `2024-11-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-08-22` .. `2026-05-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Vyriausiosios rinkimų komisijos informacinė sistema renka duomenis apie „Rinkėjo puslapis“ naudotojo paveikslą. Duomenų rinkinys sudarytas iš Vyriausiosios rinkimų komisijos informacinės sistemos (VRKIS) kaupiamų prisijungimo prie VRK tvarkomo projekto „Rinkėjo puslapis“ seansų duomenų ir pasaulinio masto IP adresų pagal geografinę vietovę rinkinio. Duomenų rinkinyje galima rasti informaciją apie prisijungimo sesijos identifikacijos numerį, pseudonimizuotą vartotojo asmens kodą, gimimo metus, lytį, tikėtiną prisijungimo valstybę ir vietovę (nustatytą pagal IP adresą), prisijungimo ir atsijungimo laiką bei priežastį. Vienos rinkinyje esančios eilutės įrašas atitinka vieną naudotojo prisijungimo prie „Rinkėjo puslapis“ sesiją. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The information system of the Central Electoral Commission collects data about the "Voter Page" user's picture. The data set is composed of data collected by the Information System of the Central Election Commission (VRKIS) of connection sessions to the "Voter's page" project managed by the CEC and a set of global IP addresses by geographic location. The data set contains information about the login session identification number, pseudonymized user ID, year of birth, gender, likely country and location of login (determined by IP address), login and logout time and reason. One row entry in the set corresponds to one user login session to the "Voter Page". For technical questions or possible errors, contact atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Vartotojas](rinkejo_puslapis/Vartotojas.md) | Rinkėjo puslapio naudotojo paveikslas | `4` | `sesijos_id` | — | `9` | Duomenų rinkinys sudarytas iš Vyriausiosios rinkimų komisijos informacinės sistemos (VRKIS) kaupiamų prisijungimo prie VRK tvarkomo projekto „Rinkėjo... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vrk/rinkejo_puslapis (https://data.gov.lt/datasets/2759/)
