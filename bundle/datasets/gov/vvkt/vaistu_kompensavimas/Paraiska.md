---
type: Table
title: "Paraiska — Sveikatos technologijų vertinimas (STV). Paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys ir vertinimo eigos stebėsena"
description: "Duomenų rinkinį sudaro Valstybinei vaistų kontrolės tarnybai prie Lietuvos Respublikos sveikatos apsaugos ministerijos pateiktų sveikatos technologijų vertinimo paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistu_kompensavimas/Paraiska"
tags: [gov, vvkt, paraiska, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_kompensavimas.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistu_kompensavimas.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2897/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkt/vaistu_kompensavimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Paraiska — Sveikatos technologijų vertinimas (STV). Paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys ir vertinimo...

Duomenų rinkinį sudaro Valstybinei vaistų kontrolės tarnybai prie Lietuvos Respublikos sveikatos apsaugos ministerijos pateiktų sveikatos technologijų vertinimo paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus duomenys. Rinkinyje pateikiama tokių paraiškų eiga – nurodomos aktualios datos, pareiškėjai, vaistiniai preparatai, indikacijos ir pan. Duomenų rinkinio viena eilutė atitinka vieną paraišką. Su rekomendacijomis ir detalesne informacija galima susipažinti čia: https://vvkt.lrv.lt/lt/sveikatos-technologiju-vertinimas/vaistiniu-preparatu-medicinos-pagalbos-priemoniu-ir-ligu-vertinimai/. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vvkt/vaistu_kompensavimas/Paraiska`[^manifest]
- **Dataset:** [Sveikatos technologijų vertinimas (STV). Paraiškų įrašyti vaistinį preparatą į kompensavimo...](../vaistu_kompensavimas.md) (`datasets/gov/vvkt/vaistu_kompensavimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvkt/vaistu_kompensavimas.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_kompensavimas.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistu_kompensavimas/Paraiska` (`deployed`)[^manifest]
- **Provider:** `vvkt` — Valstybinė vaistų kontrolės tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `paraiskos_numeris` | `string` | — | `4` | `open` | — | Paraiškos numeris | — |
| `pareiskejas` | `string` | — | `4` | `open` | — | Pareiškėjo pavadinimas | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `paraiskos_bukle` | `string` | — | `4` | `open` | — | Bendra paraiškos būklė | — |
| `vaistinis_preparatas` | `string` | — | `4` | `open` | — | Vaistinio preparato pavadinimas (firminis pavadinimas ir farmacinė forma) | — |
| `bendrinis_preparato_pav` | `string` | — | `4` | `open` | — | Bendrinis vaistinio preparato pavadinimas | — |
| `ligu_kodas_tlk` | `string` | — | `4` | `open` | — | Ligų kodai pagal TLK-AM-10 (Tarptautinė statistinė ligų ir sveikatos sutrikimų klasifikacija, dešimtasis pataisytas ir papildytas leidimas, Australijos modifikacija) | — |
| `indikacija` | `string` | — | `2` | `open` | — | Vaistinio preparato terapinės indikacijos | — |
| `palyg_vaist_prep` | `string` | — | `2` | `open` | — | Palyginamasis vaistinis preparatas, kuris naudojamas kaip pagrindas siūlomo kompensuoti vaistinio preparato lyginimui | — |
| `klausimu_issiuntimo_data` | `date` | `D` | `4` | `open` | — | Klausimų išsiuntimo data | — |
| `atsakymu_gavimo_data` | `date` | `D` | `4` | `open` | — | Atsakymų gavimo data | — |
| `vertinimo_pabaigos_data` | `date` | `D` | `4` | `open` | — | Išvadų pateikimo; užduoties įvykdymo data | — |
| `rekomendaciju_nepateikimo_priezastis` | `string` | — | `2` | `open` | — | Rekomendacijų nepateikimo priežastis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistu_kompensavimas.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_kompensavimas.csv#L10)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkt/vaistu_kompensavimas (https://data.gov.lt/datasets/2897/)
