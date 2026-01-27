unflat_json = {'user':
               {'Rachel':
                {'UserID': 1717171717,
                 'Email': 'rachel1999@gmail.com',
                 'friends': ['John', 'Jeremy', 'Emily']
                 }
                }
               }

def flatten_json(s):
    ans = {}
    for k,v in s.items():
        if isinstance(v,dict):
            nested = flatten_json(v)
            for n_k,n_v in nested.items():
                ans[n_k]=n_v
        else:
            ans[k]=v
    return ans 

print(flatten_json(unflat_json))