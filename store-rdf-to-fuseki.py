import SemanticOperations

semantic_server = SemanticOperations.SemanticOperations('drd', '3030')
data = (
            ('Device', 'rt', 'Temperature'),
            ('Device', 'ep', 'coap://device/temperature')
        )
semantic_server.insertData(data)