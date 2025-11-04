import json
import os

class ExpertSystem:
    def __init__(self, knowledge_base_path="knowledge_base/rules.json"):
        """Load and initialize the knowledge base."""
        if not os.path.exists(knowledge_base_path):
            raise FileNotFoundError("Knowledge base not found at " + knowledge_base_path)

        with open(knowledge_base_path, "r") as file:
            self.rules = json.load(file)

    def get_recommendation(self, goal, level, equipment):
        """
        Matches user inputs with rules from the knowledge base.
        Includes fallback logic and reasoning trace.
        """
        exact_matches = []
        partial_matches = []

        # Step 1: Exact match (goal + level + equipment)
        for rule in self.rules:
            if (
                rule["goal"].lower() == goal.lower()
                and rule["level"].lower() == level.lower()
                and rule["equipment"].lower() == equipment.lower()
            ):
                exact_matches.append(rule)

        if exact_matches:
            return {
                "status": "success",
                "recommendations": exact_matches[0]["recommendation"],
                "explanation": f"Matched exact rule for {goal} at {level} level using {equipment}."
            }

        # Step 2: Partial match (if exact not found)
        for rule in self.rules:
            score = 0
            if rule["goal"].lower() == goal.lower():
                score += 1
            if rule["level"].lower() == level.lower():
                score += 1
            if rule["equipment"].lower() == equipment.lower():
                score += 1

            if score >= 2:  # at least 2 attributes match
                partial_matches.append((score, rule))

        if partial_matches:
            best_match = sorted(partial_matches, key=lambda x: x[0], reverse=True)[0][1]
            return {
                "status": "partial",
                "recommendations": best_match["recommendation"],
                "explanation": (
                    f"No exact rule found, but found close match for goal '{best_match['goal']}', "
                    f"level '{best_match['level']}', and equipment '{best_match['equipment']}'."
                )
            }

        # Step 3: No match at all
        return {
            "status": "error",
            "recommendations": ["No matching workout found. Try different inputs."],
            "explanation": "No rule matched any of the input attributes."
        }


# ---------- Standalone function (for Flask) ---------- #
def get_recommendation(goal, level, equipment):
    """Wrapper function for Flask integration."""
    system = ExpertSystem()
    result = system.get_recommendation(goal, level, equipment)
    return result["recommendations"]

