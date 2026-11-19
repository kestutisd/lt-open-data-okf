---
type: Dataset
title: "MOKESČIŲ MOKĖTOJŲ (JURIDINIŲ ASMENŲ) KODŲ, TIPŲ, GRUPIŲ DUOMENYS"
description: "Juridinio asmens kodas, pavadinimas, vykdomos ekonominės veiklos (pažymint kuri pagrindinė), savivaldybė, priklausymas grupei (PVM mokėtojas, specialaus apmokestinimo momentas, paramos gavėjas) data nuo kada galioja grupė, PVM mokėtojo kodas, mokesčių mokėtojo tipas..."
resource: "https://get.data.gov.lt/datasets/gov/vmi/mm_registras"
tags: [gov, vmi, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/mm_registras.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/mm_registras.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/607/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/mm_registras"
    author: "team:vda"
    last_modified: "2026-03-09T00:00:00Z"
---

# MOKESČIŲ MOKĖTOJŲ (JURIDINIŲ ASMENŲ) KODŲ, TIPŲ, GRUPIŲ DUOMENYS

- **Namespace:** `datasets/gov/vmi/mm_registras`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/mm_registras.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/mm_registras.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/mm_registras` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/607/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/mm_registras`[^dcat]
- **Portal Title (`@lt`):** Mokesčių mokėtojų registre fiksuoti juridinių asmenų duomenys[^dcat]
- **Portal Title (`@en`):** Information on taxpayers / VAT payers[^dcat]
- **Issued (`dct:issued`):** `2021-07-02`[^dcat]
- **Last Modified (`dct:modified`):** `2026-03-09`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-04-06` .. `2026-10-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Juridinio asmens kodas, pavadinimas, vykdomos ekonominės veiklos (pažymint kuri pagrindinė), savivaldybė, priklausymas grupei (PVM mokėtojas, specialaus apmokestinimo momentas, paramos gavėjas) data nuo kada galioja grupė, PVM mokėtojo kodas, mokesčių mokėtojo tipas, galiojimo data. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data specified in Paragraph 93 of the Regulations on the Register of Taxpayers and additional data, the dates of validity of these data[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MokesciuMoketojas](mm_registras/MokesciuMoketojas.md) | MOKESČIŲ MOKĖTOJŲ (JURIDINIŲ ASMENŲ) KODŲ, TIPŲ, GRUPIŲ DUOMENYS | `4` | `id` | — | `37` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/mm_registras.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/mm_registras.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/mm_registras (https://data.gov.lt/datasets/607/)
