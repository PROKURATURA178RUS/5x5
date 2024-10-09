input_data = open('input.txt','r')
data = input_data.read ()
a = int(data[0])
k = 0
for i in range(5, 4 * 10**5):
    k = a * a
    

output_data = open('output.txt','w')
output_data.write(str(k))
input_data.close()
output_data.close()