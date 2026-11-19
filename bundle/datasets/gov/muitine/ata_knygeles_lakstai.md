---
type: Dataset
title: "ATA knygelės lakštai"
description: "Informacija apie muitinės postuose registruojamus ATA knygelių lakštus"
resource: "https://get.data.gov.lt/datasets/gov/muitine/ata_knygeles_lakstai"
tags: [gov, muitine, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/ata_knygeles_lakstai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/muitine/ata_knygeles_lakstai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2817/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/ata_knygeles_lakstai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ATA knygelės lakštai

Informacija apie muitinės postuose registruojamus ATA knygelių lakštus[^manifest]

- **Namespace:** `datasets/gov/muitine/ata_knygeles_lakstai`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/ata_knygeles_lakstai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/ata_knygeles_lakstai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/ata_knygeles_lakstai` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2817/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/muitine/ata_knygeles_lakstai`[^dcat]
- **Portal Title (`@lt`):** ATA knygelės panaudojimo Lietuvos Respublikos muitinėje atvejai[^dcat]
- **Portal Title (`@en`):** ATA Carnet Uses at Lithuanian Customs Posts[^dcat]
- **Issued (`dct:issued`):** `2024-10-03`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-10-03` .. `2026-09-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

„Duomenų rinkinį sudaro ATA knygelių informacija apie eksporto, importo, reeksporto, reimporto ir tranzito šakneles atitinkančius atplėšiamuosius lakštus, kurie įforminami muitinės postuose. ATA knygelė (ATA Carnet) – tarptautinis unifikuotas muitinės dokumentas, suteikiantis teisę neapmokestinant importo muitais ir mokesčiais laikinai įvežti prekes (pvz.: parodų ir mugių eksponatus, prekių pavyzdžius ar profesinę įrangą), atstojantis muitinės deklaraciją ir liudijantis, kad su juo gabenamoms prekėms taikoma tarptautinė garantija, o pažeidus nustatytą ATA procedūros atlikimo tvarką, bus sumokėti už prekes nustatyti importo muitai ir mokesčiai. Įrašai sistemoje registruojami nuo 2018 m. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

'The dataset shall consist of ATA carnet information on release vouchers conforming to the export, import, re-export, re-import and transit roots, which shall be recorded at customs posts. ATA Carnet is an international unified customs document granting the right to temporarily import goods (e.g. exhibitions, exhibits of fairs, samples of goods or professional equipment) free of import duties and taxes, representing the customs declaration and certifying that goods carried with it are covered by an international guarantee and that import duties and taxes imposed on goods will be paid in the event of breach of the established ATA procedure. Entries have been registered in the system since 2018. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Lakstas](ata_knygeles_lakstai/Lakstas.md) | ATA knygelės lakštai | `4` | `laksto_id` | — | `10` | Informacija apie muitinės postuose registruojamus ATA knygelių lakštus |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/ata_knygeles_lakstai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/ata_knygeles_lakstai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/ata_knygeles_lakstai (https://data.gov.lt/datasets/2817/)
