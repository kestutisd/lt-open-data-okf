---
type: Dataset
title: "Gyventojų pajamų mokesčio deklaracijų duomenys"
description: "GPM311 – metinė gyventojų pajamų mokesčio deklaracijos forma, kurioje kaupiami duomenys apie gyventojų metines pajamas, pritaikytus mokesčių atskaitymus ir mokėtiną arba grąžintiną gyventojų pajamų mokestį (GPM)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/gpm_deklaracijos"
tags: [gov, lsd, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gpm_deklaracijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/gpm_deklaracijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2924/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/gpm_deklaracijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Gyventojų pajamų mokesčio deklaracijų duomenys

- **Namespace:** `datasets/gov/lsd/gpm_deklaracijos`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/gpm_deklaracijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gpm_deklaracijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/gpm_deklaracijos` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2924/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/gpm_deklaracijos`[^dcat]
- **Portal Title (`@lt`):** Gyventojų pajamų mokesčio deklaracijų duomenys[^dcat]
- **Portal Title (`@en`):** Personal income tax returns data[^dcat]
- **Issued (`dct:issued`):** `2025-02-10`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2025-01-29` .. `2025-02-08`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

GPM311 – metinė gyventojų pajamų mokesčio deklaracijos forma, kurioje kaupiami duomenys apie gyventojų metines pajamas, pritaikytus mokesčių atskaitymus ir mokėtiną arba grąžintiną gyventojų pajamų mokestį (GPM). Deklaracija pildoma pasibaigus kalendoriniams metams. Deklaraciją turi pateikti: •	Gyventojai, vykdantys individualią veiklą; •	Asmenys, kurie nori susigrąžinti GPM permoką; •	Asmenys, gavę pajamų iš užsienio; •	Asmenys, norintys pasinaudoti mokesčių lengvatomis; •	Asmenys, kurie privalo deklaruoti visas metines pajamas. Pateikimo terminas paprastai yra iki gegužės 2 d. Norint pateikti deklaraciją, reikia prisijungti prie VMI Elektroninio deklaravimo sistemos (EDS) per elektroninę bankininkystę ar kitą autorizavimo priemonę. Deklaracijoje nurodomi visi per metus gauti pajamų šaltiniai. Įtraukiamos visos apmokestinamos pajamos ir taikomos mokesčių lengvatos. Vienas gyventojas deklaracijoje gali turėti įrašų apie pajamas iš kelių šaltinių, įskaitant darbo užmokestį, dividendus, finansinių priemonių pardavimą ir kitas pajamų rūšis. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

GPM311 is an annual form of personal income tax return which collects data on the annual income of the population, adjusted tax deductions and personal income tax payable or repayable (GPM). The declaration shall be completed after the end of the calendar year. The declaration must be made by: • Individuals carrying out individual activities; • Persons who wish to recover GPM overpayment; • Individuals who have received foreign income; • Persons wishing to benefit from tax advantages; • Persons who are required to declare their full annual income. The deadline for submission is usually up to 2 May. In order to submit a declaration, it is necessary to join the BMI Electronic Declaration System (EDS) through electronic banking or any other authorisation measure. The declaration shall state all sources of income received during the year. All taxable income and tax benefits are included. One resident may record revenue from several sources in the declaration, including wages, dividends, sales of financial instruments and other types of income. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Deklaracija](gpm_deklaracijos/Deklaracija.md) | Gyventojų pajamų mokesčio deklaracijos | `4` | `id` | — | `19` | Gyventojų pajamų mokesčio deklaracijos |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/gpm_deklaracijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gpm_deklaracijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/gpm_deklaracijos (https://data.gov.lt/datasets/2924/)
