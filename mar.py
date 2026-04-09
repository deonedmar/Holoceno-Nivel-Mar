import matplotlib.pyplot as plt

# Dados do texto original (Anos A.P. vs. Nível Relativo do Mar em metros)
# Invertemos os anos para que o "presente" (0 anos A.P.) esteja à direita do gráfico.
# Os pontos de dados foram estimados do texto para criar uma curva representativa.
years_bp = [7100, 5100, 4900, 4200, 3900, 3600, 3000, 2800, 2700, 2500, 0] # Anos Antes do Presente
sea_level_m = [0.0, 4.8, 3.0, 1.0, -0.5, 3.5, 1.0, -0.5, 1.0, 2.5, 0.0] # Nível do mar em metros (relativo ao atual)

# Reverter os anos para que 0 A.P. (Presente) esteja à direita no eixo X
# Eixo X será "Tempo (Anos antes do Presente)"
# Isso é opcional, mas frequentemente mais intuitivo para gráficos históricos
# Se preferir que o passado mais distante esteja à direita, remova .reverse()
years_bp_reversed = sorted(years_bp, reverse=True) # Para exibir o tempo do mais antigo para o mais recente
sea_level_m_reordered = [sea_level_m[years_bp.index(y)] for y in years_bp_reversed]


# Plotar o gráfico
plt.figure(figsize=(12, 6)) # Define o tamanho da figura do gráfico
plt.plot(years_bp_reversed, sea_level_m_reordered, marker='o', linestyle='-', color='blue') # Plota a linha

# Adicionar marcadores e anotações para os eventos chave
# Picos e Vales específicos
key_events = {
    7100: "Primeiro 'Zero Atual'",
    5100: "1º Máximo (+4.8m)",
    3900: "Mínimo (~0m)",
    3600: "2º Máximo (+3.5m)",
    2800: "Mínimo (~0m)",
    2500: "3º Máximo (+2.5m)",
    0: "Posição Atual"
}

for year, label in key_events.items():
    if year in years_bp: # Verifica se o ano está nos nossos dados originais
        idx = years_bp.index(year)
        plt.annotate(f"{label} ({year} AP)",
                     (year, sea_level_m[idx]), # Coordenadas do ponto
                     textcoords="offset points", # Método de posicionamento do texto
                     xytext=(0,10), # Deslocamento do texto em relação ao ponto
                     ha='center', # Alinhamento horizontal do texto
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2", color='gray')) # Seta
        plt.plot(year, sea_level_m[idx], 'ro') # Desenha um ponto vermelho para o evento

# Adicionar linha de referência para o nível do mar atual (0 metros)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8, label='Nível do Mar Atual (0m)')

# Configurações do gráfico
plt.title('Variações do Nível Relativo do Mar no Holoceno')
plt.xlabel('Anos Antes do Presente (A.P.)')
plt.ylabel('Nível Relativo do Mar (metros)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.gca().invert_xaxis() # Inverte o eixo X para que 0 A.P. (presente) fique à direita
plt.legend()
plt.tight_layout() # Ajusta o layout para evitar sobreposição
plt.show()

