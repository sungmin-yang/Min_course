model_agnews = RNNModel(rnn_type, ntoken_agnews, ninp, nhid, nlayers, nclass, nhid_linear,
                 dropout, dropouth, dropouti, dropoute, wdrop, tied, pooling) #,
                 #batch_norm, dropout_additional, relu)

model_wiki = RNNModel(rnn_type, ntoken_wiki, ninp, nhid, nlayers, nclass, nhid_linear,
                 dropout, dropouth, dropouti, dropoute, wdrop, tied, pooling)

model_yahoo = RNNModel(rnn_type, ntoken_wiki, ninp, nhid, nlayers, nclass, nhid_linear,
                 dropout, dropouth, dropouti, dropoute, wdrop, tied, pooling)

model_cat  = CatModel(final_out_dim, nclass, nhid_linear, batch_norm, dropout_additional, relu)


describe(model_cat)


# model_list = ['model_agnews', 'model_wiki']
model_list = [model_agnews, model_wiki, model_yahoo]
import gc;
for model, checkpoint_path in zip(model_list, checkpoint_list):
    pretrained_dict = torch.load(checkpoint_path)['state_dict']
    load_pretrained_model(model, pretrained_dict)
    del model, pretrained_dict
    gc.collect()

model_list += [model_cat]
    
# pretrained_dict = torch.load(checkpoint_list[0])['state_dict']
# load_pretrained_model(model_agnews, pretrained_dict)
# pretrained_dict = torch.load(checkpoint_list[1])['state_dict']
# load_pretrained_model(model_wiki, pretrained_dict)






# ======================== Above lines had no errors ===============================





# ======================== Below lines has error ===============================

# ================= Load pretrained LMs =================
# RuntimeError: cuda runtime error (10) : invalid device ordinal at torch/csrc/cuda/Module.cpp:88
# for model, checkpoint_path in zip(model_list, checkpoint_list):

for i, (model, checkpoint_path) in enumerate(zip(model_list, checkpoint_list)):
    import pdb;pdb.set_trace()
    pretrained_dict = torch.load(checkpoint_path)['state_dict']
    load_pretrained_model(model, pretrained_dict)
    import pdb;pdb.set_trace()
    del model, pretrained_dict; gc.collect()
    #del model, pretrained_dict; gc.collect()
    
    
    
    
    
    
    
    
    
# Problem function



def load_pretrained_model(model, pretrained_dict=None, pre_model_path=None):
    """
    How to use :
    model = load_pretrained_model(model, pretrained_dict, "smAWD.pt")

    one shot: model.load_state_dict(torch.load(pre_model_path))
    
    it seems that, this function occur forcing GPU use.
    """
    import torch

    if pre_model_path:
        pretrained_dict = torch.load(pre_model_path)
    elif pretrained_dict is None:
        raise ValueError("You must give one of pretrained_dict or pre_model_path")


    model_dict = model.state_dict()

    # 1. filter out unnecessary keys
    pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict}
    pre_weights = list(model_dict.keys())
    current_weights = list(pretrained_dict.keys())
    excluded_weights = [k  for k in pre_weights if k not in current_weights]

    # 2. overwrite entries in the existing state dict
    try : print("Before update encoder weight: ", model.encoder.weight)
    except : print("Loading stroed weights")
    model_dict.update(pretrained_dict)
    # 3. load the new state dict
    # model.load_state_dict(pretrained_dict) or
    model.load_state_dict(model_dict)
    try : print("After update encoder weight: ", model.encoder.weight)
    except : pass

    print("Successfully loaded pretrained weights, except weights in : ", excluded_weights)
    del [model, model_dict, pretrained_dict, current_weights, excluded_weights]
    
    return None
    
    
    
