---
type: Table
title: "KursoGrupe — MVG kursų duomenys"
description: "Lentelėje pateikiami projekte „Mokykis visą gyvenimą!“ (MVG) vykdomus kursus."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/mvg_programa/KursoGrupe"
tags: [gov, lamabpo, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/mvg_programa.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/mvg_programa.csv#L21"
    last_modified: "2026-11-11T14:39:20Z"
---

# KursoGrupe — MVG kursų duomenys

Lentelėje pateikiami projekte „Mokykis visą gyvenimą!“ (MVG) vykdomus kursus. Kiekviena eilutė atitinka vieną kursų grupę. Eilutėje pateikiama informacija apima: kursų grupės identifikacinį numerį, dabartinį bei maksimalų grupės dydį, kursų pradžios ir pabaigos datas, mokymosi būdą, kalbą, tiekėjo JAR kodą su jo validacijos požymiu ir, priklausomai nuo mokymosi būdo, kursų teikėjo arba vykdomų kursų, vietos adresą. Taip pat nurodytos WGS koordinatės, žyminčios adresą. Be to, pateikiama kursų švietimo sritis, posritis, paskirtis, profesijos tipas ir požymiai, nurodantys, ar kursai yra aukštos pridėtinės vertės programos dalis, skaitmeninė programa ar pritaikyti mokiniams, turintiems klausos, regėjimo, intelekto ar judėjimo sutrikimų.

- **Model:** `datasets/gov/lamabpo/mvg_programa/KursoGrupe`[^manifest]
- **Dataset:** [Projekto „Mokykis visą gyvenimą!“ dalyvių ir kursų duomenys](../mvg_programa.md) (`datasets/gov/lamabpo/mvg_programa`)
- **Manifest CSV:** [datasets/gov/lamabpo/mvg_programa.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/mvg_programa.csv#L21)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/mvg_programa/KursoGrupe`
- **Primary Key (`ref`):** `kursu_grupes_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kursu_grupes_id` | `string` | — | `4` | `open` | — | Kursų grupės identifikacinis numeris | — |
| `dabartinis_grupes_dydis` | `integer` | — | `4` | `open` | — | Dabartinis grupės dydis | — |
| `maks_grupes_dydis` | `integer` | — | `4` | `open` | — | Maksimalus grupės dydis | — |
| `pradzios_data` | `date` | `D` | `4` | `open` | — | Kurso pradžios data | — |
| `pabaigos_data` | `date` | `D` | `4` | `open` | — | Kurso pabaigos data | — |
| `mokymosi_budas` | `string` | — | `4` | `open` | — | Kurso mokymosi būdas | — |
| `kalba` | `string` | — | `4` | `open` | — | Kalba | Kalba, kuria vykdomi kursai |
| `mokymo_teikejas` | `string` | — | `4` | `open` | — | Mokymų tiekėjas | Kursų tiekėjo juridinio asmens kodas (JAR) |
| `validus_jar` | `string` | — | `4` | `open` | — | JAR kodo validacija | Stulpelis, kuriame nustatoma ar JAR kodas yra validus. Validumas nustatomas tik lietuviškom įstaigom |
| `mokymosi_adresas` | `string` | — | `4` | `open` | — | Mokymosi adresas | Adresas, kuriame vykdomi kursai, esant kontaktiniam mokymosi būdui, arba kursų tiekėjo adresas, esant nuotoliniam mokymosi būdui |
| `geometrija_wgs` | `geometry(4326)` | — | `4` | `open` | — | WGS geometrinis taškas | Stulpelis, kuris nurodo mokymosi adreso WGS koordinates |
| `geo_tikslumas` | `number` | — | `4` | `open` | — | Geometrijos tikslumas | Stulpelis, kuris nurodo koordinačių tikslumą procentinėje skalėje. Esant tikslumui daugiau nei 90 %, laikoma, kad koordinatės yra tikslios |
| `svietimo_sritis` | `string` | — | `4` | `open` | — | Švietimo sritis | Švietimo sritis, kuriai priklauso kurso programa |
| `svietimo_posritis` | `string` | — | `4` | `open` | — | Švietimo posritis | Švietimo posritis, kuriai priklauso kursų programa |
| `aukstos_vertes_prog` | `boolean` | — | `4` | `open` | — | Aukštos pridėtinės vertės programa | Požymis, nurodantis, ar kursai yra priskirti prie aukštą pridėtinę vertę kuriančių programų |
| `paskirtis` | `string` | — | `4` | `open` | — | Kursų programos paskirtis | — |
| `profesijos_tipas` | `string` | — | `4` | `open` | — | Kursų profesijos tipas | — |
| `skaitmenine_programa` | `boolean` | — | `4` | `open` | — | Skaitmeninė programa | Požymis, nurodantis, ar kursai priskiriami prie skaitmeninės programos |
| `klausos_sutrikimai` | `boolean` | — | `4` | `open` | — | Klausos sutrikimai | Požymis, nurodantis, ar kursai pritaikyti klausos sutrikimų turintiems mokiniams |
| `intelekto_sutrikimai` | `boolean` | — | `4` | `open` | — | Intelekto sutrikimai | Požymis, nurodantis, ar kursai pritaikyti intelekto sutrikimų turintiems mokiniams |
| `judejimo_sutrikimai` | `boolean` | — | `4` | `open` | — | Judėjimo sutrikimai | Požymis, nurodantis, ar kursai pritaikyti judėjimo sutrikimų turintiems mokiniams |
| `regos_sutrikimai` | `boolean` | — | `4` | `open` | — | Regos sutrikimai | Požymis, nurodantis, ar kursai pritaikyti regos sutrikimų turintiems mokiniams |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `mokymosi_budas` | — | `"Nuotolinis sinchroninis"` | — | Nuotolinis sinchroninis | — |
| `mokymosi_budas` | — | `"Kontaktinis"` | — | Kontaktinis | — |
| `validus_jar` | — | `"Tinkamas"` | — | Tinkamas | — |
| `validus_jar` | — | `"Netinkamas ilgis"` | — | Netinkamas ilgis | — |
| `validus_jar` | — | `"Netinkamas kontrolinis skaitmuo"` | — | Netinkamas kontrolinis skaitmuo | — |
| `validus_jar` | — | `"Yra ne skaitmenų"` | — | Yra ne skaitmenų | — |
| `validus_jar` | — | `"Tuščia reikšmė"` | — | Tuščia reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/mvg_programa.csv
