from ..models import Choice


class ChoiceService:

    def voteChoice(self, choice_id):
        choice = Choice.objects.get(pk=choice_id)
        if choice is not None:
            choice.votes += 1
            choice.save()
        else:
            raise Exception('Choice %s doesn\'t exists' % choice_id)