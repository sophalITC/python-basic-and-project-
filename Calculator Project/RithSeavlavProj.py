from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.geometry("340x420+500+200")
root.resizable(width=False, height=False)
root.grid()
Calculate = Frame(root)
Calculate.grid(pady=1, padx=1)


class Calculate():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.inp_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def n_enter(self, num):
        self.result = False
        st_num = text_display.get()
        nd_num = str(num)
        if self.inp_value:
            self.current = nd_num
            self.inp_value = False
        else:
            if nd_num == ".":
                if nd_num in st_num:
                    return
            self.current = st_num + nd_num
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_fun()
        else:
            self.total = float(text_display.get())

    def display(self, value):
        text_display.delete(0, END)
        text_display.insert(0, value)

    def valid_fun(self):
        if self.op == "sum":
            self.total += self.current
        if self.op == "subtract":
            self.total -= self.current
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "power":
            self.total **= self.current
        self.inp_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_fun()
        elif not self.result:
            self.total = self.current
            self.inp_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def all_clear_enter(self):
        self.clear_enter()
        self.total = 0

    def clear_enter(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.inp_value = True

    def sin_x(self):
        self.result = False
        self.current = math.sin(math.radians(float(text_display.get())))
        self.display(self.current)

    def sinh_x(self):
        self.result = False
        self.current = math.sinh(math.radians(float(text_display.get())))
        self.display(self.current)

    def cos_x(self):
        self.result = False
        self.current = math.cos(math.radians(float(text_display.get())))
        self.display(self.current)

    def cosh_x(self):
        self.result = False
        self.current = math.cosh(math.radians(float(text_display.get())))
        self.display(self.current)

    def tan_x(self):
        self.result = False
        self.current = math.tan(math.radians(float(text_display.get())))
        self.display(self.current)

    def tanh_x(self):
        self.result = False
        self.current = math.tanh(math.radians(float(text_display.get())))
        self.display(self.current)

    def squ(self):
        self.result = False
        self.current = math.sqrt(float(text_display.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def factorial(self):
        self.result = False
        self.current = math.factorial(int(text_display.get()))
        self.display(self.current)

    def logten(self):
        self.result = False
        self.current = math.log10(int(text_display.get()))
        self.display(self.current)

added_value = Calculate()

text_display = Entry(root, font=("arial", 20, "bold"), bd=18, bg="gray", width=20, justify=RIGHT)
text_display.grid(row=0, columnspan=5)
text_display.insert(0, "0")

num_pad = "123456789"
a = 0
btn = []
for b in range(3, 6):
    for c in range(2, 5):
        btn.append(Button(root, text=num_pad[a], font=("ariel", 12, "bold"), bd=4, bg="brown", height=2, width=5))
        btn[a].grid(row=b, column=c, pady=1)
        btn[a] ["command"] = lambda x = num_pad[a] : added_value.n_enter(x)
        a += 1

bt_all_clear = Button(root, text="CE", font=("ariel", 12, "bold"), bd=4, bg="green", height=2,width=5,
                    command=added_value.all_clear_enter).grid(row=1, column=0, pady=1)

bt_clear = Button(root, text="C", font=("ariel", 12, "bold"), bd=4,bg="green", height=2, width=5,
                 command=added_value.clear_enter).grid(row=1, column=1, pady=1)

bt_sum = Button(root, text="+", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
               command=lambda : added_value.operation("sum")).grid(row=3, column=1, pady=1)

bt_sub = Button(root, text="_", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
               command=lambda : added_value.operation("subtract")).grid(row=4, column=1, pady=1)

bt_mult = Button(root, text="x", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
                command=lambda : added_value.operation("multiply")).grid(row=5, column=1, pady=1)

bt_div = Button(root, text=chr(247), font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
               command=lambda : added_value.operation("divide")).grid(row=6, column=1, pady=1)

bt_zero = Button(root, text=0, font=("ariel", 12, "bold"), bd=4, bg="brown", height=2, width=5,
                command=lambda : added_value.n_enter(0)).grid(row=6, column=3, pady=1)

bt_dot = Button(root, text=".", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
               command=lambda : added_value.n_enter(".")).grid(row=6, column=2, pady=1)

bt_equals = Button(root, text="=", font=("ariel", 12, "bold"), bd=4, bg="green", height=2, width=5,
                  command=added_value.sum_of_total).grid(row=6, column=4, pady=1)

bt_sin = Button(root, text="sin", font=("ariel", 12, "bold"), bd=4, padx=1, bg="gray", height=2, width=5,
               command=added_value.sinh_x).grid(row=1, column=2, pady=1)

bt_sinh = Button(root, text="sinh", font=("ariel", 12, "bold"), bd=4, padx=1, bg="gray", height=2, width=5,
               command=added_value.sinh_x).grid(row=2, column=2, pady=1)

bt_cosh = Button(root, text="cosh", font=("ariel", 12, "bold"), bd=4, padx=1, bg="gray", height=2, width=5,
               command=added_value.cosh_x).grid(row=2, column=3, pady=1)

bt_tanh = Button(root, text="tanh", font=("ariel", 12, "bold"), bd=4, padx=1, bg="gray", height=2, width=5,
               command=added_value.tanh_x).grid(row=2, column=4, pady=1)

bt_cos = Button(root, text="cos", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
               command=added_value.cos_x).grid(row=1, column=3, pady=1)

bt_tan = Button(root, text="tan", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
               command=added_value.tan_x).grid(row=1, column=4, pady=1)

bt_pi = Button(root, text="pi", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
              command=added_value.pi).grid(row=6, column=0, pady=1)

bt_fact = Button(root, text="!", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
                 command=added_value.factorial).grid(row=2, column=0, pady=1)

bt_power = Button(root, text="^", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
                 command=lambda :added_value.operation("power")).grid(row=3, column=0, pady=1)

bt_squ = Button(root, text="√", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
               command=added_value.squ).grid(row=4, column=0, pady=1)

bt_exp = Button(root, text="e", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
              command=added_value.exp).grid(row=5, column=0, pady=1)

bt_logten = Button(root, text="log10", font=("ariel", 12, "bold"), bd=4, bg="gray", height=2, width=5,
              command=added_value.logten).grid(row=2, column=1, pady=1)

root.mainloop()