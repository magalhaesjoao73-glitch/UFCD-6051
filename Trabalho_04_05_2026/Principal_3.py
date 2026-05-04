import tkinter as tk  # importa a biblioteca para criar interfaces gráficas
from PIL import Image, ImageTk  # importa ferramentas para trabalhar com imagens

# Criar janela principal
janela = tk.Tk()  # cria a janela
janela.title("Ficha do Aluno - Instalações Elétricas")  # define o título da janela
janela.geometry("400x500")  # define o tamanho da janela (largura x altura)
janela.configure(bg="#f0f0f0")  # define a cor de fundo da janela

# ===== FRAME SUPERIOR =====
frame_topo = tk.Frame(janela, bg="#f0f0f0")  # cria um "container" para organizar elementos no topo
frame_topo.pack(pady=10)  # posiciona o frame com espaço vertical

# ===== FOTO DO ALUNO =====
try:
    # tenta abrir a imagem no caminho indicado
    imagem = Image.open(r"C:\Users\35191\Desktop\curso de eletricista\UFCD6051\Trabalho_04_05_2026\foto.jpg")
    
    imagem = imagem.resize((150, 150))  # redimensiona a imagem para 150x150 pixels
    
    foto = ImageTk.PhotoImage(imagem)  # converte a imagem para formato compatível com tkinter

    label_foto = tk.Label(frame_topo, image=foto, bg="#f0f0f0")  # cria um label para mostrar a imagem
    label_foto.pack()  # coloca a imagem no ecrã
except:
    # se houver erro (ex: imagem não encontrada)
    label_foto = tk.Label(frame_topo, text="(Sem Foto)", bg="#f0f0f0")  # mostra texto alternativo
    label_foto.pack()

# ===== NOME =====
label_nome = tk.Label(
    janela,  # onde vai aparecer (janela principal)
    text="Nome: João Magalhães",  # texto a mostrar
    font=("Arial", 14, "bold"),  # tipo de letra, tamanho e estilo
    bg="#f0f0f0"  # cor de fundo
)
label_nome.pack(pady=5)  # posiciona com espaçamento vertical

# ===== TÍTULO =====
label_titulo = tk.Label(
    janela,
    text="UFCDs - Instalações Elétricas",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0"
)
label_titulo.pack(pady=10)

# ===== FRAME DAS UFCDs =====
frame_ufcds = tk.Frame(
    janela,
    bg="white",  # fundo branco
    bd=1,  # espessura da borda
    relief="solid"  # estilo da borda
)
frame_ufcds.pack(padx=20, fill="both", expand=True)  # ocupa espaço com margens laterais

# Lista de UFCDs
ufcds = [
    "UFCD 1 - Segurança em instalações elétricas",
    "UFCD 2 - Eletricidade básica",
    "UFCD 3 - Instalações elétricas residenciais",
    "UFCD 4 - Máquinas elétricas"
]

# Criar um label para cada UFCD
for ufcd in ufcds:
    label = tk.Label(
        frame_ufcds,  # dentro do frame
        text=ufcd,  # texto da UFCD
        anchor="w",  # alinha à esquerda
        bg="white"  # fundo branco
    )
    label.pack(fill="x", padx=10, pady=2)  # ocupa largura e tem margens

# ===== EXECUTAR =====
janela.mainloop()  # inicia o programa (loop da interface)