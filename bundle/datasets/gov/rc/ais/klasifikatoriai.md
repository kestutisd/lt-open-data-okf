---
type: Dataset
title: "AIS tipų ir potipių klasifikatoriai"
description: "AIS esančių aukcionų ir elektroninių varžytynių rūšių duomenys (paskelbta ir įvyko)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/klasifikatoriai"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/klasifikatoriai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# AIS tipų ir potipių klasifikatoriai

AIS esančių aukcionų ir elektroninių varžytynių rūšių duomenys (paskelbta ir įvyko). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie aukcionus ir elektronines varžytynes. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0

- **Namespace:** `datasets/gov/rc/ais/klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/klasifikatoriai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/klasifikatoriai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TurtoPotipis](klasifikatoriai/TurtoPotipis.md) | AIS parduodamo turto potipių klasifikatorius | — | `kodas` | — | 3 | — |
| [TurtoTipas](klasifikatoriai/TurtoTipas.md) | AIS parduodamo turto tipų klasifikatorius | — | `kodas` | — | 2 | — |
| [AukcionoOrganizatoriausTipas](klasifikatoriai/AukcionoOrganizatoriausTipas.md) | AIS elektroninių varžytynių ir aukcionų organizatorių klasifikatorius | — | `kodas` | — | 2 | — |
| [AukcionoTipas](klasifikatoriai/AukcionoTipas.md) | AIS elektroninių varžytynių ir aukcionų tipų klasifikatorius | — | `kodas` | — | 2 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/klasifikatoriai.csv
