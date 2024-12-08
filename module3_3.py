def print_params(a= 1, b= "string", c= True):
    print(a,b,c)
print_params()
print_params(a=2, c=False)
print_params(a=10, b=12, c="Привет")
print_params(b= 25)
print_params(c=[1,2,3])

value_list = [10, False, "Здравствуйте"]
value_dict = {"a":10, "b":False, "c": "Hello"}
print_params(*value_list)
print_params(**value_dict)

values_list_2 = [10.22, "Margo"]
print_params(*values_list_2, 42)