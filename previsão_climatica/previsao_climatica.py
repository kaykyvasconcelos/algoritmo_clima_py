import random

class PrevisaoClimatica:
    """Classe para simulação de previsão climática."""

    # Definindo constantes para os limites de temperatura
    TEMPERATURA_MINIMA_FRIA = 0
    TEMPERATURA_MAXIMA_AGRADAVEL = 20
    TEMPERATURA_MAXIMA_QUENTE = 40

    def __init__(self):
        # Inicializando a temperatura e umidade com valores aleatórios
        self.temperatura = random.randint(PrevisaoClimatica.TEMPERATURA_MINIMA_FRIA, PrevisaoClimatica.TEMPERATURA_MAXIMA_QUENTE)
        self.umidade = random.randint(0, 100)
        self.precipitacao = random.choice(['Chuva', 'Neve', 'Nublado', 'Ensolarado', 'Tempestade'])

    def obter_condicao(self):
        """Retorna a condição climática baseada na temperatura."""
        # Verificando a temperatura para determinar a condição climática
        if self.temperatura < PrevisaoClimatica.TEMPERATURA_MAXIMA_AGRADAVEL:
            return "Frio"  # Retorna 'Frio' se a temperatura for menor que o limite agradável
        elif self.temperatura < PrevisaoClimatica.TEMPERATURA_MAXIMA_QUENTE:
            return "Agradável"  # Retorna 'Agradável' se a temperatura estiver entre os limites agradável e quente
        else:
            return "Quente"  # Retorna 'Quente' se a temperatura ultrapassar o limite quente

    def obter_dica(self):
        """Fornece uma dica com base na condição climática."""
        condicao = self.obter_condicao()
        if condicao == "Frio":
            return "Use roupas quentes e aproveite uma xícara de chocolate quente!"
        elif condicao == "Agradável":
            return "Aproveite o clima agradável para um passeio ao ar livre."
        else:
            return "Mantenha-se fresco e hidratado durante o dia."

    def alterar_umidade(self, nova_umidade):
        """Altera a umidade para o valor fornecido."""
        if nova_umidade >= 0 and nova_umidade <= 100:
            self.umidade = nova_umidade
            print(f"A umidade foi atualizada para {self.umidade}%.")
        else:
            print("A umidade deve estar entre 0 e 100.")

    def simular_variacao_tempo(self):
        """Simula uma variação no tempo atual."""
        # Variando a temperatura e umidade ligeiramente
        self.temperatura += random.randint(-2, 2)
        self.umidade += random.randint(-5, 5)
        self.precipitacao = random.choice(['Chuva', 'Neve', 'Nublado', 'Ensolarado', 'Tempestade'])
        print("Variação no tempo simulada com sucesso.")

    def alerta_climatico(self):
        """Fornece um alerta climático com base na temperatura e umidade."""
        if self.temperatura > 30:
            return "Alerta de calor: temperatura muito alta!"
        elif self.umidade > 80:
            return "Alerta de umidade: risco de chuvas intensas!"
        else:
            return "Sem alertas no momento."

    def __str__(self):
        """Retorna uma representação em string da previsão climática."""
        # Retorna uma string formatada com temperatura, umidade, condição climática e precipitação
        return f"Temperatura: {self.temperatura}°C, Umidade: {self.umidade}%, Condição: {self.obter_condicao()}, Precipitação: {self.precipitacao}"

def previsao_climatica():
    """Retorna uma instância de PrevisaoClimatica."""
    return PrevisaoClimatica()

# Exemplo de uso
previsao = previsao_climatica()  # Cria uma nova instância de PrevisaoClimatica
print(previsao)  # Imprime a representação em string da previsão climática
print(previsao.obter_dica())  # Imprime uma dica com base na condição climática
previsao.simular_variacao_tempo()  # Simula uma variação no tempo
print(previsao)  # Imprime a representação atualizada da previsão climática
previsao.alterar_umidade(80)  # Altera a umidade para 80%
print(previsao)  # Imprime a representação atualizada da previsão climática
print(previsao.alerta_climatico())  # Verifica se há alertas climáticos com base na previsão atual
