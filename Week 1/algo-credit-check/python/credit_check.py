def credit_check(str):
  length = len(str)-1
  math_check = []
  while length >= 0:
    main_num = int(str[length])
    if main_num % 2 == 0:
      doubled = main_num * 2
      string_doubled = f"{doubled}"
      split_doubled = string_doubled.split()
      if len(split_doubled) > 1:
        temp_sum = sum(split_doubled)
        math_check.append(temp_sum)
      else:
        math_check.append(doubled)
    else:
      math_check.append(main_num)
    length -= 1
  answer_var = sum(math_check)

  return "The number is valid!" if answer_var % 10 == 0 else "The number is invalid!"

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

print(credit_check('5541808923795240'))