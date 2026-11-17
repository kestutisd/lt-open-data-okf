---
type: Table
title: "Vieta — Pateikiami Užimtumo tarnybos duomenys apie laisvas darbo vietas Lietuvoje. nuo 1990m. iki šių dienų. Lentelės objektas - laisva darbo vieta. Pateikiami išsamūs duomenys apie laisvą darbo..."
description: "Spinta table datasets/gov/uzt/ldv/Vieta (53 columns)."
resource: "https://get.data.gov.lt/datasets/gov/uzt/ldv/Vieta"
tags: [gov, uzt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/uzt/ldv.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/uzt/ldv.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vieta — Pateikiami Užimtumo tarnybos duomenys apie laisvas darbo vietas Lietuvoje. nuo 1990m. iki šių dienų. Lentelės objektas - laisva darbo vieta. Pateikiami išsamūs duomenys apie laisvą darbo...

- **Model:** `datasets/gov/uzt/ldv/Vieta`[^manifest]
- **Dataset:** [Užimtumo Tarnybos skelbiamos laisvos darbo vietos](../ldv.md) (`datasets/gov/uzt/ldv`)
- **Manifest CSV:** [datasets/gov/uzt/ldv.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/uzt/ldv.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/uzt/ldv/Vieta`
- **Primary Key (`ref`):** `darbo_vietos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `darbo_vietos_id` | `string` | — | `4` | `open` | — | Unikalus įrašo identifikatorius | — |
| `statusas` | `string` | — | `4` | `open` | — | Laisvos darbo vietos statusas. Istorinėms, t.y. nebegaliojančioms darbo vietos priskiriamas statusas "archyvuota". | — |
| `ikelimo_data` | `date` | `D` | `4` | `open` | — | Įrašo apie darbo vietą įkėlimo data | — |
| `prelim_darbo_uzmokestis` | `number` | — | `4` | `open` | — | Preliminarus mėnesinis darbo užmokestis, neatskaičius mokesčių | — |
| `vid_darbo_uzmokestis` | `number` | — | `4` | `open` | — | Bazinio (tarifinio) darbo užmokesčio dydis | — |
| `maks_darbo_uzmokestis` | `number` | — | `4` | `open` | — | Bazinio (tarifinio) darbo užmokesčio dydžio intervalo maksimalioji riba | — |
| `valiuta` | `string` | — | `4` | `open` | — | Darbo užmokestyje nurodyta valiuta | — |
| `uzmokescio_komentaras_lt` | `string` | — | `4` | `open` | — | Darbdavio komentaras dėl darbo užmokesčio | — |
| `profesijos_grupes_kodas` | `string` | — | `4` | `open` | — | Profesijos grupės kodas | — |
| `profesijos_grupes_pav` | `string` | — | `4` | `open` | — | Profesijos grupės pavadinimas | — |
| `profesijos_kodas` | `string` | — | `4` | `open` | — | Profesijos kodas pagal Lietuvos profesijų klasifikatorių, parengtą pagal Tarptautinį standartinį profesijų klasifikatorių ISCO-08 | — |
| `profesijos_pareigybes_pav` | `string` | — | `4` | `open` | — | Laisvos darbo vietos pareigybės pavadinimas | — |
| `kontrakto_tipas` | `string` | — | `4` | `open` | — | Darbo sutarties tipas | — |
| `darbo_aprasymas_lt` | `string` | — | `4` | `open` | — | Darbo aprašymas | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Darbo vietos pasiūlymo galiojimo pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Darbo vietos pasiūlymo galiojimo pabaiga | — |
| `ar_aktuali_siandien` | `string` | — | `4` | `open` | — | Požymis, ar apie laisvą darbo vietą skelbiama Užimtumo tarnybos internetiniame puslapyje paskutinio duomenų atnaujinimo laikotarpiu | — |
| `ar_uzpildyta` | `string` | — | `4` | `open` | — | Požymis, ar darbo vieta buvo užpildyta. Atvejais, kai darbdavys siūlo daugiau nei vieną darbo vietą tai pačiai pareigybei, požymis yra 1, jei bent viena laisva pozicija buvo užpildyta. | — |
| `pageidaujama_darbo_pradzia` | `date` | `D` | `4` | `open` | — | Darbo pradžios data | — |
| `darbo_vietu_skaicius` | `integer` | `U` | `4` | `open` | — | Laisvų darbo vietų skaičius nurodytai pareigybei | — |
| `darbo_vietos_adresas` | `string` | — | `4` | `open` | — | Darbo vietos adresas | — |
| `darbo_vietos_sav_pav` | `string` | — | `4` | `open` | — | Darbo vietos savivaldybė | — |
| `registravimo_pagrindo_pav` | `string` | — | `4` | `open` | — | Darbo vietos registravimo pagrindas | — |
| `registravimo_budo_pav` | `string` | — | `4` | `open` | — | Darbo vietos registravimo būdas | — |
| `pageidavimo_pateikimo_pav` | `string` | — | `4` | `open` | — | Požymis, kaip darbdavys pageidauja kontaktuoti dėl darbo vietos su kandidatu | — |
| `ar_papildomai_remia` | `string` | — | `4` | `open` | — | Požymis, ar darbo vieta yra remiama | — |
| `ar_darbina_po_mokymu` | `string` | — | `4` | `open` | — | Požymis, ar kandidatas įdarbinamas po mokymo | — |
| `ar_apmoka_keliones` | `string` | — | `4` | `open` | — | Požymis, ar kelionės į/iš darbo yra apmokamos | — |
| `ar_apgyvendina` | `string` | — | `4` | `open` | — | Požymis, ar darbuotojui suteikiamas apgyvendinimas | — |
| `ar_maitina` | `string` | — | `4` | `open` | — | Požymis, ar darbuotojui suteikiamas maitinimas | — |
| `rizikos_lt` | `string` | — | `1` | `open` | — | Darbdavio įvardintos darbo rizikos | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Darbdavio juridinio asmens kodas | — |
| `darbdavys` | `string` | — | `1` | `open` | — | Darbdavio įmonės pavadinimas, imamas iš veikiančių ūkio subjektų registro pagal įmonės JAR kodą. Rinkinyje vaizduojamas tik vėliausias įmonės pavadinimas. | — |
| `teisinio_statuso_pav` | `string` | — | `4` | `open` | — | Įmonės teisinis statusas | — |
| `teisines_formos_pav` | `string` | — | `4` | `open` | — | Įmonės teisinė forma | — |
| `imones_iregistravimas` | `date` | `D` | `4` | `open` | — | Darbdavio įmonės įregistravimo data | — |
| `darbdavio_bustine` | `string` | — | `2` | `open` | — | Darbdavio įmonės būstinės adresas | — |
| `darbdavio_kontaktinis_asmuo` | `string` | — | `4` | `open` | — | — | — |
| `susisiekimo_budas` | `string` | — | `4` | `open` | — | Susisiekimo su darbdaviu dėl laisvos vietos būdas | — |
| `darbdavio_tel_nr` | `string` | — | `2` | `open` | — | Darbdavio kontaktinis telefono numeris | — |
| `darbdavio_mob_nr` | `string` | — | `2` | `open` | — | Darbdavio kontaktinio mobiliojo telefono numeris | — |
| `darbdavio_el_pastas` | `string` | — | `2` | `open` | — | Darbdavio kontaktinio elektroninio pašto adresas | — |
| `reik_darbo_patirtis` | `integer` | — | `4` | `open` | — | Reikalaujama darbo patirtis kandidatui | — |
| `reik_kompetencijos_lt` | `string` | — | `1` | `open` | — | Kandidatui reikalaujamos kompetencijos | — |
| `reik_gebejimai` | `string` | — | `4` | `open` | — | Kandidatui reikalingi gebėjimai | — |
| `reik_issilavinimo_pav` | `string` | — | `4` | `open` | — | Kandidatui reikalingas išsilavinimas | — |
| `reik_mok_progr_pav` | `string` | — | `4` | `open` | — | Mokymo programa, kurią baigęs turi būti kandidatas | — |
| `ar_moksleiviams` | `string` | — | `4` | `open` | — | Požymis, ar gali dirbti ir moksleiviai (0 - ne, 1 - taip) | — |
| `ar_iki_18` | `string` | — | `4` | `open` | — | Požymis, ar gali dirbti ir asmenys iki 18m. amžiaus (0 - ne, 1 - taip) | — |
| `ar_studentams` | `string` | — | `4` | `open` | — | Požymis, ar gali dirbti ir studentai (0 - ne, 1 - taip) | — |
| `ar_kariams` | `string` | — | `4` | `open` | — | Požymis, ar gali dirbti ir atsargos kariai (0 - ne, 1 - taip) | — |
| `ar_ukrainieciams` | `string` | — | `4` | `open` | — | Požymis, ar gali dirbti ir ukrainiečiai (karo pabėgėliai) (0 - ne, 1 - taip) | — |
| `ar_turintiems_negalia` | `string` | — | `4` | `open` | — | Požymis, ar gali dirbti ir asmenys, turintys negalią (0 - ne, 1 - taip) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | `"archyvuota"` | — | — | — | — |
| `statusas` | `"sukurta"` | — | — | — | — |
| `statusas` | `"koreguojama"` | — | — | — | — |
| `valiuta` | `"EUR"` | — | — | Darbo užmokestis, nurodytas eurais | — |
| `valiuta` | `"LTL"` | — | — | Darbo užmokestis, nurodytas litais | — |
| `valiuta` | `"USD"` | — | — | Darbo užmokestis, nurodytas doleriais | — |
| `valiuta` | `"GBP"` | — | — | Darbo užmokestis, nurodytas svarais sterlingais | — |
| `ar_aktuali_siandien` | `"1"` | — | — | Darbo vieta skelbiama Užimtumo tarnybos postale | — |
| `ar_aktuali_siandien` | `"0"` | — | — | Darbo vieta neskelbiama Užimtumo tarnybos postale | — |
| `ar_uzpildyta` | `"0"` | — | — | Neužpildyta | — |
| `ar_uzpildyta` | `"1"` | — | — | Užpildyta | — |
| `ar_papildomai_remia` | `"0"` | — | — | Neremia | — |
| `ar_papildomai_remia` | `"1"` | — | — | Remia | — |
| `ar_darbina_po_mokymu` | `"0"` | — | — | Nedarbina | — |
| `ar_darbina_po_mokymu` | `"1"` | — | — | Darbina | — |
| `ar_apmoka_keliones` | `"0"` | — | — | Neapmoka | — |
| `ar_apmoka_keliones` | `"1"` | — | — | Apmoka | — |
| `ar_apgyvendina` | `"0"` | — | — | Neapmoka | — |
| `ar_apgyvendina` | `"1"` | — | — | Apgyvendina | — |
| `ar_maitina` | `"0"` | — | — | Nemaitina | — |
| `ar_maitina` | `"1"` | — | — | Maitina | — |
| `ar_moksleiviams` | `"0"` | — | — | Ne | — |
| `ar_moksleiviams` | `"1"` | — | — | Taip | — |
| `ar_iki_18` | `"0"` | — | — | Ne | — |
| `ar_iki_18` | `"1"` | — | — | Taip | — |
| `ar_studentams` | `"0"` | — | — | Ne | — |
| `ar_studentams` | `"1"` | — | — | Taip | — |
| `ar_kariams` | `"0"` | — | — | Ne | — |
| `ar_kariams` | `"1"` | — | — | Taip | — |
| `ar_ukrainieciams` | `"0"` | — | — | Ne | — |
| `ar_ukrainieciams` | `"1"` | — | — | Taip | — |
| `ar_turintiems_negalia` | `"0"` | — | — | Ne | — |
| `ar_turintiems_negalia` | `"1"` | — | — | Taip | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `uzmokescio_komentaras_lt` | `update(property: "uzmokescio_komentaras_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `darbo_aprasymas_lt` | `update(property: "darbo_aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `rizikos_lt` | `update(property: "rizikos_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `susisiekimo_budas` | `update(property: ""susisiekimo_budas[]"", type: ""array"", source: ""Susisiekimo_budas"")` | `property` | `4` | — | — | — | — |
| `reik_kompetencijos_lt` | `update(property: "reik_kompetencijos_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `reik_gebejimai` | `update(property: ""reik_gebejimai[]"", type: ""array"", source: ""Reik_gebejimai"")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/uzt/ldv.csv
