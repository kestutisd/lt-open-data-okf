---
type: Dataset
title: "Transliacijos stočių leidimai"
description: "Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai naudoti transliacijos stotis (radijo, televizijos)."
resource: "https://get.data.gov.lt/datasets/gov/rrt/leid_transliacijos_stotys"
tags: [gov, rrt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_transliacijos_stotys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rrt/leid_transliacijos_stotys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2729/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rrt/leid_transliacijos_stotys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Transliacijos stočių leidimai

- **Namespace:** `datasets/gov/rrt/leid_transliacijos_stotys`[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/leid_transliacijos_stotys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_transliacijos_stotys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/leid_transliacijos_stotys` (`deployed`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2729/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rrt/leid_transliacijos_stotys`[^dcat]
- **Portal Title (`@lt`):** Transliacijos stočių leidimai[^dcat]
- **Portal Title (`@en`):** Broadcasting station editions[^dcat]
- **Issued (`dct:issued`):** `2024-08-01`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-08-01` .. `2026-10-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai naudoti transliacijos stotis (radijo, televizijos). Rinkinyje naudojamos WGS koordinatės, nurodančios antenos lokaciją. Pateikiami tik šiuo metu galiojantys leidimai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt. Pastaba: 2025.05.30 rinkinys papildytas nauju stulpeliu: antenos_poliarizacija (H - horizontali, V - vertikali)[^dcat]

### Portal Description (`@en`)

The table shall contain authorisations issued by the Communications Regulatory Authority of the Republic of Lithuania for the use of broadcasting stations (radio, television). The kit uses WGS coordinates to indicate the location of the antenna. Only currently valid permits are provided.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TransliacijosStotysLeidimas](leid_transliacijos_stotys/TransliacijosStotysLeidimas.md) | Transliacijos stočių leidimai | `4` | `iraso_id` | — | `15` | Lentelėje pateikiami Lietuvos Respublikos ryšių reguliavimo tarnybos išduoti leidimai naudoti transliacijos stotis (radijo, televizijos). |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/leid_transliacijos_stotys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/leid_transliacijos_stotys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rrt/leid_transliacijos_stotys (https://data.gov.lt/datasets/2729/)
