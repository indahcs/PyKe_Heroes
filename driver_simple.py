import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

   
def bc_test_questions():

    engine.reset()  

    engine.activate('bc_simple_rules_questions') 

    print("search hero")
    
    try:
        with engine.prove_goal('bc_simple_rules_questions.heroes($hero)') as gen:
            for vars, plan in gen:
                print("The character is: %s" % (vars['hero'])) 

    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")


