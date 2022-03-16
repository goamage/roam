import json
import requests as rq

# dict structure
_dict = [{'1L1': '1L1', '1L2': 2, '1L3':[{
			'2L1': 1, '2L2': 2},
			'2L3']
		},
		{'2L1': '2L1', '2L2': 2, '2L3': [{
			'2L1': 1, '2L2': '2L2'
			}]
		}]

#print(_dict)
print(json.dumps(_dict, indent=4, sort_keys=True), '\n')
#print(json.dumps(_dict[0]['1L3'], indent=4, sort_keys=True))
#print(json.dumps(_dict[0]['1L3'][0], indent=4, sort_keys=True))
print(json.dumps(_dict[0]['1L3'][0]['2L1'], indent=4, sort_keys=True))
#print(json.dumps(_dict[0]['1L3'][1], indent=4, sort_keys=True))


# save and read dict files



# https://github.com/public-apis/public-apis





# your_json = '{"bar":["baz", null, 1.0, 2]}' # string
# print(your_json)

# parsed = json.loads(your_json) # to json
# print(json.dumps(parsed, indent=4, sort_keys=True))


# auth = ('test','test')
# r = rq.get('https://httpbin.org/basic-auth/test/test', auth = auth)
# print(r.json())
# print(json.dumps(r.json(), indent=4))

# your_dict = {'1L1': '1L1', '1L2': 2, '1L3':[{
# 	'dol1': 1, 'dol2': 2},
# 	'dol3']
# 	}
# print(json.dumps(your_dict, indent=4), '\n')

# print(your_dict.keys())
# print(your_dict.values())

# print(your_dict['1L1'], '\n') # tor

# print(your_dict['1L3'],'\n') # list dol + dol3
# print(your_dict['1L3'][0]) # list dol - dol3
# print(your_dict['1L3'][0]['dol1']) # nothing