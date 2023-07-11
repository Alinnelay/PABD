#carregando as funções em outros arquivos .py
import services.database as db


#função para inserir registro no banco de dados
def incluir_usuario_funcionario(id, email, cpf, senha, nome, telefone, idade, cargo):
    db.cur.execute("""
                   INSERT into public.tbusuarios (id_user, email, cpf, senha)
                   VALUES ('%s','%s','%s','%s')
                   """ % (id, email, cpf, senha))
    
    db.cur.execute("""
                   INSERT into public.tbfuncionarios (id_funcionario, nome, telefone, idade, cargo)
                   VALUES ('%s', '%s','%s','%s', '%s')
                   """ % (id, nome, telefone, idade, cargo))
    db.con.commit()


def incluir_usuario_paciente(id, email, cpf, senha, nome, telefone, idade):
    db.cur.execute("""
                   INSERT into public.tbusuarios (id_user, email, cpf, senha)
                   VALUES ('%s','%s','%s', '%s')
                   """ % (id, email, cpf, senha))

    db.cur.execute("""
                   INSERT into public.tbpacientes (id_paciente, nome, telefone, idade)
                   VALUES ('%s', '%s','%s','%s')
                   """ % (id, nome, telefone, idade))
    db.con.commit()