import re

# 1. string that has an 'a' followed by zero or more 'b''s.
text = "ab"
print(bool(re.fullmatch(r'ab*', text)))  # True

# 2. string that has an 'a' followed by two to three 'b'.
text = "abb"
print(bool(re.fullmatch(r'ab{2,3}', text)))  # True

# 3. sequences of lowercase letters joined with a underscore.
text = "hello_world test_case example_text"
print(re.findall(r'\b[a-z]+_[a-z]+\b', text))  # ['hello_world', 'test_case', 'example_text']

# 4. one upper case letter followed by lower case letters.
text = "Hello world This Is A Test"
print(re.findall(r'\b[A-Z][a-z]+\b', text))  # ['Hello', 'This', 'Is', 'Test']

# 5. 'a' followed by anything, ending in 'b'.
text = "a123b"
print(bool(re.fullmatch(r'a.*b', text)))  # True

# 6. replace all occurrences of space, comma, or dot with a colon.
text = "hello, world. test"
print(re.sub(r'[ ,.]', ':', text))  # hello:world:test

# 7. snake_case в CamelCase
text = "hello_world"
words = text.split('_')
print(words[0] + ''.join(word.capitalize() for word in words[1:]))  # helloWorld

# 8. split a string at uppercase letters
text = "HelloWorldTest"
print(re.findall(r'[A-Z][a-z]*', text))  # ['Hello', 'World', 'Test']

# 9. insert spaces
text = "HelloWorldTest"
print(re.sub(r'(?<!^)([A-Z])', r' \1', text))  # Hello World Test

# 10 CamelCase в snake_case
text = "HelloWorldTest"
print(re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower())  # hello_world_test