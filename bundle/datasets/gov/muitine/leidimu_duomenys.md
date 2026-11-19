---
type: Dataset
title: "Muitinės leidimų sistemos leidimų ir prašymų duomenys"
description: "Leidimų sistemos duomenys aprašo kelią nuo prašymo pateikimo iki leidimo išdavimo ir galiojimo."
resource: "https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys"
tags: [gov, muitine, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3915/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/leidimu_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Muitinės leidimų sistemos leidimų ir prašymų duomenys

Leidimų sistemos duomenys aprašo kelią nuo prašymo pateikimo iki leidimo išdavimo ir galiojimo. Jie parodo, kas kreipėsi, kokio leidimo prašoma, kokia yra nagrinėjimo būsena ir kada leidimas galioja. Prie kiekvieno prašymo ir leidimo gali būti pridėtos papildomos detalės (lankstūs laukeliai), nes skirtingiems leidimų tipams reikia skirtingos informacijos. Šis rinkinys padeda aiškiai matyti, kiek ir kokių leidimų išduota bei kokioje stadijoje yra prašymai.[^manifest]

- **Namespace:** `datasets/gov/muitine/leidimu_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/leidimu_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3915/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys`[^dcat]
- **Portal Title (`@lt`):** Muitinės leidimų sistemos leidimų ir prašymų duomenys[^dcat]
- **Portal Title (`@en`):** Customs Authorisation System Permissions and Applications Data[^dcat]
- **Issued (`dct:issued`):** `2025-10-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-10-21` .. `2026-10-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Muitinės leidimų sistemos duomenys atvaizduoja kelią nuo asmens prašymo suteikti leidimą pateikimo iki leidimo suteikimo bei galimų jo būsenos pakeitimų. Jie parodo, kas kreipiasi, kokio leidimo prašo, kokia yra prašymo nagrinėjimo būsena, nuo kada leidimas galioja ir kokia yra jo aktuali būsena. Prie kiekvieno prašymo ir leidimo gali būti pridėtos papildomos detalės (lankstūs laukeliai), nes skirtingoms leidimų rūšims reikia skirtingos informacijos. Šis duomenų rinkinys padeda aiškiai matyti, kiek pateikta prašymų muitinės leidimams gauti, kokioje svarstymo būsenoje jie yra, kiek ir kokių muitinės leidimų yra suteikta ir kokia yra šių leidimų būsena. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt[^dcat]

### Portal Description (`@en`)

The data of the customs authorisation system shall represent the path from the submission of a person's application for authorisation to the granting of an authorisation and possible changes to his state. They shall show who is applying, what authorisation they are requesting, what the state of examination of the application is, from when the authorisation is valid and what its current status is. Additional details (flexible fields) may be added to each application and authorisation, as different types of authorisations require different information. This dataset provides a clear picture of the number of applications for customs authorisations, the state of reflection, the number and type of customs authorisations granted and the state of these authorisations. Please contact atverimas@stat.gov.lt by e-mail for information. For technical problems with the portal, please contact atviriduomenys@vssa.lt by e-mail[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Leidimas](leidimu_duomenys/Leidimas.md) | Leidimai | `4` | `vda_prime_key` | — | `13` | Duomenys apie suteiktą teisę atlikti tam tikrą veiklą ar naudotis lengvata. |
| [LeidimoDuomuo](leidimu_duomenys/LeidimoDuomuo.md) | Leidimų duomenys | — | `vda_prime_key` | — | `9` | Papildomos leidimo detalės eilutėmis (po vieną detalę per eilutę). |
| [Prasymas](leidimu_duomenys/Prasymas.md) | Prašymai | — | `vda_prime_key` | — | `12` | Pateiktas prašymas gauti leidimą. |
| [PrasymoDuomuo](leidimu_duomenys/PrasymoDuomuo.md) | Prašymų duomenys | — | `vda_prime_key` | — | `10` | Papildomos prašymo detalės eilutėmis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/leidimu_duomenys (https://data.gov.lt/datasets/3915/)
