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
  
  def squad_advanced_passing_opponent_squad_serie_a(self):
    texto = """
      Esta base contém estatísticas detalhadas sobre os passes de cada equipe durante a temporada da Série A do Campeonato Brasileiro de Futebol. Inclui informações como passes completos, totais, percentual de passes completados, distância total dos passes, distância progressiva dos passes, assistências esperadas (xA), entre outros.
    - Squad: Nome do time adversário
    - Pl: Número de jogadores
    - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
    - Cmp: Passes completos
    - Att: Total de tentativas de passes
    - Cmp%: Percentual de passes completados
    - TotDist: Distância total dos passes em jardas
    - PrgDist: Distância progressiva dos passes em jardas
    - Ast: Assistências (passes que levaram a finalizações)
    - xAG: Assistências esperadas em gols
    - xA: Assistências esperadas
    - A-xAG: Diferença entre assistências e assistências esperadas em gols
    - KP: Chances de criação de gol (Key Passes)
    - 1/3: Passes feitos no terço final do campo
    - PPA: Passes progressivos para a área
    - CrsPA: Passes progressivos para a área após cruzamento
    - PrgP: Passes progressivos completos
    """
    
    return texto
  
  def squad_advanced_passing_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas detalhadas sobre os passes de cada equipe durante a temporada da Série A do Campeonato Brasileiro de Futebol. Inclui informações como passes completos, totais, percentual de passes completados, distância total dos passes, distância progressiva dos passes, assistências esperadas (xA), entre outros.
    - Squad: Nome do time
    - Pl: Número de jogadores
    - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
    - Cmp: Passes completos
    - Att: Total de tentativas de passes
    - Cmp%: Percentual de passes completados
    - TotDist: Distância total dos passes em jardas
    - PrgDist: Distância progressiva dos passes em jardas
    - Ast: Assistências (passes que levaram a finalizações)
    - xAG: Assistências esperadas em gols
    - xA: Assistências esperadas
    - A-xAG: Diferença entre assistências e assistências esperadas em gols
    - KP: Chances de criação de gol (Key Passes)
    - 1/3: Passes feitos no terço final do campo
    - PPA: Passes progressivos para a área
    - CrsPA: Passes progressivos para a área após cruzamento
    - PrgP: Passes progressivos completos
    """
    
    return texto
  
  def squad_advanced_passing_types_opponent_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas detalhadas sobre os diferentes tipos de passes das equipes adversárias durante a temporada da Série A do Campeonato Brasileiro de Futebol. Inclui informações sobre passes ao vivo, passes mortos, cruzamentos, chutes, entre outros.
    - Squad: Nome do time adversário
    - Pl: Número de jogadores
    - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
    - Att: Total de tentativas de passes
    - Live: Passes ao vivo
    - Dead: Passes mortos
    - FK: Passes provenientes de faltas
    - TB: Passes provenientes de tiros de meta
    - Sw: Passes provenientes de laterais
    - Crs: Cruzamentos
    - TI: Chutes
    - CK: Cobranças de escanteio
    - In: Passes para dentro
    - Out: Passes para fora
    - Str: Passes longos
    - Cmp: Passes completos
    - Off: Fora do alvo
    - Blocks: Bloqueios
    """
    
    return texto
  
  def squad_advanced_passing_types_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas detalhadas sobre os diferentes tipos de passes das equipes durante a temporada da Série A do Campeonato Brasileiro de Futebol. Inclui informações sobre passes ao vivo, passes mortos, cruzamentos, chutes, entre outros.
    - Squad: Nome do time
    - Pl: Número de jogadores
    - 90s: Minutos convertidos para 90 minutos (tempo de jogo padrão)
    - Att: Total de tentativas de passes
    - Live: Passes ao vivo
    - Dead: Passes mortos
    - FK: Passes provenientes de faltas
    - TB: Passes provenientes de tiros de meta
    - Sw: Passes provenientes de laterais
    - Crs: Cruzamentos
    - TI: Chutes
    - CK: Cobranças de escanteio
    - In: Passes para dentro
    - Out: Passes para fora
    - Str: Passes longos
    - Cmp: Passes completos
    - Off: Fora do alvo
    - Blocks: Bloqueios
    """
    
    return texto
  
  def squad_advanced_playing_time_opponent_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas detalhadas sobre o tempo de jogo das equipes durante os confrontos na temporada da Série A do Campeonato Brasileiro de Futebol. Inclui informações sobre minutos jogados, minutos por partida, minutos iniciados, minutos completados, substituições, entre outros.
    - Squad: Nome do time
    - Pl: Número de jogadores
    - Age: Idade média do elenco
    - MP: Total de partidas
    - Min: Total de minutos jogados
    - Mn/MP: Minutos por partida
    - Min%: Porcentagem de minutos em relação ao total possível
    - 90s: Total de 90 minutos jogados
    - Starts: Total de partidas iniciadas
    - Mn/Start: Média de minutos por partida iniciada
    - Compl: Total de minutos completados
    - Subs: Total de substituições
    - Mn/Sub: Média de minutos por substituição
    - unSub: Substituições não utilizadas
    - PPM: Pontos por minuto
    - onG: Total de gols marcados enquanto esteve em campo
    - onGA: Total de gols sofridos enquanto esteve em campo
    - +/-: Diferença entre gols marcados e sofridos
    - +/-90: Diferença entre gols marcados e sofridos por 90 minutos
    - onxG: Total de xG (Expected Goals) enquanto esteve em campo
    - onxGA: Total de xGA (Expected Goals Against) enquanto esteve em campo
    - xG+/-: Diferença entre xG e xGA
    - xG+/-90: Diferença entre xG e xGA por 90 minutos
    """
    
    return texto
  
  def squad_advanced_playing_time_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas detalhadas sobre o tempo de jogo das equipes durante a temporada da Série A do Campeonato Brasileiro de Futebol. Inclui informações sobre minutos jogados, minutos por partida, minutos iniciados, minutos completados, substituições, entre outros.
    - Squad: Nome do time
    - Pl: Número de jogadores
    - Age: Idade média do elenco
    - MP: Total de partidas
    - Min: Total de minutos jogados
    - Mn/MP: Minutos por partida
    - Min%: Porcentagem de minutos em relação ao total possível
    - 90s: Total de 90 minutos jogados
    - Starts: Total de partidas iniciadas
    - Mn/Start: Média de minutos por partida iniciada
    - Compl: Total de minutos completados
    - Subs: Total de substituições
    - Mn/Sub: Média de minutos por substituição
    - unSub: Substituições não utilizadas
    - PPM: Pontos por minuto
    - onG: Total de gols marcados enquanto esteve em campo
    - onGA: Total de gols sofridos enquanto esteve em campo
    - +/-: Diferença entre gols marcados e sofridos
    - +/-90: Diferença entre gols marcados e sofridos por 90 minutos
    - onxG: Total de xG (Expected Goals) enquanto esteve em campo
    - onxGA: Total de xGA (Expected Goals Against) enquanto esteve em campo
    - xG+/-: Diferença entre xG e xGA
    - xG+/-90: Diferença entre xG e xGA por 90 minutos
    """
    
    return texto
  
  def squad_advanced_possession_opponent_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas detalhadas sobre a posse de bola das equipes durante a temporada da Série A do Campeonato Brasileiro de Futebol. Inclui informações sobre a posse de bola em porcentagem, toques na bola, distribuição dos toques em diferentes áreas do campo, lances de ataque, sucessos, tackles, carregamento de bola, distância percorrida, progressão com a bola, entre outros.
    - Squad: Nome do time
    - Pl: Número de jogadores
    - Poss: Posse de bola em porcentagem
    - 90s: Total de 90 minutos jogados
    - Touches: Total de toques na bola
    - Def Pen: Toques na área defensiva
    - Def 3rd: Toques no terço defensivo
    - Mid 3rd: Toques no terço intermediário
    - Att 3rd: Toques no terço de ataque
    - Att Pen: Toques na área adversária
    - Live: Toques em situações de jogo ativo
    - Att: Tentativas de ataque
    - Succ: Sucessos
    - Succ%: Porcentagem de sucesso
    - Tkld: Tackles sofridos
    - Tkld%: Porcentagem de tackles sofridos
    - Carries: Carregamento de bola
    - TotDist: Total de distância percorrida
    - PrgDist: Distância progressiva
    - PrgC: Progressões com a bola
    - 1/3: Passes no terço ofensivo
    - CPA: Chutes a gol (Chute de perto da área)
    - Mis: Finalizações erradas
    - Dis: Disputas
    - Rec: Recuperações
    - PrgR: Progressão de Recuperação
    """
    
    return texto
  
  def squad_advanced_possession_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas detalhadas sobre a posse de bola das equipes durante a temporada da Série A do Campeonato Brasileiro de Futebol. Inclui informações sobre a posse de bola em porcentagem, toques na bola, distribuição dos toques em diferentes áreas do campo, lances de ataque, sucessos, tackles, carregamento de bola, distância percorrida, progressão com a bola, entre outros.
    - Squad: Nome do time
    - Pl: Número de jogadores
    - Poss: Posse de bola em porcentagem
    - 90s: Total de 90 minutos jogados
    - Touches: Total de toques na bola
    - Def Pen: Toques na área defensiva
    - Def 3rd: Toques no terço defensivo
    - Mid 3rd: Toques no terço intermediário
    - Att 3rd: Toques no terço de ataque
    - Att Pen: Toques na área adversária
    - Live: Toques em situações de jogo ativo
    - Att: Tentativas de ataque
    - Succ: Sucessos
    - Succ%: Porcentagem de sucesso
    - Tkld: Tackles sofridos
    - Tkld%: Porcentagem de tackles sofridos
    - Carries: Carregamento de bola
    - TotDist: Total de distância percorrida
    - PrgDist: Distância progressiva
    - PrgC: Progressões com a bola
    - 1/3: Passes no terço ofensivo
    - CPA: Chutes a gol (Chute de perto da área)
    - Mis: Finalizações erradas
    - Dis: Disputas
    - Rec: Recuperações
    - PrgR: Progressão de Recuperação
    """
    
    return texto
  
  def squad_advanced_shooting_opponent_stats_serie_a(self):
    texto = """
      Esta base contém estatísticas detalhadas sobre os chutes das equipes adversárias durante a temporada da Série A do Campeonato Brasileiro de Futebol. Inclui informações sobre chutes a gol, chutes totais, chutes no alvo (SoT), porcentagem de chutes no alvo, média de chutes por jogo, média de chutes no alvo por jogo, média de gols por chute, média de gols por chute no alvo, distância média dos chutes, chutes de falta (FK), pênaltis (PK), cobranças de pênaltis, expectativa de gols (xG), expectativa de gols sem penalidades (npxG), expectativa de gols por chute, diferença entre gols reais e expectativa de gols (G-xG), e diferença entre gols reais sem penalidades e expectativa de gols (np:G-xG).
    - Squad: Nome do time adversário
    - Pl: Número de jogadores
    - 90s: Total de 90 minutos jogados
    - Gls: Total de gols marcados
    - Sh: Total de chutes
    - SoT: Total de chutes no alvo
    - SoT%: Porcentagem de chutes no alvo
    - Sh/90: Média de chutes por jogo
    - SoT/90: Média de chutes no alvo por jogo
    - G/Sh: Média de gols por chute
    - G/SoT: Média de gols por chute no alvo
    - Dist: Distância média dos chutes
    - FK: Chutes de falta
    - PK: Pênaltis
    - PKatt: Cobranças de pênaltis
    - xG: Expectativa de gols
    - npxG: Expectativa de gols sem penalidades
    - npxG/Sh: Expectativa de gols por chute
    - G-xG: Diferença entre gols reais e expectativa de gols
    - np:G-xG: Diferença entre gols reais sem penalidades e expectativa de gols
    """
    
    return texto
  
  def squad_advanced_shooting_stats_squad_serie_a(self):
    texto = """
      Esta base contém estatísticas detalhadas sobre os chutes das equipes adversárias durante a temporada da Série A do Campeonato Brasileiro de Futebol. 
      Inclui informações sobre chutes a gol, chutes totais, chutes no alvo (SoT), porcentagem de chutes no alvo, média de chutes por jogo, média de chutes no alvo por jogo, 
      média de gols por chute, média de gols por chute no alvo, distância média dos chutes, chutes de falta (FK), pênaltis (PK), cobranças de pênaltis, 
      expectativa de gols (xG), expectativa de gols sem penalidades (npxG), expectativa de gols por chute, diferença entre gols reais e expectativa de gols (G-xG), 
      e diferença entre gols reais sem penalidades e expectativa de gols (np:G-xG).
        - Squad: Nome do time adversário
        - Pl: Número de jogadores
        - 90s: Total de 90 minutos jogados
        - Gls: Total de gols marcados
        - Sh: Total de chutes
        - SoT: Total de chutes no alvo
        - SoT%: Porcentagem de chutes no alvo
        - Sh/90: Média de chutes por jogo
        - SoT/90: Média de chutes no alvo por jogo
        - G/Sh: Média de gols por chute
        - G/SoT: Média de gols por chute no alvo
        - Dist: Distância média dos chutes
        - FK: Chutes de falta
        - PK: Pênaltis
        - PKatt: Cobranças de pênaltis
        - xG: Expectativa de gols
        - npxG: Expectativa de gols sem penalidades
        - npxG/Sh: Expectativa de gols por chute
        - G-xG: Diferença entre gols reais e expectativa de gols
        - np:G-xG: Diferença entre gols reais sem penalidades e expectativa de gols
    """
    
    return texto
  
  def squad_standard_stats_opponent_serie_a(self):
    texto = """
    A base fornece estatísticas detalhadas sobre o desempenho das equipes adversárias durante a temporada da Série A do Campeonato Brasileiro de Futebol. Essas estatísticas são vitais para compreender o desempenho e o estilo de jogo dos times que competiram na liga.
    Ela inclui uma ampla gama de métricas, como gols marcados, assistências, posse de bola média, cartões recebidos, expectativa de gols (xG), expectativa de gols sem penalidades (npxG), expectativa de assistências (xAG), entre outras. Esses dados ajudam a avaliar não apenas o desempenho ofensivo das equipes, mas também a eficácia de suas estratégias defensivas, com informações sobre cartões recebidos e gols sofridos.
    - Squad: Nome do time adversário.
    - Pl: Número de jogadores.
    - Age: Idade média da equipe adversária.
    - Poss: Posse de bola média da equipe adversária.
    - MP: Número de partidas disputadas.
    - Starts: Total de jogadores que iniciaram as partidas.
    - Min: Total de minutos jogados.
    - 90s: Total de 90 minutos jogados.
    - Gls: Total de gols marcados pela equipe adversária.
    - Ast: Total de assistências feitas pela equipe adversária.
    - G+A: Total de gols e assistências.
    - G-PK: Total de gols excluindo pênaltis.
    - PK: Total de pênaltis marcados pela equipe adversária.
    - PKatt: Total de cobranças de pênaltis pela equipe adversária.
    - CrdY: Total de cartões amarelos recebidos.
    - CrdR: Total de cartões vermelhos recebidos.
    - xG: Expectativa de gols da equipe adversária.
    - npxG: Expectativa de gols sem penalidades da equipe adversária.
    - xAG: Expectativa de assistências da equipe adversária.
    - npxG+xAG: Expectativa de gols e assistências sem penalidades da equipe adversária.
    - PrgC: Total de progressões de passes na equipe adversária.
    - PrgP: Total de progressões de passes para finalizações na equipe adversária.
    """
    
    return texto