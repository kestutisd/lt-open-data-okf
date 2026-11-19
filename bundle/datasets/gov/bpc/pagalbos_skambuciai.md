---
type: Dataset
title: "Bendrojo pagalbos centro 112 skambučių duomenų rinkinys"
description: "Bendrojo pagalbos centro (BPC) duomenys apie gautus pranešimus apie įvykius."
resource: "https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai"
tags: [gov, bpc, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1763/"
    title: "data.gov.lt DCAT-AP — datasets/gov/bpc/pagalbos_skambuciai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Bendrojo pagalbos centro 112 skambučių duomenų rinkinys

Bendrojo pagalbos centro (BPC) duomenys apie gautus pranešimus apie įvykius.[^manifest]

- **Namespace:** `datasets/gov/bpc/pagalbos_skambuciai`[^manifest]
- **Manifest CSV:** [datasets/gov/bpc/pagalbos_skambuciai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai` (`deployed`)[^manifest]
- **Provider:** `bpc` — Bendrasis pagalbos centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1763/`[^dcat]
- **Publisher (`dct:publisher`):** Bendrasis pagalbos centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Bendrojo pagalbos centro (BPC) gauti pranešimai numeriu 112[^dcat]
- **Portal Title (`@en`):** Help calls received by Emergency Response Centre on the emergency services contact number 112[^dcat]
- **Issued (`dct:issued`):** `2022-10-07`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2022-10-07` .. `2025-01-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Bendrosios pagalbos centro (BPC) registruoti įvykiai, apie kuriuos gauti pranešimai pagalbos telefonu 112. Skelbiami duomenys nuo 2022 metų. To paties ar skirtingų asmenų pranešimai apie tą patį įvykį yra sujungti į vieną įvykį. Dėl konfidencialumo duomenys rinkinyje yra išskaidyti į kelias lentelės: pateikiamas arba tikslus įvykio laikas, bet nepateikiama lokacija, arba pateikiamos "triukšmintos" įvykių koordinatės (paslenkant tikrąsias kooridates atsitiktine kryptimi taikant normalųjį triukšmo skirstinį su standartiniu nuokrypiu nuo 100 iki 1000 metrų, priklausomai nuo gyventojų tankio: mažesnis gyventojų tankis – didesnis nuokrypis) be tikslaus laiko, arba pateikiamos įvykių savivaldybės, agreguotos mėnesio dydžio laiko intervalais. Praneštų įvykių skaičiai nebūtinai turi sutapti su Administracinių nusižengimų registro duomenimis (pranešimai gali būti melagingi arba nepasiekti administracinių nusižengimų bylos stadijos). Toliau pateikiami keturių atskirų lentelių aprašymai. [1] BPC ĮVYKIŲ KLASIFIKATORIUS: įvykių tipų klasifikatorius su žodiniais paaiškinimais. Tai yra pagalbinė lentelė, kurią reikia prijungti prie likusių trijų šio rinkinio lentelių. Klasifikatorius turi du hierarchinius lygmenis (bendresnis ir detalesnis). [2] BPC ĮVYKIŲ KOORDINATĖS: registruotų įvykių pilnas neagreguotas sąrašas, kuriame viena eilutė yra vienas įvykis. Lentelė skirta dažniams, dinamikai ir geografiniam pasiskirstymui stebėti. Dėl konfidencialumo pateiktos koordinatės yra "triukšmintos" ir neatspindi tikslios įvykio vietos (tankiai apgyvendintose vietovėse jos yra tikslesnės). BPC koordinates nustato pagal pranešėjo pateiktą įvykio adresą ir Registrų centro adresų duomenis; jeigu konkretus adresas nepateikiamas arba jo nėra, nurodomos gyvenvietės centro koordinatės; koordinatės taip pat gali būti patikslinamos pagal pagalbos prašančiojo asmens vietos nustatymo duomenis, jeigu nepavyksta nustatyti adreso ar gyvenvietės. Taip pat dėl konfidencialumo įvykio data pateikiama mėnesio tikslumu. [3] BPC ĮVYKIŲ SAVIVALDYBĖS: registruotų įvykių teritorinė statistika pagal savivaldybę, mėnesio dydžio intervalais. Tai yra agreguota lentelė, kuri į vieną eilutę sujungia unikalią šių požymių kombinaciją: įvykio tipas, savivaldybė, metai, mėnuo. Lentelės tikslas yra geografinio pasiskirstymo palengvintam stebėjimui. Dėl konfidencialumo nepateikiama tiksli įvykio data. [4] BPC ĮVYKIŲ LAIKAS: registruotų įvykių paros meto statistika. Tai yra agreguota lentelė, kuri į vieną eilutę sujungia unikalią šių požymių kombinaciją: įvykio tipas, mėnuo, savaitės diena, valanda, minutės grupė (10 min. tikslumu). Dėl konfidencialumo lentelė nėra agreguota pagal metus (t.y., visų metų duomenys yra kartu), taip pat nepateikiama tiksli mėnesio diena ar lokacija. Lentelė yra skirta įvykių paros meto tendencijoms stebėti, atsižvelgiant į šventines dienas ir sezoniškumą. Lentelėje yra pateikiamas papildomas stulpelis, nusakantis kiek konkrečių savaitės dienų (pvz., pirmadienių) yra to metų laiko (pvz., liepos mėnesio) duomenyse; šis skaičius yra svarbus korektiškoms analizėms. PASITEIRAVIMUI: Valstybės duomenų valdysenos komanda: vdv@stat.gov.lt. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Events registered by the General Assistance Center (BPC), which were reported by the emergency number 112. Data are published from 2022. Reports of the same event by the same or different persons are combined into one event. Due to confidentiality, the data in the collection is divided into several tables: either the exact time of the event is given, but the location is not given, or the &quot;noisy&quot; coordinates of the events are given (shifting the actual coordinates in a random direction using a normal noise distribution with a standard deviation of 100 to 1000 meters, depending on the population density : lower population density - higher deviation) without exact time, or the municipalities of the events are presented, aggregated in time intervals of the size of a month. The numbers of reported events do not necessarily have to coincide with the data of the Register of Administrative Misdemeanors (reports may be false or may not reach the administrative offense case stage). The following are descriptions of the four individual tables. [1] BPC EVENT CLASSIFIER: A classifier of event types with verbal explanations. This is an auxiliary table to connect to the remaining three tables in this set. The classifier has two hierarchical levels (more general and more detailed). [2] BPC EVENT COORDINATES: A complete unaggregated list of registered events, where one row is one event. The table is intended to observe frequencies, dynamics and geographical distribution. Due to confidentiality, the provided coordinates are &quot;noisy&quot; and do not reflect the exact location of the event (they are more accurate in densely populated areas). BPC determines the coordinates based on the address of the event provided by the reporter and address data of the Registry Center; if a specific address is not provided or does not exist, the coordinates of the center of the settlement are indicated; the coordinates can also be adjusted according to the location data of the person requesting help, if it is not possible to determine the address or the settlement. Also, for reasons of confidentiality, the date of the event is given to the nearest month. [3] BPC EVENTS MUNICIPALITIES: territorial statistics of registered events by municipality, in monthly intervals. This is an aggregated table that combines a unique combination of the following attributes into one row: event type, municipality, year, month. The purpose of the table is to facilitate the observation of geographical distribution. Due to confidentiality, the exact date of the event is not given. [4] BPC EVENT TIME: Time of day statistics of registered events. This is an aggregated table that combines a unique combination of the following attributes into one row: event type, month, day of the week, hour, minute group (with 10-minute precision). For confidentiality reasons, the table is not aggregated by year (ie, data from all years are included), nor is the exact day of the month or location provided. The table is designed to track trends in the time of day of events, taking into account holidays and seasonality. The table contains an additional column that indicates how many specific days of the week (e.g., Mondays) are in the data for that time of year (e.g., July); this number is important for corrective analyses. FOR INQUIRIES: State Data Management Team: vdv@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IvykiuKlasifikatorius](pagalbos_skambuciai/IvykiuKlasifikatorius.md) | BPC įvykių klasifikatorius | `4` | `ivykio_tipo_kodas` | — | `3` | Bendrojo pagalbos centro registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, tipų klasifikatorius. |
| [IvykiuKoordinates](pagalbos_skambuciai/IvykiuKoordinates.md) | BPC įvykių koordinatės | `4` | `ivykio_id` | — | `5` | Bendrojo pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, pilnas sąrašas. |
| [IvykiuSavivaldybes](pagalbos_skambuciai/IvykiuSavivaldybes.md) | BPC įvykių savivaldybės | `4` | — | — | `6` | Bendrojo pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, teritorinė statistika pagal savivaldybę. |
| [IvykiuLaikas](pagalbos_skambuciai/IvykiuLaikas.md) | BPC įvykių laikas | `4` | — | — | `7` | Bendrojo pagalbos centro (BPC) pagalbos telefonu registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, paros meto statistika. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/bpc/pagalbos_skambuciai (https://data.gov.lt/datasets/1763/)
