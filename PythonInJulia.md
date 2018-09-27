### 调用python
`using PyCall`

1.
```
pysum = pybuiltin("sum")
```

2.
```
numpy_sum = pyimport("numpy")["sum"]
```

3.
```
py"""
def foo():
    pass
"""
sum_py = py"foo"
```

note:
- py_hand = @benchmark $sum_py($a)
