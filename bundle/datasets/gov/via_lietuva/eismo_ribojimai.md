---
type: Dataset
title: "\"Eismo ribojimai valstybinės reikšmės keliuose\""
description: "\"Duomenų rinkinyje pateikiami Valstybinės reikšmės kelių eismo informacinės sistemos duomenys apie valstybinių kelių eismo ribojimus dėl renginių, remonto darbų ar kelyje atsiradusių kliūčių."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai"
tags: [gov, via_lietuva, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1250/"
    title: "data.gov.lt DCAT-AP — datasets/gov/via_lietuva/eismo_ribojimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# "Eismo ribojimai valstybinės reikšmės keliuose"

"Duomenų rinkinyje pateikiami Valstybinės reikšmės kelių eismo informacinės sistemos duomenys apie valstybinių kelių eismo ribojimus dėl renginių, remonto darbų ar kelyje atsiradusių kliūčių. Duomenų rinkinį sudaro keturios lentelės: 1. „Kelių remonto darbai“ – informacija apie kelio remonto darbus valstybinės reikšmės keliuose; 2. „Kliūtys kelyje“ – informacija apie kliūtis kelyje valstybinės reikšmės keliuose; 3. „Eismo ribojimai dėl renginių“ – eismo ribojimai dėl renginių valstybinės reikšmės keliuose; 4. „Valstybinių kelių atkarpos“ – valstybinių kelių atkarpų identifikatoriai su atitinkamų atkarpų pavadinimais ir ilgiais, kurie skirti jungti su rinkinyje esančiomis lentelėmis. Duomenų teikėjas – AB „Via Lietuva“. Duomenys kaupiami nuo 2020 m. birželio 1 d. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt."[^manifest]

- **Namespace:** `datasets/gov/via_lietuva/eismo_ribojimai`[^manifest]
- **Manifest CSV:** [datasets/gov/via_lietuva/eismo_ribojimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai` (`deployed`)[^manifest]
- **Provider:** `via_lietuva` — AB „Via Lietuva“ (buv. LAKD) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1250/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai`[^dcat]
- **Portal Title (`@lt`):** Eismo ribojimai valstybinės reikšmės keliuose[^dcat]
- **Portal Title (`@en`):** Traffic restriction data[^dcat]
- **Issued (`dct:issued`):** `2023-09-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2021-09-22` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami Valstybinės reikšmės kelių eismo informacinės sistemos duomenys apie valstybinių kelių eismo ribojimus dėl renginių, remonto darbų ar kelyje atsiradusių kliūčių. Duomenų rinkinį sudaro keturios lentelės: 1. „Kelių remonto darbai“ – informacija apie kelio remonto darbus valstybinės reikšmės keliuose; 2. „Kliūtys kelyje“ – informacija apie kliūtis kelyje valstybinės reikšmės keliuose; 3. „Eismo ribojimai dėl renginių“ – eismo ribojimai dėl renginių valstybinės reikšmės keliuose; 4. „Valstybinių kelių atkarpos“ – valstybinių kelių atkarpų identifikatoriai su atitinkamų atkarpų pavadinimais ir ilgiais, kurie skirti jungti su rinkinyje esančiomis lentelėmis. Duomenų teikėjas – AB „Via Lietuva“. Duomenys kaupiami nuo 2020 m. birželio 1 d. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Traffic restrictions, road repairs, traffic disturbances, road obstacles, restriction validity period, other data and their display parameters[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Remontas](eismo_ribojimai/Remontas.md) | Kelių remonto darbai | `4` | `darbo_id` | — | `14` | "Duomenys apie kelių remonto darbus valstybinės reikšmės keliuose. |
| [Kliutis](eismo_ribojimai/Kliutis.md) | Kliūtys kelyje | `4` | `kliuties_id` | — | `10` | "Duomenys apie kliūtis valstybinės reikšmės keliuose. |
| [Renginys](eismo_ribojimai/Renginys.md) | Eismo ribojimai dėl renginių | `4` | `ribojimo_id` | — | `10` | "Duomenys apie eismo ribojimus dėl renginių valstybinės reikšmės keliuose. |
| [KelioAtkarpa](eismo_ribojimai/KelioAtkarpa.md) | Valstybinių kelių atkarpos | `4` | `kelio_id` | — | `7` | "Duomenys apie valstybinių kelių atkarpas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/via_lietuva/eismo_ribojimai (https://data.gov.lt/datasets/1250/)
