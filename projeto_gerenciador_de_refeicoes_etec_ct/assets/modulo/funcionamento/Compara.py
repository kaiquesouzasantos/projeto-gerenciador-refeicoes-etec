class Compara:
    def func_compara(cod_aluno, alunos_dados, alunos_contabilizados):
        if (alunos_dados.count(cod_aluno) == 1 and alunos_contabilizados.count(cod_aluno) == 0):
            return True
        elif (alunos_dados.count(cod_aluno) == 1 and alunos_contabilizados.count(cod_aluno) != 0):
            return False
        return -1

    def func_retorna_existencia_cadastro(email_aluno_cripto, alunos_dados):
        if (alunos_dados.count(email_aluno_cripto) == 1):
            return True
        return False