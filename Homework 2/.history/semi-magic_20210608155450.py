import pdb
from csp import *
from random import shuffle

def create_domains(vars):
    domains_dict = dict()
    for key in vars:
        domains_dict[key] = [1, 2, 3]
    return domains_dict

def create_neighbours(): #as long as the key is different from each item in the list
    neighbours_dict = { 'V1':['V2', 'V3', 'V4', 'V5', 'V7', 'V9'],
                        'V2':['V1', 'V3', 'V5', 'V8'],
                        'V3':['V1', 'V2', 'V6', 'V9'],
                        'V4':['V1', 'V5', 'V6', 'V7'],
                        'V5':['V1', 'V2', 'V4', 'V6', 'V8', 'V9'],
                        'V6':['V3', 'V4', 'V5', 'V9'],
                        'V7':['V1', 'V4', 'V8', 'V9'],
                        'V8':['V2', 'V5', 'V7', 'V9'],
                        'V9':['V1', 'V3', 'V5', 'V6', 'V7', 'V8'],}
    return neighbours_dict

def solve_semi_magic(algorithm=backtracking_search, **args):
    """ From CSP class in csp.py
        vars        A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b
                    """
    # Use the variable names in the figure
    csp_vars = ['V%d'%d for d in range(1,10)]
    #print (csp_vars)

    #########################################
    # Fill in these definitions

    csp_domains = create_domains(csp_vars)
    csp_neighbors = create_neighbours()
    
    def csp_constraints(A, a, B, b):
        if a != b:
            return True
        else:
            return False

    #########################################
    
    # define the CSP instance
    csp = CSP(csp_vars, csp_domains, csp_neighbors,
              csp_constraints)

    # run the specified algorithm to get an answer (or None)
    ans = algorithm(csp, **args)
    
    print ('number of assignments', csp.nassigns) 
    assign = csp.infer_assignment()
    if assign:
        for x in sorted(assign.items()):
            print (x)
    return csp

solve_semi_magic()
'''
Regular backtracking - Number of assignments 9
V1 -> 1, V2 -> 2, V3 -> 3
V4 -> 2, V5 -> 3, V6 -> 1,
V7 -> 3, V8 -> 1, V9 -> 2 
'''