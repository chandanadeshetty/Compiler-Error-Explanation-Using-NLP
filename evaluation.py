class Evaluator:

    def evaluate(self, predicted, expected):
        score = 0

        # Format check
        if "Mistake" in predicted:
            score += 1
        if "Reason" in predicted:
            score += 1
        if "Fix" in predicted:
            score += 1

        format_score = score / 3

        # Word similarity
        pred_words = set(predicted.lower().split())
        exp_words = set(expected.lower().split())

        common = pred_words & exp_words
        similarity = len(common) / max(len(exp_words), 1)

        final_score = (format_score + similarity) / 2

        return {
            "format_score": round(format_score, 2),
            "similarity_score": round(similarity, 2),
            "final_score": round(final_score, 2)
        }