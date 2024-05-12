import random

class PrevisaoLua:
    """Classe para simulação de previsão do clima com influência da lua."""

    TEMPERATURA_MINIMA = 10
    TEMPERATURA_MAXIMA = 30
    UMIDADE_SOLO_MINIMA = 20
    UMIDADE_SOLO_MAXIMA = 80

    DIRECOES_VENTO = ['Norte', 'Nordeste', 'Leste', 'Sudeste', 'Sul', 'Sudoeste', 'Oeste', 'Noroeste']
    VENTOS_NORTE = ['Norte', 'Nordeste', 'Noroeste']
    VENTOS_SUL = ['Sul', 'Sudeste', 'Sudoeste']

    FASES_LUA = ['Nova', 'Crescente', 'Cheia', 'Minguante']

    def __init__(self):
        """Inicializa os atributos da classe."""
        self._temperatura = random.randint(PrevisaoLua.TEMPERATURA_MINIMA, PrevisaoLua.TEMPERATURA_MAXIMA)
        self._umidade_solo = random.randint(PrevisaoLua.UMIDADE_SOLO_MINIMA, PrevisaoLua.UMIDADE_SOLO_MAXIMA)
        self._direcao_vento = random.choice(PrevisaoLua.DIRECOES_VENTO)
        self._fase_lua = random.choice(PrevisaoLua.FASES_LUA)

    def _ajustar_umidade_solo(self, umidade):
        """Garante que a umidade do solo esteja dentro dos limites."""
        return max(PrevisaoLua.UMIDADE_SOLO_MINIMA, min(umidade, PrevisaoLua.UMIDADE_SOLO_MAXIMA))

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
        if self._direcao_vento in PrevisaoLua.VENTOS_NORTE:
            return "Proteja as áreas expostas ao vento do Norte."
        elif self._direcao_vento in PrevisaoLua.VENTOS_SUL:
            return "Prepare-se para possíveis ventos fortes do Sul."
        else:
            return "Condições de vento moderadas."

    def obter_influencia_lua(self):
        """Retorna a influência da lua nas condições climáticas."""
        if self._fase_lua == "Cheia":
            return "A lua cheia pode causar marés mais altas e influenciar levemente as condições climáticas."
        elif self._fase_lua == "Nova":
            return "A lua nova geralmente não tem grande influência nas condições climáticas."
        elif self._fase_lua == "Crescente":
            return "A lua crescente pode intensificar ventos e causar mudanças nas marés."
        elif self._fase_lua == "Minguante":
            return "A lua minguante geralmente traz condições climáticas mais estáveis."

    def simular_variacao_solo(self):
        """Simula uma variação na condição do solo."""
        self._temperatura += random.randint(-1, 1)
        self._umidade_solo = self._ajustar_umidade_solo(self._umidade_solo + random.randint(-5, 5))
        print("Variação na condição do solo simulada com sucesso.")

    def __str__(self):
        """Retorna uma representação em string da previsão do clima."""
        return f"Temperatura: {self._temperatura}°C, Umidade do Solo: {self._umidade_solo}%, Condição do Solo: {self.obter_condicao()}, Direção do Vento: {self._direcao_vento}, Fase da Lua: {self._fase_lua}"

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
    previsao_lua = PrevisaoLua()
    print(previsao_lua)
    print(previsao_lua.obter_controle_ventos())
    print(previsao_lua.obter_influencia_lua())
    previsao_lua.simular_variacao_solo()
    print(previsao_lua)
    print(previsao_lua.detalhes_clima())
    previsao_lua.ajustar_temperatura(25)
    previsao_lua.ajustar_umidade(75)
    print(previsao_lua)
