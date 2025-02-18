snomed = {
    "concept":
        """
        CREATE NODE TABLE concept(
            id INT64,
            effectiveTime DATE,
            active BOOLEAN,
            moduleId INT64,
            definitionStatusId INT64,
            PRIMARY KEY (id)
        );
        """,
    "relationship":
        """
        CREATE REL TABLE relationship(
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