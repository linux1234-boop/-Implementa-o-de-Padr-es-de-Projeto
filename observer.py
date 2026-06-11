class Observer:
    def atualizar(self, **dados):
        raise NotImplementedError("Subclasse deve implementar atualizar()")


class Subject:
    def __init__(self):
        self.observers = []

    def anexar(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def desanexar(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notificar(self, **dados):
        for obs in self.observers:
            obs.atualizar(**dados)


class EstacaoMeteorologica(Subject):
    def __init__(self):
        super().__init__()
        self.temperatura = 0
        self.umidade = 0

    def set_dados(self, temperatura, umidade):
        self.temperatura = temperatura
        self.umidade = umidade
        print("\nNova leitura -> Temperatura: " + str(temperatura) +
              "C, Umidade: " + str(umidade) + "%")
        self.notificar(temperatura=temperatura, umidade=umidade)


class DisplayTelao(Observer):
    def atualizar(self, **dados):
        print("  [TELAO]  Temperatura: " + str(dados["temperatura"]) +
              "C | Umidade: " + str(dados["umidade"]) + "%")


class DisplayApp(Observer):
    def atualizar(self, **dados):
        print("  [APP]    Mostrando: " + str(dados["temperatura"]) + "C na home")


class AlertaTempestade(Observer):
    def atualizar(self, **dados):
        if dados["temperatura"] > 35:
            print("  [ALERTA] Calor extremo de " +
                  str(dados["temperatura"]) + "C!")


class AlertaUmidade(Observer):
    def atualizar(self, **dados):
        if dados["umidade"] > 80:
            print("  [ALERTA] Umidade alta de " +
                  str(dados["umidade"]) + "% (chuva proxima)")


estacao = EstacaoMeteorologica()
telao  = DisplayTelao()
app    = DisplayApp()
alerta = AlertaTempestade()
alerta_umidade = AlertaUmidade()

print("=== Estacao Meteorologica ===")
print("1 - Ativar Telao")
print("2 - Desativar Telao")
print("3 - Ativar App")
print("4 - Desativar App")
print("5 - Ativar Alerta de Calor")
print("6 - Desativar Alerta de Calor")
print("7 - Ativar Alerta de Umidade")
print("8 - Desativar Alerta de Umidade")
print("9 - Nova leitura (temperatura umidade)")
print("0 - Sair")

opcao = ""
while opcao != "0":
    opcao = input("\nOpcao: ")

    if opcao == "1":
        estacao.anexar(telao)
        print("Telao ativado.")
    elif opcao == "2":
        estacao.desanexar(telao)
        print("Telao desativado.")
    elif opcao == "3":
        estacao.anexar(app)
        print("App ativado.")
    elif opcao == "4":
        estacao.desanexar(app)
        print("App desativado.")
    elif opcao == "5":
        estacao.anexar(alerta)
        print("Alerta de calor ativado.")
    elif opcao == "6":
        estacao.desanexar(alerta)
        print("Alerta de calor desativado.")
    elif opcao == "7":
        estacao.anexar(alerta_umidade)
        print("Alerta de umidade ativado.")
    elif opcao == "8":
        estacao.desanexar(alerta_umidade)
        print("Alerta de umidade desativado.")
    elif opcao == "9":
        leitura = input("Digite temperatura e umidade (ex: 25 60): ")
        partes = leitura.split()
        if len(partes) == 2:
            try:
                temp = float(partes[0])
                umid = float(partes[1])
                estacao.set_dados(temp, umid)
            except ValueError:
                print("Valores invalidos.")
        else:
            print("Digite dois numeros separados por espaco.")
    elif opcao == "0":
        print("Encerrando...")
    else:
        print("Opcao invalida.")
