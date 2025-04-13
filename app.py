import streamlit as st
import os
from database import RedshiftConnection
from nl_to_sql import NLToSQL

def main():
    st.title("Natural Language to SQL Query Converter")
    
    # Initialize connections
    db = RedshiftConnection()
    nl_to_sql = NLToSQL(os.getenv('OPENAI_API_KEY'))
    
    # Connect to Redshift
    if not db.connect():
        st.error("Failed to connect to Redshift")
        return
        
    # Input for natural language query
    nl_query = st.text_area("Enter your question in natural language:", 
                           "Show me all orders from customers in New York")
    
    if st.button("Generate and Execute Query"):
        # Generate SQL query
        sql_query = nl_to_sql.generate_sql(nl_query)
        
        # Display generated SQL
        st.subheader("Generated SQL Query:")
        st.code(sql_query, language='sql')
        
        # Execute query and show results
        if st.button("Execute Query"):
            results = db.execute_query(sql_query)
            if results is not None:
                st.subheader("Query Results:")
                st.dataframe(results)
            else:
                st.error("Error executing query")

if __name__ == "__main__":
    main()