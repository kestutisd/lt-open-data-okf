---
type: Table
title: "Dalykas — AIS išieškojimo dalykų klasifikatorius"
description: "AIS išieškojimo dalykų ir bylų būsenų klasifikatoriai (duomenų rinkinių grupė, viso 2vnt.) (AIS išieškojimo kategorijų klasifikatorius; AIS bylų būsenų klasifikatorius)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/busenu_dalyku_klasifikatorius/Dalykas"
tags: [gov, rc, dalykas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/busenu_dalyku_klasifikatorius.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/busenu_dalyku_klasifikatorius.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2183/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/busenu_dalyku_klasifikatorius"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Dalykas — AIS išieškojimo dalykų klasifikatorius

**Dataset Context:** AIS išieškojimo dalykų ir bylų būsenų klasifikatoriai (duomenų rinkinių grupė, viso 2vnt.) (AIS išieškojimo kategorijų klasifikatorius; AIS bylų būsenų klasifikatorius). Antstolių informacinės sistemos (AIS) klasifikatoriai. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 12 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/busenu_dalyku_klasifikatorius/Dalykas`[^manifest]
- **Dataset:** [AIS išieškojimo dalykų ir bylų būsenų klasifikatoriai](../busenu_dalyku_klasifikatorius.md) (`datasets/gov/rc/ais/busenu_dalyku_klasifikatorius`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/busenu_dalyku_klasifikatorius.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/busenu_dalyku_klasifikatorius.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/busenu_dalyku_klasifikatorius/Dalykas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Išieškojimo dalyko kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Išieškojimo dalyko pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/busenu_dalyku_klasifikatorius.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/busenu_dalyku_klasifikatorius.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/busenu_dalyku_klasifikatorius (https://data.gov.lt/datasets/2183/)
