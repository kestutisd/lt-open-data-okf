---
type: Dataset
title: "Labai mažo darbo intensyvumo namų ūkiuose gyvenantys asmenys"
description: "Statistinė metinė labai mažo darbo intensyvumo Lietuvos privačių namų ūkių informacija, kuriuose visų darbingo (18–64 metų) amžiaus asmenų (neįskaitant 18–24 metų amžiaus moksleivių ir studentų, pensininkams save priskyrusių arba bet kokią pensiją (išskyrus našlių pensiją)..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys"
tags: [gov, lsd, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2546/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Labai mažo darbo intensyvumo namų ūkiuose gyvenantys asmenys

- **Namespace:** `datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys` (`deployed`)[^manifest]
- **Provider:** `lsd` — Oficialiosios statistikos portalo rodiklių duomenų bazės rinkiniai *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `7` (7 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2546/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys`[^dcat]
- **Portal Title (`@lt`):** Labai mažo darbo intensyvumo namų ūkiuose gyvenantys asmenys[^dcat]
- **Portal Title (`@en`):** Persons living in households with very low labour intensity[^dcat]
- **Issued (`dct:issued`):** `2024-03-02`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-02-15` .. `2026-08-13`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Statistinė metinė labai mažo darbo intensyvumo Lietuvos privačių namų ūkių informacija, kuriuose visų darbingo (18–64 metų) amžiaus asmenų (neįskaitant 18–24 metų amžiaus moksleivių ir studentų, pensininkams save priskyrusių arba bet kokią pensiją (išskyrus našlių pensiją) gaunančių darbingo amžiaus asmenų bei 60–64 metų amžiaus ekonomiškai neaktyvių asmenų, gyvenančių namų ūkyje, kurio pagrindinis pajamų šaltinis yra pensijos) dirbto laiko suma neviršija 20 proc. galimo dirbti viso darbo laiko. Statistinės informacijos skelbimo periodiškumas – metinis, nuo 2021 metų. Naudojamas teritorinių statistinių vienetų klasifikatorius (NUTS). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Statistical annual information of Lithuanian private households of very low intensity of work in which the amount of working time of all working-age (18-64 years) persons (excluding pupils and students aged 18-24, self-employed pensioners or persons of working age receiving any pension (excluding widow's pension) and economically inactive persons aged 60-64 living in a household whose main source of income is pensions) does not exceed 20% of the total working time available. The frequency of publication of statistical information is annual, from 2021. A classification of territorial statistical units (NUTS) shall be used.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [S3R0470M3080357](mazo_darbo_intensyvumo_asmenys/S3R0470M3080357.md) | Labai mažo darbo intensyvumo namų ūkiuose gyvenantys asmenys (pagal amžių ir lytį) | `4` | `vda_id` | — | `11` | Lietuvos privačių namų ūkių, kuriuose visų darbingo amžiaus asmenų dirbto laiko suma neviršija 20 proc. |
| [S3R0470M3080375](mazo_darbo_intensyvumo_asmenys/S3R0470M3080375.md) | Labai mažo darbo intensyvumo namų ūkiuose gyvenantys asmenys (pagal pajamų kvantilines grupes) | `4` | `vda_id` | — | `9` | Lietuvos privačių namų ūkių, kuriuose visų darbingo amžiaus asmenų dirbto laiko suma neviršija 20 proc. |
| [S3R0470M3080376](mazo_darbo_intensyvumo_asmenys/S3R0470M3080376.md) | Labai mažo darbo intensyvumo namų ūkiuose gyvenantys asmenys (pagal amžių ir pilietybę) | `4` | `vda_id` | — | `11` | Lietuvos privačių namų ūkių, kuriuose visų darbingo amžiaus asmenų dirbto laiko suma neviršija 20 proc. |
| [S3R0470M3080377](mazo_darbo_intensyvumo_asmenys/S3R0470M3080377.md) | Labai mažo darbo intensyvumo namų ūkiuose gyvenantys asmenys (pagal amžių ir gimimo šalį) | `4` | `vda_id` | — | `11` | Lietuvos privačių namų ūkių, kuriuose visų darbingo amžiaus asmenų dirbto laiko suma neviršija 20 proc. |
| [S3R0470M3080378](mazo_darbo_intensyvumo_asmenys/S3R0470M3080378.md) | Labai mažo darbo intensyvumo namų ūkiuose gyvenantys asmenys (pagal išsilavinimą) | `4` | `vda_id` | — | `9` | Lietuvos privačių namų ūkių, kuriuose visų darbingo amžiaus asmenų dirbto laiko suma neviršija 20 proc. |
| [S3R0470M3080379](mazo_darbo_intensyvumo_asmenys/S3R0470M3080379.md) | Labai mažo darbo intensyvumo namų ūkiuose gyvenantys asmenys (pagal aktyvumo statusą) | `4` | `vda_id` | — | `9` | Lietuvos privačių namų ūkių, kuriuose visų darbingo amžiaus asmenų dirbto laiko suma neviršija 20 proc. |
| [S3R0470M3080380](mazo_darbo_intensyvumo_asmenys/S3R0470M3080380.md) | Labai mažo darbo intensyvumo namų ūkiuose gyvenantys asmenys (pagal amžių ir regioną) | `4` | `vda_id` | — | `12` | Lietuvos privačių namų ūkių, kuriuose visų darbingo amžiaus asmenų dirbto laiko suma neviršija 20 proc. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/mazo_darbo_intensyvumo_asmenys (https://data.gov.lt/datasets/2546/)
