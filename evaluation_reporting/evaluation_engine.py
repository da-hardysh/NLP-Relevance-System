# text_processing/evaluation_reporting/evaluator.py
class RelevanceEvaluator:
    def __init__(self, course_keywords, test_keywords):
        self.course_keywords = course_keywords
        self.test_keywords = test_keywords

    def evaluate_global(self):
        matched = set(self.course_keywords) & set(self.test_keywords)
        coverage = len(matched) / len(set(self.course_keywords)) if self.course_keywords else 0
        return round(coverage, 2)

    def get_uncovered_terms(self):
        return list(set(self.course_keywords) - set(self.test_keywords))


# text_processing/evaluation_reporting/reporter.py
import json

class EvaluationReporter:
    def __init__(self, results):
        self.results = results

    def generate_summary(self):
        summary = f"Coverage: {self.results['coverage']*100}%\n"
        summary += "Uncovered terms: " + ", ".join(self.results['uncovered']) + "\n"
        return summary

    def export_to_json(self, filepath):
        with open(filepath, 'w') as f:
            json.dump(self.results, f, indent=2)

