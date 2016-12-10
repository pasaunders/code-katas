# code-katas
Codewars practice code
Katas completed and recorded in the following format:
  Do the Thing with the Stuff
    - Module: module_name.py
    - Tests: test_module_name.py
    - Link: http://www.codewars.com/some-kata-url
Followed by the most interesting solution provided by codewars after kata completion:
  ```python
    def some_func():
      """This was the solution by programmer_username."""
      # some stuff happens in this function
  ```


Add two numbers and convert to a binary string
    - Module: binary_addition.py
    - Tests: test_binary_addtion.py
    - Link: https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python
```python
    def add_binary(a, b):
    """This was the solution by Loontje, zebulan, Zerazera, Myon, jamenlong, 13ROY (plus 41 more warriors)."""
        return format(a + b, 'b')
```


Return the highest and lowest numbers in a list
    -module: high_low.py
    -tests: test_high_low.py
    -link: https://www.codewars.com/kata/highest-and-lowest/train/python
```python
    def high_and_low(numbers): #z.
        """This was the solution by Deantwo."""
        nn = [int(s) for s in numbers.split(" ")]
        return "%i %i" % (max(nn),min(nn))
```