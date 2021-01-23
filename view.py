from graphviz import Digraph
import item

# create a graphviz root node
def comp(g, x, raw, bp):
    n = x.name + ' ' + str(x.count)
    s = x.name + '\n' + str(x.count)
    g.node(n, s)
    aux(g, x, raw, bp)

# auxiliary method for comp(x)
# used to create leave nodes and edges from a parent node
def aux(g, x, raw, bp):
    if not x.isRaw:
        ing = x.getIngredient()[0]
        lst = x.getByproduct()[0]
        p = x.name + ' ' + str(x.count)
        # add byproduct node
        if lst is not None:
            bp.extend(lst)
            bps = ''
            for y in lst:
                bps += y.name + ' ' + str(y.count) + '\n'
            g.node(bps, bps, shape='box')
            g.edge(p, bps)
        # leave nodes
        for y in ing:
            n = y.name + ' ' + str(y.count)
            s = y.name + '\n' + str(y.count)
            
            g.node(n, s)
            g.edge(p, n)
            aux(g, y, raw, bp)
    else:
        # update total raw materials
        raw[x.name] += x.count

materials = {
    'iron ore' : 0.0,
    'bauxite' : 0.0,
    'caterium ore' : 0.0,
    'coal' : 0.0,
    'copper ore' : 0.0,
    'crude oil': 0.0,
    'limestone' : 0.0,
    'raw quartz' : 0.0,
    'S.A.M. ore' : 0.0,
    'sulfur' : 0.0,
    'uranium' : 0.0,
    'water' : 0.0,
    'allen carapace' : 0.0,
    'allen organs' : 0.0,
    'flower petals' : 0.0,
    'leaves' : 0.0,
    'mycelia' : 0.0,
    'green power slug' : 0.0,
    'yellow power slug' : 0.0,
    'purple power slug' : 0.0,
    'wood' : 0.0,
    'bacon agaric' : 0.0,
    'beryl nut' : 0.0,
    'paleberry' : 0.0
} 

def start(lst):
    g = Digraph('G', filename='result', format='png')
    c = materials.copy()
    b = []
    for x in lst:
        comp(g, x, c, b)
    total = result(c)
    bp = result_bp(b)
    g.node('count', total, shape='box')
    g.node('byproduct', bp, shape='box')
    g.render('./photo', view=True)

# return total count of raw materials as string
def result(dict):
    res = 'Total:\n'
    for x in dict:
        if dict[x] > 0:
            res += x + ': ' + str(dict[x]) + '\n'
    return res

# return byproducts as a string
def result_bp(lst):
    d = {}
    for x in lst:
        name = x.name
        count = x.count
        if name in d.keys():
            d[name] += count
        else:
            d[name] = count
    res = 'Byproducts:\n'
    for x in d:
        res += x + ': ' + str(d[x]) + '\n'
    return res