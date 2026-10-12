from agent_state import *

async def run_agent_loop (user_request,planner,execute_action,format_answer,tools,client):
    #step1 create initial state
    state = create_state(user_request)
    while can_continue(state):
        action = planner(state,tools)
        print("Planner selected:",action)
        if action =="FINISH":
            answer = format_answer(state)
            finish(state,answer)
            break
        #We execute that action
        observation = await execute_action(
            action,state,client
        )

        #we add that action in a state
        add_action(
            state,action
        )

        #We remember what happened by recording observation
        record_observation(state,action,observation)
        #we move to next iteration
        next_step(state)
    
    #finaly after comming out of Can_continue
    return state