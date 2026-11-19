---
type: Dataset
title: "Viešojo sektoriaus sąskaitų administravimo bendroji informacinė sistema"
description: "Duomenų rinkinį sudaro keturios lentelės apie viešojo sektoriaus įstaigų sąskaitas nuo 2015 m. Lentelėje „Sąskaitos“ sujungti informacinių sistemų „E."
resource: "https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos"
tags: [gov, nbfc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3924/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nbfc/viesojo_sektoriaus_saskaitos"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Viešojo sektoriaus sąskaitų administravimo bendroji informacinė sistema

- **Namespace:** `datasets/gov/nbfc/viesojo_sektoriaus_saskaitos`[^manifest]
- **Manifest CSV:** [datasets/gov/nbfc/sabis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos` (`deployed`)[^manifest]
- **Provider:** `nbfc` — Nacionalinis bendrųjų funkcijų centras *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3924/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos`[^dcat]
- **Portal Title (`@lt`):** Viešojo sektoriaus sąskaitos[^dcat]
- **Portal Title (`@en`):** Public Procurement Accounts[^dcat]
- **Issued (`dct:issued`):** `2025-11-26`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-20`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-11-26` .. `2026-09-25`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinį sudaro keturios lentelės apie viešojo sektoriaus įstaigų sąskaitas nuo 2015 m. Lentelėje „Sąskaitos“ sujungti informacinių sistemų „E. Sąskaita“ ir SABIS duomenys. Iki 2024 m. rugpjūčio sąskaitos buvo įkeliamos į „E. Sąskaitos“ informacinę sistemą pagal Lietuvos arba Europos Sąjungos standartą. Nuo 2024 m. rugpjūčio mėn. sąskaitos įkeliamos į SABIS sistemą. Sąskaitos, kurių ID prasideda „LT“, yra lietuviško standarto sąskaitos, sąskaitos, kurių ID prasideda „EU“, yra europietiško standarto sąskaitos, o ID, sudarytas iš skaičių, žymi į SABIS sistemą registruojamas sąskaitas. Lentelėje „Saskaitos“ informacija agreguojama iki vienos sąskaitos, tačiau viena sąskaita gali turėti kelis PVM tarifus. Net ir tuo atveju, jei pirktos kelios prekės / paslaugos pagal Bendro viešųjų pirkimų žodyno (BVPŽ) klasifikatorių, sąskaita gali turėti tik vieną BVPŽ kodą; šis kodas privalomas nuo 2025 m. Sąskaitos pirkėjų ir tiekėjų informacija pateikiama lentelėje „Saskaitu_salys“, lentelės jungiamos pagal sąskaitos faktūros identifikatorių „sf_id“. Viešųjų pirkimų (VP) sutarčių informacija pateikiama lentelėje „Sutartys“. „E. Sąskaitos“ sistemoje įkeltų sąskaitų sutarčių informacijos nėra, todėl VP sutarčių informacija pateikiama tik nuo 2024 m. rugpjūčio mėn., suvesta į SABIS. Sąskaitų informacija su VP sutarčių informacija jungiamos pagal „sutarties_uid“. Sutarčių šalių informacija pateikiama lentelėje „Sutarciu_salys“. Sutartys ir sutarčių šalys jungiamos pagal „sutarties_id“ stulpelį. Duomenų teikėjas – SĮ „Nacionalinis bendrųjų funkcijų centras“. Duomenys atnaujinami kartą per mėnesį. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table shows procurement of public procurement contracts by the end of August 2024. In this table, the data were transferred from E. Sskaitos and submitted via THE SABAS system. The information in the table is aggregated to one account. Lithuanian and European Union accounts have been merged. “Data provider” means THIS “National Centre for General Functions”. Data is not updated. Contact the atverimas@stat.gov.lt for technical questions or possible errors. ”[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Saskaitos](viesojo_sektoriaus_saskaitos/Saskaitos.md) | Sąskaitos | `4` | — | — | `18` | Viešojo sektoriaus sąskaitų duomenys |
| [SaskaituSalys](viesojo_sektoriaus_saskaitos/SaskaituSalys.md) | Sąskaitų šalys | `4` | — | — | `11` | Viešojo sektoriaus sąskaitų šalys |
| [Sutartys](viesojo_sektoriaus_saskaitos/Sutartys.md) | Sutartys | `4` | — | — | `11` | Viešųjų pirkimų sutarčių informacija |
| [SutarciuSalys](viesojo_sektoriaus_saskaitos/SutarciuSalys.md) | Sutarčių šalys | `4` | — | — | `10` | Viešųjų pirkimų sutarčių šalys |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nbfc/viesojo_sektoriaus_saskaitos (https://data.gov.lt/datasets/3924/)
