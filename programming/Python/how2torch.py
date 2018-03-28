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
    


# Issue with fast/slow pack/unpack
# https://github.com/pytorch/pytorch/issues/1788



# Add <pad> for word-dictionary
index = len(word_dict["word2index"])
word_dict["word2index"]["<pad>"] = index
word_dict["index2word"][index]   = "<pad>"
# Add one more index-weights in embedding state_dict
# > Either : pretrained_state_dict["encoder"]["weight"] += [Embedding_dim_weights] 
# > OR     : pretrained_state_dict.encoder.weight.append([Embedding_dim_weights])
