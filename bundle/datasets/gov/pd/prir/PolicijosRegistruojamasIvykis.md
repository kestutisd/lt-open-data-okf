---
type: Table
title: "PolicijosRegistruojamasIvykis"
description: "Spinta table datasets/gov/pd/prir/PolicijosRegistruojamasIvykis (25 columns)."
tags: [gov, pd, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pd/prir.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/prir.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# PolicijosRegistruojamasIvykis

- **Model:** `datasets/gov/pd/prir/PolicijosRegistruojamasIvykis`[^manifest]
- **Dataset:** [datasets/gov/pd/prir](../prir.md) (`datasets/gov/pd/prir`)
- **Manifest CSV:** [datasets/gov/pd/prir.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/prir.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | ID numeris | — |
| `info_gavimo_laikas` | `datetime` | `T` | `4` | `open` | — | Informacijos gavimo laikas | — |
| `iregistravimo_data` | `datetime` | `T` | `4` | `open` | — | Įregistravimo data | — |
| `ivykio_data` | `datetime` | `T` | `4` | `open` | — | Įvykio data | — |
| `ivykio_data_iki` | `datetime` | `T` | `4` | `open` | — | Įvykio data iki | — |
| `kategorija` | `string` | — | `4` | `open` | — | Įvykio kategorija | — |
| `pranesimo_forma_kt` | `string` | — | `3` | `open` | — | Pranešimo forma | — |
| `create_date` | `datetime` | `T` | `4` | `open` | — | Sukūrimo data | — |
| `last_change_date` | `datetime` | `T` | `4` | `open` | — | Paskutinio redagavimo data | — |
| `teises_pazeidimo_pozymis` | `string` | — | `4` | `open` | — | Teisės pažeidimo požymis | — |
| `tipas1` | `string` | — | `4` | `open` | — | Įvykio tipas 1 | — |
| `tipas2` | `string` | — | `4` | `open` | — | Įvykio tipas 2 | — |
| `policijos_istaiga` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `2` | `open` | — | Policijos įstaiga | — |
| `policijos_istaigal2` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `2` | `open` | — | Policijos įstaiga 2 | — |
| `policijos_komisariatas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `2` | `open` | — | Policijos komisariatas | — |
| `pranesejo_statusas` | `string` | — | `4` | `open` | — | Pranešėjo statusas | — |
| `ar_dalyvauja_nepilnameciai` | `integer` | — | `4` | `open` | — | Ar dalyvauja nepilnamečiai | — |
| `vieta` | `string` | — | `3` | `open` | — | Įvykio vieta | — |
| `vieta2` | `string` | — | `3` | `open` | — | Detalesnė įvykio vieta | — |
| `valstybe` | `string` | — | `3` | `open` | — | Valstybė | — |
| `vietove` | `ref` | [/datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove[pavadinimas]](../../rc/ar/gyvenamojivietove/GyvenamojiVietove.md) | `2` | `open` | — | Vietovė | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe[pavadinimas]](../../rc/ar/savivaldybe/Savivaldybe.md) | `2` | `open` | — | Savivaldybė | — |
| `seniunija` | `ref` | [/datasets/gov/rc/ar/seniunija/Seniunija[pavadinimas]](../../rc/ar/seniunija/Seniunija.md) | `2` | `open` | — | Seniūnija | — |
| `gatve` | `ref` | [/datasets/gov/rc/ar/gatve/Gatve[pavadinimas]](../../rc/ar/gatve/Gatve.md) | `2` | `open` | — | Gatvė | — |
| `kertanti_gatve` | `ref` | [/datasets/gov/rc/ar/gatve/Gatve[pavadinimas]](../../rc/ar/gatve/Gatve.md) | `2` | `open` | — | Kertanti gatvė (sankryža) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kategorija` | `"A"` | — | — | A | Pranešimas apie rengiamą, daromą ar padarytą labai sunkų ar sunkų, apysunkį nusikaltimą, kai nukentėjusiojo gyvybei, sveikatai ar didelės vertės turtui gresia pavojus (nustatoma, kai reaguoti reikia labai skubiai). |
| `kategorija` | `"B"` | — | — | B | Pranešimas apie rengiamą, daromą ar padarytą sunkų, apysunkį ar nesunkų nusikaltimą arba kai nukentėjusiojo gyvybei ar sveikatai gali kilti pavojus, nėra informacijos apie nukentėjusiojo būklę, yra neteisėto turto pasisavinimo ar jo sunaikinimo pavojus, jeigu neturintis įgaliojimų asmuo sulaikė teisės pažeidėją, taip pat pranešimas apie chuliganiškus viešosios tvarkos pažeidimus, viešosios rimties trikdymą, kiti teisės pažeidimai, kai gali kilti pavojus žmonių gyvybei ar sveikatai (nustatoma, kai reaguoti reikia skubiai). |
| `kategorija` | `"C"` | — | — | C | Pranešimas apie rengiamą, daromą ar padarytą apysunkį, nesunkų nusikaltimą, baudžiamąjį nusižengimą ar įvykį ir kai asmens, kuriam reikalinga policijos pagalba, gyvybei, sveikatai arba jo didelės vertės turtui negresia pavojus, taip pat kai pranešama apie kitus teisės pažeidimus (nustatoma, kai skubiai reaguoti nereikia arba fiksuojamas informacinis policijos registruojamas įvykis). |
| `teises_pazeidimo_pozymis` | `"Administracinis nusižengimas"` | — | — | Administracinis nusižengimas | — |
| `teises_pazeidimo_pozymis` | `"Informacija nepasitvirtino"` | — | — | Informacija nepasitvirtino | — |
| `teises_pazeidimo_pozymis` | `"Kita"` | — | — | Kita | — |
| `teises_pazeidimo_pozymis` | `"Nusikalstama veika"` | — | — | Nusikalstama veika | — |
| `teises_pazeidimo_pozymis` | `"Tarnybinės drausmės pažeidimas"` | — | — | Tarnybinės drausmės pažeidimas | — |
| `tipas1` | `"Eismo saugumas"` | — | — | Eismo saugumas | — |
| `tipas1` | `"Ginklai, šaudmenys, sprogmenys"` | — | — | Ginklai, šaudmenys, sprogmenys | — |
| `tipas1` | `"Įvykiai susiję su valstybės tarnyba"` | — | — | Įvykiai susiję su valstybės tarnyba | — |
| `tipas1` | `"Kiti įvykiai"` | — | — | Kiti įvykiai | — |
| `tipas1` | `"Neklasifikuoti"` | — | — | Neklasifikuoti | — |
| `tipas1` | `"Nusikaltimai asmeniui"` | — | — | Nusikaltimai asmeniui | — |
| `tipas1` | `"Turtinė veika"` | — | — | Turtinė veika | — |
| `tipas1` | `"Viešosios tvarkos pažeidimai"` | — | — | Viešosios tvarkos pažeidimai | — |
| `tipas2` | `"Asmens paieška"` | — | — | Asmens paieška | — |
| `tipas2` | `"Eismo įvykis"` | — | — | Eismo įvykis | — |
| `tipas2` | `"Ekonominės ir verslo tvarkos veikos"` | — | — | Ekonominės ir verslo tvarkos veikos | — |
| `tipas2` | `"Ginklai, šaudmenys, karo laikų sprogmenys"` | — | — | Ginklai, šaudmenys, karo laikų sprogmenys | — |
| `tipas2` | `"Įtartini asmenys"` | — | — | Įtartini asmenys | — |
| `tipas2` | `"Įvairūs viešosios tvarkos pažeidimai"` | — | — | Įvairūs viešosios tvarkos pažeidimai | — |
| `tipas2` | `"Įvykiai susiję su policijos veikla"` | — | — | Įvykiai susiję su policijos veikla | — |
| `tipas2` | `"Kaliningrado tranzitas"` | — | — | Kaliningrado tranzitas | — |
| `tipas2` | `"KET pažeidimas"` | — | — | KET pažeidimas | — |
| `tipas2` | `"Lavonas"` | — | — | Lavonas | — |
| `tipas2` | `"Narkotinės medžiagos"` | — | — | Narkotinės medžiagos | — |
| `tipas2` | `"Neapykantos kalba ir neapykantos kurstymas"` | — | — | Neapykantos kalba ir neapykantos kurstymas | — |
| `tipas2` | `"Neigiama informacija internete"` | — | — | Neigiama informacija internete | — |
| `tipas2` | `"Neklasifikuoti"` | — | — | Neklasifikuoti | — |
| `tipas2` | `"Nusikaltimai asmeniui anksčiau"` | — | — | Nusikaltimai asmeniui anksčiau | — |
| `tipas2` | `"Nusikaltimai asmeniui dabar"` | — | — | Nusikaltimai asmeniui dabar | — |
| `tipas2` | `"Pagalba specialiosioms tarnyboms"` | — | — | Pagalba specialiosioms tarnyboms | — |
| `tipas2` | `"Pavojus eismo saugumui"` | — | — | Pavojus eismo saugumui | — |
| `tipas2` | `"Pavojus gyvybei"` | — | — | Pavojus gyvybei | — |
| `tipas2` | `"Rasti ar pamesti daiktai"` | — | — | Rasti ar pamesti daiktai | — |
| `tipas2` | `"Rinkimų tvarkos pažeidimai"` | — | — | Rinkimų tvarkos pažeidimai | — |
| `tipas2` | `"Smurtas artimoje aplinkoje"` | — | — | Smurtas artimoje aplinkoje | — |
| `tipas2` | `"Sprogimas ar sprogimo grėsmė"` | — | — | Sprogimas ar sprogimo grėsmė | — |
| `tipas2` | `"Turtinė veika anksčiau"` | — | — | Turtinė veika anksčiau | — |
| `tipas2` | `"Turtinė veika dabar"` | — | — | Turtinė veika dabar | — |
| `tipas2` | `"Valstybės tarnautojų korupcija"` | — | — | Valstybės tarnautojų korupcija | — |
| `pranesejo_statusas` | `"įmonės, įstaigos ar organizacijos atstovas"` | — | — | Įmonės, įstaigos ar organizacijos atstovas | — |
| `pranesejo_statusas` | `"kita"` | — | — | Kita | — |
| `pranesejo_statusas` | `"kitos teisėsaugos institucijos pareigūnas"` | — | — | Kitos teisėsaugos institucijos pareigūnas | — |
| `pranesejo_statusas` | `"kriminalinės policijos pareigūnas"` | — | — | Kriminalinės policijos pareigūnas | — |
| `pranesejo_statusas` | `"policijos rėmėjas, tarnybos ar saugos padalinio darbuotojas"` | — | — | Policijos rėmėjas, tarnybos ar saugos padalinio darbuotojas | — |
| `pranesejo_statusas` | `"privatus fizinis asmuo"` | — | — | Privatus fizinis asmuo | — |
| `pranesejo_statusas` | `"sveikatos priežiūros įstaigos darbuotojas"` | — | — | Sveikatos priežiūros įstaigos darbuotojas | — |
| `pranesejo_statusas` | `"užsienio pilietis"` | — | — | Užsienio pilietis | — |
| `pranesejo_statusas` | `"viešosios policijos\\apsaugos policijos padalinio pareigūnas"` | — | — | Viešosios policijos\\apsaugos policijos padalinio pareigūnas | — |
| `pranesejo_statusas` | `"viešosios policijos\\eismo priežiūros tarnybos pareigūnas"` | — | — | Viešosios policijos\\eismo priežiūros tarnybos pareigūnas | — |
| `pranesejo_statusas` | `"viešosios policijos\\patrulinės tarnybos pareigūnas"` | — | — | Viešosios policijos\\patrulinės tarnybos pareigūnas | — |
| `pranesejo_statusas` | `"viešosios policijos\\prevencinio padalinio pareigūnas"` | — | — | Viešosios policijos\\prevencinio padalinio pareigūnas | — |
| `ar_dalyvauja_nepilnameciai` | `true` | `1` | — | Taip | — |
| `ar_dalyvauja_nepilnameciai` | `false` | `0` | — | Ne | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/prir.csv
