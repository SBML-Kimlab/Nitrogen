from qminospy.me1 import ME_NLP1
from cobrame.io.json import load_json_me_model
import ecolime
import cobra
import cobra.solvers
import pickle
import pandas as pd
import json
import multiprocessing

problems = ["EX_etha_e"]

def solve_me_model(n_reaction):
    model = "/home/joonyoung/Python/iJL1678b.json"
    path = "/home/joonyoung/Python"
    max_mu = 1.5
    precision = 1e-8
    carbon_uptake = -10
    nitrogen_uptake = -10  
    
    print ("Loading me_model into CobraME....")
    me = load_json_me_model(model)
    
    me.reactions.EX_glc__D_e.lower_bound = carbon_uptake
    me.reactions.EX_nh4_e.lower_bound = 0
    me.reactions.get_by_id(str(n_reaction)).lower_bound = nitrogen_uptake
        
    me_nlp = ME_NLP1(me, growth_key='mu')
    muopt, hs, xopt, cache = me_nlp.bisectmu(precision=precision, mumax = max_mu)
    me.solution.f = me.solution.x_dict['biomass_dilution']
    solution = me.solution
    
    n_source = n_reaction.split("EX_")[1]
    
    print ("Writing Me_model solution....")
    with open(path+"/tem/%s_COBRAme_metabolic.json" % n_source,'w') as f:
        json.dump(me.get_metabolic_flux(solution=solution), f)
    with open(path+"/tem/%s_COBRAme_transcription.json" % n_source,'w') as f:
        json.dump(me.get_transcription_flux(solution=solution), f)
    with open(path+"/tem/%s_COBRAme_translation.json" % n_source,'w') as f:
        json.dump(me.get_translation_flux(solution=solution), f)
    print ("%s simulation is done!" % n_source)

if __name__ == '__main__':
    p = multiprocessing.Pool(processes=6)
    p.map(solve_me_model,problems)
    p.start()
    p.join()
