---
type: Table
title: "BylaKiekis — Antstolių informacinės sistemos (AIS) duomenys apie vykdomąsias bylas pagal jų kiekį"
description: "Spinta table datasets/gov/rc/ais/bylos_pagal_kiekius/BylaKiekis (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/bylos_pagal_kiekius/BylaKiekis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/bylos_pagal_kiekius.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_pagal_kiekius.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# BylaKiekis — Antstolių informacinės sistemos (AIS) duomenys apie vykdomąsias bylas pagal jų kiekį

- **Model:** `datasets/gov/rc/ais/bylos_pagal_kiekius/BylaKiekis`[^manifest]
- **Dataset:** [Antstolių informacinės sistemos (AIS) duomenys apie vykdomąsias bylas pagal jų kiekį](../bylos_pagal_kiekius.md) (`datasets/gov/rc/ais/bylos_pagal_kiekius`)
- **Manifest CSV:** [datasets/gov/rc/ais/bylos_pagal_kiekius.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_pagal_kiekius.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/bylos_pagal_kiekius/BylaKiekis`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai, kuriais pradėta išieškojimo byla | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurioje deklaruota skolininko (fizinio asmens) gyvenamoji vieta arba registruota skolininko (juridinio asmens) buveinė, kodas iš Adresų registro (kai gyvenamoji vieta arba buveinė nenurodyta - -1) | — |
| `tipas` | `string` | — | `4` | `open` | — | Asmens, iš kurio vykdomas išieškojimas, tipas (Fizinis asmuo - kai fizinis asmuo; Juridinis asmuo pats iš savęs (lot. Per se); LR juridinis asmuo; Užsienio juridinis asmuo - kai juridinis asmuo; Nenustatytas - kai asmens tipas nenurodytas) | — |
| `bylu_kiekis` | `string` | — | `3` | `open` | — | Vykdomų bylų kiekis (sugrupuotas pagal metus, savivaldybę ir asmens tipą) | — |
| `skolu_suma` | `integer` | — | `3` | `open` | — | Vykdomų bylų bendra skolų suma (sugrupuota pagal metus, savivaldybę ir asmens tipą) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/bylos_pagal_kiekius.csv
