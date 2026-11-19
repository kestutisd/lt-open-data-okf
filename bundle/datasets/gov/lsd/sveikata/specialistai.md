---
type: Dataset
title: "Sveikatos priežiūros specialistai"
description: "Pateikiamas unikalių licencijų* suminis skaičius pagal licencijos kvalifikaciją nuo 1996 m. Duomenų šaltinis – Sveikatos priežiūros ir farmacijos specialistų praktikos licencijų registras (LICREG)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/specialistai"
tags: [gov, lsd, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/specialistai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/specialistai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2896/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/specialistai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sveikatos priežiūros specialistai

- **Namespace:** `datasets/gov/lsd/sveikata/specialistai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/specialistai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/specialistai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/specialistai` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2896/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/specialistai`[^dcat]
- **Portal Title (`@lt`):** Sveikatos priežiūros specialistų licencijos[^dcat]
- **Portal Title (`@en`):** Healthcare professionals licenses[^dcat]
- **Issued (`dct:issued`):** `2024-12-11`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-12-11` .. `2026-01-10`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiamas unikalių licencijų* suminis skaičius pagal licencijos kvalifikaciją nuo 1996 m. Duomenų šaltinis – Sveikatos priežiūros ir farmacijos specialistų praktikos licencijų registras (LICREG). Metinio specialistų skaičiaus apskaičiavimo kriterijai: 1. Licencija galiojo bent 1 dieną tais metais. 2. Jeigu specialistas turi kelias skirtingas licencijas, jis priskaičiuojamas prie kiekvienos iš jų. Metinio specialistų vidutinio amžiaus apskaičiavimas: 1. Specialisto amžius nustatomas kaip skirtumas tarp specialisto gimimo metų ir ataskaitinių metų. 2. Kiekvienos kvalifikacijos specialistų vidutinis amžius apskaičiuojamas kaip visų tos kvalifikacijos specialistų amžių aritmetinis vidurkis. Duomenų nuasmeninimo priemonės: 1. Jei tam tikros kvalifikacijos specialistų metinis skaičius yra 1, jų amžius nerodomas. Teikiami duomenys nėra oficialiosios statistikos dalis. *Lietuvoje sveikatos specialisto licencija yra oficialus dokumentas, suteikiantis teisę verstis tam tikros rūšies sveikatos priežiūros praktika. Licencija patvirtina, kad specialistas atitinka nustatytus profesinės kvalifikacijos reikalavimus ir gali teisėtai teikti sveikatos priežiūros paslaugas. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^dcat]

### Portal Description (`@en`)

The total number of unique licenses* by qualification type is presented, starting from 1996. The data source is the Register of Licenses for Healthcare and Pharmacy Professionals (LICREG). Criteria for calculating the annual number of professionals: The license was valid for at least 1 day during the index year; If a specialist has multiple different licenses, they are counted under each of them. Calculation of the annual average age of professionals: A specialist's age is determined as the difference between the year of their birth and the reporting year; The average age of specialists for each qualification is calculated as the arithmetic mean of the ages of all specialists with that qualification. Data anonymization methods: If the annual number of professionals for a specific qualification is 1, the age is not displayed. The provided data is not part of official statistics. *In Lithuania, a healthcare professional’s license is an official document granting the right to practice a specific type of healthcare . The license confirms that the professional meets the established qualification requirements and is authorized to provide healthcare services legally[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LicregSpecialistas](specialistai/LicregSpecialistas.md) | Sveikatos priežiūros specialistų skaičius pamečiui | — | `vda_id` | — | `5` | Sveikatos priežiūros specialistų licencijų skaičius pagal specialisto kvalifikaciją ir licencijos galiojimo metus pagal VASPVT LICREG duomenis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/specialistai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/specialistai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/specialistai (https://data.gov.lt/datasets/2896/)
