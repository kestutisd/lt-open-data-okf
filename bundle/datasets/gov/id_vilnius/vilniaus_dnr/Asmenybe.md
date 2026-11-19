---
type: Table
title: "Asmenybe — Mieste įamžintos asmenybės"
description: "\"Duomenys iš „ID Vilnius“ apie asmenybes, kurioms Vilniaus mieste įrengtos atminimo lentos, skulptūros, paminklai ar jų vardais pavadintos gatvės."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/Asmenybe"
tags: [gov, id_vilnius, asmenybe, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L20"
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L20"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Asmenybe — Mieste įamžintos asmenybės

"Duomenys iš „ID Vilnius“ apie asmenybes, kurioms Vilniaus mieste įrengtos atminimo lentos, skulptūros, paminklai ar jų vardais pavadintos gatvės. Viena lentelės eilutė atitinka informaciją apie vieną asmenybę. Eilutėje esančią informaciją sudaro: asmenybės vardas ir pavardė, slapyvardis(-džiai), pagrindinė šnekamoji kalba, gimimo ir mirties datos ir vietos, požymis, nurodantis, ar asmenybei pastatyta atminimo lenta, atminimo lentos lokacija, prieinamumas, asmenybės profesija, kūryba, ryšys su Vilniumi, apdovanojimai, nuotrauka bei jos aprašymas ir šaltinis, iš kurio gauta informacija apie asmenybę. Paskutiniuose keturiuose stulpeliuose pateikiamas asmenybės vardas ir pavardė kitomis kalbomis."[^manifest]

- **Model:** `datasets/gov/id_vilnius/vilniaus_dnr/Asmenybe`[^manifest]
- **Dataset:** [Vilniaus miesto istoriniai duomenys - Vilniaus DNR](../vilniaus_dnr.md) (`datasets/gov/id_vilnius/vilniaus_dnr`)[^manifest]
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L20)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/Asmenybe` (`deployed`)[^manifest]
- **Provider:** `id_vilnius`[^manifest]
- **Primary Key (`ref`):** `asmenybes_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `asmenybes_id` | `string` | — | `4` | `open` | — | Sisteminis asmenybės identifikacinis numeris (pirminis raktas) | — |
| `var_pavar` | `string` | — | `4` | `open` | — | Asmenybės vardas ir pavardė lietuvių kalba | — |
| `slapyvardis` | `string` | — | `4` | `open` | — | Asmenybės slapyvardis(-džiai) | — |
| `pagr_kalba` | `string` | — | `4` | `open` | — | Asmenybės pagrindinė šnekamoji kalba | — |
| `gimimo_data_text` | `string` | — | `3` | `open` | — | Gimimo arba krikšto data tekstiniu formatu | — |
| `gimimo_data_form` | `date` | `D` | `4` | `open` | — | Suformatuota gimimo arba krikšto data datos tipo formatu iš tekstinio gimimo datos laukelio | — |
| `gimimo_vieta` | `string` | — | `4` | `open` | — | Asmenybės gimimo vieta | — |
| `mirties_data_text` | `string` | — | `3` | `open` | — | Mirties data tekstiniu formatu | — |
| `mirties_data_form` | `date` | `D` | `4` | `open` | — | Mirties data datos tipo formatu gauta iš tekstinio mirties datos stulpelio | — |
| `mirties_vieta` | `string` | — | `4` | `open` | — | "Miestas arba šalis, kurioje asmenybė mirė" | — |
| `kapines` | `string` | — | `4` | `open` | — | "Kapinės, kurios palaidota asmenybė" | — |
| `palaid_vieta` | `string` | — | `4` | `open` | — | Palaidojimo vieta žemėlapyje | — |
| `ar_yra_lenta` | `boolean` | — | `4` | `open` | — | "Požymis, nurodantis ar asmenybei turi atminimo lentą" | — |
| `lentos_prieinamumas` | `string` | — | `4` | `open` | — | Atminimo lentos prieinamumas | — |
| `lentos_adresas` | `string` | — | `4` | `open` | — | Atminimo lentos adresas | — |
| `profesija` | `string` | — | `4` | `open` | — | Asmens profesija | — |
| `kuryba` | `string` | — | `4` | `open` | — | Asmens kūryba | "Asmens kūryba arba veikla, kuri įamžino asmenybę" |
| `rys_su_vln` | `string` | — | `4` | `open` | — | Asmenybės ryšys su Vilniumi | — |
| `apdovanojimai` | `string` | — | `4` | `open` | — | Asmenybės apdovanojimai | "Apdovanojimai, kuriuos gavo asmenybė" |
| `nuotrauka` | `string` | — | `4` | `open` | — | Asmenybės nuotrauka | — |
| `nuotraukos_aprasymas` | `string` | — | `4` | `open` | — | Nuotraukos aprašymas | — |
| `saltinis` | `string` | — | `4` | `open` | — | Faktų apie asmenybę šaltinis | — |
| `var_pavar_kt_kalba` | `string` | — | `4` | `open` | — | Vardas ir pavardė kita kalba | — |
| `var_pavar_ang` | `string` | — | `4` | `open` | — | Vardas ir pavardė anglų kalba | — |
| `var_pavar_len` | `string` | — | `4` | `open` | — | Vardas ir pavardė lenkų kalba | — |
| `var_pavar_ru` | `string` | — | `4` | `open` | — | Vardas ir pavardė rusų kalba | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L20 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L20)
