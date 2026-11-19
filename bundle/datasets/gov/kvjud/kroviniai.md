---
type: Dataset
title: "Krovininių laivų operacijos Klaipėdos valstybiniame jūrų uoste"
description: "Duomenų rinkinyje pateikiami Klaipėdos valstybinio jūrų uosto direkcijos duomenys apie krovininių laivų operacijas Klaipėdos jūrų uoste."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/kroviniai"
tags: [gov, kvjud, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/kroviniai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kvjud/kroviniai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2857/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kvjud/kroviniai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Krovininių laivų operacijos Klaipėdos valstybiniame jūrų uoste

Duomenų rinkinyje pateikiami Klaipėdos valstybinio jūrų uosto direkcijos duomenys apie krovininių laivų operacijas Klaipėdos jūrų uoste. Rinkinio objektas - atvykimo arba išvykimo operacija. Duomenys pateikiami nuo 2002m. iki šių dienų. Nurodoma operacijos rūšis, laivo savininko atstovas, su laivo atvykimu/išvykimu (išvykimo ir atvykimo uostas, faktiniai išvykimo laikai) bei su laivu (pavadinimas, tipas, vėliava, IMO numeris, dedveitas ir bendroji talpa) susijusi informacija. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/kvjud/kroviniai`[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/kroviniai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/kroviniai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/kroviniai` (`deployed`)[^manifest]
- **Provider:** `kvjud` — AB Klaipėdos valstybinio jūrų uosto direkcija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2857/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kvjud/kroviniai`[^dcat]
- **Portal Title (`@lt`):** Krovininių laivų operacijos Klaipėdos valstybiniame jūrų uoste[^dcat]
- **Portal Title (`@en`):** Cargo ship operations in Klaipėda State Seaport[^dcat]
- **Issued (`dct:issued`):** `2024-11-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-15` .. `2026-10-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by-sa/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami Klaipėdos valstybinio jūrų uosto direkcijos duomenys apie krovininių laivų operacijas Klaipėdos jūrų uoste. Rinkinio objektas - atvykimo arba išvykimo operacija. Duomenys pateikiami nuo 2002 m. iki šių dienų. Nurodoma operacijos rūšis, laivo savininko atstovas, su laivo atvykimu/išvykimu (išvykimo ir atvykimo uostas, faktiniai išvykimo laikai) bei su laivu (pavadinimas, tipas, vėliava, IMO numeris, dedveitas ir bendroji talpa) susijusi informacija. Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set contains data of the Klaipėda State Seaport Authority on cargo ship operations in Klaipėda Seaport. The object of the kit is an entry or exit operation. Data shall be provided from 2002 to the present day. Indicate the type of operation, the representative of the shipowner, the information relating to the arrival/departure of the vessel (port of departure and arrival, actual departure times) and the vessel (name, type, flag, IMO number, loading and gross tonnage). Data provider – AB Klaipėda State Seaport Authority. If you have any questions about the dataset, please contact the State Data Control Opening Team by e-mail atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Operacija](kroviniai/Operacija.md) | Krovininių laivų operacijos Klaipėdos valstybinio jūrų uoste | `4` | `vda_id` | — | `19` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/kroviniai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/kroviniai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kvjud/kroviniai (https://data.gov.lt/datasets/2857/)
