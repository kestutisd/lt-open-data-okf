---
type: Table
title: "Pirkimas — Ataskaitų duomenys"
description: "Rinkinyje pateikiami Viešųjų pirkimų tarnybos Pirkimo procedūrų (ATN1) ir Papildomos viešojo pirkimo ir pirkimo procedūrų (ATN2) ataskaitų duomenys nuo 2017m."
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/ataskaitos/Pirkimas"
tags: [gov, lsd, pirkimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/ataskaitos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/ataskaitos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2858/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/vpt/ataskaitos"
    author: "team:vda"
    last_modified: "2026-06-12T00:00:00Z"
---

# Pirkimas — Ataskaitų duomenys

Rinkinyje pateikiami Viešųjų pirkimų tarnybos Pirkimo procedūrų (ATN1) ir Papildomos viešojo pirkimo ir pirkimo procedūrų (ATN2) ataskaitų duomenys nuo 2017m. iki šių dienų. Rinkinio objektas - paskelbta ataskaita. Pateikiama detali informacija apie ataskaitą, viešajame pirkime dalyvavusią perkančiąją arba įgaliotąją organizacijas, pirkimo objektą bei vykdytą pirkimą. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lsd/vpt/ataskaitos/Pirkimas`[^manifest]
- **Dataset:** [Viešųjų pirkimų ataskaitų duomenys](../ataskaitos.md) (`datasets/gov/lsd/vpt/ataskaitos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/vpt/ataskaitos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/ataskaitos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/ataskaitos/Pirkimas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Viešųjų pirkimų tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-06-12`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `ataskaitos_nr` | `string` | — | `4` | `open` | — | Ataskaitos numeris | — |
| `ataskaitos_forma` | `string` | — | `4` | `open` | — | Ataskaitos forma | — |
| `ataskaitos_tipas` | `string` | — | `4` | `open` | — | Ataskaitos tipas | — |
| `ataskaitos_url` | `string` | — | `4` | `open` | — | Nuoroda į ataskaita | — |
| `istatymas` | `string` | — | `4` | `open` | — | Įstatymas, pagal kurį teikiama ataskaita | — |
| `pirkimo_nr` | `string` | — | `4` | `open` | — | Pirkimo numeris | — |
| `pirkimo_objektas_lt` | `string` | — | `2` | `open` | — | Pirkimo objekto pavadinimas | — |
| `paskelbimas` | `datetime` | `U` | `4` | `open` | — | Ataskaitos paskelbimo data | — |
| `po_tipas` | `string` | — | `4` | `open` | — | Perkančiosios organizacijos arba perkančiojo subjekto tipas | — |
| `po_jar` | `string` | — | `4` | `open` | — | Perkančiosios organizacijos juridinio asmens kodas | — |
| `po_pav` | `string` | — | `4` | `open` | — | Perkančiosios organizacijos pavadinimas | — |
| `po_adresas` | `string` | — | `2` | `open` | — | Perkančiosios organizacijos adresas | — |
| `po_nuoroda` | `string` | — | `4` | `open` | — | Nuoroda į perkančiosios organizacijos internetinį puslapį | — |
| `igaliot_istaiga` | `string` | — | `4` | `open` | — | Įgaliotoji perkančioji organizacija, įgaliotasis perkantysis subjektas arba centrinė perkančioji organizacija | — |
| `igaliot_istaigos_jar` | `string` | — | `4` | `open` | — | Įgaliotosios perkančiosios organizacijos, įgaliotojo perkančiojo subjekto arba centrinės perkančiosios organizacijos juridinio asmens kodas | — |
| `pirkimo_pagr_bvpz` | `string` | — | `4` | `open` | — | Pagrindinis pirkimo Bendrojo Viešųjų Pirkimo Žodynų (BVPŽ) kodas | — |
| `bvpz_reiksme` | `string` | — | `4` | `open` | — | Pirkimo objekto grupė pagal BVPŽ kodą | — |
| `pirkimo_rusis` | `string` | — | `4` | `open` | — | Pirkimo rūšis | — |
| `pirkimo_verte` | `string` | — | `4` | `open` | — | Pirkimo tipas | — |
| `pirkimo_daliu_skaicius` | `integer` | `U` | `4` | `open` | — | Pirkimą sudarančios dalys | — |
| `pirkimo_budas` | `string` | — | `4` | `open` | — | Pirkimo būdo pavadinimas | — |
| `budo_pagr_straipsnis` | `string` | — | `4` | `open` | — | Pirkimo būdo pasirinkimo pagrindimo straipsnis | — |
| `budo_pagr_dalis` | `string` | — | `4` | `open` | — | Pirkimo būdo pasirinkimo pagrindimo straipsnio dalis | — |
| `budo_pagr_punktas` | `string` | — | `4` | `open` | — | Pirkimo būdo pasirinkimo pagrindimo straipsnio punktas | — |
| `ar_finansuojama_es` | `boolean` | — | `4` | `open` | — | Požymis, ar pirkimas finansuojamas Europos Sąjungos | — |
| `ar_igaliojimai_suteikti_kitai_po` | `boolean` | — | `4` | `open` | — | Požymis, ar pirkimo įgaliojimai buvo suteikti kitai perkančiajai organizacijai arba kitam perkančiajam subjektui | — |
| `ar_preliminar_sutartis` | `boolean` | — | `4` | `open` | — | Požymis, ar pirkimas atliktas siekiant sudaryti preliminariąją sutartį? | — |
| `ar_dinam_pirk_sistema` | `boolean` | — | `4` | `open` | — | Požymis, ar pirkimas atliktas siekiant sukurti dinaminę pirkimo sistemą. | — |
| `ar_pateiktas_ieskinys_teismui` | `boolean` | — | `4` | `open` | — | Požymis, ar buvo pateiktas ieškinys teismui | — |
| `ar_pateikta_pretenzija_po` | `boolean` | — | `4` | `open` | — | Požymis, ar buvo pateikta pretenzija perkančiajai organizacijai | — |
| `ar_vertinta_kaina_kokybe` | `boolean` | — | `4` | `open` | — | Požymis, ar kainos ir kokybės santykis pasiūlyme buvo vertinimo kriterijus | — |
| `ar_vertintos_sanaudos_kokybe` | `boolean` | — | `4` | `open` | — | Požymis, ar sąnaudų ir kokybės santykis pasiūlyme buvo vertinimo kriterijus | — |
| `ar_vertinamos_sanaudos` | `boolean` | — | `4` | `open` | — | Požymis, ar sąnaudos pasiūlyme buvo vertinimo kriterijus | — |
| `ar_vertinama_kaina` | `boolean` | — | `4` | `open` | — | Požymis, ar kaina pasiūlyme buvo vertinimo kriterijus | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ataskaitos_forma` | `"ATN1"` | — | — | Pirkimo procedūrų ataskaita | — |
| `ataskaitos_forma` | `"ATN2"` | — | — | Papildoma viešojo pirkimo ir pirkimo procedūrų ataskaita | — |
| `ataskaitos_tipas` | `"Pirkimo procedūrų ataskaita"` | — | — | — | — |
| `ataskaitos_tipas` | `"Pirkimo procedūrų ataskaita preliminariosios sutarties pagrindu"` | — | — | — | — |
| `ataskaitos_tipas` | `"Pirkimo procedūrų ataskaita dinaminės pirkimo sistemos pagrindu"` | — | — | — | — |
| `ataskaitos_tipas` | `"Projekto konkurso procedūrų ataskaita"` | — | — | — | — |
| `istatymas` | `"Viešųjų pirkimų įstatymas"` | — | — | — | — |
| `istatymas` | `"Komunalinio sektoriaus pirkimų įstatymas"` | — | — | — | — |
| `pirkimo_rusis` | `"prekės"` | — | — | — | — |
| `pirkimo_rusis` | `"paslaugos"` | — | — | — | — |
| `pirkimo_rusis` | `"darbai"` | — | — | — | — |
| `pirkimo_verte` | `"supaprastintas pirkimas"` | — | — | — | — |
| `pirkimo_verte` | `"tarptautinis pirkimas"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pirkimo_objektas_lt` | `update(property: "pirkimo_objektas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [BVPŽ / CPV Procurement Vocabulary (Reg. (EC) No 213/2008)](../../../../../references/cpv-bvpz-kodai.md) — 45 2-digit CPV divisions (`03`–`98`) and 272 3-digit groups.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/ataskaitos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/ataskaitos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/vpt/ataskaitos (https://data.gov.lt/datasets/2858/)
