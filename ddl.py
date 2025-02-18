snomed = {
    "Concept":
        """
        CREATE NODE TABLE Concept(
            id INT64,
            effectiveTime DATE,
            active BOOLEAN,
            moduleId INT64,
            definitionStatusId INT64,
            fullQualifiedName STRING,
            synonyms STRING[],
            PRIMARY KEY (id)
        );
        """,
    "Relationship":
        """
        CREATE REL TABLE Relationship(
            FROM concept to concept,
            id INT64,
            effectiveTime DATE,
            active BOOLEAN,
            moduleId INT64,
            relationshipGroup INT64,
            typeId INT64,
            characteristicTypeId INT64,
            modifierId INT64
        );
        """
}