---
type: Table
title: "MedicinosPriemone — Brangių medicinos priemonių sąrašas"
description: "Spinta table datasets/gov/vaspvt/priemones/MedicinosPriemone (32 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/priemones/MedicinosPriemone"
tags: [gov, vaspvt, medicinospriemone, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2310/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/priemones"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MedicinosPriemone — Brangių medicinos priemonių sąrašas

- **Model:** `datasets/gov/vaspvt/priemones/MedicinosPriemone`[^manifest]
- **Dataset:** [Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys](../priemones.md) (`datasets/gov/vaspvt/priemones`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/medicinos_iranga.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/priemones/MedicinosPriemone` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | kodas | — |
| `numeris` | `string` | — | `4` | `open` | — | Priemonės Nr. | — |
| `pagaminta` | `date` | `D` | `4` | `open` | — | Pagaminimo data | — |
| `naudojimo_pradzia` | `date` | `D` | `4` | `open` | — | Naudojimo pradžios data | — |
| `naudojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Naudojimo pabaigos data | — |
| `isigyta` | `date` | `D` | `4` | `open` | — | Įsigijimo data | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `ce_numeris` | `boolean` | — | `3` | `open` | — | CE numeris | — |
| `naudojimo_vieta` | `string` | — | `1` | `open` | — | Naudojimo vieta (skyrius) | — |
| `serijos_numeris` | `string` | — | `4` | `open` | — | Serijos/partijos Nr. | — |
| `aprobavimo_dok` | `boolean` | — | `3` | `open` | — | Aprobavimo dokumento Nr. | — |
| `skyrius` | `string` | — | `2` | `open` | — | Filialas | — |
| `teisine_forma` | `string` | — | `2` | `open` | — | Teisinė forma | — |
| `istaigos_nr` | `string` | — | `2` | `open` | — | Paskelbtosios įstaigos Nr. | — |
| `kaina_su_priedais` | `number` | — | `2` | `open` | — | Priemonės įsigijimo kaina su priedais | — |
| `kaina_be_priedu` | `number` | — | `2` | `open` | — | Priemonės įsigijimo kaina be priedų | — |
| `instaliavimo_kaina` | `number` | — | `2` | `open` | — | Priemones instaliavimo kaina | — |
| `planiniai_bukles_tikrinimai` | `date` | `D` | `4` | `open` | — | Planuojamos techninės būklės tikrinimo data | — |
| `paskutinis_bukles_tikrinimas` | `date` | `D` | `4` | `open` | — | Paskutinės techninės būklės tikrinimo data | — |
| `istaigos_pavadinimas` | `string` | — | `2` | `open` | — | Įstaigos pavadinimas | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Įstaigos juridinio asmens kodas | — |
| `modelis` | `string` | — | `4` | `open` | — | Tipas/Modelis | — |
| `pristatymas` | `date` | `D` | `4` | `open` | — | Pateikimo data | — |
| `bukle` | `string` | — | `4` | `open` | — | Būsena | — |
| `institucijos_kodas` | `string` | — | `2` | `open` | — | Įstaigos juridinio asmens kodas | — |
| `priemones_rusis` | `string` | — | `4` | `open` | — | Med. priemonės tipas | — |
| `pirminis_auditas` | `date` | `D` | `4` | `open` | — | Pirmojo audito data | — |
| `pakartotinas_auditas` | `date` | `D` | `4` | `open` | — | Pakartotinioi audito laikas | — |
| `gamintojo_kodas` | `string` | — | `2` | `open` | — | Gamintojo pavadinimas | — |
| `gamintojo_salis` | `string` | — | `2` | `open` | — | Gamintojo šalies kodas | — |
| `gamintojas` | `string` | — | `2` | `open` | — | Gamintojas | — |
| `atnaujinta` | `date` | `D` | `4` | `open` | — | Atnaujinta | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `bukle` | `"1"` | — | — | Naudojamas | — |
| `bukle` | `"2"` | — | — | Laikinai nenaudojamas | — |
| `bukle` | `"3"` | — | — | Nurašytas | — |
| `bukle` | `"4"` | — | — | Panaikintas | — |
| `priemones_rusis` | `"1"` | — | — | Diagnostinis Ultragarsinis Prietaisas | — |
| `priemones_rusis` | `"2"` | — | — | Diagnostinė Rentgeno Įranga | — |
| `priemones_rusis` | `"3"` | — | — | Kompiuterinis Tomografas | — |
| `priemones_rusis` | `"4"` | — | — | Mamografas | — |
| `priemones_rusis` | `"5"` | — | — | Magnetinio Rezonanso Tomografas | — |
| `priemones_rusis` | `"6"` | — | — | Angiografas | — |
| `priemones_rusis` | `"7"` | — | — | Linijinis Greitintuvas | — |
| `priemones_rusis` | `"8"` | — | — | Gama Kamera | — |
| `priemones_rusis` | `"9"` | — | — | Pozitronų Emisijos Tomografas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", ref: "ja_kodas")` | `base` | `4` | `open` | — | — | — |
| `kaina_su_priedais` | `update(type:"money", ref:"EUR")` | `type` | `4` | `open` | — | — | — |
| `kaina_be_priedu` | `update(type:"money", ref:"EUR")` | `type` | `4` | `open` | — | — | — |
| `instaliavimo_kaina` | `update(type:"money", ref:"EUR")` | `type` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/priemones (https://data.gov.lt/datasets/2310/)
