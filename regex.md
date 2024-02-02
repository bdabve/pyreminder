<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content:

- [Matching Regex Objects](#matching-regex-objects)
- [Grouping with Parentheses](#grouping-with-parentheses)
- [Matching Multiple Groups with the Pipe](#matching-multiple-groups-with-the-pipe)
- [Optional Matching with the Question Mark](#optional-matching-with-the-question-mark)
- [Matching Zero or More with the Star](#matching-zero-or-more-with-the-star)
- [Matching One or More with the Plus](#matching-one-or-more-with-the-plus)
- [Matching Specific Repetitions with Curly Brackets](#matching-specific-repetitions-with-curly-brackets)
- [Greedy and Nongreedy Matching](#greedy-and-nongreedy-matching)
- [The findall() Method](#the-findall-method)
- [Making Your Own Character Classes](#making-your-own-character-classes)
- [The Caret and Dollar Sign Characters](#the-caret-and-dollar-sign-characters)
- [The Wildcard Character](#the-wildcard-character)
- [Matching Everything with Dot-Star](#matching-everything-with-dot-star)
- [Matching Newlines with the Dot Character](#matching-newlines-with-the-dot-character)
- [Review of Regex Symbols](#review-of-regex-symbols)
- [Case-Insensitive Matching](#case-insensitive-matching)
- [Substituting Strings with the sub() Method](#substituting-strings-with-the-sub-method)
- [Managing Complex Regexes](#managing-complex-regexes)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## Regular Expressions

1. Import the regex module with `import re`.
1. Create a Regex object with the `re.compile()` function. (Remember to use a raw string.)
1. Pass the string you want to search into the Regex object’s `search()` method. This returns a `Match` object.
1. Call the Match object’s `group()` method to return a string of the actual matched text.


- All the regex functions in Python are in the re module:

  ```python
  >>> import re
  ```

[*Return to the Top*](#table-of-content)

### Matching Regex Objects

```python
>>> phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phone_num_regex.search('My number is 415-555-4242.')
>>> print('Phone number found: {}'.format(mo.group()))              # Phone number found: 415-555-4242
```

[*Return to the Top*](#table-of-content)

### Grouping with Parentheses

```python
>>> phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phone_num_regex.search('My number is 415-555-4242.')
>>> mo.group(1)             # '415'
>>> mo.group(2)             # '555-4242'
>>> mo.group(0)             # '415-555-4242'
>>> mo.group()              # '415-555-4242'
```

- To retrieve all the groups at once: use the `groups()` method note the plural form for the name.

  ```python
  >>> phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
  >>> mo = phone_num_regex.search('My number is 415-555-4242.')
  >>> mo.groups()                           # ('415', '555-4242')
  >>> area_code, main_number = mo.groups() 
  >>> print(area_code)                      # 415
  >>> print(main_number)                    # 555-4242
  ```

- To Match parentheses escape them. They have a special meaning in regular expressions.

  ```python
  >>> phone_number = 'My phone number is: (415) 555-4242.'
  >>> found_number = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
  >>> mo = found_number.search(phone_number)
  >>> print(mo.group(1))                    # (415)
  >>> print(mo.group(2))                    # 555-4242
  ```

[*Return to the Top*](#table-of-content)

### Matching Multiple Groups with the Pipe

- The `|` character is called a pipe. 
- You can use it anywhere you want to match one of many expressions. 
- For example, the regular expression `r'Batman|Tina Fey'` will match either 'Batman' or 'Tina Fey'.

  ```python
  >>> hero_regex = re.compile (r'Batman|Tina Fey')
  >>> mo1 = hero_regex.search('Batman and Tina Fey.')
  >>> mo1.group()               # 'Batman'

  >>> mo2 = hero_regex.search('Tina Fey and Batman.')
  >>> mo2.group()               # 'Tina Fey'
  ```

- You can also use the pipe to match one of several patterns as part of your regex:

  ```python
  >>> bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
  >>> mo = bat_regex.search('Batmobile lost a wheel')
  >>> mo.group()                # 'Batmobile'
  >>> mo.group(1)               # 'mobile'
  
  >>> mo1 = bat_regex.search('Batbote lost a wheel')
  >>> mo1 is None           # True
  ```

[*Return to the Top*](#table-of-content)

### Optional Matching with the Question Mark

- The `?` character flags the group that precedes it as an optional part of the pattern.
  > (wo)?: means that the pattern (wo) is an optional group.
  > The regex will match text that has zero instances or one instance of wo in it.
  
  ```python
  >>> bat_regex = re.compile(r'Bat(wo)?man')
  >>> mo1 = bat_regex.search('The Adventures of Batman')
  >>> mo1.group()               # 'Batman'

  >>> mo2 = bat_regex.search('The Adventures of Batwoman')
  >>> mo2.group()               # 'Batwoman'
  ```

- Make the regex look for phone numbers that do or do not have an area code.

  ```python
  >>> found_number = re.compile(r'(\d\d\d\-)?\d\d\d-\d\d\d\d')
  >>> mo = found_number.search('My phone number is: 415-555-4242.')
  >>> print(mo.group())                    # 415-555-4242
  >>> mo = found_number.search('My phone number is: 555-4242.')
  >>> print(mo.group())             # 555-4242
  ```

[*Return to the Top*](#table-of-content)

### Matching Zero or More with the Star

- The `*` means 'match zero or more' the group that precedes the star can occur any number of times in the text.

  ```python
  >>> bat_regex = re.compile(r'Bat(wo)*man')
  >>> mo1 = bat_regex.search('The Adventures of Batman')
  >>> mo1.group()                 # 'Batman'

  >>> mo2 = bat_regex.search('The Adventures of Batwoman')
  >>> mo2.group()                 # 'Batwoman'

  >>> mo3 = bat_regex.search('The Adventures of Batwowowowoman')
  >>> mo3.group()                 # 'Batwowowowoman'
  ```

[*Return to the Top*](#table-of-content)

### Matching One or More with the Plus

- While `*` means 'match zero or more,' the `+` (or plus) means 'match one or more'. 
- The group preceding a plus must appear at least once. It is not optional:

  ```python
  >>> bat_regex = re.compile(r'Bat(wo)+man')
  >>> mo1 = bat_regex.search('The Adventures of Batwoman')
  >>> mo1.group()               # 'Batwoman'
  
  >>> mo2 = bat_regex.search('The Adventures of Batwowowowoman')
  >>> mo2.group()               # 'Batwowowowoman'
  
  # The regex Bat(wo)+man will not match the string 'The Adventures of Batman'
  # Because at least one wo is required by the plus sign.
  >>> mo3 = bat_regex.search('The Adventures of Batman')
  >>> mo3 is None                   # True
  ```

[*Return to the Top*](#table-of-content)

### Matching Specific Repetitions with Curly Brackets

- If you have a group that you want to repeat a specific number of times, follow the group in your regex with a number in curly brackets. 
- For example, the regex (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa', since the latter has only two repeats of the (Ha) group.

- Instead of one number, you can specify a range by writing a minimum, a comma, and a maximum in between the curly brackets. 
- For example, the regex `(Ha){3,5}` will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.

  ```python
  >>> ha_regex = re.compile(r'(Ha){3}')
  >>> mo1 = ha_regex.search('HaHaHa')
  >>> mo1.group()                       # 'HaHaHa'

  >>> mo2 = ha_regex.search('Ha')
  >>> mo2 is None                       # True
  ```

[*Return to the Top*](#table-of-content)

### Greedy and Nongreedy Matching

- Python's regular expressions are greedy by default, Which means they will match the longest string possible.
- `(Ha){3,5}` returns 'HaHaHaHaHa' instead of the shorter possibilities

- The non-greedy version of the curly brackets, which matches the shortest string possible, has the closing curly bracket followed by a question mark.

  ```python
  >>> greedy_ha_regex = re.compile(r'(Ha){3,5}')
  >>> mo1 = greedy_ha_regex.search('HaHaHaHaHa')
  >>> mo1.group()               # 'HaHaHaHaHa'

  >>> nongreedy_ha_regex = re.compile(r'(Ha){3,5}?')
  >>> mo2 = nongreedy_ha_regex.search('HaHaHaHaHa')
  >>> mo2.group()               # 'HaHaHa'
  
  >>> nonGreedy = re.compile(r'<.*?>')
  >>> mo = nonGreedy.search('<To serve man> for dinner.>')
  >>> print(mo.group())                     # <To serve man>

  >>> greedy = re.compile(r'<.*>')
  >>> mo = greedy.search('<To serve man> for dinner.>')
  >>> print(mo.group())                     # <To serve man> for dinner>
  ```

[*Return to the Top*](#table-of-content)

### The findall() Method

- In addition to the search() method, Regex objects also have a findall() method. 
- While `search()` will return a Match object of the first matched text in the searched string, 
- the `findall()` method will return the strings of every match in the searched string.

  ```python
  >>> phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')                 # has no groups
  >>> phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')        # ['415-555-9999', '212-555-0000']
  
  >>> found_number = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
  >>> mo_all = found_number.findall(phone_number)
  >>> print(mo_all)        # [('415', '555', '9999'), ('212', '555', '0000')]
  ```

- When called on a regex with no groups, such as \d-\d\d\d-\d\d\d\d, the method findall() returns a list of n matches, such as ['415-555-9999', '212-555-0000'].

- When called on a regex that has groups, such as (\d\d\d)-(d\d)-(\d\d\d\d), the method findall() returns a list of strings (one string for each group), such as [('415', '555', '9999'), ('212', '555', '0000')].

[*Return to the Top*](#table-of-content)

### Making Your Own Character Classes

- There are times when you want to match a set of characters but the shorthand character classes (\d, \w, \s, and so on) are too broad. 
- You can define your own character class using square brackets. 
- For example, the character class `[aeiouAEIOU]` will match any vowel, both lowercase and uppercase.

  ```python
  >>> vowel_regex = re.compile(r'[aeiouAEIOU]')
  >>> vowel_regex.findall('Robocop eats baby food. BABY FOOD.')
  ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
  ```

- You can also include ranges of letters or numbers by using a hyphen. 
- For example, the character class `[a-zA-Z0-9]` will match all lowercase letters, uppercase letters, and numbers.

- By placing a caret character (^) just after the character class's opening bracket, you can make a negative character class. 
- A negative character class will match all the characters that are not in the character class. 

  ```python
  >>> consonant_regex = re.compile(r'[^aeiouAEIOU]')
  >>> consonant_regex.findall('Robocop eats baby food. BABY FOOD.')
  ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '
  ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
  ```

[*Return to the Top*](#table-of-content)

### The Caret and Dollar Sign Characters

- You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text.

- Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern.

- And you can use the ^ and $ together to indicate that the entire string must match the regex—that is, it’s not enough for a match to be made on some subset of the string.

- The r'^Hello' regular expression string matches strings that begin with 'Hello':

  ```python
  >>> begins_with_hello = re.compile(r'^Hello')

  >>> begins_with_hello.search('Hello world!')              # <_sre.SRE_Match object; span=(0, 5), match='Hello'>
  >>> begins_with_hello.search('He said hello.') is None    # True
  ```

- The r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9:

  ```python
  >>> whole_string_is_num = re.compile(r'^\d+$')
  >>> whole_string_is_num.search('1234567890')              # <_sre.SRE_Match object; span=(0, 10), match='1234567890'>
  >>> whole_string_is_num.search('12345xyz67890') is None   # True
  >>> whole_string_is_num.search('12 34567890') is None     # True
  ```

[*Return to the Top*](#table-of-content)

### The Wildcard Character

- The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline:

  ```python
  >>> at_regex = re.compile(r'.at')

  >>> at_regex.findall('The cat in the hat sat on the flat mat.')       # ['cat', 'hat', 'sat', 'lat', 'mat']
  ```

[*Return to the Top*](#table-of-content)

### Matching Everything with Dot-Star

```python
>>> name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = name_regex.search('First Name: Al Last Name: Sweigart')
>>> mo.group(1)             # 'Al'
>>> mo.group(2)             # 'Sweigart'
```

- The dot-star uses greedy mode: It will always try to match as much text as possible. 
- To match any and all text in a nongreedy fashion, use the dot, star, and question mark (.*?). 
- The question mark tells Python to match in a nongreedy way:

  ```python
  >>> nongreedy_regex = re.compile(r'<.*?>')
  >>> mo = nongreedy_regex.search('<To serve man> for dinner.>')
  >>> mo.group()                            # '<To serve man>'

  >>> greedy_regex = re.compile(r'<.*>')
  >>> mo = greedy_regex.search('<To serve man> for dinner.>')
  >>> mo.group()                            # '<To serve man> for dinner.>'
  ```

[*Return to the Top*](#table-of-content)

### Matching Newlines with the Dot Character

- The dot-star will match everything except a newline. 
- By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character:

  ```python
  >>> no_newline_regex = re.compile('.*')
  >>> no_newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
  'Serve the public trust.'

  >>> newline_regex = re.compile('.*', re.DOTALL)
  >>> newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
  'Serve the public trust.\nProtect the innocent.\nUphold the law.'
  ```

[*Return to the Top*](#table-of-content)

### Review of Regex Symbols

| Symbol                   | Matches                                                      |
| ------------------------ | ------------------------------------------------------------ |
| `?`                      | zero or one of the preceding group.                          |
| `*`                      | zero or more of the preceding group.                         |
| `+`                      | one or more of the preceding group.                          |
| `{n}`                    | exactly n of the preceding group.                            |
| `{n,}`                   | n or more of the preceding group.                            |
| `{,m}`                   | 0 to m of the preceding group.                               |
| `{n,m}`                  | at least n and at most m of the preceding p.                 |
| `{n,m}?` or `*?` or `+?` | performs a nongreedy match of the preceding p.               |
| `^spam`                  | means the string must begin with spam.                       |
| `spam$`                  | means the string must end with spam.                         |
| `.`                      | any character, except newline characters.                    |
| `\d`, `\w`, and `\s`     | a digit, word, or space character, respectively.                 |
| `\D`, `\W`, and `\S`     | anything except a digit, word, or space acter, respectively. |
| `[abc]`                  | any character between the brackets (such as a, b, ).         |
| `[^abc]`                 | any character that isn’t between the brackets.              |

- Character Classes

| Shorthand |   Represents
| ----------|------------------------------------------
|   \d      | Any numeric digit from 0 to 9.
|   \D      | Any character that is not a numeric digit from 0 to 9.
|   \w      | Any letter, numeric digit, or the underscore character. (word)
|   \W      | Any character that is not a letter, numeric digit or the _ char.
|   \s      | Any space, tab, or newline character. (Think of this as 'space')
|   \S      | Any character that is not a space, tab or newline.
|

- Character classes are nice for shortening regex.
- The character class [0-5] will match only the numbers 0 to 5

  ```python
  >>> xmas_regex = re.compile(r'\d+\s\w+')
  >>> print(xmas_regex.findall('12 drummers, 11 pipers, lords, 8 maids, 7swans, 4 birds, 3 hens, 2doves, partridge'))
  ['12 drummers', '11 pipers', '8 maids', '4 birds', '3 hens']
  ```

- The regular expression < \d+\s\w+ > will match text that has one or more
- numeric digits (\d+), followed by a whitespace character (\s),
- followed by one or more letter/digit/underscore characters (\w+).
-
[*Return to the Top*](#table-of-content)

### Case-Insensitive Matching

- To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile():

  ```python
  >>> robocop = re.compile(r'robocop', re.I)
  >>> robocop.search('Robocop is part man, part machine, all cop.').group()         # 'Robocop'
  
  >>> robocop.search('ROBOCOP protects the innocent.').group()                      # 'ROBOCOP'

  >>> robocop.search('Al, why does your programming book talk about robocop so much?').group()  # 'robocop'
  ```

[*Return to the Top*](#table-of-content)

### Substituting Strings with the sub() Method

- The sub() method for Regex objects is passed two arguments:

  1. The first argument is a string to replace any matches.
  1. The second is the string for the regular expression.

- The sub() method returns a string with the substitutions applied:

  ```python
  >>> names_regex = re.compile(r'Agent \w+')

  >>> names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
  'CENSORED gave the secret documents to CENSORED.'
  ```

- Another example:

  ```python
  >>> agent_names_regex = re.compile(r'Agent (\w)\w*')

  >>> agent_names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
  A**** told C**** that E**** knew B**** was a double agent.'
  ```

[*Return to the Top*](#table-of-content)

### Managing Complex Regexes

- To tell the re.compile() function to ignore whitespace and comments inside the regular expression string, “verbose mode” can be enabled by passing the variable re.VERBOSE as the second argument to re.compile().

- Now instead of a hard-to-read regular expression like this:

  ```python
  phone_regex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
  ```

- you can spread the regular expression over multiple lines with comments like this:

  ```python
  phone_regex = re.compile(r'''(
      (\d{3}|\(\d{3}\))?            # area code
      (\s|-|\.)?                    # separator
      \d{3}                         # first 3 digits
      (\s|-|\.)                     # separator
      \d{4}                         # last 4 digits
      (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
      )''', re.VERBOSE)
  ```

- Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
- If you want a regular expression that's caseinsensitive and includes newlines
- to match the dot character, you would form your re.compile() call like this:

  ```python
  >>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
  >>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
  ```

[*Return to the Top*](#table-of-content)
