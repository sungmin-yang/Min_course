def double_pool1d(inputs, pool_type="average", batch_first=False, window_size=5, padding=0, max_units=50, stride_factor=32):
    """
    X with batch_fist False is, output of lstm. from ( output, (ht, ct) = lstm(x_embed) )
    batch_fist is False : (seq_len, batch_size, lstm_out_dim)
    batch_fist is True  : (batch_size, seq_len, lstm_out_dim)
    """
    from torch.nn import functional as F
    
    #=================== Step1 - just average Pooling =================== 
    if not batch_first: inputs = inputs.t() # (L, B, D) -> (B, L, D)
    elif batch_first : pass

    if pool_type is "average":
        out = F.adaptive_avg_pool1d(inputs, 1)
    elif pool_type is "max":
        out = F.adaptive_max_pool1d(inputs, 1)
    # ===================================================================
        
        
    #=================== Step2 - Apply Real Pooling =====================
    batch_size = out.size(0)
    seq_len    = out.size(1)

    out_reshape = out.view(batch_size, 1, seq_len)

    
    # We made window size as same as stride(gap) value.
    filter_size     = window_size # window size is fixed. or, should we apply variable filter_size(window size)?
    stride_interval = int(seq_len/stride_factor) if int(seq_len/stride_factor) <= window_size else window_size # stride_interval = int(seq_len/stride_factor)

    
    print(filter_size, stride_interval)
    out_pooled = F.avg_pool1d(out_reshape, filter_size, stride=stride_interval)
    # ===================================================================
    
    
    #=================== Step3 - Make all size of pooled matrix same. ===================== 
    current_units = out_pooled.size(2)
    import pdb; pdb.set_trace()
    
    if currnet_units < max_units:
        # Paddding
        pass
    else:
        # Clip, randomly drop(pop) the elements
        pass
    
    return out
    
    
    
    
import torch
import torch.nn as nn
from torch.nn import functional as F

inputs = torch.autograd.Variable(torch.randn(3, 190, 10)) # (batch size, seq_len, embedding_dim)
double_pool1d(inputs, batch_first=True)

# @TODO, randomly pop element for clip.
# @TODO, padding.
    
