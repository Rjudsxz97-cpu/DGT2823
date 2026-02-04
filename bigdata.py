import pandas as pd

# -----------------------------
# MICROATIVIDADE 1
# Ler o CSV com Pandas
# -----------------------------
df = pd.read_csv("dados.csv", sep=";", engine="python")
print("\n=== Dados originais ===")
print(df)


# -----------------------------
# MICROATIVIDADE 2
# Criar subconjunto com 3 colunas
# -----------------------------
subset = df[["ID", "Date", "Calories"]]
print("\n=== Subconjunto ===")
print(subset)


# -----------------------------
# MICROATIVIDADE 3
# Configurar exibição de linhas
# -----------------------------
pd.set_option("display.max_rows", 9999)
print("\n=== DataFrame completo (to_string) ===")
print(df.to_string())


# -----------------------------
# MICROATIVIDADE 4
# Exibir primeiros e últimos 10 registros
# -----------------------------
print("\n=== Primeiras 10 linhas ===")
print(df.head(10))

print("\n=== Últimas 10 linhas ===")
print(df.tail(10))


# -----------------------------
# MICROATIVIDADE 5
# Informações gerais
# -----------------------------
print("\n=== Informações gerais do DataFrame ===")
print(df.info())
print("\nDescrição:")
print(df.describe(include="all"))


# ==============================
# TRABALHO PRÁTICO
# Limpeza e tratamento de dados
# ==============================

# Copiar o dataframe
df_clean = df.copy()

# Substituir NaN em Calories por 0
df_clean["Calories"] = df_clean["Calories"].fillna(0)
print("\n=== Após substituir NaN em Calories por 0 ===")
print(df_clean)

# Substituir NaN em Date por valor placeholder
df_clean["Date"] = df_clean["Date"].fillna("1900/01/01")
print("\n=== Após substituir NaN em Date por '1900/01/01' ===")
print(df_clean)

# Tentar converter para datetime (vai falhar com o 1900/01/01)
# Corrigir manualmente
df_clean["Date"] = df_clean["Date"].replace("1900/01/01", pd.NA)
df_clean["Date"] = pd.to_datetime(df_clean["Date"], errors="coerce")

# Ajustar o valor mal formatado 20201226
df_clean["Date"] = df_clean["Date"].fillna(
    pd.to_datetime(df_clean["Date"].replace("20201226", "2020/12/26"), errors="coerce")
)

print("\n=== Após converter Date para datetime ===")
print(df_clean)

# Remover registros com Date nulo (linha 22)
df_clean = df_clean.dropna(subset=["Date"])

print("\n=== DataFrame final ===")
print(df_clean)
