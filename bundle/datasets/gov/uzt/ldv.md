---
type: Dataset
title: "Užimtumo Tarnybos skelbiamos laisvos darbo vietos"
description: "Pateikiami Užimtumo tarnybos duomenys apie laisvas darbo vietas Lietuvoje."
resource: "https://get.data.gov.lt/datasets/gov/uzt/ldv"
tags: [gov, uzt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/uzt/ldv.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/uzt/ldv.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2894/"
    title: "data.gov.lt DCAT-AP — datasets/gov/uzt/ldv"
    author: "team:vda"
    last_modified: "2026-05-06T00:00:00Z"
---

# Užimtumo Tarnybos skelbiamos laisvos darbo vietos

Pateikiami Užimtumo tarnybos duomenys apie laisvas darbo vietas Lietuvoje. nuo 1990m. iki šių dienų. Lentelės objektas - laisva darbo vieta. Pateikiami išsamūs duomenys apie laisvą darbo vietą, darbdavį, darbo užmokestį, kandidatui keliamus reikalavimus ir tikslines gyventojų grupes, kurioms taikomas darbo skelbimas. Rinkinys apima ne tik juridinių, bet ir kitų teisinės veiklos formą turinčių subjektų (pvz. asmenys su verslo liudijimais) skelbiamas laisvas darbo vietas. Naudotojų patogumui išskiriamas požymis, ar darbo vieta yra laisva einamajai dienai.[^manifest]

- **Namespace:** `datasets/gov/uzt/ldv`[^manifest]
- **Manifest CSV:** [datasets/gov/uzt/ldv.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/uzt/ldv.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/uzt/ldv` (`deployed`)[^manifest]
- **Provider:** `uzt` — Užimtumo Tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2894/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/uzt/ldv`[^dcat]
- **Portal Title (`@lt`):** Užimtumo Tarnybos skelbiamos laisvos darbo vietos[^dcat]
- **Portal Title (`@en`):** Vacancies published by the Employment Office[^dcat]
- **Issued (`dct:issued`):** `2024-12-11`[^dcat]
- **Last Modified (`dct:modified`):** `2026-05-06`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-04-03` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiami Užimtumo tarnybos duomenys apie laisvas darbo vietas Lietuvoje. nuo 1990m. iki šių dienų. Lentelės objektas - laisva darbo vieta. Pateikiami išsamūs duomenys apie laisvą darbo vietą, darbdavį ir kandidatui keliamus reikalavimus. Rinkinys apima ne tik juridinių, bet ir kitų teisinės veiklos formą turinčių subjektų (pvz. asmenys su verslo liudijimais) skelbiamas laisvas darbo vietas. Naudotojų patogumui išskiriamas požymis, ar darbo vieta yra laisva einamajai dienai. 2026-02-10: Į rinkinį įtraukti nauji laukai apie darbo užmokestį, darbo skelbimo statusą ir darbdavio kontaktiniai duomenys. Panaikinti sisteminiai kodų laukai. 2026-04-24: Rinkinys papildytas naujais laukais iš Tarptautinio standartinio profesijų klasifikatoriaus (ISCO-08) ir požymiais apie tikslines grupes, kurioms skirtas darbo skelbimas (moksleiviai, nepilnamečiai, studentai, kariai, ukrainiečiai (karo pabėgėliai) ir asmenys, turintys negalią). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on vacancies in Lithuania shall be provided by the Employment Service. From 1990 to the present day. The object of the table is a vacancy. Details of the vacancy, employer and candidate requirements shall be provided. The package covers vacancies published not only by legal entities but also by entities with a form of legal activity (e.g. persons with business attestations). For the convenience of users, an indication is given as to whether the workplace is vacant for the current day. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Vieta](ldv/Vieta.md) | Pateikiami Užimtumo tarnybos duomenys apie laisvas darbo vietas Lietuvoje. nuo 1990m. iki šių dienų. Lentelės objektas - laisva darbo vieta. Pateikiami išsamūs duomenys apie laisvą darbo vietą, darbdavį ir kandidatui keliamus reikalavimus. Rinkinys apima ne tik juridinių, bet ir kitų teisinės veiklos formą turinčių subjektų (pvz. asmenys su verslo liudijimais) skelbiamas laisvas darbo vietas. Naudotojų patogumui išskiriamas požymis, ar darbo vieta yra laisva einamajai dienai. | `4` | `darbo_vietos_id` | — | `53` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/uzt/ldv.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/uzt/ldv.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/uzt/ldv (https://data.gov.lt/datasets/2894/)
