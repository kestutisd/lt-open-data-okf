---
type: Dataset
title: "Į aplinkos orą išmetamų teršalų apskaitos duomenys"
description: "Teršalų išmetimų į aplinkos orą Lietuvoje iš stacionarių ir mobilių taršos šaltinių apskaitos duomenys."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_tersalu_duomenys"
tags: [gov, aaa, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tersalu_duomenys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_tersalu_duomenys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/884/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/oro_tersalu_duomenys"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Į aplinkos orą išmetamų teršalų apskaitos duomenys

- **Namespace:** `datasets/gov/aaa/oro_tersalu_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/oro_tersalu_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tersalu_duomenys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_tersalu_duomenys` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/884/`[^dcat]
- **Publisher (`dct:publisher`):** Aplinkos apsaugos agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/aaa/oro_tersalu_duomenys`[^dcat]
- **Portal Title (`@lt`):** Į aplinkos orą išmetamų teršalų apskaitos duomenys[^dcat]
- **Portal Title (`@en`):** Air pollution data[^dcat]
- **Issued (`dct:issued`):** `2022-10-26`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-10-24` .. `2026-01-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Teršalų išmetimų į aplinkos orą Lietuvoje iš stacionarių ir mobilių taršos šaltinių apskaitos duomenys. Iš stacionarių ir mobilių šaltinių į aplinkos orą išmetamų teršalų struktūra. Pateikiami duomenys apie šių teršalų ir jų grupių išmetimus – sieros oksidų (SOx), azoto oksidų (NOx), nemetaninių lakiųjų organinių junginių (NMLOJ), amoniako (NH3), kietųjų dalelių (KD2,5; KD10, TSP, BC), anglies monoksido (CO), sunkiųjų metalų (Cd, Cr, Cu, Hg, Ni, Pb, Se ir Zn), patvariųjų organinių teršalų (dioksinai ir furanai, benzo(a)pirenas, benzo(b)fluorantenas, benzo(k)fluorantenas, indeno(1,2,3cd)pirenas, heksachlorobenzenas, polichlorinti bifenilai). Ūkio sektoriai, kurių išmetamų teršalų apskaita vykdoma – energetika, transportas, žemės ūkis, namų ūkiai, pramonė, atliekos. Apskaitos duomenys rengiami vadovaujantis Europos Parlamento ir Tarybos Direktyvos (ES) 2016/2284 bei Tolimųjų Tarpvalstybinių Oro Teršalų Pernašų Konvencijos (TTOTPK) ir jos protokolų reikalavimais. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Accounting data for emissionsfrom stationary and mobile sources of ambient air pollution in Lithuania. Structure of emissions from stationary and mobile sources. Data provided on emissions of these pollutants; sulphur oxide (SOx), nitrogen oxide (NOx), non-methane volatile organic compounds (NMLOJ), ammonia (NH3), particulate matter (PM2,5); PM10, TSP, BC), carbon monoxide (CO), heavy metals (Cd, Cr, Cu, Hg, Ni, Pb, Se and Zn), persistent organic pollutants (dioxins and furans, benzo(a)pyrene, benzo(b)fluoranthene, benzo(k)fluoranthene, indeno(1,2,3cd)pyrene, hexachlorobenzene, polychlorinated biphenyls). The sectors of the economy for which emissions are accounted for are energy, transport, agriculture, households, industry, waste. Accounting data is compiled in accordance with the requirements of Directive (EU) 2016/2284 of the European Parliament and the Council and the Convention on Long-Range Transboundary Air Pollution (ICRC) and its Protocols.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IAtmosferaIsmetamiTersalai](oro_tersalu_duomenys/IAtmosferaIsmetamiTersalai.md) | Į atmosferą išmestų teršalų kiekis | `4` | — | — | `6` | — |
| [UkioSektoriai](oro_tersalu_duomenys/UkioSektoriai.md) | Ūkio sektoriai | `4` | — | — | `2` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_tersalu_duomenys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tersalu_duomenys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/oro_tersalu_duomenys (https://data.gov.lt/datasets/884/)
