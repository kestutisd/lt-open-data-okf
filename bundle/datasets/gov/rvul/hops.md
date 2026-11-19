---
type: Dataset
title: "Pacientams atliktų operacijų duomenys"
description: "Respublikinės Vilniaus universitetinės ligoninės Operacijų planavimo ir valdymo sistemoje (HOPS) kaupiami pacientams atliktų operacijų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/rvul/hops"
tags: [gov, rvul, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3865/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rvul/hops"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pacientams atliktų operacijų duomenys

Respublikinės Vilniaus universitetinės ligoninės Operacijų planavimo ir valdymo sistemoje (HOPS) kaupiami pacientams atliktų operacijų duomenys. Rinkinyje pateikiami nuo 2023 metų rugpjūčio mėnesio sukaupti ir iki šiol atnaujinami duomenys. Bendras duomenų rinkinys sudarytas iš penkių lentelių: „Operacijos“, „Medikai“, „Anestezijos“, „Vaidmenys“ ir „Pacientai“. Rinkinyje visi laikai nurodyti Centrinės Europos (CET) laiko zona. Duomenų teikėjai – VšĮ Respublikinė Vilniaus universitetinė ligoninė ir Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba prie Sveikatos Apsaugos Ministerijos (VASPVT). Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt[^manifest]

- **Namespace:** `datasets/gov/rvul/hops`[^manifest]
- **Manifest CSV:** [datasets/gov/rvul/hops.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rvul/hops` (`deployed`)[^manifest]
- **Provider:** `rvul` — VšĮ Respublikinė Vilniaus universitetinė ligoninė *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3865/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rvul/hops`[^dcat]
- **Portal Title (`@lt`):** Pacientams atliktų operacijų duomenys[^dcat]
- **Portal Title (`@en`):** Data on operations performed by patients[^dcat]
- **Issued (`dct:issued`):** `2025-07-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-07-09` .. `2026-10-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Respublikinės Vilniaus universitetinės ligoninės Operacijų planavimo ir valdymo sistemoje (HOPS) kaupiami pacientams atliktų operacijų duomenys. Rinkinyje pateikiami nuo 2023 metų rugpjūčio mėnesio sukaupti ir iki šiol atnaujinami duomenys. Bendras duomenų rinkinys sudarytas iš penkių lentelių: „Operacijos“, „Medikai“, „Anestezijos“, „Vaidmenys“ ir „Pacientai“. Rinkinyje visi laikai nurodyti Centrinės Europos (CET) laiko zona. Duomenų teikėjai – VšĮ Respublikinė Vilniaus universitetinė ligoninė ir Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba prie Sveikatos Apsaugos Ministerijos (VASPVT). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Operational Planning and Management System (HOPS) of the Republican Vilnius University Hospital collects data on the operations performed on patients. The set includes data that has been accumulated since August 2023 and is still up-to-date. The overall dataset consists of five tables: “Operations,” “Medics,” “Anesthesia,” “Firearms,” and “Patients.” The set specifies all times in the Central Europe (CET) time zone. Data providers shall mean the Public Enterprise Republican Vilnius University Hospital and the State Health Care Accreditation Service under the Ministry of Health Care (VASPVT). Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Operacija](hops/Operacija.md) | Operacijos | `4` | `vda_prime_key` | — | `12` | Lentelė „Operacijos“. Lentelę sudaro: sudarančios procedūros, paciento asmens kodas, operacijos rūšis, diagnozės, pagal kurią operuojama, TLK kodas ir... |
| [Medikas](hops/Medikas.md) | Medikai | `4` | `vda_prime_key` | — | `16` | Lentelė „Medikai“. Lentelę sudaro: mediko identifikatorius, asmens kodas, jo validacijos stulpelis, gimimo metai iš tinkamo asmens kodo bei VASPVT Sveikatos... |
| [Pacientas](hops/Pacientas.md) | Pacientai | `4` | `vda_prime_key` | — | `6` | Lentelė „Pacientai“. Lentelę sudaro: paciento asmens kodas bei jo validacijos požymis, paciento gimimo metai iš atskiro gimimo datos stulpelio ir gimimo... |
| [Anestezija](hops/Anestezija.md) | Anestezijos | `4` | `vda_prime_key` | — | `8` | Lentelė „Anestezijos“. Lentelę sudaro: operacijos, jos procedūros bei anestezijos identifikatoriai, anestezijos pavadinimas, rūšis, paskyrimo pradžios ir... |
| [Vaidmuo](hops/Vaidmuo.md) | Vaidmenys | `4` | `vda_prime_key` | — | `5` | Lentelė „Vaidmenys“. Lentelę sudaro operacijos, procedūros bei mediko identifikatoriai ir vaidmuo. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rvul/hops (https://data.gov.lt/datasets/3865/)
