#test = 'test'
#print(help(test))
#print(dir(test))


inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0]
		  ,[0.5, -0.91, 0.26, -0.5]
		  ,[-0.26, -0.27, 0.17, 0.87]]

#print(weights[0][0])

biases = [2, 3, 0.5]

# output = [inputs[0]*weights[0][0] + inputs[1]*weights[0][1] + inputs[2]*weights[0][2] + inputs[3]*weights[0][3] + biases[0]
# 		 ,inputs[0]*weights[1][0] + inputs[1]*weights[1][1] + inputs[2]*weights[1][2] + inputs[3]*weights[1][3] + biases[1]
# 		 ,inputs[0]*weights[2][0] + inputs[1]*weights[2][1] + inputs[2]*weights[2][2] + inputs[3]*weights[2][3] + biases[2]]

# print('neurone outputs', output)


layer_outputs = []
for n_w, n_b in zip(weights, biases):
	print('__________\\nweights per neuron')
	print(n_w, n_b, '\n__________')
	n_out = 0
	for n_in, w in zip(inputs, n_w):
		n_out += n_in*w
		print('input: ', n_in, '| weight: ', w, '| neurone bias: ', n_b)
		print('input * weight: ', n_out)
	n_out += n_b
	#print('____________\\nneurone output:', n_out)
	layer_outputs.append(n_out)

print(layer_outputs)