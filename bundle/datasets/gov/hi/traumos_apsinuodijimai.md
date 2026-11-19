---
type: Dataset
title: "\"Stacionaro ir ambulatoriniai ligoniai, gydyti nuo traumų ir apsinuodijimų\""
description: "\"Duomenys iš Higienos Instituto apie pacientus, kurie kreipėsi į gydymo įstaigas dėl traumų ir apsinuodijimų, ir kuriems buvo priskirtas stacionarus arba ambulatorinis gydymo tipas."
resource: "https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai"
tags: [gov, hi, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2829/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/traumos_apsinuodijimai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# "Stacionaro ir ambulatoriniai ligoniai, gydyti nuo traumų ir apsinuodijimų"

"Duomenys iš Higienos Instituto apie pacientus, kurie kreipėsi į gydymo įstaigas dėl traumų ir apsinuodijimų, ir kuriems buvo priskirtas stacionarus arba ambulatorinis gydymo tipas. Duomenų rinkinys yra sudarytas iš trijų lentelių: 1. Traumas ir apsinuodijimus patyrusių pacientų duomenys, 2. Traumų ir apsinuodijimų atvejai dėl kurių kreiptasi į gydymo įstaigą, 3. Gydymo įstaigų duomenys. Duomenų teikėjas – Higienos institutas Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/hi/traumos_apsinuodijimai`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/traumos_apsinuodijimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2829/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai`[^dcat]
- **Portal Title (`@lt`):** Stacionaro ir ambulatoriniai ligoniai, gydyti nuo traumų ir apsinuodijimų[^dcat]
- **Portal Title (`@en`):** Inpatient and outpatient patients treated for injuries and poisonings[^dcat]
- **Issued (`dct:issued`):** `2024-10-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-20`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-11-01` .. `2026-04-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys iš Higienos Instituto apie pacientus, kurie kreipėsi į gydymo įstaigas dėl traumų ir apsinuodijimų, ir kuriems buvo priskirtas stacionarus arba ambulatorinis gydymo tipas. Duomenų rinkinys yra sudarytas iš dviejų lentelių: * TraumaApsinuodijimasPacientai (sisteminis pavadinimas) - vieną eilutę sudaro informacija apie paciento traumą/apsinuodijimą. Eilutėje pateikiama informacija apie pacientą - lytis, gimimo metai, savivaldybė, kurioje registruotas paciento gyvenamasis adresas, ir gyvenvietės tipas. Taip pat pateikiama pagrindinė su trauma susijusi informacija - gydymo lapo pradžios data, gydymo tipas (jei gydymas "Stacionarinis", nurodomas ir stacionaro tipas), bei traumą/apsinuodijimą apibūdinantys TLK-10-AM kodai nurodantys traumos - pavadinimą, aplinkybes, veiklą (įvykstant traumai) ir įvykio vietą. * TraumaApsinuodijimasLigonines (sisteminis pavadinimas) - vieną eilutę sudaro traumos/apsinuodijimo atvejis ir gydymo įstaiga, į kurią buvo kreiptasi. Eilutėje yra informacija apie gydymo įstaigą - pavadinimas ir juridinio asmens kodas (JAR). Informacija apie traumą/apsinuodijimą - gydymo lapo pradžios ir pabaigos laiko žymos, traumos TLK-10-AM kodas, gydymo tipas (jei gydymas "Stacionarinis", nurodomas ir stacionaro tipas). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data from the Hygiene Institute on patients who have sought treatment for injuries and poisonings and who have been assigned a hospital or outpatient type of treatment. The dataset consists of two tables: * Poisoning Patients (systemic name) - one line contains information about the patient's trauma/poisoning. The line contains information about the patient - gender, year of birth, the municipality where the patient's residential address is registered, and the type of settlement. Key trauma-related information shall also be provided - the starting date of the treatment sheet, the type of treatment (if “Stationary” treatment is indicated, both the stationary type) and TLK-10-AM codes describing the trauma - name, circumstances, activity (in the event of injury) and the scene. * Poisoning Hospital (systemic name) - one line consists of a case of trauma/poisoning and a treatment institution that has been contacted. The line contains information about the medical institution - name and legal entity number (Jaris). Information on trauma/poisoning means the start and end time marks of the treatment sheet, the injury TLK-10-AM code, the type of treatment (if the treatment is “Stationary”, the type of hospital shall also be indicated). Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pacientas](traumos_apsinuodijimai/Pacientas.md) | Traumas ir apsinuodijimus patyrusių pacientų duomenys | `4` | `vda_pk` | — | `14` | "Duomenys iš Higienos instituto apie traumas arba apsinuodijimus patyrusius pacientus. |
| [Ligonine](traumos_apsinuodijimai/Ligonine.md) | Traumų ir apsinuodijimų atvejai dėl kurių kreiptasi į gydymo įstaigą | `4` | `vda_pk` | — | `7` | "Duomenys iš Higienos instituto apie traumų ir apsinuodijimų atvejus dėl kurių buvo kreiptasi į gydymo įstaigą. |
| [GydymoIstaiga](traumos_apsinuodijimai/GydymoIstaiga.md) | Gydymo įstaigų duomenys | `4` | `gist_id` | — | `7` | "Duomenys iš Higienos instituto apie gydymo įstaigas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/traumos_apsinuodijimai (https://data.gov.lt/datasets/2829/)
