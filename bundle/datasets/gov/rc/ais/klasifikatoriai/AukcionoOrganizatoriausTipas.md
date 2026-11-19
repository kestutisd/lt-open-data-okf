---
type: Table
title: "AukcionoOrganizatoriausTipas — AIS elektroninių varžytynių ir aukcionų organizatorių klasifikatorius"
description: "AIS esančių aukcionų ir elektroninių varžytynių rūšių duomenys (paskelbta ir įvyko)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/klasifikatoriai/AukcionoOrganizatoriausTipas"
tags: [gov, rc, aukcionoorganizatoriaustipas, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/klasifikatoriai.csv#L13"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/klasifikatoriai.csv#L13"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2182/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AukcionoOrganizatoriausTipas — AIS elektroninių varžytynių ir aukcionų organizatorių klasifikatorius

**Dataset Context:** AIS esančių aukcionų ir elektroninių varžytynių rūšių duomenys (paskelbta ir įvyko). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie aukcionus ir elektronines varžytynes. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/klasifikatoriai/AukcionoOrganizatoriausTipas`[^manifest]
- **Dataset:** [AIS tipų ir potipių klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/rc/ais/klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/klasifikatoriai.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/klasifikatoriai.csv#L13)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/klasifikatoriai/AukcionoOrganizatoriausTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `3` | `open` | — | Organizatoriaus tipo kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Organizatoriaus tipo pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/klasifikatoriai.csv#L13 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/klasifikatoriai.csv#L13)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/klasifikatoriai (https://data.gov.lt/datasets/2182/)
