import openai
from schema_manager import SchemaManager

class NLToSQL:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.schema_manager = SchemaManager()
        
    def generate_sql(self, natural_language_query):
        # Create a prompt that includes schema information and relationships
        prompt = f"""
        Given the following natural language query: "{natural_language_query}"
        Convert it to a SQL query using the defined table relationships.
        Make sure to use appropriate JOIN conditions based on the table relationships.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a SQL query generator."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating SQL: {e}"