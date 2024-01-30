import streamlit as st
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
# Função para carregar dados de previsão do banco de dados
def load_data():
    conn = psycopg2.connect("dbname=ipea user=postgres password=postgres")
    query = "SELECT * FROM ipea.previsao_preco_petro"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Carregar dados de previsão
df_previsao = load_data()

# Título do Aplicativo
st.title('Previsões do Preço do Petróleo')

# Mostrar dados em um gráfico
st.write("### Previsões para os próximos 7 dias")
plt.figure(figsize=(10, 4))
plt.plot(df_previsao['data_coleta'], df_previsao['preco'], marker='o')
plt.xticks(rotation=45)
plt.xlabel('Data')
plt.ylabel('Preço do Petróleo (USD)')
plt.title('Previsão do Preço do Petróleo')
st.pyplot(plt)
