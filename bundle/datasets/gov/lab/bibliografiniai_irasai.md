---
type: Dataset
title: "Bibliografiniai įrašai"
description: "Lentelėje pateikiamas Elektroninių leidinių valdymo informacinės sistemos (ELVIS) bibliografinių įrašų sąrašas nuo 2012 m. vasario mėn."
resource: "https://get.data.gov.lt/datasets/gov/lab/bibliografiniai_irasai"
tags: [gov, lab, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab/bibliografiniai_irasai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lab/bibliografiniai_irasai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3841/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lab/bibliografiniai_irasai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Bibliografiniai įrašai

- **Namespace:** `datasets/gov/lab/bibliografiniai_irasai`[^manifest]
- **Manifest CSV:** [datasets/gov/lab/bibliografiniai_irasai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab/bibliografiniai_irasai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab/bibliografiniai_irasai` (`deployed`)[^manifest]
- **Provider:** `lab` — Lietuvos audiosensorinė biblioteka *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3841/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lab/bibliografiniai_irasai`[^dcat]
- **Portal Title (`@lt`):** Lietuvos audiosensorinės bibliotekos bibliografiniai įrašai[^dcat]
- **Portal Title (`@en`):** Bibliographic records[^dcat]
- **Issued (`dct:issued`):** `2025-05-19`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-05-19` .. `2026-01-19`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikiamas Elektroninių leidinių valdymo informacinės sistemos (ELVIS) bibliografinių įrašų sąrašas nuo 2012 m. vasario mėn. Duomenys atnaujinami kas mėnesį. Lentelėje pateikiama informacija apie leidinį, leidinio leidėją, autorius, kopijos rengėją, diktorius, kopijos vidutinį vertinimą, taip pat nurodytas leidinį įvertinusių naudotojų ir naudotojų, pažymėjusių leidinį kaip mėgstamiausią, skaičius (stulpelis – „megstamiausiu_kiekis“). Data, kuriai apskaičiuoti leidinio vertinimai, pateikiama stulpelyje „apskaiciuoto_vertinimo_data“. Stulpelyje „matomas“ reikšmę „FALSE“ turintys leidiniai bibliotekos naudotojams neprieinami dėl pasibaigusios licencijos ar kitų priežasčių; stulpelyje „atvirtas“ reikšmę „FALSE“ turintys leidiniai prieinami tik naudotojams, negalintiems skaityti įprasto spausdinto teksto. Duomenų teikėjas – Lietuvos audiosensorinė biblioteka (LAB). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table provides a list of bibliographic records of the Electronic Publications Management Information System (ELVA) from February 2012. The data is updated monthly. The table contains information about the publication, the publisher, the author, the originator of the copy, the dictators, the average evaluation of the copy, as well as the number of users who rated the publication and the number of users who marked the publication as their favourite (column is the “most favourite quantity”). The date on which the estimates of the publication are calculated is shown in the “Accounted_Estimated_Date” column. Publications with the “visible” value “FALSE” in the column are not available to library users due to expired license or other reasons; publications with the “open” value “FALSE” in the column are only available to users unable to read normal printed text. Data provider – Lithuanian Audiosensory Library (LAB). Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AudiosensorinisIrasas](bibliografiniai_irasai/AudiosensorinisIrasas.md) | Bibliografiniai įrašai | `4` | — | — | `33` | Elektroninių leidinių valdymo informacinės sistemos (ELVIS) bibliografinių įrašų sąrašas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab/bibliografiniai_irasai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab/bibliografiniai_irasai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lab/bibliografiniai_irasai (https://data.gov.lt/datasets/3841/)
