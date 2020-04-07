def notas(*n, sit=False):
    """

    :param n: Notas do Aluno
    :param sit: (Se sit=True) mostra a situação do aluno
    :return: Retorna uma biblioteca que nela se encontra o total de notas, maior nota, menor, média e situação (se sit=True)
    """
    aluno = dict()
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = sum(n) / len(n)
    if sit:
        if aluno['media'] <= 6:
            aluno['situação'] = 'RUIM'
        elif aluno['media'] > 6 and aluno['media'] <= 7:
            aluno['situação'] = 'RAZOÁVEL'
        elif aluno['media'] > 7:
            aluno['situação'] = 'BOA'

    return aluno



resp = notas(3, 2, 5, 7, 9, sit=True)
print(resp)
