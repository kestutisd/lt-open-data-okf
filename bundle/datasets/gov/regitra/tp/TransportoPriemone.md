---
type: Table
title: "TransportoPriemone"
description: "Spinta table datasets/gov/regitra/tp/TransportoPriemone (69 columns)."
tags: [gov, regitra, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/regitra/tp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/tp.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# TransportoPriemone

- **Model:** `datasets/gov/regitra/tp/TransportoPriemone`[^manifest]
- **Dataset:** [datasets/gov/regitra/tp](../tp.md) (`datasets/gov/regitra/tp`)
- **Manifest CSV:** [datasets/gov/regitra/tp.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/tp.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `keb_kodas, spec_kodas`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `marke` | `string` | — | `3` | `open` | — | Gamybinë markë (gamintojo prekës pavadinimas) | Kai `vald_tipas="Fizinis"` ir `marke+komercinis_pav+savivaldyb=1`, tomet vietoje "Gamybinë markë" yra nurodoma `Nuasmeninta`, atsiþvelgiant á asmens duomenø apsaugà. |
| `komercinis_pav` | `string` | — | `3` | `open` | — | Komercinis pavadinimas | Kai `vald_tipas="Fizinis"` ir `marke+komercinis_pav+savivaldybe=1`, tomet vietoje "Komercinis pavadinimas" yra nurodoma `Nuasmeninta`, atsiþvelgiant á asmens duomenø apsaugà. |
| `gamintojo_pav` | `string` | — | `3` | `open` | — | Gamintojo pavadinimas | — |
| `gamintojo_pav_baz` | `string` | — | `3` | `open` | — | Bazinës transporto priemonës gamintojo pavadinimas | — |
| `tipas` | `string` | — | `3` | `open` | — | Tipas | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Tipas" yra nurodoma "Nuasmeninta", atsiþvelgiant á asmens duomenø apsaugà |
| `variantas` | `string` | — | `3` | `open` | — | Variantas | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Variantas" yra nurodoma "Nuasmeninta", atsiþvelgiant á asmens duomenø apsaugà |
| `versija` | `string` | — | `3` | `open` | — | Versija | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Versija" yra nurodoma "Nuasmeninta", atsiþvelgiant á asmens duomenø apsaugà |
| `es_tipo_patvirtinimo_nr` | `string` | — | `4` | `open` | — | ES tipo patvirtinimo numeris | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "ES tipo patvirtinimo numeris" yra nurodoma "Nuasmeninta", atsiþvelgiant á asmens duomenø apsaugà |
| `nac_tipo_patvirtinimo_nr` | `string` | — | `4` | `open` | — | Nacionalinis tipo patvirtinimo, áskaitant iðplëtimà, numeris | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Nacionalinis tipo patvirtinimo, áskaitant iðplëtimà, numeris" yra nurodoma "Nuasmeninta", atsiþvelgiant á asmens duomenø apsaugà |
| `individual_patvirtinimo_nr` | `string` | — | `4` | `open` | — | Individualaus patvirtinimo numeris | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Individualaus patvirtinimo numeris" yra nurodoma "Nuasmeninta", atsiþvelgiant á asmens duomenø apsaugà |
| `interpoliacija` | `string` | — | `4` | `open` | — | Interpoliacijos ðeimos identifikatorius | Kai VALD_TIPAS - "Fizinis" ir MARKE+KOMERCINIS_PAV+SAVIVALDYBE=1, tomet vietoje "Interpoliacijos ðeimos identifikatorius" yra nurodoma "Nuasmeninta", atsiþvelgiant á asmens duomenø apsaugà |
| `uzbaigtumo_pakopa` | `string` | — | `3` | `open` | — | Transporto priemonës uþbaigtumo pakopa | — |
| `vairas_desineje` | `boolean` | — | `3` | `open` | — | Vairas deðinëje pusëje | Transporto priemonë pritaikyta eismui kairiàja kelio puse ir (ar) turi vairà deðinëje pusëje |
| `kategorija_pilnai` | `string` | — | `3` | `open` | — | Kategorija, klasë, këbulo kodas, specialios paskirties kodas | — |
| `kategorija_klase` | `string` | — | `3` | `open` | — | Kategorija, klasë | — |
| `keb_kodas` | `string` | — | `4` | `open` | — | Këbulo kodas | — |
| `keb_pavadinimas` | `string` | — | `3` | `open` | — | Këbulo kodas (þodþiais) | — |
| `spec_kodas` | `string` | — | `4` | `open` | — | Specialios paskirties kodas | — |
| `spec_pavadinimas` | `string` | — | `3` | `open` | — | Specialios paskirties kodas (þodþiais) | — |
| `keb_kodas_es` | `string` | — | `4` | `open` | — | Këbulo kodas (ES) | — |
| `nuosava_mase` | `integer` | `kg` | `4` | `open` | — | Parengtos eksploatuoti transporto priemonës masë | — |
| `nuosava_mase_baz` | `integer` | `kg` | `4` | `open` | — | Parengtos eksploatuoti bazinës transporto priemonës masë | — |
| `maks_mase` | `integer` | `kg` | `4` | `open` | — | Didþiausia techniðkai leidþiama pakrautos transporto priemonës masë | — |
| `maks_mase_f2` | `integer` | `kg` | `4` | `open` | — | Didþiausia leistina pakrautos transporto priemonës, kuri eksploatuojama registracijos valstybëje, masë | — |
| `maks_mase_f5` | `integer` | `kg` | `4` | `open` | — | Puspriekabës aðims tenkanti didþiausia techniðkai leidþiama pakrautos transporto priemonës masës dalis | — |
| `bandomoji_mase` | `integer` | `kg` | `4` | `open` | — | Bandomoji masë | — |
| `darbinis_turis` | `number` | `cm³` | `4` | `open` | — | Variklio darbinis tûris | — |
| `galia` | `number` | `kW` | `3` | `open` | — | Didþiausia naudingoji galia | — |
| `sukiu_sk` | `number` | — | `3` | `open` | — | Vardinis sûkiø skaièius | — |
| `galia_elektr` | `number` | `kW` | `4` | `open` | — | Didþiausia nuolatinë elektrinio variklio vardinë galia | — |
| `degalai` | `string` | — | `3` | `open` | — | Degalø tipas arba galios ðaltinis | — |
| `degalu_rezimas` | `string` | — | `3` | `open` | — | Degalø reþimas | — |
| `elektrine_tp` | `boolean` | — | `3` | `open` | — | Elektrinë transporto priemonë | — |
| `hibridines_tp_kategorija` | `string` | — | `3` | `open` | — | Hibridinës (elektrinës) transporto priemonës kategorija | Galimos reikðmës: VC-HEV |
| `pavaru_dezes_tipas` | `string` | — | `3` | `open` | — | Pavarø dëþës tipas | — |
| `co2_kiekis` | `number` | `g/km` | `4` | `open` | — | Bendras iðmetamo CO2 kiekis | NEDC reikðmë arba nenustatytos bandymø procedûros |
| `co2_kiekis_wltp` | `number` | `g/km` | `4` | `open` | — | Bendras iðmetamo CO2 kiekis (WLTP reikðmë) | — |
| `eko_naujoves_kodas` | `string` | — | `3` | `open` | — | Bendrasis ekologinës naujovës kodas | — |
| `co2_sumazejimas_nedc` | `number` | `g/km` | `4` | `open` | — | Dël ekologinës naujovës (-iø) sumaþëjæs bendras iðmetamo CO? kiekis, taikant NEDC | — |
| `co2_sumazejimas_wltp` | `number` | `g/km` | `4` | `open` | — | Dël ekologinës naujovës (-iø) sumaþëjæs bendras iðmetamo CO? kiekis, taikant WLTP | — |
| `elektr_energ_sanaud_nedc` | `number` | — | `3` | `open` | — | Elektros energijos sànaudos (NEDC reikðmë) | — |
| `elektr_energ_sanaud_wltp_e` | `number` | — | `3` | `open` | — | Elektros energijos sànaudos (WLTP reikðmë - elenktrinë) | — |
| `elektr_energ_sanaud_wltp_h` | `number` | — | `3` | `open` | — | Elektros energijos sànaudos (WLTP reikðmë - hibridas) | — |
| `elektrine_rida_nedc` | `number` | `km` | `4` | `open` | — | Elektrinë rida (NEDC reikðmë) | — |
| `elektrine_rida_wltp_e` | `number` | `km` | `4` | `open` | — | Elektrinë rida (WLTP reikðmë - elektrinë) | — |
| `elektrine_rida_wltp_h` | `number` | `km` | `4` | `open` | — | Elektrinë rida (WLTP reikðmë - hibridas) | — |
| `tersalu_lygis` | `string` | — | `3` | `open` | — | Iðmetamø terðalø lygis | — |
| `tersalu_norm_akto_nr` | `string` | — | `3` | `open` | — | Iðmetamø terðalø norminio akto numeris | — |
| `ratu_baze` | `integer` | `mm` | `4` | `open` | — | Ratø bazë | — |
| `tv_plotis1` | `integer` | `mm` | `4` | `open` | — | Priekinës aðies vëþës plotis | — |
| `tv_plotis2` | `integer` | `mm` | `4` | `open` | — | Galinës aðies vëþës plotis | — |
| `galios_mases_sant` | `integer` | — | `3` | `open` | — | Galios ir masës santykis (tik motociklams) | — |
| `spalva` | `string` | — | `3` | `open` | — | Spalva | — |
| `maks_greitis` | `integer` | — | `3` | `open` | — | Didþiausias leidþiamas greitis | — |
| `sedimu_vietu_sk` | `integer` | — | `3` | `open` | — | Sëdimø vietø skaièius (áskaitant vairuotojo vietà) | — |
| `stovimu_vietu_sk` | `integer` | — | `3` | `open` | — | Stovimø vietø skaièius | — |
| `gamybos_metai` | `date` | `Y` | `4` | `open` | — | Gamybos metai | — |
| `modelio_metai` | `date` | `Y` | `4` | `open` | — | Modelio metai | — |
| `rida` | `number` | `km` | `4` | `open` | — | Rida | Uþfiksuota registravimo metu, nustatant transporto priemonës tapatumà arba perkelta ið ES ðalies privalomosios techninës apþiûros dokumentø |
| `pirm_reg_data` | `date` | `D` | `4` | `open` | — | Pirmosios registracijos data | — |
| `pirm_reg_data_lt` | `date` | `D` | `4` | `open` | — | Pirmosios registracijos Lietuvoje data | — |
| `galiojimo_laikas` | `date` | `D` | `4` | `open` | — | Registracijos galiojimo pabaigos data | — |
| `paskutines_reg_data` | `temporal` | `D` | `4` | `open` | — | Paskutinës operacijos data | — |
| `dae_statusas` | `boolean` | — | `3` | `open` | — | Dalyvavimo vieðajame eisme statusas | — |
| `kilmes_salis` | `string` | — | `5` | `open` | `locn:geographicName` | Uþsienio ðalies kodas | Kurios registracijos dokumentø pagrindu transporto priemonë registruota Lietuvoje. |
| `vald_tipas` | `string` | — | `3` | `open` | — | Valdytojo tipas | — |
| `vald_gim_dat_int` | `string` | — | `3` | `open` | — | Valdytojo (fizinio asmens) gimimo datos intervalas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) | `5` | `open` | `locn:geographicName` | Savivaldybë | Pagal valdytojo registracijos adresà |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../rc/ar/apskritis/Apskritis.md) | `5` | `open` | `locn:geographicName` | Apskritis | Pagal valdytojo registracijos adresà |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vairas_desineje` | `true` | `Y` | — | Taip | — |
| `vairas_desineje` | `false` | `N` | — | Ne | — |
| `vairas_desineje` | `null` | — | — | — | — |
| `elektrine_tp` | `true` | `Y` | — | Taip | — |
| `elektrine_tp` | `false` | `N` | — | Ne | — |
| `elektrine_tp` | `null` | — | — | Nenurodyta | — |
| `dae_statusas` | `true` | `T` | — | leidþiama | — |
| `dae_statusas` | `false` | `N` | — | draudþiama | — |
| `vald_tipas` | `"fizinis"` | — | — | Fizinis | — |
| `vald_tipas` | `"juridinis"` | — | — | Juridinis | — |

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
| `keb_pavadinimas` | Code for bodywork (description in Lithuanian) | — |
| `spec_kodas` | Code for bodywork | — |
| `spec_pavadinimas` | Code for bodywork (description in Lithuanian) | — |
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
| `spalva` | Colour | — |
| `maks_greitis` | Maximum speed | — |
| `sedimu_vietu_sk` | Number of seating positions (including the driver) | — |
| `stovimu_vietu_sk` | Number of standing places | — |
| `gamybos_metai` | Production year | — |
| `modelio_metai` | Model year | — |
| `rida` | Mileage | Recorded during registration and vehicle identification or transferred from EU country mandatory roadworthiness test documents |
| `pirm_reg_data` | Date of first registration | — |
| `pirm_reg_data_lt` | Date of first registration in Lithuania | — |
| `galiojimo_laikas` | Expiry date of registration | — |
| `paskutines_reg_data` | Date of last operation | — |
| `dae_statusas` | Status of participation in public traffic | — |
| `kilmes_salis` | Foreign country code | On the basis of registration documents vehicle registered in the Lithuania. |
| `vald_tipas` | Holder type | — |
| `vald_gim_dat_int` | Holder (Natural person) date of birth interval | — |
| `savivaldybe` | Municipality | According to the holder's registration address |
| `apskritis` | County | According to the holder's registration address |

# Prefixes

| Prefix | URI |
| --- | --- |
| `locn` | `http://www.w3.org/ns/locn#` |

[^manifest]: atviriduomenys/manifest — datasets/gov/regitra/tp.csv
