---
type: Table
title: "AukcionoRusis — Antstolių informacinėje sistemoje (AIS) esančių aukcionų ir elektroninių varžytynių rūšių duomenys"
description: "AIS esančių aukcionų ir elektroninių varžytynių rūšių duomenys (paskelbta ir įvyko)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/aukcionu_rusys/AukcionoRusis"
tags: [gov, rc, aukcionorusis, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/aukcionu_rusys.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/aukcionu_rusys.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2179/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/aukcionu_rusys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AukcionoRusis — Antstolių informacinėje sistemoje (AIS) esančių aukcionų ir elektroninių varžytynių rūšių duomenys

**Dataset Context:** AIS esančių aukcionų ir elektroninių varžytynių rūšių duomenys (paskelbta ir įvyko). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie aukcionus ir elektronines varžytynes. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/aukcionu_rusys/AukcionoRusis`[^manifest]
- **Dataset:** [Antstolių informacinėje sistemoje (AIS) esančių aukcionų ir elektroninių varžytynių rūšių duomenys](../aukcionu_rusys.md) (`datasets/gov/rc/ais/aukcionu_rusys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/aukcionu_rusys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/aukcionu_rusys.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/aukcionu_rusys/AukcionoRusis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `aukciono_tipas` | `ref` | [AukcionoTipas](../klasifikatoriai/AukcionoTipas.md) (`level=4 UUID`: `aukciono_tipas._id`) | `4` | `open` | — | Varžytynių / aukcionų tipo kodas iš AIS varžytynių ir aukcionų tipų klasifikatoriaus | — |
| `kiek_paskelbta` | `string` | — | `3` | `open` | — | Bendras paskelbtų varžytinių, aukcionų kiekis | — |
| `kiek_ivyko` | `string` | — | `3` | `open` | — | Bendras įvykusių varžytinių, aukcionų kiekis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/aukcionu_rusys.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/aukcionu_rusys.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/aukcionu_rusys (https://data.gov.lt/datasets/2179/)
