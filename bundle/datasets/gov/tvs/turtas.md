---
type: Dataset
title: "Duomenys apie savyvaldybės turtą"
description: "Rinkinys pateikia informaciją apie savivaldybių valdomą nekilnojamąjį turtą."
resource: "https://get.data.gov.lt/datasets/gov/tvs/turtas"
tags: [gov, tvs, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/turtas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/tvs/turtas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3825/"
    title: "data.gov.lt DCAT-AP — datasets/gov/tvs/turtas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Duomenys apie savyvaldybės turtą

Rinkinys pateikia informaciją apie savivaldybių valdomą nekilnojamąjį turtą. Duomenyse nurodomas turto identifikatorius, NT registro kodas, objekto pavadinimas, statybos pabaigos metai, objekto paskirtis, plotas kvadratiniais metrais, bei geografinė vieta. Geografinė informacija pateikiama tiek geografinių koordinačių, tiek LKS-94 plokštuminių koordinačių formatais. Taip pat įtrauktas objekto adreso informacijos aktualumas bei geografinio koordinavimo patikimumo procentas. Duomenų teikėjas: Savivaldybių administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/tvs/turtas`[^manifest]
- **Manifest CSV:** [datasets/gov/tvs/turtas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/turtas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tvs/turtas` (`deployed`)[^manifest]
- **Provider:** `tvs` — Savivaldybių turto valdymo duomenų rinkinys *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3825/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/tvs/turtas`[^dcat]
- **Portal Title (`@lt`):** Savivaldybių turto valdymo duomenų rinkinys[^dcat]
- **Portal Title (`@en`):** Collection of municipal property management data[^dcat]
- **Issued (`dct:issued`):** `2025-04-16`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2026-04-01` .. `2026-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinys pateikia informaciją apie savivaldybių valdomą nekilnojamąjį turtą bei nuomos sutartis. Duomenys apima nuomos sutarčių detales, tokias kaip unikalus sutarties identifikatorius, nuomininko duomenys (šifruoti fizinių asmenų atvejais), nuomos pradžios data, sutarties tipas, mėnesio įmokos suma (eurais, pagal sutartį), galimi sutarties sustabdymai bei teisinis pagrindas. Taip pat pateikiama informacija apie savivaldybėms priklausantį nekilnojamąjį turtą – nekilnojamojo turto registro kodai, paskirties kategorijos, statybos pabaigos metai, turto plotas (kvadratiniais metrais), adresai bei geografinė informacija su koordinatėmis, patikimumo koeficientas ir objekto tipas geografinėje dalyje. Duomenų rinkinys yra nuolat atnaujinamas. Duomenų laikotarpis siekia nuo duomenų kaupimo pradžios iki dabar. Visi duomenys pateikiami atsižvelgiant į teisės aktų keliamus duomenų atvėrimo reikalavimus, todėl kai kurios reikšmės, tokios kaip asmenų identifikavimo duomenys, yra užšifruotos. Rinkinys suskirstytas į atskiras duomenų korteles, kiekvienai savivaldybei pateikiant atskirą išklotinę su turto valdymo informacija. Kortelėse pateikiamos tiek nuomos sutartys, tiek nekilnojamojo turto įrašai, leidžiantys išsamiau analizuoti savivaldybės valdomą turtą ir jo naudojimą. Duomenų teikėjas: Telšių rajono savivaldybės administracija; Kėdainių rajono savivaldybės administracija; Marijampolės savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The set shall provide information on real estate and lease contracts managed by municipalities. The data include details of lease agreements such as a unique contract identifier, tenant details (encrypted for natural persons), start date of lease, type of contract and possible contract suspensions. Information on real estate belonging to municipalities shall also be provided – real estate register codes, purpose categories, addresses and geographic information with coordinates. Addition: The set was expanded to include the following additional data columns in order to increase the completeness of the information and the value of its use: The area of the property (in square metres), Year of completion of construction, Legal basis, Amount of monthly instalment (euro, contract) Reliability factor and object type in the geographical part. Taking into account the method of identification of information infrastructure of particular importance approved by the Resolution of the Government of the Republic of Lithuania, geographic coordinates presented in the data of this set may be noisy (we determine whether or not such objects are present during analysis) in order to ensure the requirements of national security. This means that the exact location of the assets will not be disclosed and the geographical information will be processed in such a way that the exact location of strategic infrastructure objects cannot be determined (in accordance with Article 5(2) of the Law of the Republic of Lithuania on Cyber Security, which obliges state institutions to protect critical infrastructure data). The dataset is constantly updated. Data period from the start of data collection to the present. All data are provided in accordance with the legal requirements for data opening and some values, such as personal identification data, are encrypted. The set is divided into separate data cards, with a separate breakdown with asset management information for each municipality. The cards include both lease contracts and real estate records, allowing for a more detailed analysis of the property managed by the municipality and its use. Data provider: Telsiai District Municipality administration. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TelsiuRajSav](turtas/TelsiuRajSav.md) | — | `4` | `id` | — | `13` | — |
| [KedainiuRajSav](turtas/KedainiuRajSav.md) | — | `4` | `id` | — | `13` | — |
| [MarijampolesRajSav](turtas/MarijampolesRajSav.md) | — | `4` | `id` | — | `13` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/tvs/turtas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/turtas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/tvs/turtas (https://data.gov.lt/datasets/3825/)
