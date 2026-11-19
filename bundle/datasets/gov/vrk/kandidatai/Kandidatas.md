---
type: Table
title: "Kandidatas"
description: "Spinta table datasets/gov/vrk/kandidatai/Kandidatas (28 columns)."
tags: [gov, vrk, kandidatas, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/kandidatai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vrk/kandidatai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kandidatas

- **Model:** `datasets/gov/vrk/kandidatai/Kandidatas`[^manifest]
- **Dataset:** [datasets/gov/vrk/kandidatai](../kandidatai.md) (`datasets/gov/vrk/kandidatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/kandidatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/kandidatai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `kandidato_id`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rinkimu_id` | `integer` | — | `2` | `open` | — | Rinkimų identifikatorius | — |
| `rinkimu_pavad` | `string` | — | `2` | `open` | — | Rinkimų pavadinimas | — |
| `rink_apyg_id` | `integer` | — | `2` | `open` | — | Rinkimų apygardos identifikatorius | — |
| `apyg_id` | `integer` | — | `2` | `open` | — | Apygardos identifikatorius | — |
| `apyg_nr` | `integer` | — | `2` | `open` | — | Apygardos numeris | — |
| `apyg_pavad` | `string` | — | `2` | `open` | — | Apygardos pavadinimas | — |
| `p_kamp_dal_id` | `integer` | — | `2` | `open` | — | Politinės kampanijos dalyvio identifikatorius | Politinės kampanijos dalyvio ID |
| `p_kamp_dal_pavad` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvis | Politinės kampanijos dalyvio pavadinimas |
| `dal_tipas` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvio tipas | Politinės kampanijos dalyvio tipas (Politinė partija / Politinės partijos keltas kandidatų sąrašas / Visuomeninis rinkimų komitetas/ Išsikėlęs kandidatas) |
| `dal_reg_busena` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvio registravimo būsena | Dalyvio registravimo būsena (Registruotas / Praradęs statusą) |
| `ja_kodas` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvio juridinio asmens kodas Juridinių asmenų registre | — |
| `kandidato_id` | `integer` | — | `4` | `open` | — | Kandidato identifikatorius | — |
| `rink_kandidato_id` | `integer` | — | `4` | `open` | — | Kandidato identifikatorius rinkimuose | — |
| `vardas` | `string` | — | `3` | `open` | — | Kandidato vardas | — |
| `pavarde` | `string` | — | `3` | `open` | — | Kandidato pavardė | — |
| `lytis` | `string` | — | `4` | `open` | — | Kandidato lytis | Kandidato lytis (V/M) |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Kandidato amžiaus grupė (rinkimų dieną) | Kandidato amžiaus grupė rinkimų dieną intervalais (nuo - iki), kas 5 metai Amžiaus grupės: 18-24; 25-29; 30-34; 35-39; ....; 75-79; 80 +; |
| `v_org_id` | `integer` | — | `2` | `open` | — | Kandidatą vienmandatėje apygardoje iškėlusios organizacijos identifikatorius | — |
| `v_org_pavad` | `string` | — | `2` | `open` | — | Kandidatą vienmandatėje apygardoje iškėlusios organizacijos pavadinimas | — |
| `v_org_ja_kodas` | `string` | — | `2` | `open` | — | Kandidatą vienmandatėje apygardoje iškėlusios organizacijos juridinio asmens kodas Juridinių asmenų registre | — |
| `v_ar_pats` | `string` | — | `2` | `open` | — | Požymis ar kandidatas vienmandatėje apygardoje išsikėlė pats | Požymis ar kandidatas vienmandatėje apygardoje išsikėlė pats (T) |
| `d_org_id` | `integer` | — | `2` | `open` | — | Kandidatą daugiamandatėje apygardoje iškėlusios organizacijos identifikatorius | — |
| `d_org_pavad` | `string` | — | `2` | `open` | — | Kandidatą daugiamandatėje apygardoje iškėlusios organizacijos pavadinimas | — |
| `d_org_ja_kodas` | `string` | — | `2` | `open` | — | Kandidatą daugiamandatėje apygardoje iškėlusios organizacijos juridinio asmens kodas Juridinių asmenų registre | — |
| `saraso_id` | `integer` | — | `2` | `open` | — | Kandidatų sąrašo (rinkimų organizacijos), keliamo daugiamandatėje apygardoje identifikatorius | — |
| `saraso_nr` | `integer` | — | `2` | `open` | — | Kandidatų sąrašo numeris | Kandidatų sąrašo, keliamo daugiamandatėje apygardoje, numeris |
| `saraso_pavad` | `string` | — | `2` | `open` | — | Kandidatų sąrašo pavadinimas | Kandidatų sąrašo, keliamo daugiamandatėje apygardoje, pavadinimas |
| `saraso_ja_kodas` | `string` | — | `2` | `open` | — | Kandidatų sąrašo juridinio asmens kodas Juridinių asmenų registre | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dal_tipas` | `"Fizinis asmuo"` | — | — | Fizinis asmuo | — |
| `dal_tipas` | `"Kandidatas ar kandidatų sąrašas, kai yra juos iškėlusios partijos teikimas"` | — | — | Kandidatas ar kandidatų sąrašas, kai yra juos iškėlusios partijos teikimas | — |
| `dal_tipas` | `"Kandidatas ar kandidatų sąrašas, kai nėra juos iškėlusios partijos teikimo"` | — | — | Kandidatas ar kandidatų sąrašas, kai nėra juos iškėlusios partijos teikimo | — |
| `dal_tipas` | `"Politinė partija"` | — | — | Politinė partija | — |
| `dal_tipas` | `"Politinės partijos iškeltas kandidatas"` | — | — | Politinės partijos iškeltas kandidatas | — |
| `dal_tipas` | `"Pretendentas"` | — | — | Pretendentas | — |
| `dal_tipas` | `"Referendumo iniciatoriai"` | — | — | Referendumo iniciatoriai | — |
| `dal_tipas` | `"Rinkimų organizacija"` | — | — | Rinkimų organizacija | — |
| `dal_tipas` | `"Save iškėlęs kandidatas"` | — | — | Save iškėlęs kandidatas | — |
| `dal_reg_busena` | `"Atstovaujamasis"` | — | — | Atstovaujamasis | — |
| `dal_reg_busena` | `"Praradęs PKD statusą"` | — | — | Praradęs PKD statusą | — |
| `dal_reg_busena` | `"Registruotas"` | — | — | Registruotas | — |
| `dal_reg_busena` | `"Savarankiškas"` | — | — | Savarankiškas | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `amziaus_grupe` | `"18-24"` | — | — | Amžiaus grupė nuo 18 iki 24 metų | — |
| `amziaus_grupe` | `"25-29"` | — | — | Amžiaus grupė nuo 25 iki 29 metų | — |
| `amziaus_grupe` | `"30-34"` | — | — | Amžiaus grupė nuo 30 iki 34 metų | — |
| `amziaus_grupe` | `"35-39"` | — | — | Amžiaus grupė nuo 35 iki 39 metų | — |
| `amziaus_grupe` | `"40-44"` | — | — | Amžiaus grupė nuo 40 iki 44 metų | — |
| `amziaus_grupe` | `"45-49"` | — | — | Amžiaus grupė nuo 45 iki 49 metų | — |
| `amziaus_grupe` | `"50-54"` | — | — | Amžiaus grupė nuo 50 iki 54 metų | — |
| `amziaus_grupe` | `"55-59"` | — | — | Amžiaus grupė nuo 55 iki 59 metų | — |
| `amziaus_grupe` | `"60-64"` | — | — | Amžiaus grupė nuo 60 iki 64 metų | — |
| `amziaus_grupe` | `"65-69"` | — | — | Amžiaus grupė nuo 65 iki 69 metų | — |
| `amziaus_grupe` | `"70-74"` | — | — | Amžiaus grupė nuo 70 iki 74 metų | — |
| `amziaus_grupe` | `"75-79"` | — | — | Amžiaus grupė nuo 75 iki 79 metų | — |
| `amziaus_grupe` | `"80+"` | — | — | Amžiaus grupė nuo 80 metų | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/kandidatai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/kandidatai.csv#L4)
