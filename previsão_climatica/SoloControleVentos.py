import random

class SoloControleVentos:
    """Classe para simulação de previsão do solo e controle de ventos."""

    TEMPERATURA_MINIMA = 10
    TEMPERATURA_MAXIMA = 30
    UMIDADE_SOLO_MINIMA = 20
    UMIDADE_SOLO_MAXIMA = 80

    DIRECOES_VENTO = ['Norte', 'Nordeste', 'Leste', 'Sudeste', 'Sul', 'Sudoeste', 'Oeste', 'Noroeste']
    VENTOS_NORTE = ['Norte', 'Nordeste', 'Noroeste']
    VENTOS_SUL = ['Sul', 'Sudeste', 'Sudoeste']

    def __init__(self):
        """Inicializa os atributos da classe."""
        self._temperatura = random.randint(SoloControleVentos.TEMPERATURA_MINIMA, SoloControleVentos.TEMPERATURA_MAXIMA)
        self._umidade_solo = random.randint(SoloControleVentos.UMIDADE_SOLO_MINIMA, SoloControleVentos.UMIDADE_SOLO_MAXIMA)
        self._direcao_vento = random.choice(SoloControleVentos.DIRECOES_VENTO)

    def _ajustar_umidade_solo(self, umidade):
        """Garante que a umidade do solo esteja dentro dos limites."""
        return max(SoloControleVentos.UMIDADE_SOLO_MINIMA, min(umidade, SoloControleVentos.UMIDADE_SOLO_MAXIMA))

    def obter_condicao(self):
        """Retorna a condição do solo baseada na umidade."""
        if self._umidade_solo < 40:
            return "Seco"
        elif self._umidade_solo < 70:
            return "Moderado"
        else:
            return "Úmido"

    def obter_controle_ventos(self):
        """Fornece uma sugestão de controle de ventos com base na direção."""
        if self._direcao_vento in SoloControleVentos.VENTOS_NORTE:
            return "Proteja as áreas expostas ao vento do Norte."
        elif self._direcao_vento in SoloControleVentos.VENTOS_SUL:
            return "Prepare-se para possíveis ventos fortes do Sul."
        else:
            return "Condições de vento moderadas."

    def simular_variacao_solo(self):
        """Simula uma variação na condição do solo."""
        self._temperatura += random.randint(-1, 1)
        self._umidade_solo = self._ajustar_umidade_solo(self._umidade_solo + random.randint(-5, 5))
        print("Variação na condição do solo simulada com sucesso.")

    def __str__(self):
        """Retorna uma representação em string da previsão do solo e controle de ventos."""
        return f"Temperatura: {self._temperatura}°C, Umidade do Solo: {self._umidade_solo}%, Condição do Solo: {self.obter_condicao()}, Direção do Vento: {self._direcao_vento}"

    def detalhes_clima(self):
        """Retorna detalhes adicionais sobre o clima."""
        return f"O clima está {self.obter_condicao().lower()}, com ventos predominantes do {self._direcao_vento.lower()}."

    def ajustar_temperatura(self, nova_temperatura):
        """Permite ajustar manualmente a temperatura."""
        self._temperatura = nova_temperatura

    def ajustar_umidade(self, nova_umidade):
        """Permite ajustar manualmente a umidade do solo."""
        self._umidade_solo = self._ajustar_umidade_solo(nova_umidade)

# Exemplo de uso
if __name__ == "__main__":
    previsao_solo = SoloControleVentos()
    print(previsao_solo)
    print(previsao_solo.obter_controle_ventos())
    previsao_solo.simular_variacao_solo()
    print(previsao_solo)
    print(previsao_solo.detalhes_clima())
    previsao_solo.ajustar_temperatura(25)
    previsao_solo.ajustar_umidade(75)
    print(previsao_solo)
