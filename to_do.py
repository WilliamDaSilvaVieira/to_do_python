# To_Do
import os

txt = "\t{0}\t{1}\t{2}"


def list():
    f = open("to_do.txt", "r")
    print(f.read())
    f.close()


def add(i):
    while True:
        print("Digite a tarefa a ser adicionada. Ou = para voltar.")
        tarefa = input("--> ").strip()
        match tarefa:
            case "=":
                break
            case _:
                f = open("to_do.txt", "a")
                f.write(txt.format(i, "[ ]", tarefa) + "\n")
                f.close()
                i += 1
                print("\nTarefa adicionada com sucesso!\n")


def finish():
    while True:
        print("Digite o número da tarefa a ser concluída. Ou 0 para voltar")
        list()
        try:
            i = int(input("--> "))
        except Exception:
            print("Digite apenas números inteiros!")
            continue
        f = open("to_do.txt", "r")
        index = 0
        for _ in f:
            index += 1
        f.close()
        if i >= 0 and i <= index:
            match i:
                case 0:
                    break
                case _:
                    text = []
                    f = open("to_do.txt", "r")
                    for x in f:
                        text.append(x)
                    f.close()
                    text[i - 1] = text[i - 1].replace("[ ]", "[-]", 1)
                    f = open("to_do.txt", "w")
                    for y in text:
                        f.write(y)
                    f.close()
                    print("Tarefa marcada como concluída.")
                    continue
        else:
            print("Tarefa não encontrada. Digite novamente!")
            continue


def delete():
    if os.path.exists("to_do.txt"):
        os.remove("to_do.txt")
        print("\nLista limpa com sucesso!\n")
    else:
        print("A lista está vazia!")


print("Bem Vindo ao To Do!")
while True:
    print("""Opções:
    Ver Lista -> #
    Adicionar -> +
    Concluir -> !
    Apagar -> - (*TODA A LISTA SERÁ APAGADA*)
    Sair -> =""")
    option = input("--> ").strip()
    match option:
        case "#":
            if os.path.exists("to_do.txt"):
                list()
            else:
                print("A lista está vazia!")
        case "+":
            if os.path.exists("to_do.txt"):
                index = 1
                f = open("to_do.txt", "r")
                for _ in f:
                    index += 1
                f.close()
                add(index)
            else:
                add(1)
            continue
        case "!":
            if os.path.exists("to_do.txt"):
                finish()
            else:
                print("A lista está vazia!")
            continue
        case "-":
            delete()
            continue
        case "=":
            break
        case _:
            print("Opção invalida!")
            continue
print("Fechando...")
