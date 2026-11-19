---
type: Dataset
title: "Administracinių nusižengimų registras"
description: "Registro objektai: LR administracinių nusižengimų kodekso nustatyta tvarka užfiksuoti administraciniai nusižengimai; LR įstatymų ir ES teisės aktų nustatyta tvarka užfiksuoti ūkio subjektų padaryti teisės pažeidimai, už kuriuos priežiūros institucijos skiria poveikio priemones."
resource: "https://get.data.gov.lt/datasets/gov/ird/anr"
tags: [gov, ird, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/ird/anr.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2558/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/anr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Administracinių nusižengimų registras

Registro objektai: LR administracinių nusižengimų kodekso nustatyta tvarka užfiksuoti administraciniai nusižengimai; LR įstatymų ir ES teisės aktų nustatyta tvarka užfiksuoti ūkio subjektų padaryti teisės pažeidimai, už kuriuos priežiūros institucijos skiria poveikio priemones. Registro valdytojas - LR Vidaus reikalų ministerija; tvarkytojas - Informatikos ir ryšių departamentas.[^manifest]

- **Namespace:** `datasets/gov/ird/anr`[^manifest]
- **Manifest CSV:** [datasets/gov/ird/anr.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/anr` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2558/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ird/anr`[^dcat]
- **Portal Title (`@lt`):** ANK 45 str. pažeidimai ir pažeidėjai[^dcat]
- **Portal Title (`@en`):** Infringements and infringements of Article 45 of the ANC[^dcat]
- **Issued (`dct:issued`):** `2024-03-12`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2025-01-21` .. `2026-04-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Administracinių nusižengimų registro (ANR) bylos, kuriose minimas Administracinių nusižengimų kodekso (ANK) 45 straipsnis ("Visuomenės sveikatos srities Europos Sąjungos reglamentų ar sprendimų, higienos norminių aktų ar kitų visuomenės sveikatos srities teisės aktų, Lietuvos Respublikos žmonių užkrečiamųjų ligų profilaktikos ir kontrolės įstatymo pažeidimas"). Pateikiama neagreguota lentelė (mikroduomenys). Viena eilutė yra vieno administracinio nusižengimo vieno straipsnio vienos dalies vienas pažeidėjas. Detalizuojama demografinė informacija apie pažeidėją bei pažeidimo vietos aplinkybes. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt. ANK 45 straipsnio dalys: 1. pažeidimas; 2. pažeidimas, padarytas pakartotinai; 3. pažeidimas, kuomet veikos sukėlė pavojų išplisti pavojingoms ar ypač pavojingoms užkrečiamosioms ligoms; 4. pažeidimas, kuomet veikos, sukėlusios pavojų išplisti pavojingoms ar ypač pavojingoms užkrečiamosioms ligoms, padarytos karo, nepaprastosios padėties, mobilizacijos, karantino, riboto karantino metu, taip pat susidarius ekstremaliajai situacijai ar ekstremaliajam įvykiui, jeigu ekstremalioji situacija ar ekstremalusis įvykis kelia pavojų žmonių gyvybei ar sveikatai.[^dcat]

### Portal Description (`@en`)

Administrative offences cases referring to Article 45 of the Code of Administrative Offences (“Violation of the Law on Prevention and Control of Communicable Diseases of People of the Republic of Lithuania”). Detailed demographic information about the offender and the circumstances of the location of the offence shall be provided. Parts of the article: 1. violation of the law; 2. a repeated infringement; 3. an infringement where the conduct has endangered the spread of dangerous or particularly dangerous communicable diseases; 4. an infringement where acts which endangered the spread of dangerous or particularly dangerous communicable diseases were committed during war, emergency, mobilisation, quarantine, restricted quarantine, also in the event of an emergency or an emergency, where an emergency or an emergency poses a danger to human life or health.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Bauda](anr/Bauda.md) | Administracinių nusižengimų bylose paskirtos baudos | `4` | `anr_id` | — | `9` | Administracinių nusižengimų registro (ANR) duomenų neagreguota lentelė (mikroduomenys), kurioje viena eilutė yra vienas administracinis nusižengimas už kurį... |
| [KetPazeidejas](anr/KetPazeidejas.md) | Kelių eismo taisyklių pažeidimai ir pažeidėjai | `4` | `vda_prime_key` | — | `10` | Administracinių nusižengimų registro (ANR) duomenų neagreguota lentelė (mikroduomenys), kurioje įtraukti tik tie nusižengimai kurių sudėtį nustatantys... |
| [Nusizengimas](anr/Nusizengimas.md) | Administracinių nusižengimų detali mėnesinė statistika | `3` | — | — | `7` | Administracinių nusižengimų registro (ANR) mėnesiniai statistiniai duomenys apie Administracinių nusižengimų kodekso nustatyta tvarka užfiksuotus... |
| [Str45Pazeidimas](anr/Str45Pazeidimas.md) | ANK 45 str. pažeidimai ir pažeidėjai | `4` | `vda_id` | — | `12` | Administracinių nusižengimų registro (ANR) bylos, kuriose minimas Administracinių nusižengimų kodekso (ANK) 45 straipsnis ("Visuomenės sveikatos srities... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/anr.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/anr (https://data.gov.lt/datasets/2558/)
