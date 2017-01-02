# code-katas

Proper Parenthetics challenge code:
    The idea is to record  the index numbers of each parenthetical, then compare them in pairs
    by iterating through two queues. If the closing parentheical has a lower index than its paired
    opening parenthetical, it's broken. If there are more opens than closes, it's open. If there
    are more closes than opens, it's broken again. If there are exactly the same number, and the
    opens always come first, they're balanced.

Sort Cards code:
    I wanted to avoid looping through the list of cards more than once, so I built a dictonary with
    keys for each card value, appended cards to lists tied to the appropriate keys, and then
    concatenated the lists in the correct order. There's probably a dryer way to do it.



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

Test if club member is a senior
    -module: open_or_senior.py
    -tests: test_open_or_senior.py
    -link: https://www.codewars.com/kata/categorize-new-member/train/python
```python
    def openOrSenior(data):
        """This was the solution by taw. I was trying for this exact thing, but I couldn't get the and syntax working."""
        return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
```

Test if a number is even or odd
    -module even_odd.py
    -test test_even_odd.py
    -link https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
```python
    def even_or_odd(number):
    """laoris, colbydauph, gdude2002, Wynkth, ksolademi, ilgiz (plus 208 more warriors) came up with this solution."""
  return 'Odd' if number % 2 else 'Even'
```

Remove the first and last char of a string.
    -module remove_chars.py
    -test test_remove_chars.py
    -link https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/solutions/python
```python
    remove_char=lambda s: s[1:-1]
    """GiacomoSorbi, suic, LazyWolf, lechevalier, sperry, Mikhail158 (plus 5 more warriors) came up with this solution."""
```

Remove the first and last char of a string.
    -module opposite.py
    -test test_opposite.py
    -link https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python
```python
    def opposite(number):
        return -number
    """CrazyMerlyn, ChristianECooper, Nuskeur, tigretoncio, VadimPopov, Django99 (plus 562 more warriors )came up with this solution."""
```

Remove the first and last char of a string.
    -module next_square.py
    -test test_next_square.py
    -link https://www.codewars.com/kata/find-the-next-perfect-square/train/python
```python
    from math import sqrt
    def find_next_square(sq):
        return (sqrt(sq)+1)**2 if sqrt(sq)%1 == 0 else -1
        """AndrewOsentoski, JustinDenk came up with this solution."""
```

Remove the first and last char of a string.
    -module np_year.py
    -test test_np_year.py
    -link https://www.codewars.com/kata/growth-of-a-population/train/python
```python
    def nb_year(population, percent, aug, target):
        """S666, MMMAAANNN came up with this solution."""
        year = 0
        while population < target:
            population += population * percent / 100. + aug
            year += 1
        return year
```

Remove the first and last char of a string.
    -module sheep.py
    -test test_sheep.py
    -link https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python
```python
    def count_sheeps(arrayOfSheeps):
        """jhoffner, mortonfox, zmoses, f331a, misuburlacu, MatthiasLenz (plus 376 more warriors) came up with this solution."""
        return arrayOfSheeps.count(True)
```

Remove the first and last char of a string.
    -module count.py
    -test test_count.py
    -link https://www.codewars.com/kata/vowel-count/train/python
```python
    def getCount(inputStr):
    """javaafreak, ChingChangChong, hdang101, ronanodufaigh, rbordiya, alpharom came up with this solution."""
        return sum(1 for let in inputStr if let in "aeiouAEIOU")
```

Generate sum and round to two decimal places a list of n items.
    -module sum_terms.py
    -test test_sum_terms.py
    -link http://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/train/python
```python
    series_sum = lambda n: '{:.2f}'.format(sum(1.0/(3*i-2) for i in xrange(1, n+1)))
    """tchar came up with this solution. I like the brevity."""
```