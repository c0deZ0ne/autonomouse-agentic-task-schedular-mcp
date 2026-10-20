from agent.agent_state import *
# state = create_state("Generate a password and tell me the current time.")
# print("initial state")
# print(state)
# add_action(state,"generate_password")
# record_observation(state,"generate_password","Password:qwqeqmnem")
# next_step(state)
# print("\nState after one iteration")
# print(state)

# finish(state,"password:sdksdfjkfd\nCurrent Time 10:40AM")
# print("\n Final state")
# print(state)


async def run_agent_loop (user_request,planner,execute_action,format_answer,tools,client):
    #step1 create initial state
    state = create_state(user_request)
    while can_continue:
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