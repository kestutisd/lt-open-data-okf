---
type: Table
title: "NepriklElEnergTiekPlanas — Nepriklausomų elektros energijos tiekėjų planai"
description: "Duomenų rinkinyje pateikiami nepriklausomų elektros energijos tiekėjų planai buitiniams vartotojams."
resource: "https://get.data.gov.lt/datasets/gov/vert/neprikl_ee_tiek_planai/NepriklElEnergTiekPlanas"
tags: [gov, vert, nepriklelenergtiekplanas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vert/neprikl_ee_tiek_planai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vert/neprikl_ee_tiek_planai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2802/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vert/neprikl_ee_tiek_planai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# NepriklElEnergTiekPlanas — Nepriklausomų elektros energijos tiekėjų planai

Duomenų rinkinyje pateikiami nepriklausomų elektros energijos tiekėjų planai buitiniams vartotojams. Plano kainą sudaro tiekėjo kaina, ESO plano kaina, persiuntimo, skirstymo ir viap dedamosios. Biržos planų kainą sudaro „Nordpool“ biržos kaina (rinkinyje nepateikta), kuri keičiasi kas mėnesį arba valandą (priklauso nuo pasirinkto plano), tiekėjo kaina, ESO kaina ir valstybės reguliuojamos kainos dalys. Valstybės reguliuojamos kainų dalys (skirstymo, persiuntimo ir viap dedamosios) fiksuojamos nepriklausomai nuo plano fiksavimo termino, todėl bendra fiksuoto plano kaina gali kisti. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vert/neprikl_ee_tiek_planai/NepriklElEnergTiekPlanas`[^manifest]
- **Dataset:** [Nepriklausomų elektros energijos tiekėjų planai](../neprikl_ee_tiek_planai.md) (`datasets/gov/vert/neprikl_ee_tiek_planai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vert/neprikl_ee_tiek_planai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vert/neprikl_ee_tiek_planai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vert/neprikl_ee_tiek_planai/NepriklElEnergTiekPlanas` (`deployed`)[^manifest]
- **Provider:** `vert` — Valstybinė energetikos reguliavimo tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `tiek_plano_id` | `string` | — | `4` | `open` | — | Tiekėjo identifikatorius | — |
| `tiekejas` | `string` | — | `4` | `open` | — | Tiekėjo pavadinimas | — |
| `tiekejo_planas` | `string` | — | `4` | `open` | — | Tiekėjo plano pavadinimas | — |
| `eso_planas` | `string` | — | `4` | `open` | — | ESO plano pavadinimas | — |
| `laiko_zonu_sk` | `integer` | — | `4` | `open` | — | Laiko zonų skaičius | — |
| `zalioji_energija` | `boolean` | — | `4` | `open` | — | Ar naudojama žalioji energija | — |
| `plano_trukme_men` | `integer` | `mo` | `4` | `open` | — | Plano trukmė, mėnesiais | — |
| `tiekim_atidet_iki` | `date` | `M` | `4` | `open` | — | Tiekimas atidėtas iki | — |
| `tiek_1lz_kwh_kaina` | `number` | — | `4` | `open` | — | Tiekėjo kaina už vieną kilovatvalandę vienai laiko zonai | — |
| `tiek_2lz_dien_kwh_kaina` | `number` | — | `4` | `open` | — | Tiekėjo kaina už vieną kilovatvalandę dienos laiko zonai, kai yra dvi laiko zonos | — |
| `tiek_2lz_nakt_kwh_kaina` | `number` | — | `4` | `open` | — | Tiekėjo kaina už vieną kilovatvalandę nakties laiko zonai, kai yra dvi laiko zonos | — |
| `tiek_nordpool_kwh_kaina` | `number` | — | `4` | `open` | — | Tiekėjo kaina už vieną kilovatvalandę, kai naudojamas biržos planas | — |
| `tiek_men_kaina` | `number` | — | `4` | `open` | — | Tiekėjo mėnesinis mokestis už planą | — |
| `zal_energ_tiek_kwh_kaina` | `number` | — | `4` | `open` | — | Tiekėjo kaina už vieną žaliosios energijos kilovatvalandę | — |
| `zal_energ_tiek_men_kaina` | `number` | — | `4` | `open` | — | Tiekėjo mėnesinis mokestis už žaliąją energiją | — |
| `nuolaida_per_men` | `number` | — | `4` | `open` | — | Nuolaida per mėnesį | — |
| `nuolaidos_per_men_trukme` | `integer` | `mo` | `4` | `open` | — | Nuolaidos per mėnesį trukmė | — |
| `kwh_nuolaida` | `number` | — | `4` | `open` | — | Nuolaida kilovatvalandžių skaičiui | — |
| `vienkartine_nuolaida` | `number` | — | `4` | `open` | — | Vienkartinės nuolaidos dydis | — |
| `eso_plano_men_kaina` | `number` | — | `4` | `open` | — | ESO plano mėnesinis mokestis | — |
| `lz1_persiunt_kwh_kaina` | `number` | — | `4` | `open` | — | Vienos kilovatvalandės persiuntimo kaina vienai laiko zonai | — |
| `lz2_dien_persiunt_kwh_kaina` | `number` | — | `4` | `open` | — | Vienos kilovatvalandės persiuntimo kaina dviems laiko zonoms dieną | — |
| `lz2_nakt_persiunt_kwh_kaina` | `number` | — | `4` | `open` | — | Vienos kilovatvalandės persiuntimo kaina dviems laiko zonoms naktį | — |
| `lz4_ryto_persiunt_kwh_kaina` | `number` | — | `4` | `open` | — | Vienos kilovatvalandės persiuntimo kaina keturioms laiko zonoms ryte | — |
| `lz4_dien_persiunt_kwh_kaina` | `number` | — | `4` | `open` | — | Vienos kilovatvalandės persiuntimo kaina keturioms laiko zonoms dieną | — |
| `lz4_vak_persiunt_kwh_kaina` | `number` | — | `4` | `open` | — | Vienos kilovatvalandės persiuntimo kaina keturioms laiko zonoms vakare | — |
| `lz4_nakt_persiunt_kwh_kaina` | `number` | — | `4` | `open` | — | Vienos kilovatvalandės persiuntimo kaina keturioms laiko zonoms naktį | — |
| `skirstymo_kaina_kwh` | `number` | — | `4` | `open` | — | Vienos kilovatvalandės skirstymo kaina | — |
| `viap_kaina` | `number` | — | `4` | `open` | — | Viešuosius interesus atitinkančių paslaugų kaina | — |
| `papildomos_naudos` | `boolean` | — | `4` | `open` | — | Papildomos naudos | — |
| `papildoma_info` | `string` | — | `4` | `open` | — | Papildoma informacija | — |
| `vda_ingest_time` | `date` | `D` | `4` | `open` | — | Duomenų gavimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `laiko_zonu_sk` | `1` | — | — | Viena laiko zona | — |
| `laiko_zonu_sk` | `2` | — | — | Dvi laiko zonos | — |
| `laiko_zonu_sk` | `4` | — | — | Keturios laiko zonos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vert/neprikl_ee_tiek_planai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vert/neprikl_ee_tiek_planai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vert/neprikl_ee_tiek_planai (https://data.gov.lt/datasets/2802/)
