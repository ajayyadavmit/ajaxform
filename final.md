Lambdas, comprehensions, closures, and decorators in Python all share functional programming concepts, particularly in how they can encapsulate behavior or modify functions. Here’s how they are similar:

### Lambdas and Closures

- **Lambdas**: Anonymous functions that can capture variables from their surrounding scope, making them closures.
  
  ```python
  def make_multiplier(n):
      return lambda x: x * n
  
  double = make_multiplier(2)
  print(double(5))  # Output: 10
  ```

### Comprehensions and Closures

- **Comprehensions**: Can use variables from the enclosing scope, similar to closures.
  
  ```python
  base = 2
  squares = [x**2 + base for x in range(5)]
  print(squares)  # Output: [2, 3, 6, 11, 18]
  ```

### Decorators as Closures

- **Decorators**: Are a form of closure, where the inner function retains access to the outer function’s variables.
  
  ```python
  def my_decorator(func):
      def wrapper():
          print("Before")
          func()
          print("After")
      return wrapper
  
  def say_hello():
      print("Hello!")

  decorated = my_decorator(say_hello)
  decorated()
  ```

### Similarities

1. **Scope**: All can capture variables from their surrounding scope.
2. **Functional Style**: They enable concise and functional programming patterns.
3. **Behavior Encapsulation**: They encapsulate behavior or transformations in a compact form.

### Differences

- **Lambdas**: Single-expression functions used for short operations.
- **Comprehensions**: Used for creating lists, sets, or dictionaries in a clear and concise way.
- **Closures**: Functions that capture their surrounding context.
- **Decorators**: Higher-order functions specifically designed to modify or enhance other functions.

Feel free to ask for more details or examples!
