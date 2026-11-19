---
type: Table
title: "Skrydis — Oro Navigacijos skrydžių statistikos duomenys"
description: "Rinkinyje pateikiami Lietuvos oro erdvėje vykusių skrydžių duomenys iš Oro Navigacijos skrydžių statistikos duomenų bazės."
resource: "https://get.data.gov.lt/datasets/gov/on/statistika/Skrydis"
tags: [gov, "on", skrydis, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/flight_data.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/on/flight_data.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2890/"
    title: "data.gov.lt DCAT-AP — datasets/gov/on/statistika"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Skrydis — Oro Navigacijos skrydžių statistikos duomenys

Rinkinyje pateikiami Lietuvos oro erdvėje vykusių skrydžių duomenys iš Oro Navigacijos skrydžių statistikos duomenų bazės. Nurodoma su skrydžiais susijusi informacija: skrydžio data, orlaivio tipas, skrydį operavęs oro vežėjas, išvykimo ir atvykimo laikai bei išvykimo ir atvykimo oro uostai. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/on/statistika/Skrydis`[^manifest]
- **Dataset:** [Oro Navigacijos skrydžių statistikos duomenys](../statistika.md) (`datasets/gov/on/statistika`)[^manifest]
- **Manifest CSV:** [datasets/gov/on/flight_data.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/flight_data.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/on/statistika/Skrydis` (`deployed`)[^manifest]
- **Provider:** `on` — Oro Navigacija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `date` | `date` | `D` | `4` | `open` | — | Skrydžio data | — |
| `acft_type` | `string` | — | `4` | `open` | — | Orlaivio tipas | — |
| `airline_abbr` | `string` | — | `4` | `open` | — | Oro vežėjas (ICAO kodas) | — |
| `airline` | `string` | — | `4` | `open` | — | Oro vežėjas | — |
| `country` | `string` | — | `4` | `open` | — | Oro vežėjo kilmės šalis | — |
| `wtc` | `string` | — | `4` | `open` | — | Orlaivio masės (valkčio turbulencijos kategorijos) faktorius. | — |
| `dep_time` | `string` | — | `4` | `open` | — | Orlaivio pakilimo laikas | — |
| `dep_airport` | `string` | — | `4` | `open` | — | Pakilimo oro uostas (ICAO kodas) | — |
| `dep_airport_name` | `string` | — | `4` | `open` | — | Išvykimo oro uosto pavadinimas | — |
| `dep_airport_location` | `string` | — | `4` | `open` | — | Išvykimo oro uosto lokacija | — |
| `dep_airport_city` | `string` | — | `4` | `open` | — | Išvykimo oro uosto miestas | — |
| `dep_airport_country` | `string` | — | `4` | `open` | — | Išvykimo oro uosto šalis | — |
| `dep_airport_region` | `string` | — | `4` | `open` | — | Išvykimo oro uosto regionas | — |
| `des_time` | `string` | — | `4` | `open` | — | Orlaivio nusileidimo laikas | — |
| `des_airport` | `string` | — | `4` | `open` | — | Nusileidimo oro uostas (ICAO kodas) | — |
| `des_airport_name` | `string` | — | `4` | `open` | — | Atvykimo oro uosto pavadinimas | — |
| `des_airport_location` | `string` | — | `4` | `open` | — | Atvykimo oro uosto lokacija | — |
| `des_airport_city` | `string` | — | `4` | `open` | — | Atvykimo oro uosto miestas | — |
| `des_airport_country` | `string` | — | `4` | `open` | — | Atvykimo oro uosto šalis | — |
| `des_airport_region` | `string` | — | `4` | `open` | — | Atvykimo oro uosto regionas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `wtc` | `"M"` | — | — | MEDIUM orlaiviai, kurių didžiausioji sertifikuotoji kilimo masė mažesnė nei 136 000 kg, bet didesnė nei 7 000 kg | — |
| `wtc` | `"J"` | — | — | SUPER, orlaivio tipas, kuris toks nurodytas ICAO dokumento Nr. 643 „Orlaivių tipų kodai“ naujausioje redakcijoje | — |
| `wtc` | `"H"` | — | — | HEAVY orlaiviai, kurių didžiausioji sertifikuotoji kilimo masė ne mažesnė nei 136 000 kg, išskyrus orlaivius, kurie ICAO dokumente Nr. 8643 išvardyti kategorijoje SUPER (J) | — |
| `wtc` | `"L"` | — | — | LIGHT orlaiviai, kurių didžiausioji sertifikuotoji kilimo masė ne didesnė nei 7 000 kg. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/on/flight_data.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/flight_data.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/on/statistika (https://data.gov.lt/datasets/2890/)
