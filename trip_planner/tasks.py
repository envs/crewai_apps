from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Indetify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice

Key Steps for Task Creation:
1. Identify the desired outcome: Define what success looks like for your project.
    - A detailed 7-day travel itinenary.

2. Task breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itinenary Planning: develop a detailed plan for each day of the trip.
    - City Selection: analyze and pick the best cities to visit
    - Local Tour Guide: find a local expert to provide insights and recommendations.

3. Assign tasks to agents: Match tasks with agents based on their roless and expertise.

4. Task description template:
    - Use this template as a guide to define each task in your CrewAI application.
    - This template helps ensure that each task is clearly define, actionable, and aligned with the specific goals of...

    Template:
    ---------
    def [task_name](self, agent, [parameters]):
        return Task(description=dedent(f'''
            Task: [Provide a concise name or summary of the task]
            Description: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required]
            Parameters:
                - Parameter_1: [Description]
                - Parameter)2: [Description]
            Note: [Optional section for incentives or encouragement for high-quality work. This can include tips, ..]
        '''), agent=agent)
"""


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinenary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**: Develop a 7-day Travel Itinenary

                    **Description**: Expand teh city guide into a full 7-day travel itinenary with detailed
                    per-day plans, including weather forecasts, places to eat, packing suggestions, and a budget breakdown.
                    You MUST suggest actual places to visit, actual hotels to stay, and actual restaurants to go to.
                    This itinenary should cover all aspects of the trip, form arrival to departure, integrating the city guide 
                    information with practical travel logstics.

                    **Parameters**:
                    - City: {city}
                    - Trip Date: {travel_dates}
                    - Traveler Interests: {interests}

                    **Notes**:
                    {self.__tip_section()}
        """
            ),
            # expected_output="The expected output of the task",
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                    **Task**: Identify the Best City for the Trip

                    **Description**: Analyze and select the best city for the trip based on specific criteria such as weather 
                    patterns, seasonal events, and travel costs. This task involves comparing multiple cities, considering 
                    factors like current weather conditions, upcoming cultural or seasonal events, and overall travel expenses.
                    Your final answer MUST be a detailed report on the chosen city, including actual flight costs, weather forecasts, 
                    and attractions.

                    **Parameters**:
                    - Origin: {origin}
                    - City: {cities}
                    - Interests: {interests}
                    - Travel Date: {travel_dates}

                    **Notes**:
                    {self.__tip_section()}
        """
            ),
            # expected_output="The expected output of the task",
            agent=agent,
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**: Gather In-0depth City Guide Information

                    **Description**: Compile an in-depth guide for the selected city, gathering information about key attractions, 
                    local customs, special events, and daily activity recommendations.
                    This guide should provide a thorough overview of what the city has to offer, including hidden gems, cultural 
                    hotspots, must-visit landmarks, weather forecasts, and high-level costs.

                    **Parameters**:
                    - City: {city}
                    - Interests: {interests}
                    - Travel Date: {travel_dates}

                    **Notes**:
                    {self.__tip_section()}
        """
            ),
            # expected_output="The expected output of the task",
            agent=agent,
        )
