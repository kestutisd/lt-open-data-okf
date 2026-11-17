---
type: Table
title: "TransportoPriemone"
description: "Spinta table datasets/gov/regitra/jtp/TransportoPriemone (70 columns)."
tags: [gov, regitra, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/regitra/jtp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/jtp.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# TransportoPriemone

- **Model:** `datasets/gov/regitra/jtp/TransportoPriemone`[^manifest]
- **Dataset:** [datasets/gov/regitra/jtp](../jtp.md) (`datasets/gov/regitra/jtp`)
- **Manifest CSV:** [datasets/gov/regitra/jtp.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/jtp.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `keb_kodas, spec_kodas`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `marke` | `string` | — | `3` | `open` | — | Gamybinė markė (gamintojo prekės pavadinimas) | Kai `vald_tipas="Fizinis"` ir `marke+komercinis_pav+savivaldyb=1`, tomet vietoje "Gamybinė markė" yra nurodoma `Nuasmeninta`, atsižvelgiant į asmens duomenų apsaugą. |
| `komercinis_pav` | `string` | — | `3` | `open` | — | Komercinis pavadinimas | Kai `vald_tipas="Fizinis"` ir `marke+komercinis_pav+savivaldybe=1`, tomet vietoje "Komercinis pavadinimas" yra nurodoma `Nuasmeninta`, atsižvelgiant į asmens duomenų apsaugą. |
| `gamintojo_pav` | `string` | — | `3` | `open` | — | Gamintojo pavadinimas | — |
| `gamintojo_pav_baz` | `string` | — | `3` | `open` | — | Bazinės transporto priemonės gamintojo pavadinimas | — |
| `tipas` | `string` | — | `3` | `open` | — | Tipas | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Tipas" yra nurodoma "Nuasmeninta", atsižvelgiant į asmens duomenų apsaugą |
| `variantas` | `string` | — | `3` | `open` | — | Variantas | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Variantas" yra nurodoma "Nuasmeninta", atsižvelgiant į asmens duomenų apsaugą |
| `versija` | `string` | — | `3` | `open` | — | Versija | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Versija" yra nurodoma "Nuasmeninta", atsižvelgiant į asmens duomenų apsaugą |
| `es_tipo_patvirtinimo_nr` | `string` | — | `3` | `open` | — | ES tipo patvirtinimo numeris | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "ES tipo patvirtinimo numeris" yra nurodoma "Nuasmeninta", atsižvelgiant į asmens duomenų apsaugą |
| `nac_tipo_patvirtinimo_nr` | `string` | — | `3` | `open` | — | Nacionalinis tipo patvirtinimo, įskaitant išplėtimą, numeris | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Nacionalinis tipo patvirtinimo, įskaitant išplėtimą, numeris" yra nurodoma "Nuasmeninta", atsižvelgiant į asmens duomenų apsaugą |
| `individual_patvirtinimo_nr` | `string` | — | `3` | `open` | — | Individualaus patvirtinimo numeris | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Individualaus patvirtinimo numeris" yra nurodoma "Nuasmeninta", atsižvelgiant į asmens duomenų apsaugą |
| `interpoliacija` | `string` | — | `3` | `open` | — | Interpoliacijos šeimos identifikatorius | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Interpoliacijos šeimos identifikatorius" yra nurodoma "Nuasmeninta", atsižvelgiant į asmens duomenų apsaugą |
| `uzbaigtumo_pakopa` | `string` | — | `3` | `open` | — | Transporto priemonės užbaigtumo pakopa | — |
| `vairas_desineje` | `boolean` | — | `3` | `open` | — | Vairas dešinėje pusėje | Transporto priemonė pritaikyta eismui kairiąja kelio puse ir (ar) turi vairą dešinėje pusėje |
| `kategorija_pilnai` | `string` | — | `3` | `open` | — | Kategorija, klasė, kėbulo kodas, specialios paskirties kodas | — |
| `kategorija_klase` | `string` | — | `3` | `open` | — | Kategorija, klasė | — |
| `keb_kodas` | `string` | — | `3` | `open` | — | Kėbulo kodas | — |
| `spec_kodas` | `string` | — | `3` | `open` | — | Specialios paskirties kodas | — |
| `keb_kodas_es` | `string` | — | `3` | `open` | — | Kėbulo kodas (ES) | — |
| `nuosava_mase` | `integer` | `kg` | `4` | `open` | — | Parengtos eksploatuoti transporto priemonės masė | — |
| `nuosava_mase_baz` | `integer` | `kg` | `4` | `open` | — | Parengtos eksploatuoti bazinės transporto priemonės masė | — |
| `maks_mase` | `integer` | `kg` | `4` | `open` | — | Didžiausia techniškai leidžiama pakrautos transporto priemonės masė | — |
| `maks_mase_f2` | `integer` | `kg` | `4` | `open` | — | Didžiausia leistina pakrautos transporto priemonės, kuri eksploatuojama registracijos valstybėje, masė | — |
| `maks_mase_f5` | `integer` | `kg` | `4` | `open` | — | Puspriekabės ašims tenkanti didžiausia techniškai leidžiama pakrautos transporto priemonės masės dalis | — |
| `bandomoji_mase` | `integer` | `kg` | `4` | `open` | — | Bandomoji masė | — |
| `darbinis_turis` | `integer` | `cm³` | `4` | `open` | — | Variklio darbinis tūris | — |
| `galia` | `integer` | `kW` | `4` | `open` | — | Didžiausia naudingoji galia | — |
| `sukiu_sk` | `integer` | — | `3` | `open` | — | Vardinis sūkių skaičius | — |
| `galia_elektr` | `integer` | `kW` | `4` | `open` | — | Didžiausia nuolatinė elektrinio variklio vardinė galia | — |
| `degalai` | `string` | — | `3` | `open` | — | Degalų tipas arba galios šaltinis | — |
| `degalu_rezimas` | `string` | — | `3` | `open` | — | Degalų režimas | — |
| `elektrine_tp` | `boolean` | — | `3` | `open` | — | Elektrinė transporto priemonė | — |
| `hibridines_tp_kategorija` | `string` | — | `3` | `open` | — | Hibridinės (elektrinės) transporto priemonės kategorija | Galimos reikšmės: VC-HEV; NOVC-HEV; OVC-FCHV; NOVC-FCHV |
| `pavaru_dezes_tipas` | `string` | — | `3` | `open` | — | Pavarų dėžės tipas | — |
| `co2_kiekis` | `integer` | `g/km` | `4` | `open` | — | Bendras išmetamo CO2 kiekis | NEDC reikšmė arba nenustatytos bandymų procedūros |
| `co2_kiekis_wltp` | `integer` | `g/km` | `4` | `open` | — | Bendras išmetamo CO2 kiekis (WLTP reikšmė) | — |
| `eko_naujoves_kodas` | `string` | — | `3` | `open` | — | Bendrasis ekologinės naujovės kodas | — |
| `co2_sumazejimas_nedc` | `number` | `g/km` | `4` | `open` | — | Dėl ekologinės naujovės (-ių) sumažėjęs bendras išmetamo CO? kiekis, taikant NEDC | — |
| `co2_sumazejimas_wltp` | `number` | `g/km` | `4` | `open` | — | Dėl ekologinės naujovės (-ių) sumažėjęs bendras išmetamo CO? kiekis, taikant WLTP | — |
| `elektr_energ_sanaud_nedc` | `number` | — | `3` | `open` | — | Elektros energijos sąnaudos (NEDC reikšmė) | — |
| `elektr_energ_sanaud_wltp_e` | `number` | — | `3` | `open` | — | Elektros energijos sąnaudos (WLTP reikšmė – elenktrinė) | — |
| `elektr_energ_sanaud_wltp_h` | `number` | — | `3` | `open` | — | Elektros energijos sąnaudos (WLTP reikšmė - hibridas) | — |
| `elektrine_rida_nedc` | `number` | `km` | `4` | `open` | — | Elektrinė rida (NEDC reikšmė) | — |
| `elektrine_rida_wltp_e` | `number` | `km` | `4` | `open` | — | Elektrinė rida (WLTP reikšmė – elektrinė) | — |
| `elektrine_rida_wltp_h` | `number` | `km` | `4` | `open` | — | Elektrinė rida (WLTP reikšmė - hibridas) | — |
| `tersalu_lygis` | `string` | — | `3` | `open` | — | Išmetamų teršalų lygis | — |
| `tersalu_norm_akto_nr` | `string` | — | `3` | `open` | — | Išmetamų teršalų norminio akto numeris | — |
| `ratu_baze` | `integer` | `mm` | `4` | `open` | — | Ratų bazė | — |
| `tv_plotis1` | `integer` | `mm` | `4` | `open` | — | Priekinės ašies vėžės plotis | — |
| `tv_plotis2` | `integer` | `mm` | `4` | `open` | — | Galinės ašies vėžės plotis | — |
| `galios_mases_sant` | `integer` | — | `4` | `open` | — | Galios ir masės santykis (tik motociklams) | — |
| `maks_greitis` | `integer` | — | `3` | `open` | — | Didžiausias leidžiamas greitis | — |
| `sedimu_vietu_sk` | `number` | — | `4` | `open` | — | Sėdimų vietų skaičius (įskaitant vairuotojo vietą) | — |
| `stovimu_vietu_sk` | `number` | — | `4` | `open` | — | Stovimų vietų skaičius | — |
| `gamybos_metai` | `date` | `Y` | `4` | `open` | — | Gamybos metai | — |
| `modelio_metai` | `date` | `Y` | `4` | `open` | — | Modelio metai | — |
| `pirm_reg_data` | `date` | — | `3` | `open` | — | Pirmosios registracijos data | — |
| `pirm_reg_data_lt` | `date` | — | `3` | `open` | — | Pirmosios registracijos Lietuvoje data | — |
| `paskutines_reg_data` | `temporal` | — | `3` | `open` | — | Paskutinės operacijos data | — |
| `dae_statusas` | `boolean` | — | `3` | `open` | — | Dalyvavimo viešajame eisme statusas | — |
| `kilmes_salis` | `string` | — | `3` | `open` | `locn:geographicName` | Užsienio šalies kodas | Kurios registracijos dokumentų pagrindu transporto priemonė registruota Lietuvoje. |
| `tp_valdymo_teise` | `string` | — | `3` | `open` | — | Transporto priemonės valdymo teisė | — |
| `kodas` | `string` | — | `3` | `open` | — | Juridinio asmens kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Juridinio asmens pavadinimas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) | `4` | `open` | `locn:geographicName` | Savivaldybė | — |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../rc/ar/apskritis/Apskritis.md) | `4` | `open` | `locn:geographicName` | Apskritis | — |
| `tp_valdymo_teise_sav` | `string` | — | `3` | `open` | — | Transporto priemonės valdymo teisė | — |
| `kodas_sav` | `string` | — | `3` | `open` | — | Juridinio asmens kodas | — |
| `pavadinimas_sav` | `string` | — | `3` | `open` | — | Juridinio asmens pavadinimas | — |
| `savivaldybe_sav` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) | `4` | `open` | `locn:geographicName` | Savivaldybė | — |
| `apskritis_sav` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../rc/ar/apskritis/Apskritis.md) | `4` | `open` | `locn:geographicName` | Apskritis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vairas_desineje` | `true` | `Y` | — | Taip | — |
| `vairas_desineje` | `false` | `N` | — | Ne | — |
| `vairas_desineje` | `null` | — | — | No | — |
| `elektrine_tp` | `true` | `Y` | — | Taip | — |
| `elektrine_tp` | `false` | `N` | — | Ne | — |
| `elektrine_tp` | `null` | — | — | Nenurodyta | — |
| `dae_statusas` | `true` | `T` | — | leidžiama | — |
| `dae_statusas` | `false` | `N` | — | draudžiama | — |
| `tp_valdymo_teise` | `"A"` | — | — | Valdytojas-savininkas | — |
| `tp_valdymo_teise` | `"V"` | — | — | Valdytojas | — |
| `tp_valdymo_teise_sav` | `"S"` | — | — | Savininkas | — |
| `tp_valdymo_teise_sav` | `null` | — | — | Nėra | — |

# Translations (`@en`)

| Property | Title (`@en`) | Description (`@en`) |
| --- | --- | --- |
| `marke` | Make (Trade name of the manufacturer) | When `vald_tipas="Fizinis"` (Legal) and `marke+komercinis_pav+savivaldyeb=1`, then instead "Make (trade name of the manufacturer)" indicated `Nuasmeninta`, taking into account the protection of personal data. |
| `komercinis_pav` | Commercial name | When `vald_tipas="Fizinis"` (Legal) and `marke+komercinis_pav+savivaldybe=1`, then instead "Commercial name" indicated `Nuasmeninta`, taking into account the protection of personal data). |
| `gamintojo_pav` | Name of manufacturer | — |
| `gamintojo_pav_baz` | Name of the manufacturer of the base vehicle | — |
| `tipas` | Type | When VALD_TIPAS - "Fizinis (Legal)" and MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, then instead "Type" indicated "Nuasmeninta", taking into account the protection of personal data |
| `variantas` | Variant | When VALD_TIPAS - "Fizinis (Legal)" and MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, then instead "Variant" indicated "Nuasmeninta", taking into account the protection of personal data |
| `versija` | Version | When VALD_TIPAS - "Fizinis (Legal)" and MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, then instead "Version" indicated "Nuasmeninta", taking into account the protection of personal data |
| `es_tipo_patvirtinimo_nr` | EU type approval number | When VALD_TIPAS - "Fizinis (Legal)" and MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, then instead "EU type approval number" indicated "Nuasmeninta", taking into account the protection of personal data |
| `nac_tipo_patvirtinimo_nr` | National type approval, including extension number | When VALD_TIPAS - "Fizinis (Legal)" and MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, then instead "National type approval, including extension number" indicated "Nuasmeninta", taking into account the protection of personal data |
| `individual_patvirtinimo_nr` | Individual approval number | When VALD_TIPAS - "Fizinis (Legal)" and MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, then instead "Individual approval number" indicated "Nuasmeninta", taking into account the protection of personal data |
| `interpoliacija` | Interpolation family’s identifier | When VALD_TIPAS - "Fizinis (Legal)" and MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, then instead "Interpolation family’s identifier" indicated "Nuasmeninta", taking into account the protection of personal data |
| `uzbaigtumo_pakopa` | Vehicle completion stage | — |
| `vairas_desineje` | Steering wheel on the right | The vehicle is designed for left-hand traffic and / or has a right-hand drive |
| `kategorija_pilnai` | Vehicle category and code for bodywork | — |
| `kategorija_klase` | Vehicle category | — |
| `keb_kodas` | Code for bodywork | — |
| `spec_kodas` | Code for bodywork | — |
| `keb_kodas_es` | Code for bodywork (EU) | — |
| `nuosava_mase` | Mass of the vehicle in running order | — |
| `nuosava_mase_baz` | Technically permissible maximum laden mass of the base vehicle | — |
| `maks_mase` | Technically permissible maximum laden mass | — |
| `maks_mase_f2` | The maximum permissible laden mass of the vehicle in service in the State of registration | — |
| `maks_mase_f5` | The technically permissible maximum laden mass on the axle of the semi-trailer | — |
| `bandomoji_mase` | Test mass | — |
| `darbinis_turis` | Engine capacity | — |
| `galia` | Maximum net power | — |
| `sukiu_sk` | Rated engine speed | — |
| `galia_elektr` | Maximum continuous electric motor rated power | — |
| `degalai` | Fuel type or power source | — |
| `degalu_rezimas` | Fuel mode | — |
| `elektrine_tp` | Pure electric vehicle | — |
| `hibridines_tp_kategorija` | Class of hybrid (electric) vehicle | — |
| `pavaru_dezes_tipas` | Gearbox type | — |
| `co2_kiekis` | Combined CO2 emissions | NEDC value or no test procedure specified |
| `co2_kiekis_wltp` | Combined CO2 emissions (WLTP value) | — |
| `eko_naujoves_kodas` | General code of the eco-innovations | — |
| `co2_sumazejimas_nedc` | Total CO? emissions NEDC savings due to the eco-innovations | — |
| `co2_sumazejimas_wltp` | Total CO? emissions WLTP savings due to the eco-innovations | — |
| `elektr_energ_sanaud_nedc` | Electric energy consumption (NEDC value) | — |
| `elektr_energ_sanaud_wltp_e` | Electric energy consumption (WLTP value - electric) | — |
| `elektr_energ_sanaud_wltp_h` | Electric energy consumption (WLTP value - hybrid) | — |
| `elektrine_rida_nedc` | Electric range (NEDC value) | — |
| `elektrine_rida_wltp_e` | Electric range (WLTP value - electric) | — |
| `elektrine_rida_wltp_h` | Electric range (WLTP value - hybrid) | — |
| `tersalu_lygis` | Exhaust emission level | — |
| `tersalu_norm_akto_nr` | Number of the regulatory act of the exhaust emission level | — |
| `ratu_baze` | Wheelbase | — |
| `tv_plotis1` | Front axle track | — |
| `tv_plotis2` | Rear axle track | — |
| `galios_mases_sant` | Power-to-mass ratio (for motorcycles only) | — |
| `maks_greitis` | Maximum speed | — |
| `sedimu_vietu_sk` | Number of seating positions (including the driver) | — |
| `stovimu_vietu_sk` | Number of standing places | — |
| `gamybos_metai` | Production year | — |
| `modelio_metai` | Model year | — |
| `pirm_reg_data` | Date of first registration | — |
| `pirm_reg_data_lt` | Date of first registration in Lithuania | — |
| `paskutines_reg_data` | Date of last operation | — |
| `dae_statusas` | Status of participation in public traffic | — |
| `kilmes_salis` | Foreign country code | On the basis of registration documents vehicle registered in the Lithuania. |
| `tp_valdymo_teise` | Vehicle control right | — |
| `kodas` | Legal person code | — |
| `pavadinimas` | Name of the Legal person | — |
| `savivaldybe` | Municipality | — |
| `apskritis` | County | — |
| `tp_valdymo_teise_sav` | Vehicle control right | — |
| `kodas_sav` | Legal person code | — |
| `pavadinimas_sav` | Name of the Legal person | — |
| `savivaldybe_sav` | Municipality | — |
| `apskritis_sav` | County | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `locn` | `http://www.w3.org/ns/locn#` |

[^manifest]: atviriduomenys/manifest — datasets/gov/regitra/jtp.csv
