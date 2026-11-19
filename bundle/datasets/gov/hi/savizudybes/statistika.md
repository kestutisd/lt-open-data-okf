---
type: Dataset
title: "Agreguoti savižudybės atvejų ir savižudybės grėsmių skaičiai"
description: "Duomenų rinkinio pagrindu yra parengta viešai prieinama „Savižudybių stebėsenos“ švieslentė: https://osp.stat.gov.lt/savizudybiu-stebesena Rinkinį sudaro: Savižudybės atvejų duomenys, remiantis HI Mirties atvejų ir jų priežasčių valstybės registru."
resource: "https://get.data.gov.lt/datasets/gov/hi/savizudybes/statistika"
tags: [gov, hi, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/savizudybes/statistika.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/hi/savizudybes/statistika.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/6010/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/savizudybes/statistika"
    author: "team:vda"
    last_modified: "2026-09-07T00:00:00Z"
---

# Agreguoti savižudybės atvejų ir savižudybės grėsmių skaičiai

- **Namespace:** `datasets/gov/hi/savizudybes/statistika`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/savizudybes/statistika.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/savizudybes/statistika.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/savizudybes/statistika` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/6010/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/hi/savizudybes/statistika/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Agreguoti savižudybės atvejų ir savižudybės grėsmių skaičiai[^dcat]
- **Portal Title (`@en`):** Agreguoti savižudybės atvejų ir savižudybės grėsmių skaičiai[^dcat]
- **Issued (`dct:issued`):** `2026-09-07`[^dcat]
- **Last Modified (`dct:modified`):** `2026-09-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-09-07` .. `2026-09-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinio pagrindu yra parengta viešai prieinama „Savižudybių stebėsenos“ švieslentė: https://osp.stat.gov.lt/savizudybiu-stebesena Rinkinį sudaro: Savižudybės atvejų duomenys, remiantis HI Mirties atvejų ir jų priežasčių valstybės registru. Atvejis – asmuo, kurio pagrindinė mirties priežastis pagal Pasaulio sveikatos organizacijos taisykles oficialiojoje statistikoje yra tyčinis susižalojimas (X60-X84 pagal TLK-10-AM sisteminį ligų sąrašą). Savižudybės grėsmės atvejų duomenys, remiantis Privalomojo sveikatos draudimo informacinės sistemos informacija (SVEIDRA). Grėsmės atvejis – tai vienas apsilankymo sveikatos priežiūros įstaigoje atvejis (kortelė), susijęs su savižudybės grėsme. Įtraukti tų asmenų įrašai, kurių stacionare gydomo asmens statistinėje kortelėje (F066/a-LK) įrašytos pagrindinės/lydinčios diagnozės (TLK-10-AM kodas) arba ambulatorinio gydymo apskaitos kortelėje (F025/a-LK) pagrindinės diagnozės (TLK-10-AM kodas) yra: ◦ tyčiniai susižalojimai X60-X84 arba ◦ tyčinis apsinuodijimas alkoholiu X65 arba ◦ mintys apie savižudybę R45.81 arba ◦ tyčinio savęs žalojimo padariniai Y87.0 ar buvęs savęs žalojimas Z91.5 Jei gydymo kortelėje yra nurodytas daugiau nei vienas aukščiau paminėtas TLK-10-AM kodas, grėsmės atvejis skaitomas kaip vienas unikaliam asmeniui. Šie skaičiai buvo agreguoti pagal įvykio metus ir kitus pjūvius. Duomenys atnaujinami kiekvieno mėnesio pirmąją dieną. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AtvejuStatistika](statistika/AtvejuStatistika.md) | Atvejų statistika | `4` | `vda_id` | — | `11` | Agreguota atvejų statistika pagal metus, gyvenamąją vietą ir demografinius bei socialinius pjūvius |
| [GresmiuStatistika](statistika/GresmiuStatistika.md) | Grėsmių statistika | `4` | `vda_id` | — | `11` | Agreguota atvejų statistika pagal metus, gyvenamąją vietą ir demografinius bei socialinius pjūvius |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/savizudybes/statistika.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/savizudybes/statistika.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/savizudybes/statistika (https://data.gov.lt/datasets/6010/)
