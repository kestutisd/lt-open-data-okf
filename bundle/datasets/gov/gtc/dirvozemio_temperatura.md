---
type: Dataset
title: "Dirvožemio temperatūra ir drėgmė bei dirvožemyje augantys augalai"
description: "Informacija apie P.B Šivickio Gamtos Tyrimų Centro mokslinių darbuotojų tiriamą dirvožemio temperatūrą ir drėgmę natūraliose arba pusiau natūraliose pievų bendrijose Lietuvos teritorijoje"
resource: "https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura"
tags: [gov, gtc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/gtc/dirvozemio_temperatura.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2638/"
    title: "data.gov.lt DCAT-AP — datasets/gov/gtc/dirvozemio_temperatura"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Dirvožemio temperatūra ir drėgmė bei dirvožemyje augantys augalai

Informacija apie P.B Šivickio Gamtos Tyrimų Centro mokslinių darbuotojų tiriamą dirvožemio temperatūrą ir drėgmę natūraliose arba pusiau natūraliose pievų bendrijose Lietuvos teritorijoje[^manifest]

- **Namespace:** `datasets/gov/gtc/dirvozemio_temperatura`[^manifest]
- **Manifest CSV:** [datasets/gov/gtc/dirvozemio_temperatura.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura` (`deployed`)[^manifest]
- **Provider:** `gtc` — Gamtos tyrimų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2638/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura`[^dcat]
- **Portal Title (`@lt`):** Dirvožemio temperatūra ir drėgmė bei dirvožemyje augantys augalai[^dcat]
- **Portal Title (`@en`):** Soil temperature and humidity and soils[^dcat]
- **Issued (`dct:issued`):** `2024-05-03`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-05-09` .. `2026-04-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Publikuojama informacija apie Gamtos Tyrimų Centro Floros ir geobotanikos laboratorijos mokslinių darbuotojų tiriamą dirvožemio temperatūrą ir drėgmę natūraliose arba pusiau natūraliose pievų bendrijose Lietuvos teritorijoje nuo 2018 metų. Tokie duomenys leidžia tiksliau įvertinti klimato kaitą ir kaitos padarinius augalų bendrijoms lyginant su tradiciniais meteorologinių stotelių kaupiamais duomenimis. Dirvožemio drėgmė apskaičiuojama remiantis informacija pateikta adresu https://tomst.com/web/en/systems/tms/software/ bei esančia skyrelyje „TMS Calibr utility“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Information on soil temperature and moisture in natural or Šivickis-natural grassland communities in the territory of Lithuania from 2018 shall be published. Such data allow for a more accurate assessment of climate change and the effects of change on plant communities compared to the traditional data collected by meteorological stations. Soil humidity shall be calculated on the basis of the information provided at the address https://tomst.com/web/en/systems/tms/software/ and in the section “TMS Calibr utility”.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VietovesTemperaturaDregme](dirvozemio_temperatura/VietovesTemperaturaDregme.md) | Vietovės dirvožemio temperatūra ir drėgmė | `4` | `atvejo_id` | — | `10` | Informacija apie Gamtos Tyrimų Centro mokslinių darbuotojų tiriamą dirvožemio temperatūrą ir drėgmę įvairiose vietovėse Lietuvos teritorijoje |
| [VietovesAugalas](dirvozemio_temperatura/VietovesAugalas.md) | Vietovės dirvožemio augalai | `4` | `iraso_id` | — | `3` | Informacija apie Lietuvos teritorijos vietovėse, kuriose Gamtos Tyrimų Centro moksliniai darbuotojai tiria dirvožemio temperatūrą ir drėgmę, augalus augančius. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/gtc/dirvozemio_temperatura.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/gtc/dirvozemio_temperatura (https://data.gov.lt/datasets/2638/)
