from ..models import Question
from ..services.ChoiceService import ChoiceService


class QuestionService:

    def __init__(self):
        self.choiceService = ChoiceService()

    def loadQuestions(self):
        return {'latest_question_list': Question.objects.all()}

    def loadQuestionById(self, questionId):
        try:
            question = Question.objects.get(pk=questionId)
        except Question.DoesNotExist:
            return None

        return question

    def voteChoice(self, question_id, choice_id):
        try:
            self.choiceService.voteChoice(choice_id)
            return True
        except Exception:
            return False