class Compara:
    def func_compara(cod_aluno, alunos_dados, alunos_contabilizados):
        if (alunos_dados.count(cod_aluno) == 0 or alunos_contabilizados.count(cod_aluno) != 0):
            return False
        return True

    def func_retorna_existencia_cadastro(email_aluno_cripto, alunos_dados):
        if (alunos_dados.count(email_aluno_cripto) == 1):
            return True
        return False