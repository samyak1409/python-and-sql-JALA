# 4. Define the local and Global variables with the same name and print both variables and
# understand the scope of the variables.


def func() -> None:
    var = 'local'  # (python doesn't promote this)
    print(var)


var = 'global'

func()

print(var)
