---
type: Table
title: "Patalpa — Vilniaus miesto savivaldybės nuomojamos patalpos"
description: "Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Patalpa"
tags: [gov, vilniaus_m_sav, patalpa, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3859/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/patalpos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Patalpa — Vilniaus miesto savivaldybės nuomojamos patalpos

**Dataset Context:** Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos. Platformoje kaupiama informacija apie nuomojamus aktyvaus laisvalaikio objektus: sporto ir aktų sales, kabinetus, žaidimo ir sporto aikšteles bei kita. Šias laisvalaikio zonas nuomoti gali fiziniai bei juridiniai asmenys. Rinkinyje pateikiami duomenys apie nuomojamas patalpas, nuomotojus, esamus ir buvusius nuomininkus bei išrašytas sąskaitas-faktūras už naudojimąsi paslaugomis. Nuomos įkainiai ir mokėtinos sumos sąskaitose už suteiktas paslaugas nėra skelbiami, tačiau viešinamas reitingas, kur mokėtinos sumos išrikiuojamos eilės tvarka nuo didžiausios iki mažiausios. Sutarčių ir sąskaitų duomenys skelbiami nuo 2020m. liepos mėnesio iki šių dienų. Duomenų teikėjas: Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/patalpos/Patalpa`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys](../patalpos.md) (`datasets/gov/vilniaus_m_sav/patalpos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/patalpos.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Patalpa` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `patalpos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patalpos_id` | `string` | — | `4` | `open` | — | Patalpos identifikacinis numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Patalpos pavadinimas | — |
| `aprasymas_lt` | `string` | — | `2` | `open` | — | Patalpos aprašymas | — |
| `vietos_tipas` | `string` | — | `4` | `open` | — | Patalpos vietos tipas | — |
| `patalpos_tipas` | `string` | — | `4` | `open` | — | Patalpos tipas | — |
| `adresas` | `string` | — | `4` | `open` | — | Patalpos adresas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Patalpos adreso koordinatės (LKS) | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | Patalpos adreso ilgumos koordinatė | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Patalpos adreso platumos koordinatė | — |
| `istaiga_savininke` | `string` | — | `4` | `open` | — | Patalpų savininkas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Patalpų savininko JAR kodas | — |
| `jar_kodas_validus` | `boolean` | — | `4` | `open` | — | JAR kodo validacijos požymis | — |
| `plotas_kv_m` | `number` | `m²` | `4` | `open` | — | Patalpų plotas, nurodytas kvadratiniais metrais | — |
| `statybos_data` | `date` | `D` | `4` | `open` | — | Pastato statybos data | — |
| `talpina_zmoniu` | `integer` | `U` | `4` | `open` | — | Nurodomas patalpoje telpančių asmenų skaičius | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Patalpos duomenų atnaujinimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vietos_tipas` | `"Vidaus patalpa"` | — | — | — | — |
| `vietos_tipas` | `"Lauko erdve"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L10)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/patalpos (https://data.gov.lt/datasets/3859/)
