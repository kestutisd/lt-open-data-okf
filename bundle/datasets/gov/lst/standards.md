---
type: Dataset
title: "Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė"
description: "Kaupiama ir pateikiama informacija apie Lietuvos standartus (standarto žymuo, pavadinimas, išleidimo data, panaikinimo data, taikymo sritis lietuvių ir anglų kalbomis, kita informacija), nacionalinių, tarptautinių ir Europos standartų projektus, jų rengimo etapus, ryšius su..."
resource: "https://get.data.gov.lt/datasets/gov/lst/standards"
tags: [gov, lst, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/standards"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė

- **Namespace:** `datasets/gov/lst/standards`[^manifest]
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `43` (43 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1636/`[^dcat]
- **Publisher (`dct:publisher`):** Lietuvos standartizacijos departamentas[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lst/standards`[^dcat]
- **Portal Title (`@lt`):** Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė[^dcat]
- **Portal Title (`@en`):** Bibliographic database of Lithuanian standards and other standardisation deliverables[^dcat]
- **Issued (`dct:issued`):** `2023-01-05`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-02`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2021-10-16` .. `2026-10-25`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Kaupiama ir pateikiama informacija apie Lietuvos standartus (standarto žymuo, pavadinimas, išleidimo data, panaikinimo data, taikymo sritis lietuvių ir anglų kalbomis, kita informacija), nacionalinių, tarptautinių ir Europos standartų projektus, jų rengimo etapus, ryšius su galiojančiais standartais, Lietuvos standartizacijos departamento technikos komitetus (LST TK) ir jų ryšius su tarptautinių standartizacijos institucijų ir Europos standartizacijos organizacijų technikos komitetais. Standartų tekstai atvirų duomenų formatu negali būti pateikti, kadangi standartai yra autorių teisių objektas.[^dcat]

### Portal Description (`@en`)

The database contains information on Lithuanian standards (standard number, title, date of publication, date of withdrawal, scope in Lithuanian and English, other information), national, international, and European draft-standards, their development stages, their relation to standards, technical committees of the Lithuanian Standards Board (LST TK) and their relations with technical committees of international standardisation institutions and European standardisation organisations. Considering that standards are subject to copyright, their texts cannot be provided in open data format.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TermApprovedBy](standards/TermApprovedBy.md) | — | — | `id` | — | `2` | Standarte nurodyto termino straipsnį aprobavęs subjektas |
| [TermSource](standards/TermSource.md) | — | — | `id` | — | `2` | Šaltinis iš kur paimtas terminas (iš terminų standarto arba iš standarto apibrėžimų skyriaus) |
| [ActionType](standards/ActionType.md) | — | — | `id` | — | `3` | Standarto rengimo eiga (etapai, kurie nurodo kokius veiksmus sistemoje turi atlikti departamento darbuotojas) |
| [DegreeOfEquivalence](standards/DegreeOfEquivalence.md) | — | — | `id` | — | `3` | Nacionalinio standarto atitikties tarptautiniam standartui laipsnis (tapatus, modifikuotas, nelygiavertis, nacionalinis) |
| [ForeignTcMembershipStatus](standards/ForeignTcMembershipStatus.md) | — | — | `id` | — | `2` | LST TK dalyvavimas tarptautinių standartizacijos organizacijų veikloje tikrojo nario arba nario stebėtojo teisėmis |
| [ImplementationType](standards/ImplementationType.md) | — | — | `id` | — | `2` | Tarptautinių ir Europos standartų perėmimo nacionaliniais standartais būdai (atgaminimo, vertimo, atgaminimo ir vertimo, patvirtinimo) |
| [LRLawStatementType](standards/LRLawStatementType.md) | — | — | `id` | — | `2` | Europos Sąjungos direktyvą įgyvendinančio nacionalinio teisės akto tipas (įstatymas, nutarimas, įsakymas, taisyklės) |
| [Language](standards/Language.md) | — | — | `id` | — | `3` | Kalbos ir jų kodai |
| [OrganisationUnitStatus](standards/OrganisationUnitStatus.md) | — | — | `id` | — | `2` | Lietuvos standartizacijos departamento technikos komitetų veiklos būsena (aktyvus, sustabdytas, likviduotas) |
| [OrganisationUnitType](standards/OrganisationUnitType.md) | — | — | `id` | — | `3` | Lietuvos standartizacijos departamento struktūriniai subjektai (vidinis skyrius, darbo grupė, technikos komitetas, laikinoji darbo grupė, terminologijos... |
| [ProjectNotificationStatus](standards/ProjectNotificationStatus.md) | — | — | `id` | — | `4` | Nacionalinio standarto projekto notifikavimo CEN arba CLC statusas (nauja darbo tema, projektas pateiktas viešai apklausai) |
| [ProjectStatus](standards/ProjectStatus.md) | — | — | `id` | — | `2` | Projekto rengimo būsena (aktyvus, atmestas, sujungtas, nepatvirtintas, pabaigtas, išverstas, išskaidytas) |
| [ProjectType](standards/ProjectType.md) | — | — | `id` | — | `2` | Rengiamo projekto tipas (pagrindinis, keitinys, pataisa, aiškinamasis lapas, pagrindinis+keitinys, pagrindinis+keitinys+pataisa, pagrindinis+pataisa) |
| [ProjectRelationType](standards/ProjectRelationType.md) | — | — | `id` | — | `2` | Projekto ryšys su standartu |
| [StandardDocumentType](standards/StandardDocumentType.md) | — | — | `id` | — | `2` | Standarto dokumento tipas (publikuotas dokumentas) |
| [StandardNotificationState](standards/StandardNotificationState.md) | — | — | `id` | — | `3` | Nacionalinio standarto projekto notifikavimo CEN arba CLC būsena (keitinys, pataisa, peržiūra) |
| [StandardRelationType](standards/StandardRelationType.md) | — | — | `id` | — | `3` | Standartų tarpusavio ryšiai (pakeičia, keičiantis) |
| [StandardStatus](standards/StandardStatus.md) | — | — | `id` | — | `2` | Standarto leidybos būsenos (publikuotas, nepublikuotas, panaikintas) |
| [TextType](standards/TextType.md) | — | — | `id` | — | `2` | Su standartu susijusios tekstinės informacijos tipai |
| [TypeOfPublication](standards/TypeOfPublication.md) | — | — | `id` | — | `2` | Standartų ir standartizacijos leidinių bei jų projektų nomenklatūra |
| [Directive](standards/Directive.md) | — | — | `id` | — | `6` | Europos Sąjungos direktyvos |
| [ICS](standards/ICS.md) | — | — | `id` | — | `6` | Tarptautinė standartų klasifikacija (ICS), ją sudaro sritys, grupės ir pogrupiai |
| [Organisation](standards/Organisation.md) | — | — | `id` | — | `7` | Tarptautinės standartizacijos institucijos, Europos standartizacijos organizacijos ir nacionalinė standartizacijos institucija |
| [Project](standards/Project.md) | — | — | `id` | — | `23` | Nacionalinių, tarptautinių ir Europos standartų projektų duomenys |
| [ProjectStage](standards/ProjectStage.md) | — | — | `id` | — | `15` | Standarto projekto rengimo etapai |
| [ICSRemark](standards/ICSRemark.md) | — | — | `id` | — | `4` | Tarptautinės standartų klasifikacijos (ICS) sričių, grupių ar pogrupių paaiškinimai |
| [LRLawStatement](standards/LRLawStatement.md) | — | — | `id` | — | `13` | Nacionalinių teisės aktų, kuriais į nacionalinę teisę perkelta Europos Sąjungos direktyva arba standartas turi nuokrypą arba standartas turi išskirtinę... |
| [Stage](standards/Stage.md) | — | — | `id` | — | `5` | Standarto rengimo etapų duomenys (etapo kodas, pavadinimas, atlikimo terminas) |
| [ForeignTC](standards/ForeignTC.md) | — | — | `id` | — | `8` | Tarptautinių standartizacijos institucijų ir Europos standartizacijos organizacijų technikos komitetai ir jų darbo grupės |
| [OrganisationUnit](standards/OrganisationUnit.md) | — | — | `id` | — | `11` | Lietuvos standartizacijos departamento technikos komitetai ir laikinosios darbo grupės |
| [RelatedProject](standards/RelatedProject.md) | — | — | `parent_project, child_project` | — | `3` | Projekto ryšys su pagrindiniu standartu (keičiantis, keitinys, pataisa) |
| [Document](standards/Document.md) | — | — | `id` | — | `10` | Duomenys apie išleistą standartą |
| [OrganisationUnitRelation](standards/OrganisationUnitRelation.md) | — | — | `organisation_unit, foreign_tc` | — | `2` | Lietuvos standartizacijos departamento technikos komitetų ryšiai su tarptautinių standartizacijos institucijų ir Europos standartizacijos organizacijų... |
| [OrganisationUnitText](standards/OrganisationUnitText.md) | — | — | `id` | — | `5` | Lietuvos standartizacijos departamento technikos komitetų ir laikinųjų darbo grupių duomenys (pavadinimai, veiklos sritys, veiklos rizikos) |
| [ProjectForeignTC](standards/ProjectForeignTC.md) | — | — | `project, foreign_tc` | — | `2` | Standarto projektą parengęs tarptautinės standartizacijos institucijos arba Europos standartizacijos organizacijos technikos komitetas |
| [Standard](standards/Standard.md) | — | — | `id` | — | `44` | Duomenys apie Lietuvos standartus (standarto žymuo, išleidimo data, panaikinimo data, atitikties laipsnis ir kt. |
| [DocumentFile](standards/DocumentFile.md) | — | — | `id` | — | `7` | Duomenys apie standarto dokumentų tipus ir jų formatus |
| [RelatedStandard](standards/RelatedStandard.md) | — | — | `parent_standard, child_standard` | — | `3` | Standarto ryšys su kitais standartais (pakeičia, keitinys, pataisa) |
| [StandardDirective](standards/StandardDirective.md) | — | — | `directive, standard` | — | `10` | Standarto ryšys su Europos Sąjungos direktyvomis |
| [StandardDocument](standards/StandardDocument.md) | — | — | `standard, document` | — | `3` | Duomenys apie standarto dokumentus ir jų tipus |
| [StandardICS](standards/StandardICS.md) | — | — | `standard, ics` | — | `2` | Standartui priskirtos tarptautinės standartų klasifikacijos sritys, grupės ir pogrupiai |
| [StandardLRLawStatement](standards/StandardLRLawStatement.md) | — | — | `standard, lr_law_statement` | — | `2` | Standartų nuorodinių žymenų ryšys su nacionaliniais teisės aktais |
| [Text](standards/Text.md) | — | — | `id` | — | `5` | Su standartu susijusi tekstinė informacija (standarto pavadinimas (antraštė), aprašymas (abstract), taikymo sritis (scope) lietuvių ir anglų kalbomis... |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/standards (https://data.gov.lt/datasets/1636/)
