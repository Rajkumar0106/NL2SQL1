from config import TABLE_RELATIONSHIPS

class SchemaManager:
    def __init__(self):
        self.relationships = TABLE_RELATIONSHIPS
        
    def get_join_conditions(self, tables):
        join_conditions = []
        processed_tables = set()
        
        for table in tables:
            if table in self.relationships:
                for related_table, conditions in self.relationships[table].items():
                    if related_table in tables and related_table not in processed_tables:
                        for left, right in conditions.items():
                            join_conditions.append(f"{left} = {right}")
                processed_tables.add(table)
                
        return join_conditions