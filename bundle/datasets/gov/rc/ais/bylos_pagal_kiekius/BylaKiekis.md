---
type: Table
title: "BylaKiekis — Antstolių informacinės sistemos (AIS) duomenys apie vykdomąsias bylas pagal jų kiekį"
description: "AIS esančių vykdomųjų bylų duomenys pagal bylų kiekį (bylų kiekis pagal metus (bylos užvedimo datą), pagal skolininkų tipą (fizinis, juridinis), pagal skolininko teritoriją, išieškotiną sumą)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/bylos_pagal_kiekius/BylaKiekis"
tags: [gov, rc, bylakiekis, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_pagal_kiekius.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/bylos_pagal_kiekius.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2171/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/bylos_pagal_kiekius"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# BylaKiekis — Antstolių informacinės sistemos (AIS) duomenys apie vykdomąsias bylas pagal jų kiekį

**Dataset Context:** AIS esančių vykdomųjų bylų duomenys pagal bylų kiekį (bylų kiekis pagal metus (bylos užvedimo datą), pagal skolininkų tipą (fizinis, juridinis), pagal skolininko teritoriją, išieškotiną sumą). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie antstolių vykdomas bylas. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Model:** `datasets/gov/rc/ais/bylos_pagal_kiekius/BylaKiekis`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (AIS) duomenys apie vykdomąsias bylas pagal jų kiekį](../bylos_pagal_kiekius.md) (`datasets/gov/rc/ais/bylos_pagal_kiekius`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/bylos_pagal_kiekius.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_pagal_kiekius.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/bylos_pagal_kiekius/BylaKiekis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai, kuriais pradėta išieškojimo byla | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurioje deklaruota skolininko (fizinio asmens) gyvenamoji vieta arba registruota skolininko (juridinio asmens) buveinė, kodas iš Adresų registro (kai gyvenamoji vieta arba buveinė nenurodyta - -1) | — |
| `tipas` | `string` | — | `4` | `open` | — | Asmens, iš kurio vykdomas išieškojimas, tipas (Fizinis asmuo - kai fizinis asmuo; Juridinis asmuo pats iš savęs (lot. Per se); LR juridinis asmuo; Užsienio juridinis asmuo - kai juridinis asmuo; Nenustatytas - kai asmens tipas nenurodytas) | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Vykdomų bylų kiekis (sugrupuotas pagal metus, savivaldybę ir asmens tipą) | — |
| `skolu_suma` | `integer` | — | `3` | `open` | — | Vykdomų bylų bendra skolų suma (sugrupuota pagal metus, savivaldybę ir asmens tipą) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Fizinis asmuo"` | — | — | kai skolininko tipas fizinis asmuo | — |
| `tipas` | `"Juridinis asmuo"` | — | — | kai skolininko tipas juridinis asmuo pats iš savęs (lot. Per se) | — |
| `tipas` | `"LR juridinis asmuo"` | — | — | kai skolininko tipas Lietuvos Respublikoje įregistruotas juridinis asmuo | — |
| `tipas` | `"Užsienio juridinis asmuo"` | — | — | kai skolininko tipas užsienio valstybėje įregistruotas juridinis asmuo | — |
| `tipas` | `"Nenustatytas"` | — | — | kai skolininko tipas kaip asmens tipas nenurodytas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/bylos_pagal_kiekius.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_pagal_kiekius.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/bylos_pagal_kiekius (https://data.gov.lt/datasets/2171/)
