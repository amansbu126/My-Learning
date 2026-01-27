unflat_json = {'user':
               {'Rachel':
                {'UserID': 1717171717,
                 'Email': 'rachel1999@gmail.com',
                 'friends': ['John', 'Jeremy', 'Emily']
                 }
                }
               }

def flatten_json(o):
    if isinstance(o,dict):
        for k,v in o.items():
            yield k
            yield from flatten_json(v)
    elif isinstance(o,list):
        for v in o:
            yield from flatten_json(v)
    else:
        yield o
    return {k:list(flatten_json(v)) for k,v in dict.items()}


print(flatten_json(unflat_json))
