---
type: Dataset
title: "KEIS Kultūros paso edukacijos"
description: "Edukacijos. Rinkinyje pateikiamos edukacinės programos, kuriose moksleiviai gali dalyvauti pagal kultūros paso programą."
resource: "https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas"
tags: [gov, lnb, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lnb/kulturos_pasas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2659/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/kulturos_pasas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KEIS Kultūros paso edukacijos

- **Namespace:** `datasets/gov/lnb/kulturos_pasas`[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/kulturos_pasas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2659/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas`[^dcat]
- **Portal Title (`@lt`):** KEIS Kultūros paso edukacijos[^dcat]
- **Portal Title (`@en`):** CHANGE THE Education of the Cultural Passport[^dcat]
- **Issued (`dct:issued`):** `2024-05-17`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-02` .. `2026-10-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by-nc/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Edukacijos. Rinkinyje pateikiamos edukacinės programos, kuriose moksleiviai gali dalyvauti pagal kultūros paso programą. Kultūros pasas – priemonė, leidžianti moksleiviams valstybės lėšomis lankytis įvairiausiuose kultūros ir meno renginiuose: spektakliuose, koncertuose, parodose ir kitose pažintinėse bei edukacinėse kultūros veiklose. Priklausomai nuo amžiaus grupės, moksleiviai kultūros ir meno paslaugomis gali pasinaudoti dalyvaudami kartu su klase ar grupe, o nuo 16 metų paslaugomis gali pasinaudoti ir individualiai. Pasas siūlo kultūrines edukacijas kultūros paveldo, etninės kultūros, architektūros, cirko, baleto, kino, lėlių teatro, dramos teatro, literatūros ir kt. srityse. Edukacijų užsakymai. Rinkinyje pateikiami edukacijų užsakymai grupėms, kuriuose nurodoma veiklos ir užsakymo numeriai (tą pačią veiklą gali užsakyti kelios grupės); veiklos laikas ir data; statusas; vieta (nuotoliniu būdu/pas organizatorių/užsakančios įstaigos patalpose); dalyvių skaičius, iš jų – kiek su negalia; lydinčių asmenų skaičius; požymis, nurodantis, ar bus dalyvių užsieniečių; sąskaitos suma; edukacijos užsiėmimą užsakanti institucija. Jei užsakymas atšauktas – nurodytas atšaukimo laikas ir ar tai paslaugos teikėjo atšaukimas. Edukacijų dalyviai. Rinkinyje pateikiamas dalyvio unikalus šifruotas ID, dalyvio mokslo institucija, savivaldybė ir gimimo metai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes educational programmes available to students under the Culture Passport programme. Cultural passport is a tool allowing pupils to visit various cultural and art events at public expense: performances, concerts, exhibitions and other cognitive and educational cultural activities. Depending on age group, students can use cultural and artistic services to participate in conjunction with a class or group, and from the age of 16 they can also use services individually. Cultural education in cultural heritage, ethnic culture, architecture, circus, ballet, cinema, doll theatre, drama theatre, literature, etc.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Edukacija](kulturos_pasas/Edukacija.md) | KEIS Kultūros paso edukacijos | `4` | — | — | `19` | "Rinkinyje pateikiamos edukacinės programos, kurias gali(-ėjo) įsigyti mokiniai pagal kultūros paso programą. |
| [EdukacijosDalyvis](kulturos_pasas/EdukacijosDalyvis.md) | — | `4` | — | — | `8` | — |
| [EdukacijosUzsakymoIvykis](kulturos_pasas/EdukacijosUzsakymoIvykis.md) | — | `4` | — | — | `22` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/kulturos_pasas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/kulturos_pasas (https://data.gov.lt/datasets/2659/)
