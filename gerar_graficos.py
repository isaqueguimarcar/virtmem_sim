import pandas as pd
import matplotlib.pyplot as plt
import os

# Ler CSV
df = pd.read_csv("resultados.csv")

# Criar diretório para gráficos
os.makedirs("graficos", exist_ok=True)

# Lista de traces
traces = df["trace"].unique()

for trace in traces:

    dados_trace = df[df["trace"] == trace]

    # ==========================
    # Gráfico de Page Faults
    # ==========================
    plt.figure(figsize=(10, 6))

    for algoritmo in dados_trace["algoritmo"].unique():

        dados_alg = dados_trace[dados_trace["algoritmo"] == algoritmo]

        plt.plot(
            dados_alg["frames"],
            dados_alg["page_faults"],
            marker='o',
            label=algoritmo.upper()
        )

    plt.title(f"Page Faults - {trace}")
    plt.xlabel("Número de Frames")
    plt.ylabel("Quantidade de Page Faults")
    plt.xticks([2, 4, 8, 16, 32, 64])
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    nome = trace.replace(".trace", "")
    plt.savefig(f"graficos/{nome}_faults.png", dpi=300)

    plt.close()

    # ==========================
    # Gráfico de Pages Written
    # ==========================
    plt.figure(figsize=(10, 6))

    for algoritmo in dados_trace["algoritmo"].unique():

        dados_alg = dados_trace[dados_trace["algoritmo"] == algoritmo]

        plt.plot(
            dados_alg["frames"],
            dados_alg["pages_written"],
            marker='o',
            label=algoritmo.upper()
        )

    plt.title(f"Pages Written - {trace}")
    plt.xlabel("Número de Frames")
    plt.ylabel("Quantidade de Pages Written")
    plt.xticks([2, 4, 8, 16, 32, 64])
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    plt.savefig(f"graficos/{nome}_written.png", dpi=300)

    plt.close()

print("Gráficos gerados com sucesso!")
print("Arquivos salvos na pasta: graficos/")