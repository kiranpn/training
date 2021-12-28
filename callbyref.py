def test_func(param1, list_param=[]):
    list_param.append('test')
    print(param1, list_param, "-----",id(list_param))
    
test_func("one")
test_func("two", ["new"])
test_func("three")