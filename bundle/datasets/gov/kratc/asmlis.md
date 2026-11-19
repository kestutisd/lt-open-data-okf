---
type: Dataset
title: "Atliekų priėmimas / perdavimas Klaipėdos regione"
description: "Klaipėdos regiono atliekų tvarkymo centro naudojama Atliekų surinkimo, monitoringo ir logistikos informacinė sistema (ASMLIS) kaupia gabenamų atliekų duomenis."
resource: "https://get.data.gov.lt/datasets/gov/kratc/asmlis"
tags: [gov, kratc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kratc/asmlis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kratc/asmlis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2865/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kratc/asmlis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Atliekų priėmimas / perdavimas Klaipėdos regione

- **Namespace:** `datasets/gov/kratc/asmlis`[^manifest]
- **Manifest CSV:** [datasets/gov/kratc/asmlis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kratc/asmlis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kratc/asmlis` (`deployed`)[^manifest]
- **Provider:** `kratc` — UAB Klaipėdos regiono atliekų tvarkymo centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2865/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kratc/asmlis`[^dcat]
- **Portal Title (`@lt`):** Atliekų priėmimas / perdavimas Klaipėdos regione[^dcat]
- **Portal Title (`@en`):** Acceptance/transfer of waste in Klaipėda region[^dcat]
- **Issued (`dct:issued`):** `2024-11-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-11-21` .. `2026-10-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Klaipėdos regiono atliekų tvarkymo centro naudojama Atliekų surinkimo, monitoringo ir logistikos informacinė sistema (ASMLIS) kaupia gabenamų atliekų duomenis. Duomenys kaupiami nuo 2023 m., pilna apimtimi kaupiami nuo 2024 m. sausio 1 d., ir atnaujinami iki šiol. Duomenų rinkinys sudarytas iš atliekų gabenimo datos ir laiko, atliekų svorio, atliekų gabenimo kliento sistemoje identifikatoriaus, kliento pseudonimizuoto vardo su pavarde arba pavadinimo, kliento tipo, gabenamų atliekų kodo, apibūdinimo, priėmimo vietos, kurioje svertos atliekos, pavadinimo, adreso ir atliekų tvarkymo veiklos. Vienas įrašas atitinka vieną atliekų gabenimo įvykį. Klientų nurodyti kaip „galimai juridiniai“, kadangi jų asmenų kodai neatitinka JAR kodo taisyklių, tačiau pavadinimai sufleruoja, jog tai juridiniai asmenys. Duomenų teikėjas – UAB Klaipėdos regiono atliekų tvarkymo centras. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Waste collection used by Klaipeda Region Waste Management Centre, monitoring and Logistics Information System (ASMLIS) accumulates the transported waste data. Data shall be collected from 2023 and updated to so far. The data set consists of the date and time of shipment of the waste, the identification of the weight of waste, the transport of waste in the customer's system, the client's pseudonymised name, surname or name, customer type, the location of the waste code, description, acceptance where the levers are carried waste, name, address and waste management activities. Single Entry corresponds to one waste shipment event. Indicate Customers as' Perhaps legal ', whereas their personal codes do not comply with the rules of the Jaris Code, however, the names suggest that they are legal entities. Data provider - UAB Klaipėda Region Waste Management Centre. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Gabenimas](asmlis/Gabenimas.md) | Atliekų priėmimas / perdavimas Klaipėdos regione | `4` | `vda_prime_key` | — | `11` | Klaipėdos regiono atliekų tvarkymo centro naudojama Atliekų surinkimo, monitoringo ir logistikos informacinė sistema (ASMLIS) kaupia gabenamų atliekų duomenis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kratc/asmlis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kratc/asmlis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kratc/asmlis (https://data.gov.lt/datasets/2865/)
