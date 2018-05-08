
import collections

i="Mirlan  :   Tokonbekov"

my_dict = collections.OrderedDict()

d_key, d_value = i.split(" : ", 2)  # type: str
my_dict[d_key.strip()] = d_value.strip()

print(my_dict)

