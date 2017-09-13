from collections import Counter

import matplotlib.pyplot as plt

def test_transition_model(states, actions, transition):
    ''' Ensure 
            sum_{s'} P_{s s'}^{a} = 1
        for all states s and actions a.
    '''
    for s in states:
        for a in actions:
            state_action = [t[3] for t in transition if t[0] == s and t[1] == a]
            if len(state_action) > 0:
                try:
                    assert sum(state_action) == 1
                except AssertionError:
                    print("sum_(s') P_({} s')^({}) = {}".format(s, a, sum(state_action)))
                    
                    
def plot_state_history(state_history, states):
    c = Counter(state_history)

    history_dict = {}

    for s in states:
        history_dict[s] = c[s]
        
    print(history_dict)

    bar_heights = [history_dict[s] for s in states]
    x = [i+1 for i in range(len(states))]

    fig, ax = plt.subplots()
    width = 0.4

    ax.set_title('Number of times each state visited')
    ax.bar(x, bar_heights, width)

    ax.set_xlim((0, len(states)))
    ax.set_ylim((0, max(bar_heights)*1.1))

    ax.set_xticks([i+width/2 for i in x])
    ax.set_xticklabels(states)
    
    ax.set_xlabel('State')
    ax.set_ylabel('Frequency')

    plt.show()

# string representing the transition model
model_line = """
(states[0], actions[0], states[0], 1),
(states[0], actions[1], states[1], alpha),
(states[0], actions[1], states[2], 1-alpha),
(states[0], actions[2], states[2], beta),
(states[0], actions[2], states[3], 1-beta),

(states[1], actions[0], states[0], 1),
(states[1], actions[1], states[2], alpha),
(states[1], actions[1], states[3], 1-alpha),
(states[1], actions[2], states[5], beta),
(states[1], actions[2], states[6], 1-beta),

(states[2], actions[0], states[0], 1),
(states[2], actions[1], states[1], alpha),
(states[2], actions[1], states[3], 1-alpha),
(states[2], actions[2], states[7], beta),
(states[2], actions[2], states[8], 1-beta),

(states[3], actions[0], states[0], 1),
(states[3], actions[1], states[1], alpha),
(states[3], actions[1], states[2], 1-alpha),
(states[3], actions[2], states[4], beta),
(states[3], actions[2], states[9], 1-beta),

(states[4], actions[0], states[3], 1),
(states[4], actions[1], states[5], alpha),
(states[4], actions[1], states[6], 1-alpha),
(states[4], actions[2], states[8], beta),
(states[4], actions[2], states[9], 1-beta),

(states[5], actions[0], states[1], 1),
(states[5], actions[1], states[6], alpha),
(states[5], actions[1], states[7], 1-alpha),
(states[5], actions[2], states[4], beta),
(states[5], actions[2], states[9], 1-beta),

(states[6], actions[0], states[1], 1),
(states[6], actions[1], states[7], alpha),
(states[6], actions[1], states[8], 1-alpha),
(states[6], actions[2], states[4], beta),
(states[6], actions[2], states[5], 1-beta),

(states[7], actions[0], states[2], 1),
(states[7], actions[1], states[8], alpha),
(states[7], actions[1], states[9], 1-alpha),
(states[7], actions[2], states[5], beta),
(states[7], actions[2], states[6], 1-beta),

(states[8], actions[0], states[2], 1),
(states[8], actions[1], states[6], alpha),
(states[8], actions[1], states[7], 1-alpha),
(states[8], actions[2], states[4], beta),
(states[8], actions[2], states[9], 1-beta),

(states[9], actions[0], states[3], 1),
(states[9], actions[1], states[4], alpha),
(states[9], actions[1], states[5], 1-alpha),
(states[9], actions[2], states[8], beta),
(states[9], actions[2], states[10], 1-beta),

(states[10], actions[0], states[9], 1),
(states[10], actions[1], states[9], alpha),
(states[10], actions[1], states[11], 1-alpha),
(states[10], actions[2], states[9], beta),
(states[10], actions[2], states[11], 1-beta),

(states[11], actions[0], states[10], 1),
(states[11], actions[1], states[10], alpha),
(states[11], actions[1], states[12], 1-alpha),
(states[11], actions[2], states[10], beta),
(states[11], actions[2], states[12], 1-beta),

(states[12], actions[0], states[11], 1),
(states[12], actions[1], states[11], alpha),
(states[12], actions[1], states[13], 1-alpha),
(states[12], actions[2], states[11], beta),
(states[12], actions[2], states[13], 1-beta),

(states[13], actions[0], states[12], 1),
(states[13], actions[1], states[12], alpha),
(states[13], actions[1], states[14], 1-alpha),
(states[13], actions[2], states[12], beta),
(states[13], actions[2], states[14], 1-beta),

(states[14], actions[0], states[13], 1),
(states[14], actions[1], states[13], alpha),
(states[14], actions[1], states[15], 1-alpha),
(states[14], actions[2], states[13], beta),
(states[14], actions[2], states[17], 1-beta),

(states[15], actions[0], states[18], 1),
(states[15], actions[1], states[14], 1),
(states[15], actions[2], states[16], 1),

(states[16], actions[0], states[18], 1),
(states[16], actions[1], states[15], 1),
(states[16], actions[2], states[17], 1),

(states[17], actions[0], states[18], 1),
(states[17], actions[1], states[14], 1),
(states[17], actions[2], states[16], 1),

(states[18], actions[0], states[18], 1),
(states[18], actions[1], states[14], 1),
(states[18], actions[2], states[15], 1),
"""