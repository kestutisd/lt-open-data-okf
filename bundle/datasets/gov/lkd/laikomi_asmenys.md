---
type: Dataset
title: "Kalinimo įstaigose laikomų asmenų statistika"
description: "Lietuvos kalėjimų departamentas (LKD) kaupia kalinimo įstaigose laikomų asmenų statistinius duomenis nuo 2021 m., atnaujinamus kas mėnesį, gaunamus iš kalinimo įstaigų."
resource: "https://get.data.gov.lt/datasets/gov/lkd/laikomi_asmenys"
tags: [gov, lkd, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/laikomi_asmenys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lkd/laikomi_asmenys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2665/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lkd/laikomi_asmenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kalinimo įstaigose laikomų asmenų statistika

- **Namespace:** `datasets/gov/lkd/laikomi_asmenys`[^manifest]
- **Manifest CSV:** [datasets/gov/lkd/laikomi_asmenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/laikomi_asmenys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lkd/laikomi_asmenys` (`deployed`)[^manifest]
- **Provider:** `lkd` — Lietuvos kalėjimų tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2665/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lkd/laikomi_asmenys`[^dcat]
- **Portal Title (`@lt`):** Kalinimo įstaigose laikomų asmenų statistika[^dcat]
- **Portal Title (`@en`):** Statistics on persons in prison[^dcat]
- **Issued (`dct:issued`):** `2024-05-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-05-22` .. `2024-05-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos kalėjimų departamentas (LKD) kaupia kalinimo įstaigose laikomų asmenų statistinius duomenis nuo 2021 m., atnaujinamus kas mėnesį, gaunamus iš kalinimo įstaigų. Rinkinys apima momentinį laikotarpį, kuriam aktualūs pateikti skaičiai, kalinimo įstaigos pavadinimą, bendrą laisvės atėmimo vietose laikomų asmenų skaičių, suimtųjų skaičių, bendrą nuteisimų laisvės atėmimu skaičių, nuteistųjų atviro tipo bausme be Pusiaukelės namų skaičių, nuteistųjų pusiau atviro tipo bausmės atlikimo vietoje skaičių, nuteistųjų uždaro tipo bausmės atlikimo vietoje skaičių, nuteistųjų Pusiaukelės namuose skaičių, suėmimo vykdymo vietoje laikomų nuteistųjų skaičių, nuteistųjų arešto bausme skaičių, moterų skaičių, nepilnamečių skaičių, bendrą užsienio šalių piliečių skaičių, suimtų užsienio šalių piliečių skaičių ir nuteistų užsienio šalių piliečių skaičių. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Lithuanian Prison Department (LKD) collects statistics of persons held in prison institutions from 2021, updated every month from prison institutions. The package includes the snapshot period for which the figures are relevant, the name of the prison facility, the total number of persons held in prison, the number of arrests, the total number of prison sentences, the number of open-door sentences without Priestly House, the number of semi-open-door sentences, the number of inmates on the spot, the number of closed-door sentences, the number of detainees at the scene, the total number of convicted persons in custody, the number of foreign nationals, the number of foreign minors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LaikomuAsmenuStatistika](laikomi_asmenys/LaikomuAsmenuStatistika.md) | Kalinimo įstaigose laikomų asmenų statistika | `4` | `vda_id` | — | `17` | Lietuvos kalėjimų departamentas (LKD) kaupia kalinimo įstaigose laikomų asmenų statistinius duomenis nuo 2021 m., atnaujinamus kas menėsį, gaunamus iš... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lkd/laikomi_asmenys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/laikomi_asmenys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lkd/laikomi_asmenys (https://data.gov.lt/datasets/2665/)
