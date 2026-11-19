---
type: Dataset
title: "Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys"
description: "Šiame duomenų rinkinyje aprašoma viešojo transporto kelionių sistema, apimanti maršrutus, tvarkaraščius, bilietų kainas ir sustojimus."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas"
tags: [gov, ltsa, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1929/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/viesasis_transportas"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys

Šiame duomenų rinkinyje aprašoma viešojo transporto kelionių sistema, apimanti maršrutus, tvarkaraščius, bilietų kainas ir sustojimus. Lentelėse pateikiama informacija apie agentūras, valdančias transporto paslaugas, jų maršrutus bei atskiras keliones („Trip“), kurios siejamos su konkrečiais laikais ir stotelėmis („StopTime“, „Stop“). Kalendoriaus duomenys („Calendar“, „CalendarDate“) nurodo, kada paslaugos yra teikiamos, o kainų struktūra („FareAttribute“, „FareRule“) apibrėžia bilietų tipus, kainas ir galiojimo taisykles. Maršrutų geografinė informacija („Shape“) naudojama kelionių trajektorijų atvaizdavimui žemėlapyje. Šis duomenų rinkinys suteikia galimybę analizuoti transporto tinklo struktūrą, paslaugų dažnumą, kainodarą ir kelionių prieinamumą. Duomenys gali būti naudojami tiek planavimui, tiek kelionių modeliavimui ar vizualizacijai. Duomenys pateikiami GTFS, NeTex ir API formatu. Duomenų teikėjas – Lietuvos Transporto saugos administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Namespace:** `datasets/gov/ltsa/viesasis_transportas`[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `11` (11 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1929/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas`[^dcat]
- **Portal Title (`@lt`):** Viešojo transporto kelionių duomenys[^dcat]
- **Portal Title (`@en`):** Public transport travel data[^dcat]
- **Issued (`dct:issued`):** `2023-05-29`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-20`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2022-05-18` .. `2026-10-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

Public transport travel data information system data in GTFS and NeTex format: Public transport timetables for all modes; Public transport routes; Stops, stations, airports, etc. Data source: Lithuanian Transport Safety Administration, municipalities and private carriers.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [FareAttribute](viesasis_transportas/FareAttribute.md) | Viešojo transporto bilietų kainos | `4` | `fare_id` | — | `8` | Viešojo transporto bilietų kainos, valiuta ir persėdimų taisyklės. |
| [FareRule](viesasis_transportas/FareRule.md) | Viešojo transporto bilietų tarifų taikymo taisyklės | `4` | `fare_id` | — | `5` | Viešojo transporto bilietų tarifų taikymo taisyklės pagal maršrutus ar zonas. |
| [CalendarDate](viesasis_transportas/CalendarDate.md) | Viešojo transporto išimtinės paslaugų datos | `4` | `vda_prime_key` | — | `4` | Viešojo transporto išimtinės paslaugų datos (pridėtos ar atšauktos, pvz., šventinės dienos). |
| [Route](viesasis_transportas/Route.md) | Viešojo transporto maršrutai | `4` | `route_id` | — | `14` | Viešojo transporto maršrutų informacija, linijų pavadinimai ir tipai (autobusai, traukiniai). |
| [Shape](viesasis_transportas/Shape.md) | Viešojo transporto maršrutų geografinės trajektorijos | `4` | `vda_prime_key` | — | `6` | Viešojo transporto maršrutų geografinės trajektorijos (linijos žemėlapyje). |
| [Agency](viesasis_transportas/Agency.md) | Viešojo transporto paslaugų teikėjai | `4` | `agency_id` | — | `8` | Viešojo transporto operatorių (autobusų, traukinių) duomenys. |
| [Calendar](viesasis_transportas/Calendar.md) | Viešojo transporto paslaugų tvarkaraščiai | `4` | `service_id` | — | `10` | Viešojo transporto tvarkaraščiai pagal savaitės dienas. |
| [Trip](viesasis_transportas/Trip.md) | Viešojo transporto reisai | `4` | `trip_id` | — | `19` | Viešojo transporto konkretūs reisai pagal maršrutus, kryptis ir tvarkaraščius. |
| [Stop](viesasis_transportas/Stop.md) | Viešojo transporto sustojimo taškai | `4` | `stop_id` | — | `18` | Viešojo transporto sustojimo taškų (stotelių, stočių) duomenys su pavadinimais ir koordinatėmis. |
| [StopTime](viesasis_transportas/StopTime.md) | Viešojo transporto sustojimų laikai ir seka | `4` | `vda_prime_key` | — | `20` | Viešojo transporto sustojimų laikai ir jų seka kiekvienam maršruto reisui. |
| [Attribution](viesasis_transportas/Attribution.md) | Viešojo transporto duomenų priskyrimai | `4` | `id` | — | `11` | Organizacijos, susijusios su viešojo transporto duomenų kūrimu, teikimu, priežiūra ar eksploatavimu. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/viesasis_transportas (https://data.gov.lt/datasets/1929/)
