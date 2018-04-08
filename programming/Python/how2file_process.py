def get_label_dict(file_path, label_position=0):
	"""
	Input as labeled file.
	e.g.,
	one line : label, word1, word2, word3, ...
	"""
	label_dict = {'label2index': {}, 'index2label': {}}
	with open(file_path, 'r', encoding='utf8') as f:
		for line in f:
			label = line.split()[label_position]
			index = label_dict['label2index']
			label_dict['label2index'] = index
			label_dict['index2label'] = label

	return label_dict


def make_labeled_file_per_class(input_file, output_file, instance_per_class=0, shuffle=True, complexity=20, label_position=0):
    """
    How to use :
    file_path = "/Users/sungmin/Desktop/transfer_learning/Dataset/Seal-Software/41k_downsampled/2k_sample_provisions.txt"
    trainloader = get_train_loader(file_path)
    for
    """
    import numpy as np

    with open(input_file, 'r', encoding='utf8') as f:
        for line in f:
        	label = line.split()[label_position]
            try : traindata_dict[label] += 1
		    except : traindata_dict[label] == 1

		    if traindata_dict[label] >= instance_per_class:
		    	continue			

			traindata.append(line.rstrip('\n'))

	if shuffle:
	    for _ in range(complexity):
	    	np.random.shuffle(traindata)
 

    with open(output_file, 'w', encoding='utf8') as f:
    	for line in traindata:
    		if not line.endswith('\n') : line+=' \n'
    		f.write(line)

    return print("Successfully make labeled file per class, per class {} instance exist".format(instance_per_class))


def file_read_MultiProcess(file_path, process_func=False, num_workers=1, batch_size=4):
	import multiprocessing as mp

	if not process_func:
		print("You did not provide process function, using defualt function which returns just line")
		def process_fun(inputs):
			return inputs
    
    cpu_num = mp.cpu_count()
    print("You have {} CPU avaiable. You chose {} CPU for processing".format(cpu_num, num_workers))

    pool = mp.Pool(num_workers)
    with open(file_path, 'r', encoding='utf8') as source_file:
    	results = pool.map(process_line, source_file, batch_size)
	pool.close()

	return result
