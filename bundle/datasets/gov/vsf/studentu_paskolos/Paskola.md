---
type: Table
title: "Paskola — Studentų paskolų informacija"
description: "Duomenų rinkinyje pateikiami studentų paskolų paraiškų anketų ir išduotų paskolų duomenys, kuriuos teikia Valstybinis studijų fondas (https://vsf.lrv.lt/)."
resource: "https://get.data.gov.lt/datasets/gov/vsf/studentu_paskolos/Paskola"
tags: [gov, vsf, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsf/studentu_paskolos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsf/studentu_paskolos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paskola — Studentų paskolų informacija

Duomenų rinkinyje pateikiami studentų paskolų paraiškų anketų ir išduotų paskolų duomenys, kuriuos teikia Valstybinis studijų fondas (https://vsf.lrv.lt/). Rinkinyje nurodytos paskolos, suteiktos 1998–2013 m. Kiekviena rinkinio eilutė atitinka vieną unikalią studentui suteiktą paskolą. Rinkinį sudaro anketos duomenys, kuriuose nurodoma studento mokymosi įstaiga ir pateikiama šifruota asmeninė informacija, bei suteiktų paskolų duomenys, kuriuose nurodoma paskolos suma, jos grąžinimo terminai ir nustatyti delspinigiai.

- **Model:** `datasets/gov/vsf/studentu_paskolos/Paskola`[^manifest]
- **Dataset:** [Studentų paskolų informacija](../studentu_paskolos.md) (`datasets/gov/vsf/studentu_paskolos`)
- **Manifest CSV:** [datasets/gov/vsf/studentu_paskolos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsf/studentu_paskolos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vsf/studentu_paskolos/Paskola`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus indentifikatorius | — |
| `mokykla_pavadinimas` | `string` | — | `4` | `open` | — | Aukštosios mokyklos ar kitos mokymosi įstaigos oficialus pavadinimas. | — |
| `mokykla_trump_pavadinimas` | `string` | — | `4` | `open` | — | Mokymosi įstaigos trumpinys arba santrumpa. | — |
| `fakultetas_pavadinimas` | `string` | — | `4` | `open` | — | Fakulteto, kuriame studijuoja asmuo, pavadinimas. | — |
| `vda_asmens_kodas` | `string` | — | `4` | `open` | — | Anonimizuotas (užšifruotas) asmens identifikatorius | — |
| `vda_asm_k_validacija` | `string` | — | `4` | `open` | — | Požymis, nurodantis ar asmens kodas atitinka validacijos taisykles. | — |
| `lytis` | `string` | — | `4` | `open` | — | Asmens lytis | — |
| `salis` | `string` | — | `4` | `open` | — | Asmens gimtoji šalis | — |
| `miestas` | `string` | — | `4` | `open` | — | Asmens deklaruotos ar gyvenamosios vietos gyvenvietės pavadinimas. | — |
| `kursas` | `integer` | — | `4` | `open` | — | Studijų kurso numeris (pvz., 1, 2, 3 ir pan.). | — |
| `studiju_forma` | `string` | — | `4` | `open` | — | Studijų forma (pvz., deininis, ištęstinis ir kt.) | — |
| `studiju_pakopa` | `string` | — | `4` | `open` | — | Asmens studijų pakopos pavadinimas | — |
| `paskolos_rusis` | `string` | — | `4` | `open` | — | Suteiktos paskolos tipas (pvz., studijų, gyvenimo išlaidų ir pan.). | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Anonimizuotas (užšifruotas) paskolos sutarties identifikacinis numeris. | — |
| `sutarties_data` | `date` | `D` | `4` | `open` | — | Data, kada buvo pasirašyta paskolos sutartis. | — |
| `suma_eur` | `number` | — | `4` | `open` | — | Sutartyje numatyta paskolos suma eurais. | — |
| `suma_lt` | `number` | — | `4` | `open` | — | Sutartyje numatyta paskolos suma litais. | — |
| `pask_graz_pradzia` | `date` | `D` | `4` | `open` | — | Data, nuo kurios pradedamas paskolos grąžinimas. | — |
| `pask_graz_pabaiga` | `date` | `D` | `4` | `open` | — | Planuojama paskolos grąžinimo termino pabaigos data. | — |
| `palukanu_norma` | `number` | — | `4` | `open` | — | Metinė paskolos palūkanų norma procentais. | — |
| `delspinigiu_norma` | `number` | — | `4` | `open` | — | Taikoma delspinigių norma procentais už pradelstus mokėjimus. | — |
| `nurasyta_suma` | `number` | — | `4` | `open` | — | Paskolos suma arba dalis, kuri buvo nurašyta. | — |
| `busena` | `string` | — | `4` | `open` | — | Paskolos požymio reikšmės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsf/studentu_paskolos.csv
