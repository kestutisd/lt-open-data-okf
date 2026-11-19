---
type: Table
title: "Isieskojimas — Antstolių informacinės sistemos (AIS) duomenys apie išieškojimus"
description: "AIS duomenys apie išieškojimus (pagal išieškojimo dalyką, pradinę išieškotiną skolą)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/isieskojimai/Isieskojimas"
tags: [gov, rc, isieskojimas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/isieskojimai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/isieskojimai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2176/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/isieskojimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Isieskojimas — Antstolių informacinės sistemos (AIS) duomenys apie išieškojimus

**Dataset Context:** AIS duomenys apie išieškojimus (pagal išieškojimo dalyką, pradinę išieškotiną skolą). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie skolų išieškotojus. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/isieskojimai/Isieskojimas`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (AIS) duomenys apie išieškojimus](../isieskojimai.md) (`datasets/gov/rc/ais/isieskojimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/isieskojimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/isieskojimai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/isieskojimai/Isieskojimas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `isieskojimo_dalykas` | `ref` | [Dalykas](../busenu_dalyku_klasifikatorius/Dalykas.md) (`level=4 UUID`: `isieskojimo_dalykas._id`) | `4` | `open` | — | Išieškojimo dalyko kodas iš AIS išieškojimo dalykų klasifikatoriaus | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Vykdomų bylų kiekis (sugrupuota pagal išieškojimo dalyką) | — |
| `pradine_isieskojimo_suma` | `integer` | — | `3` | `open` | — | Vykdomų bylų bendra pradinė išieškojimo suma (sugrupuota pagal išieškojimo dalyką) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/isieskojimai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/isieskojimai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/isieskojimai (https://data.gov.lt/datasets/2176/)
