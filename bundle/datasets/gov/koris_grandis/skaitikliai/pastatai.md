---
type: Dataset
title: "Pastatai"
description: "Pastatų nekintanti informacija"
resource: "https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/pastatai"
tags: [gov, koris_grandis, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L102"
    title: "atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv#L102"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3969/"
    title: "data.gov.lt DCAT-AP — datasets/gov/koris_grandis/skaitikliai/pastatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pastatai

Pastatų nekintanti informacija[^manifest]

- **Namespace:** `datasets/gov/koris_grandis/skaitikliai/pastatai`[^manifest]
- **Manifest CSV:** [datasets/gov/koris_grandis/skaitikliai.csv#L102](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L102)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/pastatai` (`deployed`)[^manifest]
- **Provider:** `koris_grandis` — Komunaliniai suvartojimo įrašai sistemoje „GRANDIS“ *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3969/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/pastatai`[^dcat]
- **Portal Title (`@lt`):** Komunaliniai suvartojimo įrašai sistemoje „GRANDIS“[^dcat]
- **Portal Title (`@en`):** Komunaliniai suvartojimo įrašai UAB „KORIS“ sistemoje „GRANDIS“[^dcat]
- **Issued (`dct:issued`):** `2025-11-26`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2025-11-19` .. `2025-11-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinys sudarytas iš sistemos „GRANDIS“ duomenų apie deklaruotą vandens ir šilumos suvartojimą. Suvartojimo lentelėse viena eilutė atitinka vieno komunalinių paslaugų skaitiklio parodymų skirtumo deklaravimą per mėnesį. Lentelėse nurodomas vadinamasis „apskaitos taškas“, kaip skaitiklio tvirtinimo vieta pastate, mokėtojų duomenys (fizinių asmenų ir privačių įmonių pseudoniminti, o viešųjų – palikti atviri), apskaitos mėnuo, rodmenų deklaravimo data ir deklaruotas suvartojimas. Fizinių ir juridinių asmenų suvartojimas pateikimas atskirai. Suvartojimo lenteles galite sujungti su pastatų lentele per pastato identifikatorių. Pastatų lentelėje pateikiamas pastato tipas, požymis, ar pastate yra mažai (iki 3 imtinai), ar daug (nuo 4) apskaitos taškų, taip pat – pastatų koordinatės ir statybos metai, paskutinį metų skaitmenį pakeičiant nuliu. Jei pastate yra mažiausiai 4 apskaitos taškai, pastato koordinatės paliekamos tikslios, o jei apskaitos taškų yra mažiau nei 4, tuomet pastato koordinatės paslenkamos iki 1 km nuo tikrosios padėties. Duomenų teikėjo UAB „Vilkaviškio šilumos tinklai“ pateikiami įrašai nuo 2019 m. birželio mėn. iki 2024 m. liepos mėn., jie nebeplanuojami atnaujinti. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Rinkinys sudarytas iš UAB „KORIS“ sistemos „GRANDIS“ duomenų apie deklaruotą vandens ir šilumos suvartojimą. Suvartojimo lentelėse viena eilutė atitinka vieno komunalinių paslaugų skaitiklio parodymų skirtumo deklaravimą per mėnesį. Lentelėse nurodomas vadinamasis „apskaitos taškas“, kaip skaitiklio tvirtinimo vieta pastate, mokėtojų duomenys (fizinių asmenų ir privačių įmonių pseudoniminti, o viešųjų – palikti atviri), apskaitos mėnuo, rodmenų deklaravimo data ir deklaruotas suvartojimas. Fizinių ir juridinių asmenų suvartojimas pateikimas atskirai. Suvartojimo lenteles galite sujungti su pastatų lentele per pastato identifikatorių. Pastatų lentelėje pateikiamas pastato tipas, požymis, ar pastate yra mažai (iki 3 imtinai), ar daug (nuo 4) apskaitos taškų, taip pat – pastatų koordinatės ir statybos metai, paskutinį metų skaitmenį pakeičiant nuliu. Jei pastate yra mažiausiai 4 apskaitos taškai, pastato koordinatės paliekamos tikslios, o jei apskaitos taškų yra mažiau nei 4, tuomet pastato koordinatės paslenkamos iki 1 km nuo tikrosios padėties. Duomenų teikėjo UAB „Vilkaviškio šilumos tinklai“ pateikiami įrašai nuo 2019 m. birželio mėn. iki 2024 m. liepos mėn., jie nebeplanuojami atnaujinti. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VilkaviskioPastatas](pastatai/VilkaviskioPastatas.md) | UAB „Vilkaviškio šilumos tinklų“ aptarnaujami pastatai | `4` | `pastato_id` | — | `10` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv#L102 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L102)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/koris_grandis/skaitikliai/pastatai (https://data.gov.lt/datasets/3969/)
