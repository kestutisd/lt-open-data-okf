---
type: Dataset
title: "Lietuvių tautosakos archyvo įrašų kolekcija"
description: "Rinkinyje pateikiami Lietuvių Literatūros ir Tautosakos Instituto tautosakos archyvinė medžiagos duomenys."
resource: "https://get.data.gov.lt/datasets/gov/llti/tautosaka"
tags: [gov, llti, deployed, cadence-annual_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/archyvas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/llti/archyvas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2836/"
    title: "data.gov.lt DCAT-AP — datasets/gov/llti/tautosaka"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Lietuvių tautosakos archyvo įrašų kolekcija

Rinkinyje pateikiami Lietuvių Literatūros ir Tautosakos Instituto tautosakos archyvinė medžiagos duomenys. Lietuvių tautosakos archyvo duomenų bazė talpina duomenis iš Lietuvių tautosakos archyvo - didžiausios ir seniausios lietuvių folkloro saugyklos Lietuvoje ir pasaulyje. Ši folkloro saugykla paveldėjo duomenis iš Lietuvių mokslo draugijos, gyvavusios 1907–1940 Vilniuje, Lietuvių tautosakos archyvo, veikusio 1935–1939 Kaune, ir kitų fondų. Rinkinio objektas - į archyvą įtrauktas rankraštis, vaizdo arba garso įrašas ar kito pobūdžio artefaktas. Duomenys apima artefaktus nuo XIXa. pabaigos iki šių dienų. Pateikiami duomenys apie fizinius artefakto parametrus, inventorizavimą, klasifikaciją, sudarytojus, fiksavimo vietą ir kt. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt[^manifest]

- **Namespace:** `datasets/gov/llti/tautosaka`[^manifest]
- **Manifest CSV:** [datasets/gov/llti/archyvas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/archyvas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/tautosaka` (`deployed`)[^manifest]
- **Provider:** `llti` — Lietuvių literatūros ir tautosakos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2836/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/llti/tautosaka`[^dcat]
- **Portal Title (`@lt`):** Lietuvių tautosakos archyvo įrašų kolekcija[^dcat]
- **Portal Title (`@en`):** Collection of Records of Lithuanian Folklore Archives[^dcat]
- **Issued (`dct:issued`):** `2024-10-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-20`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_3` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_3`)[^dcat]
- **Distribution Date Span:** `2024-10-18` .. `2024-10-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvių Literatūros ir Tautosakos Instituto duomenų bazė talpina duomenis iš Lietuvių tautosakos archyvo – didžiausios ir seniausios lietuvių folkloro saugyklos Lietuvoje ir pasaulyje. Ši folkloro saugykla paveldėjo duomenis iš Lietuvių mokslo draugijos, gyvavusios 1907–1940 Vilniuje, Lietuvių tautosakos archyvo, veikusio 1935–1939 Kaune, ir kitų fondų. Rinkinio objektas – į archyvą įtrauktas rankraštis, vaizdo arba garso įrašas ar kito pobūdžio artefaktas. Duomenys apima artefaktus nuo XIX a. pabaigos iki šių dienų. Rinkinyje pateikiami duomenys apie fizinius artefakto parametrus, inventorizavimą, klasifikaciją, sudarytojus, fiksavimo vietą ir kt. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Lithuanian Literature and Tautosaka Institute database holds data from the Lithuanian Folklore Archives, the largest and oldest repository of Lithuanian folklore in Lithuania and the world. This folklore repository inherited data from the Lithuanian Society of Science, which existed between 1907 and 1940 in Vilnius, the Lithuanian Archives of Folklore, which existed between 1935 and 1939 in Kaunas, and other foundations. “Set object” means a manuscript, video or audio recording or other artifact included in an archive. The data includes artifacts from the late nineteenth century to the present day. The set contains data on physical artefact parameters, inventory, classification, maker, location of fixation, etc. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Artefaktas](tautosaka/Artefaktas.md) | Lietuvių tautosakos archyvo įrašų kolekcija | `4` | `vda_id` | — | `17` | Rinkinyje pateikiami Lietuvių Literatūros ir Tautosakos Instituto tautosakos archyvinė medžiagos duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/archyvas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/archyvas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/llti/tautosaka (https://data.gov.lt/datasets/2836/)
