---
type: Dataset
title: "Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta” skaitiklių parodymų įrašai"
description: "Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, skaitiklių parodymų įrašai."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/patalpos"
tags: [gov, asmlis, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L50"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv#L50"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2944/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/skaitikliai/patalpos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta” skaitiklių parodymų įrašai

Savivaldybių MOKESTA ir ASMLIS sistemų duomenys[^manifest]

- **Namespace:** `datasets/gov/asmlis/skaitikliai/patalpos`[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/skaitikliu_parodymai.csv#L50](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L50)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/patalpos` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2944/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/asmlis/skaitikliai/patalpos`[^dcat]
- **Portal Title (`@lt`):** Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta” skaitiklių parodymų įrašai[^dcat]
- **Portal Title (`@en`):** Metering records of service and service administration systems “Asmlis” and “Mokesta”[^dcat]
- **Issued (`dct:issued`):** `2025-02-28`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-02-28` .. `2026-10-10`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, skaitiklių parodymų įrašai. Viena eilutė atitinka vieną skaitiklio deklaravimo įrašą. Duomenų rinkinį sudaro dvi lentelės, kuriose pateikiami skaitiklių parodymų ir patalpų, kurioms priskirtas skaitiklis įrašai. Lentelėse galima rasti skaitiklio tipą, laikotarpį, kuriuo atlikta deklaracija, skaitiklių vertes nuo ir iki, patapos plotą, tūri ir apytiksles koordinates. Koordinatės „triukšminamos“ naudojant 50 metrų standartinio nuokrypio parametrą. Priklausomai nuo savivaldybės ar įstaigos, duomenų aprėptis gali skirtis, tačiau duomenis numatyta atnaujinti kas mėnesį. Duomenų teikėjai: UAB „Šiaulių šviesa“; UAB „Simno komunalininkas“; UAB „Šilutės šilumos tinklai“; AB „Šiaulių energija“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Metering records of the service and settlement administration systems “Asmlis” and “Mokesta” serving municipalities and their subsidiaries. One row corresponds to one counter declaration entry. The dataset consists of two tables showing the metering impressions and the premises to which the meter is assigned. In the tables you can find the type of counter, the period in which the declaration was made, the values of the meters from and to, the surface area, the volume and approximate coordinates. The coordinates are “noisy” using a 50 metre standard deviation parameter. Depending on the municipality or body, the scope of the data may vary, but the data is scheduled to be updated monthly. Data provider: UAB “Šiauliai šviesa”. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SiauliuSviesaPatalpa](patalpos/SiauliuSviesaPatalpa.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB „Šiaulių šviesa“ patalpų įrašai. | `4` | `patalpos_id` | — | `7` | — |
| [SiauliuEnergijaPatalpa](patalpos/SiauliuEnergijaPatalpa.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” AB „Šiaulių energija“ patalpų įrašai. | `4` | `patalpos_id` | — | `7` | — |
| [SimnoKomunalininkasPatalpa](patalpos/SimnoKomunalininkasPatalpa.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB „Simno komunalininkas“ patalpų įrašai. | `4` | `patalpos_id` | — | `7` | — |
| [SilutesSTPatalpa](patalpos/SilutesSTPatalpa.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemos „Mokesta” UAB „Šilutės šilumos tinklai“ patalpų įrašai. | `4` | `patalpos_id` | — | `7` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/skaitikliu_parodymai.csv#L50 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/skaitikliu_parodymai.csv#L50)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/skaitikliai/patalpos (https://data.gov.lt/datasets/2944/)
