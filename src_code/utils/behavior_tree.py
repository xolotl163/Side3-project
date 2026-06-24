
"""
We must remeber that the condition and action dictionaries take as argument the name of the condition/action
and the function associated to them. Thus, in the file enemy_ai the functions used are defined and passed to the methods condition and action.
These methods just add the fucntions to exceute to its respective dictionary.
The method procees is whats really works in the main file, updating and checking the status, conditons and actions of the agents.
"""

class BehaviorTree:
    """
    This class uses decorators to manage the actions of the agents 
    its the ai
    """
    def __init__(self,name="Generic Behavior Tree", id=-1):
        self.name = name
        self.id = id
        self.actions = {} #dictionary of actions to execute
        self.conditions = {} #dictionary of conditions o precondicitons to decide what to do
        self.rules = [] #list or set of rule to define the behacior priorities

    def condition(self, condition_name: str):
        """
        decorator that evaluates the environment
        returns true or false
        """
        def decorator(function):
            self.conditions[condition_name] = function
            return function
        
        return decorator
    
    def action(self, action_name: str):
        """
        decorator that adds a function that executes an action
        """
        def decorator(function):
            self.actions[action_name] = function
            return function
        
        return decorator
    
    def add_rule(self, condition_name: str, action_name: str):
        #links a condition with an action and gives it a priority in the BH
        self.rules.append((condition_name, action_name))

    def process(self, entity, objective, delta_time):
        """
        Iterate through the rules in order. 
        The first condition that returns True will trigger its corresponding action and end the loop for this frame.
        """
        for condition_name, action_name in self.rules:
            
            #we get the fucntion of the condiciton and it's evaluated
            #literally function condiciton is asiganted an true or false value
            #If it's true the associated fucntion or action is executed.
            function_condition = self.conditions.get(condition_name)
            if function_condition and function_condition(entity, objective):
                #if the condiction exists in the dictionary
                #and the condition is true 
                #we get and execute the associated action
                function_action = self.actions.get(action_name)
                if function_action:
                    function_action(entity, objective, delta_time)
                    #only one branch of the BH is executed (the most important)
                    return