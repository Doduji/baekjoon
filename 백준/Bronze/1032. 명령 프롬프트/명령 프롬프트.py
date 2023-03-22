n = int(input())
str = []

for i in range(0, n) :
   file_name = input()
   str.append(file_name)

result=str[0]

for j in range(0, len(str[0])) :
   for k in range(0, n) :
      if result[j] != str[k][j] :
         tmp_str = list(result)
         tmp_str[j] = '?'
         result=''.join(tmp_str)

print(result)