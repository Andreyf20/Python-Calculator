from tkinter import *
from tkinter import messagebox
bases = [2,8,10,16]; # Bases that can be used
binario = ['0', '1']; # Binary
octal = ['0', '1', '2', '3', '4', '5', '6', '7'];
decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];

def dec_a_binario(numero): # Func transforms a decimal number into binary
    try:
        Nuevo_n = [];
        while numero != 0:
            remainder = numero % 2
            numero = numero // 2
            Nuevo_n = [str(remainder)] + Nuevo_n
        numero_final_binario = ''.join(Nuevo_n)
        return numero_final_binario
    except:
        messagebox.showinfo('Error', 'Input Error')


def dec_a_octal(numero): # Func transforms a decimal number into octal
    try:
        Nuevo_n = [];
        while numero != 0:
            remainder = numero % 8
            numero = numero // 8
            Nuevo_n = [str(remainder)] + Nuevo_n
        numero_final_octal = ''.join(Nuevo_n)
        return numero_final_octal
    except:
        messagebox.showinfo('Error', 'Input Error')


def dec_a_hexa(numero): # Func transforms a decimal number into hexadecimal
    try:
        Nuevo_n = [];
        while numero != 0:
            remainder = numero % 16
            numero = numero // 16
            if remainder == 10:
                Nuevo_n = ['A'] + Nuevo_n
            elif remainder == 11:
                Nuevo_n = ['B'] + Nuevo_n
            elif remainder == 12:
                Nuevo_n = ['C'] + Nuevo_n
            elif remainder == 13:
                Nuevo_n = ['D'] + Nuevo_n
            elif remainder == 14:
                Nuevo_n = ['E'] + Nuevo_n
            elif remainder == 15:
                Nuevo_n = ['F'] + Nuevo_n
            else:
                Nuevo_n = [str(remainder)] + Nuevo_n
        numero_final_hexa = ''.join(Nuevo_n)
        return numero_final_hexa
    except:
        messagebox.showinfo('Error', 'Input Error')

def binario_a_dec(numero): # Func transforms a binary number into decimal
    try:
        numero_final_dec = 0
        exp = 0
        # numero = list(numero)
        for item in numero[::-1]:
            x = int(item) * (2**exp)
            exp += 1
            numero_final_dec += x
        return numero_final_dec
    except:
        messagebox.showinfo('Error', 'Input Error')

def octal_a_decimal(numero): # Func transforms a octal number into decimal
    try:
        numero_final_dec = 0
        exp = 0
        # numero = list(numero)
        for item in numero[::-1]:
            x = int(item) * (8**exp)
            exp += 1
            numero_final_dec += x
        return numero_final_dec
    except:
        messagebox.showinfo('Error', 'Input Error')

def hexa_a_dec(numero): # Func transforms a hexadecimal number into decimal
    try:
        numero_final_dec = 0
        exp = 0
        for i in range(len(numero)):
            if numero[i] == 'A':
                numero[i] = 10
            elif numero[i] == 'B':
                numero[i] = 11
            elif numero[i] == 'C':
                numero[i] = 12
            elif numero[i] == 'D':
                numero[i] = 13
            elif numero[i] == 'E':
                numero[i] = 14
            elif numero[i] == 'F':
                numero[i] = 15
        for item in numero[::-1]:
            x = int(item) * (16**exp)
            exp += 1
            numero_final_dec += x
        return numero_final_dec
    except:
        messagebox.showinfo('Error', 'Input Error')

# Graphical User Interface
calculadora = Tk()
calculadora.title('Calculadora')
# calculadora.resizable(0, 0)

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.base = 10
        self.createWidgets()

    def calculo(self): # Verifies the operation that is used
        self.entrada = self.display.get() # Gets the input from the GUI
        self.lista = list(self.entrada) # Makes a list of the input
        for i in range(len(self.lista)): # Checks the base that is asked for
            if self.lista[i] == '+':
                if self.base == 10:
                    self.calculo_suma_dec()
                elif self.base == 2:
                    self.calculo_suma_bin()
                elif self.base == 8:
                    self.calculo_suma_octal()
                elif self.base == 16:
                    self.calculo_suma_hexa()
            elif self.lista[i] == '-' and i != 0:
                if self.base == 10:
                    self.calculo_suma_dec()
                elif self.base == 2:
                    self.calculo_resta_bin()
                elif self.base == 8:
                    self.calculo_resta_octal()
                elif self.base == 16:
                    self.calculo_resta_hexa()
            elif self.lista[i] == '*':
                if self.base == 10:
                    self.calculo_suma_dec()
                elif self.base == 2:
                    self.calculo_mult_bin()
                elif self.base == 8:
                    self.calculo_mult_octal()
                elif self.base == 16:
                    self.calculo_mult_hexa()

    def calculo_suma_dec(self): # Calculates every operation in base 10, also used for other bases
        try:
            self.result = eval(self.entrada)
            self.replaceText(self.result)
        except:
            messagebox.showinfo('Error', 'Error en el input')

    '''Binary operations'''
    def calculo_suma_bin(self): # Sum of two binary numbers
        ver = 0
        if self.lista[0] == "-":
            ver = 1
            self.lista.remove(self.lista[0])
            print(ver, self.lista)
        self.num1 = []
        self.num2 = []
        bandera = 0
        for i in range(len(self.lista)-1):
            if self.lista[i] == '+':
                self.lista.remove(self.lista[i])
                bandera = 1
            if bandera == 0:
                self.num1 += self.lista[i]
            elif bandera == 1:
                self.num2 += self.lista[i]
        self.num1 = binario_a_dec(self.num1)
        self.num2 = binario_a_dec(self.num2)
        if ver == 1:
            self.result = self.num2 - self.num1
            if self.num2 > self.num1:
                ver = 0
        else:
            self.result = self.num1 + self.num2
        print(self.result)
        self.result = abs(self.result)
        self.result = dec_a_binario(self.result)
        if ver == 1:
            listanum = list(str(self.result))
            listanum = ["-"] + listanum
            self.result = "".join(listanum)
            print(self.result, listanum)
        # print(self.num1, self.num2, self.result)
        self.replaceText(self.result)

    def calculo_resta_bin(self): # Subtraction of two binary numbers
        ver = 0
        if self.lista[0] == "-":
            ver = 1
            self.lista.remove(self.lista[0])
        self.num1 = []
        self.num2 = []
        bandera = 0
        for i in range(len(self.lista)-1):
            if self.lista[i] == "-":
                self.lista.remove(self.lista[i])
                bandera = 1
            if bandera == 0:
                self.num1 += self.lista[i]
            elif bandera == 1:
                self.num2 += self.lista[i]
        self.num1 = binario_a_dec(self.num1)
        self.num2 = binario_a_dec(self.num2)
        if ver == 1:
            self.result = self.num1 + self.num2
        else:
            self.result = self.num1 - self.num2
            if self.result < 0:
                ver = 1
        self.result = abs(self.result)
        self.result = dec_a_binario(self.result)
        if ver == 1:
            listanum = list(str(self.result))
            listanum = ["-"] + listanum
            self.result = "".join(listanum)
        self.replaceText(self.result)

    def calculo_mult_bin(self): # Multiplication of two binary numbers
        ver = 0
        if self.lista[0] == '-':
            ver += 1
            self.lista.remove(self.lista[0])
        self.num1 = []
        self.num2 = []
        bandera = 0
        for i in range(len(self.lista)):
            if self.lista[i] == '*':
                bandera = 1
                pass
            elif self.lista[i] == '-':
                ver += 1
            else:
                if bandera == 0:
                    self.num1 += self.lista[i]
                elif bandera == 1:
                    self.num2 += self.lista[i]
        self.num1 = binario_a_dec(self.num1)
        self.num2 = binario_a_dec(self.num2)
        self.result = abs(self.num1 * self.num2)
        self.result = dec_a_binario(self.result)
        if ver == 1:
            listanum = list(str(self.result))
            listanum = ['-'] + listanum
            self.result = ''.join(listanum)
        self.replaceText(self.result)

    '''Octal operations'''
    def calculo_suma_octal(self): # Sum of two octal numbers
        ver = 0
        if self.lista[0] == "-":
            ver = 1
            self.lista.remove(self.lista[0])
        self.num1 = []
        self.num2 = []
        bandera = 0
        for i in range(len(self.lista)-1):
            if self.lista[i] == '+':
                self.lista.remove(self.lista[i])
                bandera = 1
            if bandera == 0:
                self.num1 += self.lista[i]
            elif bandera == 1:
                self.num2 += self.lista[i]
        self.num1 = octal_a_decimal(self.num1)
        self.num2 = octal_a_decimal(self.num2)
        if ver == 1:
            self.result = self.num2 - self.num1
            if self.num2 > self.num1:
                ver = 0
        else:
            self.result = self.num1 + self.num2
        self.result = abs(self.result)
        self.result = dec_a_octal(self.result)
        if ver == 1:
            listanum = list(str(self.result))
            listanum = ["-"] + listanum
            self.result = "".join(listanum)
            print(self.result, listanum)
        self.replaceText(self.result)

    def calculo_resta_octal(self):  # Subtraction of two octal numbers
        ver = 0
        if self.lista[0] == "-":
            ver = 1
            self.lista.remove(self.lista[0])
        self.num1 = []
        self.num2 = []
        bandera = 0
        for i in range(len(self.lista)-1):
            if self.lista[i] == "-":
                self.lista.remove(self.lista[i])
                bandera = 1
            if bandera == 0:
                self.num1 += self.lista[i]
            elif bandera == 1:
                self.num2 += self.lista[i]
        self.num1 = octal_a_decimal(self.num1)
        self.num2 = octal_a_decimal(self.num2)
        if ver == 1:
            self.result = self.num1 + self.num2
        else:
            self.result = self.num1 - self.num2
            if self.result < 0:
                ver = 1
        self.result = abs(self.result)
        self.result = dec_a_octal(self.result)
        if ver == 1:
            listanum = list(str(self.result))
            listanum = ["-"] + listanum
            self.result = "".join(listanum)
        self.replaceText(self.result)

    def calculo_mult_octal(self):  # Multiplication of two octal numbers
        ver = 0
        if self.lista[0] == '-':
            ver += 1
            self.lista.remove(self.lista[0])
        self.num1 = []
        self.num2 = []
        bandera = 0
        for i in range(len(self.lista)):
            if self.lista[i] == '*':
                bandera = 1
                pass
            elif self.lista[i] == '-':
                ver += 1
            else:
                if bandera == 0:
                    self.num1 += self.lista[i]
                elif bandera == 1:
                    self.num2 += self.lista[i]
        self.num1 = octal_a_decimal(self.num1)
        self.num2 = octal_a_decimal(self.num2)
        self.result = abs(self.num1 * self.num2)
        self.result = dec_a_octal(self.result)
        if ver == 1:
            listanum = list(str(self.result))
            listanum = ['-'] + listanum
            self.result = ''.join(listanum)
        self.replaceText(self.result)

    '''OPERACIONES EN HEXADECIMAL'''
    def calculo_suma_hexa(self): # Sum of two hexadecimal numbers
        ver = 0
        if self.lista[0] == "-":
            ver = 1
            self.lista.remove(self.lista[0])
        self.num1 = []
        self.num2 = []
        bandera = 0
        for i in range(len(self.lista)-1):
            if self.lista[i] == '+':
                self.lista.remove(self.lista[i])
                bandera = 1
            if bandera == 0:
                self.num1 += self.lista[i]
            elif bandera == 1:
                self.num2 += self.lista[i]
        self.num1 = hexa_a_dec(self.num1)
        self.num2 = hexa_a_dec(self.num2)
        if ver == 1:
            self.result = self.num2 - self.num1
            if self.num2 > self.num1:
                ver = 0
        else:
            self.result = self.num1 + self.num2
        self.result = abs(self.result)
        self.result = dec_a_hexa(self.result)
        if ver == 1:
            listanum = list(str(self.result))
            listanum = ["-"] + listanum
            self.result = "".join(listanum)
            print(self.result, listanum)
        self.replaceText(self.result)

    def calculo_resta_hexa(self): # Subtraction of two hexadecimal numbers
        ver = 0
        if self.lista[0] == "-":
            ver = 1
            self.lista.remove(self.lista[0])
        self.num1 = []
        self.num2 = []
        bandera = 0
        for i in range(len(self.lista)-1):
            if self.lista[i] == "-":
                self.lista.remove(self.lista[i])
                bandera = 1
            if bandera == 0:
                self.num1 += self.lista[i]
            elif bandera == 1:
                self.num2 += self.lista[i]
        self.num1 = hexa_a_dec(self.num1)
        self.num2 = hexa_a_dec(self.num2)
        if ver == 1:
            self.result = self.num1 + self.num2
        else:
            self.result = self.num1 - self.num2
            if self.result < 0:
                ver = 1
        self.result = abs(self.result)
        self.result = dec_a_hexa(self.result)
        if ver == 1:
            listanum = list(str(self.result))
            listanum = ["-"] + listanum
            self.result = "".join(listanum)
        self.replaceText(self.result)

    def calculo_mult_hexa(self): # Multiplication of two hexadecimal numbers
        ver = 0
        if self.lista[0] == '-':
            ver += 1
            self.lista.remove(self.lista[0])
        self.num1 = []
        self.num2 = []
        bandera = 0
        for i in range(len(self.lista)):
            if self.lista[i] == '*':
                bandera = 1
                pass
            elif self.lista[i] == '-':
                ver += 1
            else:
                if bandera == 0:
                    self.num1 += self.lista[i]
                elif bandera == 1:
                    self.num2 += self.lista[i]
        self.num1 = hexa_a_dec(self.num1)
        self.num2 = hexa_a_dec(self.num2)
        self.result = abs(self.num1 * self.num2)
        self.result = dec_a_hexa(self.result)
        if ver == 1:
            listanum = list(str(self.result))
            listanum = ['-'] + listanum
            self.result = ''.join(listanum)
        self.replaceText(self.result)

    '''This four functions change the base to work on according to the user'''
    def base2(self):
        self.base = 2

    def base8(self):
        self.base = 8

    def base10(self):
        self.base = 10

    def base16(self):
        self.base = 16

    '''Base change'''
    def cambiar_la_base_del_display2(self): # If base two to x(base)
        entrada = self.display.get()
        if self.base == 10:
            self.result = dec_a_binario(int(entrada))
        elif self.base == 8:
            self.result = octal_a_decimal(list(entrada))
            self.result = dec_a_binario(int(self.result))
        elif self.base == 16:
            self.result = hexa_a_dec(list(entrada))
            self.result = dec_a_binario(int(self.result))
        self.replaceText(self.result)

    def cambiar_la_base_del_display8(self): # If base eight to x(base)
        entrada = self.display.get()
        if self.base == 10:
            self.result = dec_a_octal(int(entrada))
        elif self.base == 2:
            self.result = binario_a_dec(list(entrada))
            self.result = dec_a_octal(int(self.result))
        elif self.base == 16:
            self.result = hexa_a_dec(list(entrada))
            self.result = dec_a_octal(int(self.result))
        self.replaceText(self.result)

    def cambiar_la_base_del_display10(self): # If base ten to x(base)
        entrada = self.display.get()
        if self.base == 2:
            self.result = binario_a_dec(list(entrada))
        elif self.base == 8:
            self.result = octal_a_decimal(list(entrada))
        elif self.base == 16:
            self.result = hexa_a_dec(list(entrada))
        self.replaceText(self.result)

    def cambiar_la_base_del_display16(self): # If base sixteen to x(base)
        entrada = self.display.get()
        if self.base == 2:
            self.result = binario_a_dec(list(entrada))
            self.result = dec_a_hexa(int(self.result))
        elif self.base == 10:
            self.result = dec_a_hexa(int(entrada))
        elif self.base == 8:
            self.result = octal_a_decimal(list(entrada))
            self.result = dec_a_hexa(int(self.result))
        self.replaceText(self.result)

    '''This is the GUI input if the number 0 is there(It is by default)'''
    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    '''Adds to the display the user input'''
    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == '0':
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)

    '''Clears the calculator display'''
    def clearText(self):
        self.replaceText('0')

    '''Every button in the calculator'''
    def createWidgets(self):
        self.display = Entry(self, relief = RAISED, justify = RIGHT, font = 100)
        self.display.insert(0, '0')
        self.display.grid(row = 0, column = 0, columnspan = 15)

        self.nueve = Button(self, font = 100, text = '9', borderwidth = 2, command = lambda: self.appendToDisplay('9'))
        self.nueve.grid(row = 1, column = 0, sticky='NWNESWSE')

        self.ocho = Button(self, font = 100, text = '8', borderwidth = 2, command = lambda: self.appendToDisplay('8'))
        self.ocho.grid(row = 1, column = 1, sticky='NWNESWSE')

        self.siete = Button(self, font = 100, text = '7', borderwidth = 2, command = lambda: self.appendToDisplay('7'))
        self.siete.grid(row = 1, column = 2, sticky='NWNESWSE')

        self.clear = Button(self, font = 100, text = 'C', borderwidth = 2, command = lambda: self.clearText())
        self.clear.grid(row = 1, column = 3, sticky='NWNESWSE')

        self.cambio_base2 = Button(self, font = 100, text = 'B2', borderwidth = 2, command = lambda: self.base2())
        self.cambio_base2.grid(row = 1, column = 4, sticky='NWNESWSE')

        self.seis = Button(self, font = 100, text = '6', borderwidth = 2, command = lambda: self.appendToDisplay('6'))
        self.seis.grid(row = 2, column = 0, sticky='NWNESWSE')

        self.cinco = Button(self, font = 100, text = '5', borderwidth = 2, command = lambda: self.appendToDisplay('5'))
        self.cinco.grid(row = 2, column = 1, sticky='NWNESWSE')

        self.cuatro = Button(self, font = 100, text = '4', borderwidth = 2, command = lambda: self.appendToDisplay('4'))
        self.cuatro.grid(row = 2, column = 2, sticky='NWNESWSE')

        self.suma = Button(self, font = 100, text = '+', borderwidth = 2, command = lambda: self.appendToDisplay('+'))
        self.suma.grid(row = 2, column = 3, sticky='NWNESWSE')

        self.cambio_base8 = Button(self, font = 100, text = 'B8', borderwidth = 2, command = lambda: self.base8())
        self.cambio_base8.grid(row = 2, column = 4, sticky='NWNESWSE')

        self.tres = Button(self, font = 100, text = '3', borderwidth = 2, command = lambda: self.appendToDisplay('3'))
        self.tres.grid(row = 3, column = 0, sticky='NWNESWSE')

        self.dos = Button(self, font = 100, text = '2', borderwidth = 2, command = lambda: self.appendToDisplay('2'))
        self.dos.grid(row = 3, column = 1, sticky='NWNESWSE')

        self.uno = Button(self, font = 100, text = '1', borderwidth = 2, command = lambda: self.appendToDisplay('1'))
        self.uno.grid(row = 3, column = 2, sticky='NWNESWSE')

        self.resta = Button(self, font = 100, text = '-', borderwidth = 2, command = lambda: self.appendToDisplay('-'))
        self.resta.grid(row = 3, column = 3, sticky='NWNESWSE')

        self.cambio_base10 = Button(self, font = 100, text = 'B10', borderwidth = 2, command = lambda: self.base10())
        self.cambio_base10.grid(row = 3, column = 4, sticky='NWNESWSE')

        self.cero = Button(self, font = 100, text = '0', borderwidth = 2, command = lambda: self.appendToDisplay('0'))
        self.cero.grid(row = 4, column = 0, sticky='NWNESWSE', columnspan = 2)

        self.igual = Button(self, font = 100, text = '=', borderwidth = 2, command = lambda: self.calculo())
        self.igual.grid(row = 4, column = 2, sticky='NWNESWSE')

        self.mult = Button(self, font = 100, text = '*', borderwidth = 2, command = lambda: self.appendToDisplay('*'))
        self.mult.grid(row = 4, column = 3, sticky='NWNESWSE')

        self.cambio_base16 = Button(self, font = 100, text = 'B16', borderwidth = 2, command = lambda: self.base16())
        self.cambio_base16.grid(row = 4, column = 4, sticky='NWNESWSE')

        self.A = Button(self, font = 100, text = 'A', borderwidth = 2, command = lambda: self.appendToDisplay('A'))
        self.A.grid(row = 5, column = 0, sticky='NWNESWSE')

        self.B = Button(self, font = 100, text = 'B', borderwidth = 2, command = lambda: self.appendToDisplay('B'))
        self.B.grid(row = 5, column = 1, sticky='NWNESWSE')

        self.C = Button(self, font = 100, text = 'C', borderwidth = 2, command = lambda: self.appendToDisplay('C'))
        self.C.grid(row = 5, column = 2, sticky='NWNESWSE')

        self.D = Button(self, font = 100, text = 'D', borderwidth = 2, command = lambda: self.appendToDisplay('D'))
        self.D.grid(row = 5, column = 3, sticky='NWNESWSE')

        self.E = Button(self, font = 100, text = 'E', borderwidth = 2, command = lambda: self.appendToDisplay('E'))
        self.E.grid(row = 5, column = 4, sticky='NWNESWSE')

        self.F = Button(self, font = 100, text = 'F', borderwidth = 2, command = lambda: self.appendToDisplay('F'))
        self.F.grid(row = 5, column = 5, sticky='NWNESWSE')

        self.c2 = Button(self, font = 100, text = 'C2', borderwidth = 2, command = lambda: self.cambiar_la_base_del_display2())
        self.c2.grid(row = 1, column = 5, sticky='NWNESWSE')

        self.C8 = Button(self, font = 100, text = 'C8', borderwidth = 2, command = lambda: self.cambiar_la_base_del_display8())
        self.C8.grid(row = 2, column = 5, sticky='NWNESWSE')

        self.C10 = Button(self, font = 100, text = 'C10', borderwidth = 2, command = lambda: self.cambiar_la_base_del_display10())
        self.C10.grid(row = 3, column = 5, sticky='NWNESWSE')

        self.C16 = Button(self, font = 100, text = 'C16', borderwidth = 2, command = lambda: self.cambiar_la_base_del_display16())
        self.C16.grid(row = 4, column = 5, sticky='NWNESWSE')

app = Application(calculadora).grid() # Tkinter commands
calculadora.mainloop()
