from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_previstas = int(input("Digite a quantidade de horas previstas: "))
valor_hora = int(input("Digite o valor da hora trabalhada: "))
prazo = input("Digite o prazo estimado: ")

print(projeto)
print(horas_previstas)
print(valor_hora)
print(prazo)

valor_total = (valor_hora) * (horas_previstas) 
print(valor_total)

pdf = FPDF()

# adicionando uma página
pdf.add_page()       
    
# configurando a fonte
pdf.set_font("Arial", size=12)       

# para colocar informações no PDF, ele não pode ser do tipo INTEIRO, precisa estar em texto

pdf.image("template.png", x=0, y=0)


# passando as coordenadas e colocando a descrição do projeto
pdf.text(115, 145, projeto)               
pdf.text(115, 160, str(horas_previstas))
pdf.text(115, 175, str(valor_hora))
pdf.text(115, 190, str(prazo))
pdf.text(115, 205, str(valor_total))


# salvando o pdf
pdf.output("Orçamento.pdf")                
print("Orçamento gerado com sucesso!")