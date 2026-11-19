---
type: Dataset
title: "Valstybės tarnautojų registras, Valstybės tarnybos valdymo informacinė sistema"
description: "Šių informacinių sistemų tikslas – vykdyti žmogiškųjų išteklių valdymo viešajame administravime, valstybės tarnybos valdymo sprendimų planavimo, Valstybės tarnybos įstatymo ir su juo susijusių teisės aktų įgyvendinimo kontrolės procedūras."
resource: "https://get.data.gov.lt/datasets/gov/ird/vataras_vatis"
tags: [gov, ird, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ird/vataras_vatis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1240/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/vataras_vatis"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Valstybės tarnautojų registras, Valstybės tarnybos valdymo informacinė sistema

Šių informacinių sistemų tikslas – vykdyti žmogiškųjų išteklių valdymo viešajame administravime, valstybės tarnybos valdymo sprendimų planavimo, Valstybės tarnybos įstatymo ir su juo susijusių teisės aktų įgyvendinimo kontrolės procedūras. Šios esybės (VATARAS ir VATIS) praktikoje yra laikomi viena sistema.[^manifest]

- **Namespace:** `datasets/gov/ird/vataras_vatis`[^manifest]
- **Manifest CSV:** [datasets/gov/ird/vataras_vatis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/vataras_vatis` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1240/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ird/vataras_vatis`[^dcat]
- **Portal Title (`@lt`):** Nestatutinių valstybės tarnautojų pareigybių statistika[^dcat]
- **Portal Title (`@en`):** Details of the positions specified in Article 53 of the Law on Civil Service[^dcat]
- **Issued (`dct:issued`):** `2023-10-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-19`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2023-06-28` .. `2024-11-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Aktuali nestatutinių valstybės tarnautojų pareigybių statistika pagal Valstybės ir savivaldybių institucijas bei įstaigas. Pareigybių statistika skaičiuojama kaip įsteigtų pareigybių suma (sumuojant etatus, nes pareigybė gali sudaryti ir ne pilną etatą). Pareigybės - tai įstaigos turimos ar suplanuotos, bet nebūtinai užpildytos įvairių tipų darbo pozicijos; įsteigtų pareigybių skaičius gali skirtis nuo užimtų pareigybių skaičiaus ar tarnautojų skaičiaus. Nestatutiniai valstybės tarnautojai - tai, pvz., įstaigų vadovai, patarėjai, padėjėjai, specialistai; dažniausiai tai nėra visi įstaigoje dirbantys darbuotojai. Duomenų šaltinis - VATIS ir VATARAS. Rodomos tik šiuo metu egzistuojančios įstaigos, turinčios bent vieną tokio tipo pareigybę. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Details of the positions specified in Article 53 of the Law on Civil Service[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [DarboSkelbimas](vataras_vatis/DarboSkelbimas.md) | Aktualūs darbo skelbimai viešajame sektoriuje | `4` | `id` | — | `16` | Valstybės tarnybos portale viešinami konkursai bei atrankos į valstybės ir savivaldybių institucijų bei įstaigų laisvas darbo pozicijas. |
| [PareigybesStatistika](vataras_vatis/PareigybesStatistika.md) | Nestatutinių valstybės tarnautojų pareigybių statistika | `3` | `jar_kodas` | — | `6` | Aktuali nestatutinių valstybės tarnautojų pareigybių statistika pagal Valstybės ir savivaldybių institucijas bei įstaigas. |
| [ValstybineIstaiga](vataras_vatis/ValstybineIstaiga.md) | Valstybės ir savivaldybių institucijos bei įstaigos, jų pavaldumas | `4` | `id` | — | `11` | Aktualus ir išsamus valstybės ir savivaldybių institucijų bei įstaigų sąrašas, šių įstaigų pavaldumas viena kitai. |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/vataras_vatis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/vataras_vatis (https://data.gov.lt/datasets/1240/)
