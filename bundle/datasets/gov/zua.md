---
type: Dataset
title: "Žemės ūkio agentūra prie Lietuvos Respublikos žemės ūkio ministerijos"
description: "Duomenų rinkinyje pateikiama informacija apie fizinių ir juridinių asmenų pateiktas paraiškas bei išduotas licencijas, susijusias su žemės ūkio produktų importu ir eksportu."
resource: "https://get.data.gov.lt/datasets/gov/zua"
tags: [gov, zua, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zua/licenzijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/zua/licenzijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3919/"
    title: "data.gov.lt DCAT-AP — datasets/gov/zua"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Žemės ūkio agentūra prie Lietuvos Respublikos žemės ūkio ministerijos

- **Namespace:** `datasets/gov/zua`[^manifest]
- **Manifest CSV:** [datasets/gov/zua/licenzijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zua/licenzijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/zua` (`deployed`)[^manifest]
- **Provider:** `zua` — Žemės ūkio agentūra prie Lietuvos Respublikos žemės ūkio ministerijos *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3919/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/zua`[^dcat]
- **Portal Title (`@lt`):** Importo ir eksporto licencijų, kvotų ir kompensacijų paraiškos[^dcat]
- **Portal Title (`@en`):** Applications for import and export licences, quotas and compensation[^dcat]
- **Issued (`dct:issued`):** `2025-10-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-01` .. `2026-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie fizinių ir juridinių asmenų pateiktas paraiškas bei išduotas licencijas, susijusias su žemės ūkio produktų importu ir eksportu. Duomenys apima paraiškų identifikatorius, pateikimo ir patvirtinimo datas, produktų aprašymus bei kiekius, eksporto ar importo tipus, garantijos sumas, įmonių pavadinimus, adresus, miestus ir geografines koordinates pagal LKS-94 sistemą. Taip pat nurodoma informacija apie taikomus teisės aktus ir reglamentus, tokius kaip Europos Komisijos reglamentai (pvz., Nr. 1342/2003, Nr. 382/2008, Nr. 174/1999), susijusius su licencijų galiojimu ar prekybos apribojimais. Duomenų rinkinį sudaro nuo 2005 metų kaupiami ir nuolat atnaujinami duomenys. Visi duomenys pateikiami laikantis teisės aktų reikalavimų dėl duomenų atvėrimo, todėl asmens identifikavimo duomenys nėra viešinami. Rinkinys suskirstytas į paraiškų įrašus, kuriuose pateikiami tiek licencijų, tiek produktų ir prekybos duomenys. Kiekvienas įrašas apima paraiškos identifikatorių, datas, produkto aprašymą, kiekius, garantijos sumą, eksporto ar importo tipą bei taikomus specifinius reglamentus. Duomenų teikėjas – Žemės ūkio agentūra prie Žemės ūkio ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The dataset shall include information on applications submitted by natural and legal persons and licences issued for the import and export of agricultural products. The data shall include the identification of applications, the dates of submission and approval, product descriptions and quantities, export or import types, guarantee amounts, business names, addresses, cities and geographical coordinates in accordance with THE LKS-94 system. Information on applicable legislation and regulations such as European Commission Regulations (e.g. No 1342/2003, No 382/2008, No 174/1999) relating to the validity of licences or trade restrictions shall also be provided. The dataset consists of data collected and kept up-to-date since 2005. All data shall be provided in accordance with the legal requirements for the opening of data and therefore personal identification data shall not be made public. The set is divided into application entries that contain both licence and product and trade data. Each entry shall include the application identifier, dates, product description, quantities, guarantee amount, type of export or import and applicable specific regulations. Data provider shall mean the Agricultural Agency under the Ministry of Agriculture of the Republic of Lithuania. Please contact atverimas@stat.gov.lt by e-mail for information. Please contact atviriduomenys@vssa.lt by e-mail for technical problems with the portal.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Licenzija](zua/Licenzija.md) | Paraiškų ir licencijų duomenys | `4` | `paraiskos_identifikatorius` | `open` | `16` | Rinkinyje pateikiama informacija apie paraiškas gauti licencijas, teikiamas Žemės ūkio agentūrai. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/zua/licenzijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zua/licenzijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/zua (https://data.gov.lt/datasets/3919/)
