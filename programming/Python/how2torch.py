def double_pool1d(inputs, pool_type="average", batch_first=False, window_size=5, padding=0, max_units=50, stride_factor=32):
    """DEPRECATED, it's in smnlp_tl"""
    return None
    
    
    
    
import torch
import torch.nn as nn
from torch.nn import functional as F



# How to make contiguous array
# When array is numpy array
# Source : https://github.com/pytorch/pytorch/issues/3468 
# HPTT provides quite a dramatic speedup for stuff like x.transpose(0, 1).contiguous(), calls which are quite common all over the place.

# With Numpy as a baseline it provides 5x+ speedup consistently.
target_array = np.transpose(target_array, (0,1,2)).continguous()
target_array = target_array.permute(0,1,2).continguous()

# When, Varibale is transposed, not contiguous anymore.
target_array = torch.autograd.Variable(torch.randn(5,10,3)).t()             # target.size()==10,5,3  # torch.randn is FloatTensor
target_array = torch.autograd.Variable(torch.randn(5,10,3)).permute(1,0,2)  # target.size()==10,5,3 
# Both of them are not contiguous, simply change by one line.
target_array.contiguous() # does not increase performance dramatically, maybe 1-2%


# Issue with fast/slow pack/unpack
# https://github.com/pytorch/pytorch/issues/1788



# Add <pad> for word-dictionary
index = len(word_dict["word2index"])
word_dict["word2index"]["<pad>"] = index
word_dict["index2word"][index]   = "<pad>"
# Add one more index-weights in embedding state_dict
# > Either : pretrained_state_dict["encoder"]["weight"] += [Embedding_dim_weights] 
# > OR     : pretrained_state_dict.encoder.weight.append([Embedding_dim_weights])



# How to use multi model

# Make multi models
model_agnews = RNNModel(rnn_type, ntoken, ninp, nhid, nlayers, nclass, nhid_linear,
                 dropout, dropouth, dropouti, dropoute, wdrop, tied, pooling,
                 batch_norm, dropout_additional, relu)

model_wiki = RNNModel(rnn_type, ntoken, ninp, nhid, nlayers, nclass, nhid_linear,
                 dropout, dropouth, dropouti, dropoute, wdrop, tied, pooling,
                 batch_norm, dropout_additional, relu)
model_cat  = CatModel(input_dim, nclass)

# Load weights for models.
if from_scratch:
    print("Learn from scratch!")
elif not from_scratch :
    load_pretrained_model(model_agnews, pretrained_dict_agnews) # e.g., file_path = "smAWD.pt"
    load_pretrained_model(model_wiki, pretrained_dict_wiki) # e.g., file_path = "smAWD.pt"
    
models = [model_agnews, model_wiki, model_cat]

# Make one or more optimizer for multi models.
if adam:
#     from functools import reduce #python 3
#     import operator
#     model_param = [list(filter(lambda : p: p.requires_grad, m.parameters())) for m in models]
#     model_param = reduce(operator.concat, model_param)
#     optimizer = optim.Adam(model_param, betas=(0.7, 0.9), lr=learning_rate, weight_decay=weight_decay)
    optimizer = optim.Adam(list(filter(lambda p: p.requires_grad, model_agnews.parameters()))+ 
                           list(filter(lambda p: p.requires_grad, model_wiki.parameters()))+
                           list(filter(lambda p: p.requires_grad, model_cat.parameters())),
                           betas=(0.7, 0.9), lr=learning_rate, weight_decay=weight_decay)
else:
    optimizer = optim.SGD(list(filter(lambda p: p.requires_grad, model_agnews.parameters()))+ 
                           list(filter(lambda p: p.requires_grad, model_wiki.parameters()))+
                           list(filter(lambda p: p.requires_grad, model_cat.parameters())),
                           lr=learning_rate, weight_decay=weight_decay)
    
  

# Foward, backward, updates Loss
output_agnews, hidden = model_agnews(seq_tensor, hidden)
output_wiki, hidden = model_wiki(seq_tensor, hidden)
output_multi = torch.cat([output_agnews, output_wiki],0)

output = model_cat(output_multi, nclass)    
criterion = nn.CrossEntropyLoss()
loss = criterion(output, target)

# ============ grad udpate ================
optimizer.zero_grad()
loss.backward()
clip = 0.01 # gradient clip
torch.nn.utils.clip_grad_norm(model.parameters(), clip)
optimizer.step()
# ============ grad udpate ================
        
