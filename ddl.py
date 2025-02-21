from collections import namedtuple
from dataclasses import dataclass

sct_rel = namedtuple("SnomedRelationship", ["name", "typeId"])

@dataclass
class sct:
    concept: str = """
        CREATE NODE TABLE SCT(
            id INT64,
            effectiveTime DATE,
            active BOOLEAN,
            moduleId INT64,
            definitionStatusId INT64,
            fullQualifiedName STRING,
            synonyms STRING[],
            PRIMARY KEY (id)
        );
        """

    @staticmethod
    def relationship(name: str) -> str:
        return f"""
            CREATE REL TABLE {name}(
                FROM SCT to SCT,
                id INT64,
                effectiveTime DATE,
                active BOOLEAN,
                moduleId INT64,
                relationshipGroup INT64,
                typeId INT64,
                characteristicTypeId INT64,
                modifierId INT64,
                fullQualifiedName STRING,
                synonyms STRING[]
            );
            """

    top10_relationships: tuple = (
        sct_rel("IsA", 116680003),
        sct_rel("FindingSite", 363698007),
        sct_rel("AssociatedMorphology", 116676008),
        sct_rel("Method", 260686004),
        sct_rel("Interprets", 363714003),
        sct_rel("SpecimenSourceTopography", 118169006),
        sct_rel("ProcedureSite", 405813007),
        sct_rel("HasBasisOfStrengthSubstance", 732943007),
        sct_rel("HasActiveIngredient", 762949000),
        sct_rel("HasManufacturedDoseForm", 411116001)
    )

@dataclass
class icd:
    Chapter: str = """
        CREATE NODE TABLE ICD10Chapter(
            number INT64,
            rubric STRING,
            PRIMARY KEY (number)
        );
        """
    
    Group: str = """
        CREATE NODE TABLE ICD10Group(
            code STRING,
            rubric STRING,
            PRIMARY KEY (code)
        );
        """
    
    Category3: str = """
        CREATE NODE TABLE ICD10Category3(
            code STRING,
            rubric STRING,
            PRIMARY KEY (code)
        );
        """
    Category4: str = """
        CREATE NODE TABLE ICD10Category4(
            code STRING,
            rubric STRING,
            PRIMARY KEY (code)
        );
        """
    
    IsSubClassOf: str = """
        CREATE REL TABLE IsSubClassOf(
            FROM ICD10Group to ICD10Chapter,
            FROM ICD10Category3 to ICD10Group,
            FROM ICD10Category4 to ICD10Category3
        );
        """