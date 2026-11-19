---
type: Dataset
title: "Juridinių asmenų akcininkų, dalininkų, narių ir pajininkų skaičiai pagal tipą"
description: "Registrų centro Juridinių asmenų dalyvių informacinė sistema (JADIS) tvarko ir apdoroja juridinių asmenų dalyvių duomenis."
resource: "https://get.data.gov.lt/datasets/gov/lsd/rc/ja_akc_dal_nar_paj"
tags: [gov, lsd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2712/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/rc/ja_akc_dal_nar_paj"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Juridinių asmenų akcininkų, dalininkų, narių ir pajininkų skaičiai pagal tipą

- **Namespace:** `datasets/gov/lsd/rc/ja_akc_dal_nar_paj`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/rc/ja_akc_dal_nar_paj` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2712/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/rc/ja_akc_dal_nar_paj/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų akcininkų, dalininkų, narių ir pajininkų skaičiai pagal tipą[^dcat]
- **Portal Title (`@en`):** Number of shareholders, stakeholders, members and members of legal persons by type[^dcat]
- **Issued (`dct:issued`):** `2024-08-02`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-04-06` .. `2026-07-08`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Registrų centro Juridinių asmenų dalyvių informacinė sistema (JADIS) tvarko ir apdoroja juridinių asmenų dalyvių duomenis. Duomenys kaupiami nuo 2014 m. ir yra atnaujinami kasdien. Duomenų rinkinys apima juridinio asmens kodą ir pavadinimą, akcininkų, dalininkų, narių ir pajininkų skaičius pagal tipą. Galimi tipai yra Lietuvos arba užsienio fizinis asmuo, Lietuvos arba užsienio juridinis asmuo bei Lietuvos Respublikos savivaldybės. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Information System of Participants of Legal Entities (JADIS) of the Centre of Registers shall process and process data of participants of legal persons. Data have been collected since 2014 and are updated on a daily basis. The dataset shall include the code and name of the legal person, the number of shareholders, stakeholders, members and members by type. Possible types are a Lithuanian or foreign natural person, a Lithuanian or foreign legal person and municipalities of the Republic of Lithuania.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [JuridinisAsmuo](ja_akc_dal_nar_paj/JuridinisAsmuo.md) | Juridinių asmenų akcininkų, dalininkų, narių ir pajininkų skaičiai pagal tipą | `4` | `org_jar_kodas` | — | `22` | Registrų centro Juridinių asmenų dalyvių informacinė sistema (JADIS) tvarko ir apdoroja juridinių asmenų dalyvių duomenis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/rc/ja_akc_dal_nar_paj (https://data.gov.lt/datasets/2712/)
