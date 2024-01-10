class Dicionario:
 
  def __init__(self):
    pass
  
  def standard_stats_squad_serie_a(self):
      texto = """
        Esse dataset contém todas as estatísticas padrões para um time do brasileirão.
        
        - Squad: Nome do time
        - Pl: Número de jogadores utilizados
        - Age: Idade média dos jogadores
        - Poss: Posse de bola média em porcentagem
        - MP: Partidas jogadas
        - Starts: Número de vezes que um jogador iniciou uma partida
        - Min: Minutos jogados
        - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
        - Gls: Número de gols marcados
        - Ast: Número de assistências para gol
        - G+A: Total de gols e assistências
        - G-PK: Gols excluindo pênaltis
        - PK: Número de pênaltis marcados
        - PKatt: Número de pênaltis tentados
        - CrdY: Cartões amarelos recebidos
        - CrdR: Cartões vermelhos recebidos
        - xG: Gols esperados com base nas chances criadas
        - npxG: Gols esperados excluindo pênaltis
        - xAG: Assistências esperadas com base nas chances criadas
        - npxG+xAG: Gols e assistências esperados excluindo pênaltis
        - PrgC: Progressões de bola em campo adversário
        - PrgP: Progressões de passes em campo adversário
      """
      
      return texto
    
  def goalkeeping_stats_squad_opponent_serie_a(self):
    texto = """
      Esses dados representam estatísticas de defesa de times em partidas contra oponentes na Serie A, incluindo métricas como gols sofridos (GA), chutes no alvo (SoTA), defesas feitas (Saves), percentual de defesas (Save%), entre outros. Cada linha corresponde a um time específico ('Squad') em diferentes jogos ('MP'), fornecendo insights sobre o desempenho dos goleiros e da defesa durante a temporada.
      
      - Squad: Nome do time adversário
      - Pl: Número de jogadores utilizados
      - MP: Partidas jogadas
      - Starts: Número de vezes que um jogador iniciou uma partida
      - Min: Minutos jogados
      - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
      - GA: Gols sofridos
      - GA90: Gols sofridos por partida em média
      - SoTA: Chutes no alvo contra o time
      - Saves: Defesas realizadas
      - Save%: Percentual de defesas realizadas
      - W: Vitórias
      - D: Empates
      - L: Derrotas
      - CS: Clean Sheets (partidas sem sofrer gol)
      - CS%: Percentual de Clean Sheets
      - PKatt: Pênaltis sofridos
      - PKA: Pênaltis marcados contra o time
      - PKsv: Pênaltis defendidos
      - PKm: Pênaltis defendidos pelo goleiro
      """
      
    return texto
  
  def goalkeeping_stats_squad_serie_a(self):
    texto = """
      Os dados fornecem estatísticas de defesa de times em partidas contra oponentes na Serie A do futebol brasileiro. Cada linha representa um time específico e apresenta métricas como gols sofridos, chutes no alvo contra o time, defesas realizadas, entre outras estatísticas relacionadas à defesa.
    
      - Squad: Nome do time adversário
      - Pl: Número de jogadores utilizados
      - MP: Partidas jogadas
      - Starts: Número de vezes que um jogador iniciou uma partida
      - Min: Minutos jogados
      - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
      - GA: Gols sofridos
      - GA90: Gols sofridos por partida em média
      - SoTA: Chutes no alvo contra o time
      - Saves: Defesas realizadas
      - Save%: Percentual de defesas realizadas
      - W: Vitórias
      - D: Empates
      - L: Derrotas
      - CS: Clean Sheets (partidas sem sofrer gol)
      - CS%: Percentual de Clean Sheets
      - PKatt: Pênaltis sofridos
      - PKA: Pênaltis marcados contra o time
      - PKsv: Pênaltis defendidos
      - PKm: Pênaltis defendidos pelo goleiro
    """
    
    return texto
  
  def regular_overall_homeaway_serie_a(self):
    texto = """
      A base contém informações sobre o desempenho das equipes ao longo de uma temporada na Série A do Campeonato Brasileiro de Futebol. Os dados abrangem diferentes métricas, incluindo partidas disputadas em casa, fora de casa e o desempenho geral. Fornece estatísticas essenciais como vitórias, empates, derrotas, gols marcados, gols sofridos, saldo de gols, pontos conquistados, pontos por partida, além de métricas esperadas, como gols esperados (xG) e gols esperados contra (xGA). Essas estatísticas são fundamentais para avaliar o desempenho das equipes, oferecendo insights sobre eficiência ofensiva, consistência defensiva e o desempenho projetado com base nos gols esperados.
      - Squad: Nome do time
      - MP: Partidas jogadas
      - W: Vitórias
      - D: Empates
      - L: Derrotas
      - GF: Gols feitos
      - GA: Gols sofridos
      - GD: Saldo de gols (Gols feitos menos Gols sofridos)
      - Pts: Pontos conquistados
      - Pts/MP: Pontos por partida
      - xG: Expected Goals (Gols esperados)
      - xGA: Expected Goals Against (Gols esperados contra)
      - xGD: Expected Goal Difference (Diferença esperada de gols)
      - xGD/90: Expected Goal Difference por 90 minutos
    """
    
    return texto
  
  def regular_overall_season_serie_a(self):
    texto = """
      A base contém informações sobre o desempenho das equipes ao longo de uma temporada na Série A do Campeonato Brasileiro de Futebol. Os dados abrangem diferentes métricas, incluindo partidas disputadas em casa, fora de casa e o desempenho geral. Fornece estatísticas essenciais como vitórias, empates, derrotas, gols marcados, gols sofridos, saldo de gols, pontos conquistados, pontos por partida, além de métricas esperadas, como gols esperados (xG) e gols esperados contra (xGA). Essas estatísticas são fundamentais para avaliar o desempenho das equipes, oferecendo insights sobre eficiência ofensiva, consistência defensiva e o desempenho projetado com base nos gols esperados.
      - Squad: Nome do time
      - MP: Partidas jogadas
      - W: Vitórias
      - D: Empates
      - L: Derrotas
      - GF: Gols feitos
      - GA: Gols sofridos
      - GD: Saldo de gols (Gols feitos menos Gols sofridos)
      - Pts: Pontos conquistados
      - Pts/MP: Pontos por partida
      - xG: Expected Goals (Gols esperados)
      - xGA: Expected Goals Against (Gols esperados contra)
      - xGD: Expected Goal Difference (Diferença esperada de gols)
      - xGD/90: Expected Goal Difference por 90 minutos
    """
    
    return texto
  
  def squad_advanced_defense_opponent_stats_serie_a(self):
    texto = """
      A base contém estatísticas avançadas relacionadas à defesa dos times em jogos contra diferentes oponentes durante a temporada da Série A do Campeonato Brasileiro de Futebol. Essas estatísticas fornecem uma visão detalhada das ações defensivas realizadas pelas equipes em diferentes áreas do campo, incluindo tackles, interceptações, bloqueios de chute, entre outros.
      - Squad: Nome do time adversário
      - Pl: Número de partidas
      - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
      - Tkl: Tackles
      - TklW: Tackles ganhos
      - Def 3rd: Ações defensivas na terceira parte defensiva do campo
      - Mid 3rd: Ações defensivas na terceira parte intermediária do campo
      - Att 3rd: Ações defensivas na terceira parte ofensiva do campo
      - Tkl%: Percentual de sucesso nos tackles
      - Lost: Bolas perdidas
      - Blocks: Blocos de chutes
      - Sh: Chutes bloqueados
      - Pass: Passes
      - Int: Intercepções
      - Tkl+Int: Tackles + Intercepções
      - Clr: Bolas afastadas
      - Err: Erros individuais
    """
    
    return texto
  
  def squad_advanced_defense_stats_serie_a(self):
    texto = """
      A base contém estatísticas avançadas relacionadas à defesa das equipes durante a temporada da Série A do Campeonato Brasileiro de Futebol. As estatísticas fornecem uma visão detalhada das ações defensivas em diferentes áreas do campo, incluindo tackles, interceptações, passes bloqueados, entre outras métricas defensivas.
    - Squad: Nome do time
    - Pl: Número de partidas
    - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
    - Tkl: Tackles
    - TklW: Tackles ganhos
    - Def 3rd: Ações defensivas na terceira parte defensiva do campo
    - Mid 3rd: Ações defensivas na terceira parte intermediária do campo
    - Att 3rd: Ações defensivas na terceira parte ofensiva do campo
    - Tkl%: Percentual de sucesso nos tackles
    - Lost: Bolas perdidas
    - Blocks: Chutes bloqueados
    - Sh: Chutes bloqueados
    - Pass: Passes
    - Int: Interceptações
    - Tkl+Int: Tackles + Interceptações
    - Clr: Bolas afastadas
    - Err: Erros individuais
    """
    
    return texto
  
  def squad_advanced_gca_opponent_stats_serie_a(self):
    texto = """
      A base contém estatísticas avançadas sobre as ações de criação de gols adversárias durante a temporada da Série A do Campeonato Brasileiro de Futebol. Ela inclui diferentes métricas relacionadas a ações de ataque que levam à criação de gols, como chutes, passes, dribles, entre outros eventos ofensivos.
    - Squad: Nome do time
    - Pl: Número de partidas
    - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
    - SCA: Ações de criação de chutes
    - SCA90: Ações de criação de chutes por 90 minutos
    - PassLive: Passes em jogo
    - PassDead: Passes de bola parada
    - TO: Dribles bem-sucedidos
    - Sh: Chutes
    - Fld: Dribles bem-sucedidos
    - Def: Dribles bem-sucedidos
    - GCA: Ações de criação de gols
    - GCA90: Ações de criação de gols por 90 minutos
    - PassLive: Passes em jogo que resultam em gols
    - PassDead: Passes de bola parada que resultam em gols
    - TO: Dribles bem-sucedidos que resultam em gols
    - Sh: Chutes que resultam em gols
    - Fld: Dribles bem-sucedidos que resultam em gols
    - Def: Dribles bem-sucedidos que resultam em gols
    """
    
    return texto
  
  def squad_advanced_gca_stats_serie_a(self):
    texto = """
      A base contém estatísticas avançadas sobre as ações de criação de gols durante a temporada da Série A do Campeonato Brasileiro de Futebol. Ela inclui diferentes métricas relacionadas a ações de ataque que levam à criação de gols, como chutes, passes, dribles, entre outros eventos ofensivos.
      - Squad: Nome do time
      - Pl: Número de partidas
      - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
      - SCA: Ações de criação de chutes
      - SCA90: Ações de criação de chutes por 90 minutos
      - PassLive: Passes em jogo
      - PassDead: Passes de bola parada
      - TO: Dribles bem-sucedidos
      - Sh: Chutes
      - Fld: Dribles bem-sucedidos
      - Def: Dribles bem-sucedidos
      - GCA: Ações de criação de gols
      - GCA90: Ações de criação de gols por 90 minutos
      - PassLive: Passes em jogo que resultam em gols
      - PassDead: Passes de bola parada que resultam em gols
      - TO: Dribles bem-sucedidos que resultam em gols
      - Sh: Chutes que resultam em gols
      - Fld: Dribles bem-sucedidos que resultam em gols
      - Def: Dribles bem-sucedidos que resultam em gols
    """
    
    return texto
  
  
  def squad_advanced_goalkeeping_opponent_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas avançadas relacionadas às ações defensivas dos times adversários durante a temporada da Série A do Campeonato Brasileiro de Futebol. As métricas incluem estatísticas de gols sofridos, chutes concedidos, defesas de goleiro, entre outras.
    - Squad: Nome do time
    - Pl: Número de partidas
    - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
    - GA: Gols sofridos
    - PKA: Pênaltis sofridos
    - FK: Chutes de falta
    - CK: Chutes de escanteio
    - OG: Gols contra
    - PSxG: Gols esperados contra (expected goals against)
    - PSxG/SoT: Gols esperados contra por chutes no alvo (expected goals against per shot on target)
    - PSxG+/-: Diferença entre gols esperados contra e gols sofridos
    - /90: Estatísticas por 90 minutos
    - Cmp: Passes completados
    - Att: Passes tentados
    - Cmp%: Porcentagem de passes completados
    - Att (GK): Passes tentados pelo goleiro
    - Thr: Chutes longos
    - Launch%: Porcentagem de lançamentos bem-sucedidos
    - AvgLen: Comprimento médio dos lançamentos
    - Opp: Chances do oponente (opponent's shots)
    - Stp: Defesas do goleiro (saves)
    - Stp%: Porcentagem de defesas do goleiro
    - #OPA: Saídas do gol do goleiro (goalkeeper's actions outside the penalty area)
    - #OPA/90: Saídas do gol por 90 minutos
    - AvgDist: Distância média das ações do goleiro
    """
    
    return texto
  
  def squad_advanced_goalkeeping_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas avançadas relacionadas às ações defensivas dos times durante a temporada da Série A do Campeonato Brasileiro de Futebol. As métricas incluem estatísticas de gols sofridos, chutes concedidos, defesas de goleiro, entre outras.
    - Squad: Nome do time
    - Pl: Número de partidas
    - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
    - GA: Gols sofridos
    - PKA: Pênaltis sofridos
    - FK: Chutes de falta
    - CK: Chutes de escanteio
    - OG: Gols contra
    - PSxG: Gols esperados contra (expected goals against)
    - PSxG/SoT: Gols esperados contra por chutes no alvo (expected goals against per shot on target)
    - PSxG+/-: Diferença entre gols esperados contra e gols sofridos
    - /90: Estatísticas por 90 minutos
    - Cmp: Passes completados
    - Att: Passes tentados
    - Cmp%: Porcentagem de passes completados
    - Att (GK): Passes tentados pelo goleiro
    - Thr: Chutes longos
    - Launch%: Porcentagem de lançamentos bem-sucedidos
    - AvgLen: Comprimento médio dos lançamentos
    - Att: Tentativas de defesa do oponente
    - Launch%: Porcentagem de tentativas de defesa do oponente bem-sucedidas
    - AvgLen: Comprimento médio das tentativas de defesa do oponente
    - Opp: Chances do oponente (opponent's shots)
    - Stp: Defesas do goleiro (saves)
    - Stp%: Porcentagem de defesas do goleiro
    - #OPA: Saídas do gol do goleiro (goalkeeper's actions outside the penalty area)
    - #OPA/90: Saídas do gol por 90 minutos
    - AvgDist: Distância média das ações do goleiro
    """
    
    return texto
  
  
  def squad_advanced_misc_opponent_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas variadas sobre o desempenho dos oponentes durante a temporada da Série A do Campeonato Brasileiro de Futebol. As métricas incluem cartões amarelos, vermelhos, segundos cartões amarelos, faltas, dribles, bolas roubadas, entre outras.
    - Squad: Nome do time
    - Pl: Número de partidas
    - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
    - CrdY: Cartões amarelos
    - CrdR: Cartões vermelhos
    - 2CrdY: Segundos cartões amarelos
    - Fls: Faltas cometidas
    - Fld: Dribles sofridos
    - Off: Impedimentos
    - Crs: Cruzamentos
    - Int: Intercepções
    - TklW: Tackles bem-sucedidos
    - PKwon: Pênaltis ganhos
    - PKcon: Pênaltis sofridos
    - OG: Gols contra
    - Recov: Recuperações de bola
    - Won: Bolas roubadas com sucesso
    - Lost: Bolas roubadas perdidas
    - Won%: Porcentagem de bolas roubadas com sucesso
    """
    
    return texto
  
  def squad_advanced_misc_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas variadas sobre o desempenho das equipes durante a temporada da Série A do Campeonato Brasileiro de Futebol. As métricas incluem cartões amarelos, vermelhos, segundos cartões amarelos, faltas, dribles, bolas roubadas, entre outras.
    - Squad: Nome do time
    - Pl: Número de partidas
    - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
    - CrdY: Cartões amarelos
    - CrdR: Cartões vermelhos
    - 2CrdY: Segundos cartões amarelos
    - Fls: Faltas cometidas
    - Fld: Dribles sofridos
    - Off: Impedimentos
    - Crs: Cruzamentos
    - Int: Intercepções
    - TklW: Tackles bem-sucedidos
    - PKwon: Pênaltis ganhos
    - PKcon: Pênaltis sofridos
    - OG: Gols contra
    - Recov: Recuperações de bola
    - Won: Bolas roubadas com sucesso
    - Lost: Bolas roubadas perdidas
    - Won%: Porcentagem de bolas roubadas com sucesso
    """
    
    return texto