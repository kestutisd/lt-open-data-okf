---
type: Dataset
title: "Vilniaus miesto viešojo transporto maršrutų keleivių srautų duomenys"
description: "Vilniaus miesto viešojo transporto keleivių skaičiavimo sistemos DILAX duomenys"
resource: "https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai"
tags: [gov, sp, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3901/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sp/keleiviu_srautai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vilniaus miesto viešojo transporto maršrutų keleivių srautų duomenys

Vilniaus miesto viešojo transporto keleivių skaičiavimo sistemos DILAX duomenys[^manifest]

- **Namespace:** `datasets/gov/sp/keleiviu_srautai`[^manifest]
- **Manifest CSV:** [datasets/gov/sp/keleiviu_srautai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai` (`deployed`)[^manifest]
- **Provider:** `sp` — Vilniaus miesto SĮ „Susisiekimo paslaugos“ *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3901/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Vilniaus miesto viešojo transporto maršrutų keleivių srautų duomenys[^dcat]
- **Portal Title (`@en`):** Traffic data for public transport routes of Vilnius City[^dcat]
- **Issued (`dct:issued`):** `2025-12-17`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-10-09` .. `2026-01-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Vilniaus miesto viešojo transporto keleivių srautų maršrutų atkarpose ir stotelėse duomenys, renkami naudojant DILAX keleivių srautų skaičiavimo sistemą. Įlipančiųjų ir išlipančiųjų keleivių skaičius fiksuojamas jutikliais, įmontuotais virš viešojo transporto priemonės durų. Rinkinį sudaro trys lentelės. Pirmojoje lentelėje „Kelionės“ pateikiama bendra informacija apie reisą – maršruto grafiko pavadinimas bei pradžia ir pabaiga, o lentelėje „Transporto priemonės“ – tik reiso metu naudotos keleivių vežimo priemonės. Šios lentelės jungiamos pagal identifikatorių „tp_id“. Lentelėje „Stotelės“ pateikiamas detalus keleivių skaičius kiekvienoje reiso stotelėjeir stotelių koordinatės WKT formatu. Lentelės „Kelionės“ ir „Stotelės“ jungiamos pagal identifikatorių „reiso_id”. Duomenyse gali būti neatitikimų dėl sistemos trikdžių, jutiklių gedimų, taip pat ne visos transporto priemonės turi šiuos jutiklius. Pavyzdžiui, dėl sistemos veiklos sutrikimo, nuo 2022-06-25 iki 2023-08-26 duomenų nėra. Dažniausiai pasitaikančias klaidas galima išfiltruoti: 1. Pašalinami duomenys iki 5 val. ryto (išskyrus naktinius maršrutus); 2.Transporto priemonė maršrute turi turėti daugiau nei 3 skirtingus „reiso_id“ (t. y. atlikti daugiau nei tris skirtingas keliones); 3. Pašalinamos kelionės, į kuriose per dieną įlipo mažiau nei 100 keleivių. Stulpeliuose „ilipusiu_sk_perskaiciuotas“ ir „islipusiu_sk_perskaiciuotas“ pateikiamas pagal DILAX sistemos integruotą algoritmą perskaičiuotas įlipusių ir išlipusių keleivių skaičius, suapvalintas iki artimiausio sveiko skaičiaus. Jutiklių užfiksuotas įlipusių ir išlipusių keleivių skaičius pateikiamas stulpeliuose „ilipusiu_sk“ ir „islipusiu_sk“. Duomenys pateikiami nuo 2019-11-01. Informacija rinkinyje atnaujinama kas mėnesį. Duomenų teikėjas – SĮ „Susisiekimo paslaugos“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes data collected using DILAX's passenger traffic calculation system on sections and stops of the public transport routes of Vilnius City. The number of passengers entering and leaving shall be recorded by sensors mounted above the door of the public vehicle. The set consists of four tables. The first table “Travel” provides general information on the voyage — the name and start and end of the itinerary schedule, and in the table “Vehicles” — the means of passenger transport used during the voyage. These tables are combined by the identifier “tp_id”. The “stops” table shows the detailed number of passengers at each stop and, in the “Coordinates” table, the station coordinates in THE WKT format. These tables are combined by the identifier “koord_id”. The Travel and Stops tables are combined by the reiso_id identifier. The data may contain discrepancies due to system failures, sensor failures, and not all vehicles have these sensors. For example, due to system malfunction, data are not available from 2022-06-25 to 2023-08-26. The most common errors can be filtered out: 1. Remove data by 5 a.m. (excluding night routes); 2. The vehicle must have more than 3 different “reiso_id” on the route (i.e. more than three different journeys); 3. Journeys with less than 100 passengers boarded a day are removed. The columns “ilipusiu_sk_read” and “islipsu_sk_read” show the number of passengers boarded and disembarked in accordance with THE integrated algorithm of the DILAX system, rounded up to the nearest healthy number. The number of passengers boarded and disembarked by sensors is reported in the “ilippusiu_sk” and “islipu _sk” columns. Data shall be provided from 01-11-2019. The information in the collection is updated monthly. “Data provider” means THIS “Communication services”. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kelione](keleiviu_srautai/Kelione.md) | — | `4` | `reiso_id` | — | `10` | Lentelėje pateikiama bendra informacija apie reisą – maršruto grafiko pavadinimas bei pradžia ir pabaiga |
| [Stotele](keleiviu_srautai/Stotele.md) | — | `4` | `keliones_stoteles_id` | — | `20` | Lentelėje pateikiamas detalus keleivių skaičius kiekvienoje reiso stotelėje |
| [TransportoPriemone](keleiviu_srautai/TransportoPriemone.md) | — | `4` | `tp_id` | — | `6` | Lentelėje pateikiamos, reiso metu naudotos, keleivių vežimo priemonės |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sp/keleiviu_srautai (https://data.gov.lt/datasets/3901/)
