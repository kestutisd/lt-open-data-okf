---
type: Dataset
title: "Nepriklausomų elektros energijos tiekėjų planai"
description: "Duomenų rinkinyje pateikiami nepriklausomų elektros energijos tiekėjų planai buitiniams vartotojams."
resource: "https://get.data.gov.lt/datasets/gov/vert/neprikl_ee_tiek_planai"
tags: [gov, vert, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vert/neprikl_ee_tiek_planai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/vert/neprikl_ee_tiek_planai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2802/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vert/neprikl_ee_tiek_planai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Nepriklausomų elektros energijos tiekėjų planai

- **Namespace:** `datasets/gov/vert/neprikl_ee_tiek_planai`[^manifest]
- **Manifest CSV:** [datasets/gov/vert/neprikl_ee_tiek_planai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vert/neprikl_ee_tiek_planai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vert/neprikl_ee_tiek_planai` (`deployed`)[^manifest]
- **Provider:** `vert` — Valstybinė energetikos reguliavimo tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2802/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vert/neprikl_ee_tiek_planai`[^dcat]
- **Portal Title (`@lt`):** Nepriklausomų elektros energijos tiekėjų planai[^dcat]
- **Portal Title (`@en`):** Plans of independent electricity suppliers[^dcat]
- **Issued (`dct:issued`):** `2025-11-19`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-09-18` .. `2025-06-18`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami nepriklausomų elektros energijos tiekėjų planai buitiniams vartotojams. Plano kainą sudaro tiekėjo kaina, ESO plano kaina, persiuntimo, skirstymo ir viap dedamosios. Biržos planų kainą sudaro „Nordpool“ biržos kaina (rinkinyje nepateikta), kuri keičiasi kas mėnesį arba valandą (priklauso nuo pasirinkto plano), tiekėjo kaina, ESO kaina ir valstybės reguliuojamos kainos dalys. Valstybės reguliuojamos kainų dalys (skirstymo, persiuntimo ir viap dedamosios) fiksuojamos nepriklausomai nuo plano fiksavimo termino, todėl bendra fiksuoto plano kaina gali kisti. Duomenų teikėjas – Valstybinė energetikos reguliavimo taryba. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set shall contain plans of independent electricity suppliers for household customers. The price of the plan shall consist of the supplier's price, the cost of the ESO plan, the components of the transfer, distribution and viap. The price of the stock exchange plans consists of Nordpool stock exchange price (not included in the set), which changes monthly or hourly (depending on the plan chosen), supplier price, ESO price and state-regulated price shares. State-regulated price components (distribution, transfer and viap components) are recorded independently of the time limit for fixation of the plan, therefore the total price of the fixed plan may change. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NepriklElEnergTiekPlanas](neprikl_ee_tiek_planai/NepriklElEnergTiekPlanas.md) | Nepriklausomų elektros energijos tiekėjų planai | `4` | `vda_prime_key` | — | `33` | Duomenų rinkinyje pateikiami nepriklausomų elektros energijos tiekėjų planai buitiniams vartotojams. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vert/neprikl_ee_tiek_planai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vert/neprikl_ee_tiek_planai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vert/neprikl_ee_tiek_planai (https://data.gov.lt/datasets/2802/)
