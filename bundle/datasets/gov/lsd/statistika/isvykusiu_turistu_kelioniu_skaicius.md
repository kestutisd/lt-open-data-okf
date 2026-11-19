---
type: Dataset
title: "Išvykusių turistų kelionių skaičius"
description: "Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį, skaičių, jų kelionių, nakvynių skaičių ir tikslus, pagal lytį, pagal amžių,pagal naudojamą pagrindinę transporto priemonės rūšį ir apgyvendinimo įstaigos tipą ir valstybę bei..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius"
tags: [gov, lsd, deployed, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2446/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Išvykusių turistų kelionių skaičius

- **Namespace:** `datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius` (`deployed`)[^manifest]
- **Provider:** `lsd` — Oficialiosios statistikos portalo rodiklių duomenų bazės rinkiniai *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `9` (9 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2446/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius`[^dcat]
- **Portal Title (`@lt`):** Išvykusių turistų kelionių skaičius[^dcat]
- **Portal Title (`@en`):** Number of tourist trips departed[^dcat]
- **Issued (`dct:issued`):** `2023-12-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `OTHER` (`http://publications.europa.eu/resource/authority/frequency/OTHER`)[^dcat]
- **Distribution Date Span:** `2026-04-04` .. `2026-10-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį, skaičių, jų kelionių, nakvynių skaičių ir tikslus, pagal lytį, pagal amžių,pagal naudojamą pagrindinę transporto priemonės rūšį ir apgyvendinimo įstaigos tipą ir valstybę bei kelionių išlaidas. Pateikta per tikslo valstybės, kelionės tikslo, apgyvendinimo įstaigos tipo, laikotarpio, amžiaus dimensijas. Naudojami klasifikatoriai: Pasaulio šalių ir teritorijų klasifikatorius. Statistinio stebėjimo vienetas: vyresni nei 15 metų amžiaus gyventojai, grįžtantys iš užsienio.. Statistinė tiriamoji visuma: tiriamąją visumą sudaro gyventojų, grįžtančių iš užsienio, kelionės. Neįskaitomos asmenų kelionės, kurių tikslas lankomoje teritorijoje yra apmokamas darbas. Geografinė aprėptis: visa šalies ekonominė teritorija. Laiko aprėptis: nuo 2005m., ketvirtiniai ir metiniai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data collection on the number of residents of Lithuania (hereinafter referred to as “residents”) travelling abroad, the number and goals of their journeys, overnight stays, by gender, age, the main type of vehicle used and the type and state of accommodation and travel expenses. Presented through the country of destination, destination, type of accommodation, period, age dimensions. Classifications used: World Country and Territorial Classification. Statistical observation unit: residents over 15 years of age returning from abroad. Statistical survey population: The survey population shall comprise journeys of residents returning from abroad. Travel of persons, the purpose of which is paid work in the territory visited, shall not be included. Geographical coverage: the entire economic territory of the country. Time coverage: from 2005, quarterly and annual.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [S8R707M40910031](isvykusiu_turistu_kelioniu_skaicius/S8R707M40910031.md) | Išvykusių turistų kelionių skaičius (pagal kelionės tikslą ir apgyvendinimo trukmę) | `4` | `vda_id` | — | `11` | Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį nakvynių skaičių. |
| [S8R707M4091102](isvykusiu_turistu_kelioniu_skaicius/S8R707M4091102.md) | Išvykusių turistų kelionių skaičius (pagal kelionės tikslą ir lytį) | `4` | `vda_id` | — | `11` | Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį. |
| [S8R707M4091103](isvykusiu_turistu_kelioniu_skaicius/S8R707M4091103.md) | Išvykusių turistų kelionių skaičius (pagal kelionės tikslą ir amžių) | `4` | `vda_id` | — | `11` | Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį. |
| [S8R707M4091104](isvykusiu_turistu_kelioniu_skaicius/S8R707M4091104.md) | Išvykusių turistų kelionių skaičius (pagal apgyvendinimo įstaigos tipą ir valstybę) | `4` | `vda_id` | — | `11` | Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį. |
| [S8R707M4091105](isvykusiu_turistu_kelioniu_skaicius/S8R707M4091105.md) | Išvykusių turistų kelionių skaičius (pagal kelionės tikslą ir amžių) | `4` | `vda_id` | — | `11` | Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį. |
| [S8R707M4091004](isvykusiu_turistu_kelioniu_skaicius/S8R707M4091004.md) | Išvykusių turistų kelionių skaičius (pagal apgyvendinimo įstaigos tipą ir kelionės tikslą) | `4` | `vda_id` | — | `11` | Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį. |
| [S8R707M4091005](isvykusiu_turistu_kelioniu_skaicius/S8R707M4091005.md) | Išvykusių turistų kelionių skaičius (pagal valstybę) | `4` | `vda_id` | — | `9` | Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį. |
| [S8R707M40910011](isvykusiu_turistu_kelioniu_skaicius/S8R707M40910011.md) | Išvykusių turistų kelionių skaičius (ketvirtiniai) | `4` | `vda_id` | — | `7` | Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį išvykusių turistų kelionių skaičius. |
| [S8R707M40911011](isvykusiu_turistu_kelioniu_skaicius/S8R707M40911011.md) | Išvykusių turistų kelionių skaičius (metiniai) | `4` | `vda_id` | — | `7` | Duomenų rinkinys apie Lietuvos nuolatinių gyventojų (toliau – gyventojai), keliaujančių į užsienį išvykusių turistų kelionių skaičius. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/isvykusiu_turistu_kelioniu_skaicius (https://data.gov.lt/datasets/2446/)
