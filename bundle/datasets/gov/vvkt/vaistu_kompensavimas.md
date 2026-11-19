---
type: Dataset
title: "Sveikatos technologijų vertinimas (STV). Paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys ir vertinimo eigos stebėsena"
description: "Duomenų rinkinį sudaro Valstybinei vaistų kontrolės tarnybai prie Lietuvos Respublikos sveikatos apsaugos ministerijos pateiktų sveikatos technologijų vertinimo paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistu_kompensavimas"
tags: [gov, vvkt, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_kompensavimas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistu_kompensavimas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2897/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkt/vaistu_kompensavimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sveikatos technologijų vertinimas (STV). Paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys ir vertinimo eigos stebėsena

Duomenų rinkinį sudaro Valstybinei vaistų kontrolės tarnybai prie Lietuvos Respublikos sveikatos apsaugos ministerijos pateiktų sveikatos technologijų vertinimo paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys. Rinkinyje pateikiama tokių paraiškų eiga – nurodomos aktualios datos, pareiškėjai, vaistiniai preparatai, indikacijos ir pan. Duomenų rinkinio viena eilutė atitinka vieną paraišką. Su rekomendacijomis ir detalesne informacija galima susipažinti čia: https://vvkt.lrv.lt/lt/sveikatos-technologiju-vertinimas/vaistiniu-preparatu-medicinos-pagalbos-priemoniu-ir-ligu-vertinimai/. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vvkt/vaistu_kompensavimas`[^manifest]
- **Manifest CSV:** [datasets/gov/vvkt/vaistu_kompensavimas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_kompensavimas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistu_kompensavimas` (`deployed`)[^manifest]
- **Provider:** `vvkt` — Valstybinė vaistų kontrolės tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2897/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vvkt/vaistu_kompensavimas`[^dcat]
- **Portal Title (`@lt`):** Sveikatos technologijų vertinimo (STV) paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys ir vertinimo eigos stebėsena[^dcat]
- **Portal Title (`@en`):** Data on Health Technology Assessment (STV) applications for inclusion in reimbursement lists and monitoring of evaluation progress[^dcat]
- **Issued (`dct:issued`):** `2024-12-16`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-12-16` .. `2026-06-10`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinį sudaro Valstybinei vaistų kontrolės tarnybai prie Lietuvos Respublikos sveikatos apsaugos ministerijos pateiktų sveikatos technologijų vertinimo paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys. Rinkinyje pateikiama tokių paraiškų eiga – nurodomos aktualios datos, pareiškėjai, vaistiniai preparatai, indikacijos ir pan. Duomenų rinkinio viena eilutė atitinka vieną paraišką. Su rekomendacijomis ir detalesne informacija galima susipažinti čia: https://vvkt.lrv.lt/lt/sveikatos-technologiju-vertinimas/vaistiniu-preparatu-medicinos-pagalbos-priemoniu-ir-ligu-vertinimai/. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set shall consist of the data on the applications for evaluation of health technologies submitted to the State Medicines Control Agency under the Ministry of Health of the Republic of Lithuania to put a medicinal product on the reimbursement lists. The package shall include the progress of such applications, including relevant dates, applicants, medicinal products, indications, etc. One line of the data set corresponds to one application. Recommendations and more detailed information can be found here: https://vvkt.lrv.lt/lt/sveikatos-Technologies-Assessment/Medicinal-Preparation-Medical-Emergency-and-Disease-Evaluations/. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Paraiska](vaistu_kompensavimas/Paraiska.md) | Sveikatos technologijų vertinimas (STV). Paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys ir vertinimo eigos stebėsena | `4` | `vda_prime_key` | — | `14` | Duomenų rinkinį sudaro Valstybinei vaistų kontrolės tarnybai prie Lietuvos Respublikos sveikatos apsaugos ministerijos pateiktų sveikatos technologijų... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistu_kompensavimas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_kompensavimas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkt/vaistu_kompensavimas (https://data.gov.lt/datasets/2897/)
