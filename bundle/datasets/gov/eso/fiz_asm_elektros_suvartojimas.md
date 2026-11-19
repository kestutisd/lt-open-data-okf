---
type: Dataset
title: "Fizinių asmenų elektros energijos suvartojimo duomenys"
description: "Lentelėje pateiktas Energijos skirstymo operatoriaus (ESO) fizinių asmenų elektros energijos suvartojimo duomenų rinkinys."
resource: "https://get.data.gov.lt/datasets/gov/eso/fiz_asm_elektros_suvartojimas"
tags: [gov, eso, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/fiz_asm_elektros_suvartojimas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/eso/fiz_asm_elektros_suvartojimas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2740/"
    title: "data.gov.lt DCAT-AP — datasets/gov/eso/fiz_asm_elektros_suvartojimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Fizinių asmenų elektros energijos suvartojimo duomenys

- **Namespace:** `datasets/gov/eso/fiz_asm_elektros_suvartojimas`[^manifest]
- **Manifest CSV:** [datasets/gov/eso/fiz_asm_elektros_suvartojimas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/fiz_asm_elektros_suvartojimas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/eso/fiz_asm_elektros_suvartojimas` (`deployed`)[^manifest]
- **Provider:** `eso` — Energijos skirstymo operatorius *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2740/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/eso/fiz_asm_elektros_suvartojimas`[^dcat]
- **Portal Title (`@lt`):** Fizinių asmenų elektros energijos suvartojimo duomenys[^dcat]
- **Portal Title (`@en`):** Electricity consumption data of natural persons[^dcat]
- **Issued (`dct:issued`):** `2024-10-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-04-23` .. `2025-05-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateiktas Energijos skirstymo operatoriaus (ESO) fizinių asmenų elektros energijos suvartojimo duomenų rinkinys. Rinkinys sudarytas Valstybės duomenų agentūros. Adresai pateikiami standartinėmis 1 kilometro dydžio stačiakampėmis gardelėmis Lietuvos koordinačių sistemoje (LKS-94). Gardelės kodu, pagal kurį galima apjungti šio rinkinio duomenis su gardelių duomenimis. Elektros suvartojimo duomenys pateikiami mėnesio tikslumu. Kliento kodas, objekto kodas, telefono numeris ir el. pašto adresai yra negrįžtamai užšifruoti. Elektros suvartojimas gali turėti neigiamą reikšmę, kai atvykęs inžinierius užfiksuoja mažesnę reikšmę, nei paskutinė deklaruota. Realus suvartotas elektros kiekis gali skirtis nuo pateikiamų duomenų tokiu atveju, kai vartotojas neteisingai deklaruoja suvartotą elektros kiekį arba turi įsirengęs saulės elektrinę savo namų ūkyje, kuriame vartoja elektrą. Duomenų laiko aprėptis – nuo 2019 m. sausio 1d. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt. Pastaba. Šis duomenų rinkinys yra didelės apimties, todėl jo atsisiuntimas gali užtrukti ilgiau nei įprasta. Prašome atsižvelgti į tai planuojant laiką ir atsisiuntimo galimybes.[^dcat]

### Portal Description (`@en`)

The table provides electricity consumption data for natural persons of the Energy Distribution Operator (ESO). The set is compiled by the State Data Agency. Addresses are provided in rectangular stalls of 1 kilometre size in the Lithuanian coordinate system (LKS-94). Electricity consumption data shall be provided with the accuracy of the month. Customer code, object code, phone number, and e-mail addresses are encrypted. The actual amount of electricity consumed may differ from the data provided in case the consumer incorrectly declares the amount of electricity consumed or has installed a solar power plant. Data time coverage: from 1 January 2019. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [FizAsmElektraSuvartojimas](fiz_asm_elektros_suvartojimas/FizAsmElektraSuvartojimas.md) | Fizinių asmenų elektros energijos suvartojimo duomenys | `4` | `iraso_id` | — | `26` | Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) fizinių asmenų elektros suvartojimo duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/eso/fiz_asm_elektros_suvartojimas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/fiz_asm_elektros_suvartojimas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/eso/fiz_asm_elektros_suvartojimas (https://data.gov.lt/datasets/2740/)
