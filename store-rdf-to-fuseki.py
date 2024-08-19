import SemanticOperations

semantic_server = SemanticOperations.SemanticOperations('drd')
data = (
            ('Device', 'rt', 'Temperature'),
            ('Device', 'ep', 'coap://device/temperature')
        )
semantic_server.insertData(data)