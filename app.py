
import random
import time

nome_do_jogador = input("Digite seu nome: ").strip() .capitalize()
hp = 100
inimigos = ["Cobra", "Onça", "Jacaré", "Mosquito venenoso"]
item = ("kit primeiros socorros", "Machado", "Comida", "Pocao")
iven = ["Picareta", "Bloco", "Espada", "Armadura","Flechas", "Arco", "Kit de emergência", "Lixo"]

while True:
    idade = int(input("Digite sua idade: "))
    if idade <= 12:
        print("Acesso negado! Você precisa ter acima de 12 anos para conseguir jogar esse jogo! ")

    elif idade > 12 and idade < 120:
        break
    else:
        print("Idade inválida por favor digita sua idade novamente!")


def fim_de_jogo():
    print("Parabens você terminou o jogo!, quero te agradecer por jogar meu primeiro jogo programado em Python com apenas 3 meses estudando!\n")
    time.sleep(5)
    print("Esse jogo foi criado  do ZERO por mim  apenas contendo 5%, de I.A nele. Foi criado com a itenção de melhorar minha lógica de programação.\n   ")
    time.sleep(5)
    print("Utilizei bastante I.A para me ajudar a descubrir erros de sintaxe, por ser minha primeira vez usando bibliotecas!\n 'randon' e 'time' essas foi as bibliotecas utilizadas para esse jogo rodado em terminal\n")
    time.sleep(15)
    print("Por esta aprendendo python 3 meses é de se esperar que sim, vai ter bastantes erros no código. \n Espero que compreendam\n Att: Daniel.C ")


def você_morreu():
    print("Puts que vacilo em ! \n espero que tenha gostado do meu primeiro jog programado em Python com apenas 3 meses estudando!\n ")
    time.sleep(5)
    print("Esse jogo foi criado  do ZERO por mim  apenas contendo 5%, de I.A nele. Foi criado com a itenção de melhorar minha lógica de programação.\n   ")
    time.sleep(5)
    print("Utilizei bastante I.A para me ajudar a descubrir erros de sintaxe, por ser minha primeira vez usando bibliotecas!\n 'randon' e 'time' essas foi as bibliotecas utilizadas para esse jogo rodado em terminal\n")
    time.sleep(15)
    print("Por esta aprendendo python 3 meses é de se esperar que sim, vai ter bastantes erros no código. \n Espero que compreendam\n Att: Daniel.C ")


def descartaritem():
    while True:
        remover = input("Deseja descartar algo de seu iventario ? Sim / Não: ") .strip(). capitalize()
        if remover == "Sim":
             time.sleep(1)
             item = input("Digite o item que deseja remover: ").strip().capitalize()
             if item in iven:
                 iven.remove(item)
                 print(f"O item {item} foi removido de sua mochila")
                 break
        elif remover == "Não":
             print("Blz segue o jogo")
             break
        else:
             print("Por favor digitar apenas oque o comando mandar! ")

def coletaritem():
    while True:
        pega = input(
            f"O player {nome_do_jogador} encontrou  {item} deseja coletar ? Sim / Não: ").strip().capitalize()
        if pega == "Sim":
            time.sleep(1)
            nome = input( "Digite o nome do item que deseja pegar: ") .strip().capitalize()
            iven.append(nome)
            ver_no_iventario = input("Item coletado! \n deseja ver em seu inventario ? Sim/Não: ").strip().capitalize()
            if ver_no_iventario == "Sim":
                time.sleep(1)
                print(iven)
                time.sleep(2)
                
            elif ver_iventario == "Não":
                print("Blz segue o jogo")
                break
        elif pega == "Não":
            print("Blz segue o jogo")
            break
        else:
            print("Error! DIGITAR APENAS Sim / Não")


print(f"Seja bem vindo ao jogo {nome_do_jogador}! sua vida agora é de {hp} hp, você ira ter que sobrevivar 3 dias!")
time.sleep(7)
print("PRIMEIRO DIA")
time.sleep(3)

print("Você acorda em um mundo desconhecido após um grande terremoto que destruiu várias cidades.\nSem entender muito bem o que aconteceu, você se encontra com uma mochila.")

while True:
    ver_iventario = input("Deseja ver seu iventario / mochila ? s/n: ").strip().lower()
    if ver_iventario == "s":
        time.sleep(1)
        print(iven)
        descartaritem()
        break
    elif ver_iventario == "n":
        print("Blz segue o jogo")
        break
    else:
        print("Por favor digitar apenas oque o comando mandar! ")

time.sleep(1)

print("Desesperado você corre para as montanhas observar melhor oque aconteceu!\n ao decorrer no caminho você encontra uma aldeia destruida com varios items espalhados no chão")
time.sleep(2)

coletaritem()

print("Após encontra vário itens jogados no chão, você decide trilhar seu caminho até as montanhas\n em uma floresta cheio de animais selvagens você decide arriscar mesmo assim!\n")
time.sleep(10)
print("s-s-s-s...")
time.sleep(3)
inimigo = random.choice(inimigos)

print("Uma cobra apareceu!\n Mantenha a calma e vamos ver oque você pode pegar para matar essa cobra!  ")
time.sleep(5)
print(iven)


armas = ["Espada", "Machado", "Pocao"]

def escolhendo():

    while True:

        arma = input("Digite o item que deseja pegar: ").strip().capitalize()

        if arma in armas and arma in iven:

            pergunta = input("Digite (s) para confirmar ou (n) para trocar: ").strip().lower()

            if pergunta == "s":
                print("Perfeita escolha!")
                print(f"Você pegou a arma {arma}")
                break

            elif pergunta == "n":
                print("Escolha outra arma.")

        else:
            print("❌ Esse item não pode ser usado ou não está no inventário.")

escolhendo()

print(
    f"Após escolher a arma ideal para matar a cobra, você matou a cobra, o(a) player {nome_do_jogador} conseguiu escapar!")
time.sleep(5)
print("SEGUNDO DIA! ")
time.sleep(7)
print("Após caminhar por um longo periodo, você acaba chegando em um pantano.\n Vendo aquela água escura e calma você já imagina oque está por vir... ")
time.sleep(7)

print("Grrr, Urr-urrr, Huuun")
time.sleep(5)
print("Shhhluuurp, Plosh, Blub-blub")
print("O jacaré sai da agua FURIOSO! correndo em sua direção")
opcoes = input("VOCÊ DESEJA CORRER OU LUTAR?: ").strip().capitalize()
while True:
    if opcoes == "Correr":
        print("Desperado você começa a correr sem pensar duas vezes!\n Mas logo percebe que isso foi uma péssima decisão\n você começa a cansar por causa da lama que esta te deixando lento(a)\n Sendo assim em poucos segundos o jacaré consegue te alcançar... ")
        time.sleep(15)
        soma = hp - 100
        print(f"CRUNCH!, jacaré te mordeu  {hp} - 100 = {hp - 100}  ")
        time.sleep(14)
        print("VOCÊ MORREU! ")
        você_morreu()
        break
    elif opcoes == "Lutar":
        print("Vemos aqui que você gosta de aventuras!\n Escolha a sua arma! ")
        print(armas)
        escolhendo()
        time.sleep(5)
        print("Depois de escolher muito bem sua arma você entra em um combate veroz contra o jacaré, perdendo muita vida ao decorrer da luta mais no final acaba vencendo! ")
        hp -= 40
        print(f"você está com {hp} de hp ")
        break
    else:
        print("Digitar apenas o que o comando mandar! ")

time.sleep(5)
print("ULTIMA DIA! ")
time.sleep(7)
print("Após passar por esses 2 dias mais terriveis de sua vida, você agora chega no ultimo dia ainda no pantano com o jacaré morto ao seu lado! ")
time.sleep(5)
print("Só que, o cheiro ruim do jacare morto atrai mosquitos, e não são qualquer mosquitos.\n SÃO VENENOSOS ")
while True:
    print("VOCÊ QUER SEGUIR ADIANTE OU MATA-LOS? ")
    opcao2 = input(
        "Digite 'Seguir' se  quiser SEGUIR ADIANTE ou digite 'Matar' se quiser MATA-LOS: ").strip().capitalize()
    if opcao2 == "Seguir":
        print("Vendo aquele tanto de mosquito você decide correr ao seu destino que é o topo da montanha!")
        time.sleep(4)
        print("zum zum zum")
        time.sleep(5)
        print("Após 3 horas andando você consegue finalmente chegar ao topo da montanha\n sem olhar pra tras você ouve um barulho alto se zumbidos se aproximando")
        time.sleep(3)
        print("zum, zuM, ZUm, ZUM")
        time.sleep(2)
        print("Essa NÃO!!! os mosquitos conseguiram te achar \n CORRE!!!!")
        time.sleep(3)
        correr = input("Digite CORRER: ")
        time.sleep(5)
        print("VOCÊ MORREU! 'Os mosquitos te pegou' ")
        fim_de_jogo()
        break
    elif opcao2 == "Matar":
        print("Escolha consciente! vamos ver com oque você pode mata-los! ")
        time.sleep(4)
        print(armas)
        escolhendo()
        time.sleep(7)
        print("Após entrar em um combate sério com os mosquitos você conseguiu elimina-los 1 por 1\n")
        time.sleep(5)
        print("Após 3 horas andando você consegue finalmente chegar ao topo da montanha\n e descobrir que o mundo todo vou completamente destruido por esse terremoto denso\n que aconteceu com uma magnitude de 14!")
        time.sleep(12)
        print("Com essa noticia você decide tirar sua propria vida se jogando de cima da montanha... ")
        time.sleep(8)
        print("CAINDO ...")
        time.sleep(10)
        print(hp - 60)
        fim_de_jogo()
        break
    else:
        print("Por favor digitar apenas o que o comando mandar! ")
     