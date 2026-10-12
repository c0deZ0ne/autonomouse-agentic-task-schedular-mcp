
#how do you define own type?
# type state = dict[str,object]
def create_state (user_request:str,max_steps:int=5) -> dict[str, object]:
    return {
        "user_request":user_request,
        "current_step":0,
        "max_step":max_steps,
        "actions":[],
        "observations":[],
        "finished":False,
        "final_answer":""

    }

def add_action (state,action):
    return state["actions"].append(action)

def record_observation(state,action,observation):
    state["observations"].append({
        "step":state["current_step"],
        "action":action,
        "observation":observation
    })

def next_step(state):
    state["current_step"]+=1

#this functions determines wether the agent loop could continue 
def can_continue(state):
    return not state["finished"] and state["current_step"]< state["max_step"]

def finish (state,answer):
    state["final_answer"] = answer
    state["finished"] = True
