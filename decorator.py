class Notificacao:
    def enviar(self, mensagem):
        raise NotImplementedError("Subclasse deve implementar enviar()")


class NotificacaoEmail(Notificacao):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    def enviar(self, mensagem):
        print("[E-MAIL] Para: " + self.destinatario)
        print("[E-MAIL] Enviando: '" + mensagem + "' via SMTP")


class NotificacaoSMS(Notificacao):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    def enviar(self, mensagem):
        print("[SMS] Para: " + self.destinatario)
        print("[SMS] Enviando: '" + mensagem + "' via operadora")


class NotificacaoPush(Notificacao):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    def enviar(self, mensagem):
        print("[PUSH] Token Firebase: " + self.destinatario)
        print("[PUSH] Enviando: '" + mensagem + "' via Firebase")


class NotificacaoFactory:
    def criar_notificacao(self, destinatario):
        raise NotImplementedError("Subclasse deve implementar criar_notificacao()")

    def notificar(self, destinatario, mensagem):
        self.criar_notificacao(destinatario).enviar(mensagem)


class EmailFactory(NotificacaoFactory):
    def criar_notificacao(self, destinatario):
        return NotificacaoEmail(destinatario)


class SMSFactory(NotificacaoFactory):
    def criar_notificacao(self, destinatario):
        return NotificacaoSMS(destinatario)


class PushFactory(NotificacaoFactory):
    def criar_notificacao(self, destinatario):
        return NotificacaoPush(destinatario)


def validar_email(email):
    if "@" not in email:
        return False
    if email.count("@") > 1:
        return False
    partes = email.split("@")
    if len(partes) != 2:
        return False
    usuario = partes[0]
    dominio = partes[1]
    if usuario == "" or dominio == "":
        return False
    if "." not in dominio:
        return False
    if dominio.startswith(".") or dominio.endswith("."):
        return False
    return True


def validar_sms(telefone):
    if not telefone.isdigit():
        return False
    if len(telefone) < 10 or len(telefone) > 11:
        return False
    return True


def validar_push(token):
    if len(token) < 10:
        return False
    return True


def pedir_destinatario(tipo):
    while True:
        if tipo == "email":
            valor = input("Digite o e-mail: ")
            if validar_email(valor):
                return valor
            else:
                print("E-mail invalido. Exemplo: usuario@dominio.com")
        elif tipo == "sms":
            valor = input("Digite o telefone (apenas digitos, com DDD): ")
            if validar_sms(valor):
                return valor
            else:
                print("SMS invalido. Use 10 ou 11 digitos. Exemplo: 11987654321")
        elif tipo == "push":
            valor = input("Digite o token do Firebase: ")
            if validar_push(valor):
                return valor
            else:
                print("Token invalido. Deve ter pelo menos 10 caracteres.")


print("=== Sistema de Notificacoes ===")
print("1 - E-mail")
print("2 - SMS")
print("3 - Push")
print("0 - Sair")

opcao = ""
while opcao != "0":
    opcao = input("\nOpcao: ")

    if opcao == "1":
        print("Canal selecionado: E-mail")
        destinatario = pedir_destinatario("email")
        msg = input("Mensagem: ")
        EmailFactory().notificar(destinatario, msg)
    elif opcao == "2":
        print("Canal selecionado: SMS")
        destinatario = pedir_destinatario("sms")
        msg = input("Mensagem: ")
        SMSFactory().notificar(destinatario, msg)
    elif opcao == "3":
        print("Canal selecionado: Push")
        destinatario = pedir_destinatario("push")
        msg = input("Mensagem: ")
        PushFactory().notificar(destinatario, msg)
    elif opcao == "0":
        print("Encerrando...")
    else:
        print("Opcao invalida.")
