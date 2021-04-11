# # -----------  *args ------------------------ 

def get_all(*args):
    for i in args:
        print(i)

# get_all("bir", 2, 3)

#-------------

def get_all(*args):
    for i in args:
        print(i)

l = [ "bir", 2, 3 ]
get_all(l)                # if we pass [ "bir", 2, 3 ]  => we get  whole '[ "bir", 2, 3 ]' 

# --------------

def get_all(*args):
    for i in args:
        print(i)

l = [ "bir", 2, 3 ]
get_all(*l)

# if we pass   '*l' prints all as expected  1,2,3,





# ----------

def sum_nums(*args):
    for num in args:
        num += 1
        print (num)

sum_nums(18, 2, 8, 20) 


# --------------------------------


def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)

# -------------------------------------------


def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)

args = ("Sammy", "Casey", "Alex")

some_args(*args)


## ++++++++++++++++++++++ **kargs +++++++


def print_kwargs(**kwargs):
        my_dic = kwargs.items()
        a=[("test", "testvalue")]
        my_dic +=a

        for key,value in my_dic:
            if "Mirlan" in str(value) and isinstance(value, str):
                print (value)
print_kwargs(name="Mirlan", age = 40, phone = 12121211)

# ----------------------------

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

# call:

print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
        )


===============================

def post(**kwargs):

    extra_payload = kwargs.get('update_payload')
    remove_payload = kwargs.get('remove_payload')
    headers = kwargs.get('headers')
    token = kwargs.get('custom_token', "self._token")
    print(token)

    print(kwargs['meaders'] )
    return kwargs


print(post(   custom_token="Bir",  headers="bash", meaders="put" ))
