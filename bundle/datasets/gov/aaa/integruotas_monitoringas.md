---
type: Dataset
title: "Integruoto monitoringo duomenys"
description: "Tyrimai Aukštaitijos ir Žemaitijos integruoto monitoringo stotyse bei Preilos atmosferos užterštumo tyrimų stotyje atliekami siekiant įvertinti tolimųjų oro teršalų pernašų iš kitų valstybių srautus, jų poveikį bendram Lietuvos oro baseino užterštumo lygiui, jų kaitą..."
resource: "https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas"
tags: [gov, aaa, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1792/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/integruotas_monitoringas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Integruoto monitoringo duomenys

- **Namespace:** `datasets/gov/aaa/integruotas_monitoringas`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/integruotas_monitoringas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1792/`[^dcat]
- **Publisher (`dct:publisher`):** Aplinkos apsaugos agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/aaa/integruotas_monitoringas`[^dcat]
- **Portal Title (`@lt`):** Integruoto monitoringo duomenys[^dcat]
- **Portal Title (`@en`):** Integrated monitoring data[^dcat]
- **Issued (`dct:issued`):** `2023-05-26`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-05-26` .. `2026-01-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Tyrimai Aukštaitijos ir Žemaitijos integruoto monitoringo stotyse bei Preilos atmosferos užterštumo tyrimų stotyje atliekami siekiant įvertinti tolimųjų oro teršalų pernašų iš kitų valstybių srautus, jų poveikį bendram Lietuvos oro baseino užterštumo lygiui, jų kaitą pagrindiniuose Lietuvos kraštovaizdžio tipuose, teršalų transformaciją ir poveikį sąlygiškai natūralių ekosistemų būklei. Tyrimai atliekami įgyvendinant Europos Parlamento ir Tarybos direktyvų 2004/107/EB dėl arseno, kadmio, gyvsidabrio, nikelio ir policiklinių aromatinių angliavandenilių aplinkos ore ir 2008/50/EB dėl aplinkos oro kokybės ir švaresnio oro Europoje reikalavimus, Europos Parlamento ir Tarybos direktyvos (ES) 2016/2284 įpareigojimus dėl neigiamo oro taršos poveikio ekosistemoms stebėsenos vykdymui (9, 10 straipsnių ir V priedo reikalavimai), atsižvelgiant į šalies įsipareigojimus dėl Tolimųjų tarpvalstybinių oro teršalų pernašų konvencijos įgyvendinimui skirtų Europos monitoringo ir vertinimo programos (EMEP) bei Tarptautinės bendradarbiavimo programos integruoto monitoringo srityje (ICP IM) reikalavimus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The research is carried out at Aukštaitija and Žemaitija and Preila integrated air pollution research stations. To estimate the long-range transmission of air pollutants from other countries. Their impact on the overall pollution level of the Lithuanian air basin. Change in the main types of Lithuanian landscape. Transformation of pollutants and effects on the condition of relatively natural ecosystems. The research are carried out in implementation of Directives 2004/107/ EC of the European Parliament and of the Council relating to arsenic, cadmium, mercury, nickel and polycyclic aromatic hydrocarbons in ambient air. And 2008/50 / EC on ambient air quality and cleaner air for Europe. The obligations of Directive (EU) 2016/2284 of the European Parliament and of the Council to monitor the adverse effects of air pollution on ecosystems (requirements of Articles 9, 10 and Annex V), taking into account the country's obligations under the European Monitoring and Evaluation Program EMEP) and the requirements of the International Cooperative Program on Integrated Monitoring (ICP IM).[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Tyrimas](integruotas_monitoringas/Tyrimas.md) | Tyrimai | `2` | — | — | `6` | — |
| [TyrimoSudedamoji](integruotas_monitoringas/TyrimoSudedamoji.md) | Tyrimų sudedamosios | `2` | — | — | `5` | — |
| [TyrimoRezultatas](integruotas_monitoringas/TyrimoRezultatas.md) | Tyrimų rezultatai | `4` | — | — | `3` | — |
| [ParametrasVienetas](integruotas_monitoringas/ParametrasVienetas.md) | Parametrai, vienetai | `2` | — | — | `4` | — |
| [Metodas](integruotas_monitoringas/Metodas.md) | Metodai | `4` | — | — | `4` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/integruotas_monitoringas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/integruotas_monitoringas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/integruotas_monitoringas (https://data.gov.lt/datasets/1792/)
