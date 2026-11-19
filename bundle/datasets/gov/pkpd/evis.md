---
type: Dataset
title: "Transporto priemonių rezervacijos kirsti pasienį"
description: "Pasienio kontrolės punktų direkcijos (PKPD) ir AB „Regitra“ duomenų bendras rinkinys, sudarytas Valstybės duomenų agentūros."
resource: "https://get.data.gov.lt/datasets/gov/pkpd/evis"
tags: [gov, pkpd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/evis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/pkpd/evis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2635/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pkpd/evis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Transporto priemonių rezervacijos kirsti pasienį

- **Namespace:** `datasets/gov/pkpd/evis`[^manifest]
- **Manifest CSV:** [datasets/gov/pkpd/evis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/evis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pkpd/evis` (`deployed`)[^manifest]
- **Provider:** `pkpd` — Pasienio kontrolės punktų direkcija prie Susisiekimo ministerijos *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2635/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/pkpd/evis`[^dcat]
- **Portal Title (`@lt`):** Transporto priemonių rezervacijos kirsti pasienį[^dcat]
- **Portal Title (`@en`):** Reservation of vehicles to cross the border[^dcat]
- **Issued (`dct:issued`):** `2024-04-25`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-04-25` .. `2025-10-20`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pasienio kontrolės punktų direkcijos (PKPD) ir AB „Regitra“ duomenų bendras rinkinys, sudarytas Valstybės duomenų agentūros. Duomenys kaupiami nuo 2013 m. ir atnaujinami kasdien. Duomenų rinkinyje saugomas paslaugos kirsti pasienį registracijos identifikatorius, registracijos kaina, mokestis ir kaina su mokesčiu. Taip pat yra nurodyti atvykimo į laukimo aikštelę, į pasienio kontrolės punktą laikai, punkto pavadinimas bei kaimyninė valstybė. Saugomas eilės tipas, transporto priemonės šifruotas valstybinis numeris, VIN šalis, rūšis, kategorija, ar transporto priemonė registruota Lietuvoje, šifruotas fizinio savininko arba atviras juridinio asmens kodas ir savininko pavadinimas, jei tai juridinis asmuo. Duomenų tiekėjai – Pasienio kontrolės punktų direkcija, AB „Regitra“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

A collection of data used by THE BORDER Inspection Point Directorate (PKPD) and the SE Regitra, compiled by the State Data Agency. The data has been collected since 2013 and updated on a daily basis. The data set stores the registration identifier for cross-border services, the registration price, the fee and the fee price. The time of arrival at the waiting area, the border crossing point, the name of the point and the neighbouring state are also indicated. The type of queue, the encrypted state number of the vehicle, the country of the VIN, the type, category, whether the vehicle is registered in Lithuania, the encrypted code of the natural owner or an open legal person and the name of the owner, if it is a legal person, shall be stored.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SienosKirtimoRezervacija](evis/SienosKirtimoRezervacija.md) | Transporto priemonių rezervacijos kirsti pasienį | `4` | `reg_id` | — | `17` | Pasienio kontrolės punktų direkcijos (PKPD) ir VĮ „Regitra“ duomenų bendras rinkinys, sudarytas Valstybės duomenų agentūros. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/pkpd/evis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/evis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pkpd/evis (https://data.gov.lt/datasets/2635/)
